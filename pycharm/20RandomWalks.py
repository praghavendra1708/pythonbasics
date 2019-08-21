import random

def randomwalkfun(nos):
    """give the distance from start point after random walk"""

    x, y = 0, 0
    for i in range(1, nos):
        dx, dy = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])
        x += dx
        y += dy

    return abs(x) + abs(y)

# talking a 1000 random walks with 30 step
for j in range(1, 1001):
    distance_traveled = randomwalkfun(30)
    print("On walk", j , " distance away from source is", distance_traveled)

# Monte carlo problem
# max length of walk where no transportation is required
for i in range(1, 31):
    no_trans_req = 0
    for j in range(1, 1001):
        dis_trav = randomwalkfun(i)
        if(dis_trav <= 4):
            no_trans_req = no_trans_req + 1

    print (no_trans_req)
    print("for steps:", i , "avg time transportation required:", ((no_trans_req * 100)/1000) )