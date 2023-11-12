#!/usr/bin/python
# ================================
# (C)2020 Dmytro Holub
# heap3d@gmail.com
# --------------------------------
# modo python
# merge PreRotation and rotation transforms
# ================================

import modo
import lx

scene = modo.scene.current()

print '----------'

# item = scene.selectedByType('mesh')[0]
items_selection = scene.selectedByType('mesh')
for item in items_selection:
    item_prerotation = modo.Item
    item_rotation = modo.Item
    for graph in item.itemGraph('xfrmCore').connectedItems['Reverse']:
        if 'PreRotation' in graph.id:
            item_prerotation = graph
        if 'rotation' in graph.id:
            item_rotation = graph
    item.select(replace=True)
    try:
        # merging two transforms:
        item_prerotation.select()
        item_rotation.select()
        lx.eval('user.value {} ?'.format(userval_page_start))
        # delete prerotation transform
        lx.eval('user.value {} ?'.format(userval_page_start))
        lx.eval('user.value {} ?'.format(userval_page_start))
    except Exception:
        print '<{}> skipped'.format(item.name)
    else:
        print '<{}> PreRotation transform merged'.format(item.name)

scene.deselect()
for item in items_selection:
    item.select()

print '=========='
