#!/usr/bin/python
# ================================
# (C)2019 Dmytro Holub
# heap3d@gmail.com
# --------------------------------
# modo python
# inspect selected item graphs
# ================================

import modo

use_selected = True

print('----------')

if use_selected:
    items_collection = modo.Scene().selected
else:
    items_collection = modo.Scene().items('mesh')

for item in items_collection:
    print('item name:<{}>   id:<{}>   type:<{}>'.format(item.name, item.id, item.type))
    for graphname in item.itemGraphNames:
        print('  graphname : graph:<{}>'.format(graphname))
        for idx in item.itemGraph(graphname).connectedItems:
            print('    idx : item:<{}>'.format(idx))
            for item_detail in item.itemGraph(graphname).connectedItems[idx]:
                print('      item_detail : name:<{}> : type:<{}> : item:<{}>'
                      .format(item_detail.name, item_detail.type, item_detail))

print('==========')
