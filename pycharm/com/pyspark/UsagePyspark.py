"""" Union of dataframes with different schema  """

import rlcompleter, readline
from pyspark.sql import HiveContext

readline.parse_and_bind("tab: complete")

hc = HiveContext(spark.sparkContext)

cj_query = """select *
FROM cemod.ps_cj_wb_dis_index_1_1_week 
where 
from_unixtime(CAST(dt/1000 as BIGINT), 'yyyy-MM-dd HH:mm:ss') = '2019-07-28 00:00:00' and subscriber_id in ('148665568')"""

cei_query = """select *
FROM cemod.ps_cei_wb_dis_index_1_1_week 
where 
from_unixtime(CAST(dt/1000 as BIGINT), 'yyyy-MM-dd HH:mm:ss') = '2019-07-28 00:00:00' and subscriber_id in ('148665568')"""

cj_df = hc.sql(cj_query)
cj_lt = cj_df.schema.names
cj_lt[:]= [ s.replace('cj_','c_') for s in cj_lt ]
cj_df = cj_df.toDF(*cj_lt)

cei_df = hc.sql(cei_query)
cei_lt = cei_df.schema.names
cei_lt[:]= [ s.replace('cei_','c_') for s in cei_lt ]
cei_df = cei_df.toDF(*cei_lt)


all_columns = set(cei_df.schema.names).union(set(cj_df.schema.names))

from pyspark.sql.functions import lit

for column0 in all_columns:
    if column0 not in cj_df.columns:
        cj_df = cj_df.withColumn(column0, lit('CNP'))
        print("column missing in cj:" + column0)
    if column0 not in cei_df.columns:
        cei_df = cei_df.withColumn(column0, lit('CNP'))
        print("column missing in cei:" + column0)
    # print(column0)


print(set(cj_df.columns).difference(set(cei_df.columns)).show)


cei_df = cei_df[sorted(cei_df.schema.names)]
cj_df = cj_df[sorted(cj_df.schema.names)]


output_df = cj_df.union(cei_df)
