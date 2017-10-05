#!/usr/bin/python3.6

import sys
import re

data = sys.stdin.read()
tab_matcher = '^|\n(\t|( {4}))+def'
"""
regex sample:
(^|\n)(\t|( {4}))(def.+)(\n(\t|( {4})){2}.+)*((\n(\t|( {4})){0,1}[a-zA-z])|([\n\t]?$))
"""

max = 0
for i in re.findall(tab_matcher,data):
	if len(i[1]) > max:
		max = len(i[1])

regs = []
begin =  '(^|\n)'
tab = '(\t|( {4}))'
define = '(def.+)'

for n in range(max+1):
	lines = '(\n('+tab+'{'+str(n+1)+',}'+'.+)*)*'
	delimeter = '((\n'+tab+'{0,'+str(n)+'}[a-zA-Z_])|([\n\t]*$))'
	regexp = '('+begin+tab+'{'+str(n)+'}'+define+lines+delimeter+')'
	regs.append(regexp)


funcs = []
for x in regs:
	if re.findall(x,data):
		funcs.extend(re.findall(x, data))


for i in range(len(funcs)):
	funcs[i] = re.sub(r'\s', '', funcs[i][0])[:-1]	# trim whitespaces 

funcs.sort()

for i in funcs:
	for j in funcs:
		if not i is j and i == j:
			print(i)
			print(j)