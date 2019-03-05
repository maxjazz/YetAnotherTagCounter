import sys
import argparse
import logging
from tktc import tktc
from tc import TC


#Init parser
parser = argparse.ArgumentParser()
parser.add_argument('-g', '--get', help = 'Get tag list from site')
parser.add_argument('-v', '--view', help = 'Vet tag list from site')

#Init logger
logging.basicConfig(format = '%(asctime)s: %(message)s', level = logging.DEBUG, filename = 'yatc.log')

def main():
	args = parser.parse_args();
	if args.get or args.view:
		tc = TC()
		tc.run(args)
	else:
		tktc.run()

if __name__ == '__main__':
    main()