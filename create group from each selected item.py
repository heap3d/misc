#!/usr/bin/python
# ================================
# (C)2021 Dmytro Holub
# heap3d@gmail.com
# --------------------------------
# modo python
# render output item mask creation
# ================================

import modo
import lx

scene = modo.scene.current()

print
print 'start...'

selected = scene.selectedByType(itype='mesh')

for item in selected:
    print 'item: <{}>; name: <{}>; type: <{}>'.format(item, item.name, item.type)
    item.select(replace=True)
    lx.eval('user.value {} ?'.format(userval_page_start))

print 'done.'
