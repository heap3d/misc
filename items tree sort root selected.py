#!/usr/bin/python
# ================================
# (C)2022 Dmytro Holub
# heap3d@gmail.com
# --------------------------------
# modo python
# sort selected items in the item tree root alphabetically
# usage: select items in the item tree root and run the script
# ================================

import modo
import modo.constants as c


def get_name(item):
    return item.name


scene = modo.scene.current()
# get selection
selection = scene.selectedByType(itype=c.LOCATOR_TYPE, superType=True)
# get sorted list
item_list = sorted(selection, key=get_name)

# get parent of first selected item
parent = selection[0].parent
# get parent index of first selected item
start_index = selection[0].parentIndex
# rearrange items by sorted list
for index, item in enumerate(item_list):
    item.setParent(parent, index)
