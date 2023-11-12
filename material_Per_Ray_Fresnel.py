#!/usr/bin/python
# ================================
# (C)2021 Dmytro Holub
# heap3d@gmail.com
# --------------------------------
# modo python
# set Per-Ray Fresnel for selected material masks(! not materials itself)
# usage: select material masks, run the script
# ================================

import modo

print
print 'start...'

scene = modo.scene.current()

# get selected masks
maskSet = scene.selectedByType(itype=c.MASK_TYPE)

for mask in maskSet:
    for item in mask.children(recursive=True):
        if item.type == 'advancedMaterial':
            item.channel('perRayFres').set(1)
            print '<{}> : <{}> processed'.format(mask.name, item.name)

print 'done.'
