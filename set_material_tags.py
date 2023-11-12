#!/usr/bin/python

import lx
import lxu


class MyCommand_Cmd(lxu.command.BasicCommand):
    def __init__(self):
        lxu.command.BasicCommand.__init__(self)

    def cmd_Flags(self):
        return lx.symbol.fCMD_UNDO | lx.symbol.fCMD_MODEL

    def basic_Execute(self, msg, flags):
        tag = lx.object.StringTag()
        layerService = lx.service.Layer()
        layerScanObject = layerService.ScanAllocate(lx.symbol.f_LAYERSCAN_EDIT)

        mesh = layerScanObject.MeshEdit(0)
        poly = mesh.PolygonAccessor()

        poly.SelectByIndex(0)
        tag.set(poly)
        tag.Set(lx.symbol.i_PTAG_MATR, 'test')

        layerScanObject.SetMeshChange(0, lx.symbol.f_MESHEDIT_GEOMETRY)
        layerScanObject.Apply()


lx.bless(MyCommand_Cmd, "assignTags")
