#!/usr/bin/python
import modo
import lx

items = modo.Scene().items(itype='mesh')

for item in items:
	print(f'{item.name=} : {item=}')
	if item.channel('visible').get() == 'allOff':
		item.select(True)
		lx.eval('item.editorColor lightgreen')
