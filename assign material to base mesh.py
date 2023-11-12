#!/usr/bin/python
import modo
import lx

selected = modo.Scene().selectedByType(itype='mesh')

for item in selected:
    item.select(replace=True)
    lx.eval('deformer.selectBaseMesh select:true')
    lx.eval('poly.setMaterial cutter {0.6 0.6 0.6} 0.8 0.04 true false')
    lx.eval('deformer.selectBaseMesh select:false')
