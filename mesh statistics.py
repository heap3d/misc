#!/usr/bin/python
# ================================
# (C)2019 Dmytro Holub
# heap3d@gmail.com
# --------------------------------
# modo python
# print poly count for every mesh in the scene
# ================================

import modo

scene = modo.scene.current()

print '------------------------------'

dict_meshes = {}

items_selected = scene.selectedByType('mesh')
test_array = list(items_selected)
for mesh in items_selected:
    # print '<{}> : {}'.format(mesh.name, mesh)
    dict_meshes[mesh] = len(mesh.geometry.polygons)
    mesh.name = '[{:07}] {}'.format(dict_meshes[mesh], mesh.name)

dict_sorted = sorted(dict_meshes.iteritems(), key=lambda x: x[1])
for item in dict_sorted:
    print '<{}> : [{}]'.format(item[0].name, item[1])

print '=============================='
