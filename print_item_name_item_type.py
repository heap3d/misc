#!/usr/bin/python
import lx
import sys
import modo
sys.path.append("{}\\scripts".format(lx.eval("query platformservice alias ? {kit_h3d_utilites:}")))
import h3d_utils as h3du


def get_item_name(item: modo.Item):
    try:
        return f'{item.name}'
    except AttributeError:
        return '--NO NAME--'


def main():
    for item in modo.Scene().selected:
        print(f'<{get_item_name(item)}>: <{item}> <{h3du.safe_type(item)}>')


main()
