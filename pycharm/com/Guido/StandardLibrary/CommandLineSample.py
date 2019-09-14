""" Accessing Commandline arguments """

import argparse
from getpass import getuser

parser = argparse.ArgumentParser(description='An argparse example')
parser.add_argument('name', nargs='?', default=getuser(), help='The name of someone to greet.')
parser.add_argument('--verbose', '-v', action='count')
args = parser.parse_args(['--verbose', 'name=xyz', '-v'] )

print(f'args {args.verbose}')
greeting = ['hi', 'hello', 'Greatings! its very nice to meet you'][args.verbose%3]

print(f'{greeting}, {args.name}')
if not args.verbose:
    print('Try running this again with multiple "-v" flags!')