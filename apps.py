#! /usr/bin/env python
# license : under Creative Common License
# version : 1.1
# by vickydasta
# simple plain text hiding tecnique

from base64 import b64encode
from base64 import b64decode
from string import maketrans
import sys
import hashlib
import random

alp='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 ' #everyone can change the chiper table
trans_alp_to_dd="""!@#$%)(*&^-=_+';:",.<>/?~1[]\|cDklPpBnisUIxvMnCd7809heEJLGOPMN/"""
trasn_dec=maketrans(trans_alp_to_dd,alp)
tab_1=maketrans(alp, trans_alp_to_dd)

def mkmd5sum(s):
	new_s=hashlib.md5(s)
	return new_s.hexdigest()

def gimerand():
	'generate random string'
	rand_="""!@#$%)(*&^-=_+';:",.<>/?~1[]\|cDklPpBnisUIxvMnCd7809heEJLGOPMN"""
	return random.choice(list(rand_))

def enc(s):return s.translate(tab_1)
'''encode string with given key
   for example : 
   	if given key are '!@#$%' and the plain text is 'father' 
   	so,father would be same as like '!@#$%' 
   	and so on
'''

def dec(s):return s.translate(trasn_dec)
'''
   translator function,it's do the reverse job of enc(s)
'''
def tob64(s):return b64encode(s)
def fromb64(s):return b64decode(s)
def bytencode(s):return enc(s)+giveRandom()

def main():
	if sys.argv[1] == '-e' or sys.argv[1] == '-E':
		print '# Encoding Method'
		while True:
			# do we need to unchiper the chiper ? 
			# i don't think so...
			inp=raw_input('>. ')			
			print '--> private chiper : {}'.format(enc(inp)+gimerand())
			print '--> base64 encoded : {}'.format(tob64(enc(inp)))
			print '--> md5            : {}'.format(mkmd5sum(inp)+giveRandom())

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
	
