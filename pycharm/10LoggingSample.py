import logging

print(dir(logging))

# logger format
MYFORMAT = "%(asctime)-15s  %(message)s"


# Creating logger
logging.basicConfig(filename = "./mylogger.txt",
                    level = logging.DEBUG, format=MYFORMAT )
log = logging.getLogger()

#Testing logger
log.info("This is an info msg")
