#!/usr/bin/python

import lx
import modo

scene = modo.scene.current()
clips = scene.selected

for image in clips:
    image.select(replace=True)
    print image.name
    lx.eval('user.value {} ?'.format(userval_page_start))

