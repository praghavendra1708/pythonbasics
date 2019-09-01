""" Testing the samples of module """
import sys

print('System __name__: {}'.format(__name__))


if __name__ == '__main__':
    for i, a in enumerate(sys.argv):
        print('arg {} value {}'.format(i, a))
else:
    print("this is not a main module")
