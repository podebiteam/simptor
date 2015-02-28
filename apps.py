#!/usr/bin/env/ python

__author__ = 'vickydasta'
__doc__    = 'simptorlib example'

import sys

try:
	from simptor import enc, tob64, dec,gimerand,mkmd5sum
except ImportError:
	print 'vick@ubuntu:~# pycompile simptor.py'
	sys.exit(0)

def main():
	if sys.argv[1] == '-e' or sys.argv[1] == '-E':
		print '# Encoding Method'
		while True:
			# do we need to unchiper the chiper ? 
			# i don't think so...
			inp=raw_input('>. ')			
			print '--> private chiper : {}'.format(enc(inp)+gimerand())
			print '--> base64 encoded : {}'.format(tob64('aaa'))
			print '--> md5            : {}'.format(mkmd5sum(inp)+gimerand())

	elif sys.argv[1] == '-d' or sys.argv[1]== '-D':
		print '# Decoding Method'
		while True:
			inp=raw_input('>>>')
			print '--> md5    : {}'.format(mkmd5sum(inp))
			print '--> string : {}'.format(dec(inp))

if __name__ == '__main__':
	if sys.argv[1] in '-d' or sys.argv[1] in '-e':
		main()
	else:
		print ' Usage : {} <mode>'.format(sys.argv[0])
		print ' Options :'
		print '          -e < for encryption>'
		print '          -d < for decription>'
		print ' example : '
		print ' simptor.py -e '
		print ' >>> do what the fuck you want to do with this script.' 
	


if __name__ == '__main__':
	if sys.argv[1] == '-d' or sys.argv[1] == '-e':
		main()
	else:
		print '{} <mode>'.format(sys.argv[0])
		print 'mode: '
		print '      -e < for encryption>'
		print '      -d < for decription>'
		print 'example : '
		print '       {} -e '.format(sys.argv[0])
		print '       >>> do what the fuck you want to do with this script.'
