#!/usr/bin/env/ python

__author__ = 'vickydasta'
__doc__    = 'simptorlib usage example'

import sys

try:
	from simptor import enc, tob64, dec
except ImportError:
	print 'vick@ubuntu:~# pycompile simptor.py'
	sys.exit(0)

def main():
	print '\n A Technique for hiding Your Ass'

	if sys.argv > 0:
		if sys.argv[1] == '-e':
			print '-'*len('text hiding method started'),'>'
			print ' text hiding method started'
			while True:
				inp=raw_input('>. ')
				if inp == '':
					print 'enter some chipered text...!!!'
				else:
					print '--> private hash : {}'.format(enc(inp))
					print '--> base64 encoded : {}'.format(tob64(nw))
		elif sys.argv[1] == '-d' or sys.argv[1]== '-D':
			print '# Decoding Method'
			while True:
				inp=raw_input('>. ')
				if inp == '':
					pass
				else:
					print '--> string : {}'.format(dec(inp))
		else:
			print '{} <mode>'.format(sys.argv[0])
			print 'mode: '
			print '      -e < for encryption>'
			print '      -d < for decription>'
			print 'example : '
			print '       {} -e '.format(sys.argv[0])
			print '       >>> do what the fuck you want to do with this script.'
	else:
		print '{} <mode>'.format(sys.argv[0])
		print 'mode: '
		print '      -e < for encryption>'
		print '      -d < for decription>'
		print 'example : '
		print '       {} -e '.format(sys.argv[0])
		print '       >>> do what the fuck you want to do with this script.'


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
