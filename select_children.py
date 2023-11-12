#!/usr/bin/python
# ================================
# (C)2023 Dmytro Holub
# heap3d@gmail.com
# --------------------------------
# modo python
# select children recursive for selected items
# ================================

import modo

scene = modo.Scene()
items = scene.selected
for item in items:
    if item.children():
        for child in item.children(recursive=True):
            child.select()
