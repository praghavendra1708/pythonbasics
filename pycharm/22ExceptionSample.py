import time
import logging

# msg format
MYFORMAT = "%(asctime)-15s  %(message)s"

logging.basicConfig(filename='./mylogger.txt', filemode='a', format=MYFORMAT, level=logging.DEBUG)
log = logging.getLogger()

file_to_read = '/Users/raghavendrareddy/Downloads/Yellowstone.2018.S02E09.720p.WEB.x265-MiNX[TGx]/Yellowstone.2018.S02E09.720p.WEB.x265-MiNX.mkv'

try:
    startTime = time.time()
    log.info('start time: {}'.format(startTime))
    fileio = open(file_to_read, mode='br')
    fileio.read()
except FileNotFoundError:
    log.error('Input file not found {}'.format(file_to_read))
    raise
else:
    log.info('Closing the file {}'.format(file_to_read))
finally:
    endTime = time.time()
    print('time taken {}'.format(endTime - startTime))
    log.info('time taken {}'.format(endTime - startTime))


len