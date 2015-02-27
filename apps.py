#!/usr/bin/env/ python

__author__ = 'vickydasta'
__doc__    = 'simptorlib example'

import sys

try:
	from simptor import enc, tob64, dec
except ImportError:
	print 'vick@ubuntu:~# pycompile simptor.py'
	sys.exit(0)

def main():
	if sys.argv > 0:
		if sys.argv[1] == '-e' or sys.argv[1] == '-E':
			print '# Encoding Method'
			while True:
				inp=raw_input('>>> ')
				nw=enc(inp)
				enc_tob64=tob64(nw)
				print '--> private hash : {}'.format(nw)
				print '--> base64 encoded : {}'.format(enc_tob64)
		elif sys.argv[1] == '-d' or sys.argv[1]== '-D':
			print '# Decoding Method'
			while True:
				inp=raw_input('>>>')
				nw=dec(inp)
				print '--> string : {}'.format(nw)


if __name__ == '__main__':
	if sys.argv[1] in '-d' or sys.argv[1] in '-e':
		main()
	else:
		print '{} <mode>'.format(sys.argv[0])
		print '-e < for encryption>'
		print '-d < for decription>'
		print 'example : '
		print 'simptor.py -e '
		print '>>> do what the fuck you want to do with this script.'
