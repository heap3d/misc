#!/usr/bin/python
# ================================
# (C)2025 Dmytro Holub
# heap3d@gmail.com
# --------------------------------
# modo python
# select polygong and run the script
# script execute following commands:
# - cut selected polygons
# - paste polygons
# - flip polygons
# ================================

import lx


def main():
    lx.eval("cut")
    lx.eval("paste")
    lx.eval("poly.flip")


if __name__ == "__main__":
    main()
