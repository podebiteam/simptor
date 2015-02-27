#!/bin/env python
#license under GPL 2.0
#version : 1.1
#by vickydasta vickydasta(at)gmail(dot)com
#simple encryptor-decrptor 
#simple,strong enough

from base64 import b64encode
from base64 import b64decode
from string import maketrans
import sys

alp='abcdefghijklmnopqrstuvwxyz'
alp_A='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alp_n='1234567890'

trans_alp_to_dd="""!@#$%)(*&^-=_+';:",.<>/?~1"""
tab_1=maketrans(alp, trans_alp_to_dd)
def enc(s):
	if s:
		new_s=s.translate(tab_1)
		return new_s
	else:
		pass

trasn_dec=maketrans(trans_alp_to_dd,alp)

def dec(s):
	if s:
		new_s=s.translate(trasn_dec)
		return new_s 
	else:
		pass


def tob64(s):
	if s:
		return b64encode(s)
	else:
		pass
def fromb64(s):
	if s:
		return b64decode(s)

# it's simplicity will kill you...
# so,be carefull !!
	
