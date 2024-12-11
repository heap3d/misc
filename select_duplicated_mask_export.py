#!/usr/bin/python
# ================================
# (C)2020-2024 Dmytro Holub
# heap3d@gmail.com
# --------------------------------
# modo python
# select duplicated material mask, keep topmost unselected
# ================================

import modo
import lx


COMPARE_BY_MATERIAL_TAG = False
EMPTY_PTAG = 'Material'
SELECTION_COLOR = 'yellow'


def get_mask_list():
    mtag_mask_list = []
    if COMPARE_BY_MATERIAL_TAG:
        for mask_item in scene.renderItem.children(True, 'mask'):
            tag_type = mask_item.channel('ptyp').get()
            mtag = mask_item.channel('ptag').get()
            if tag_type == 'Material' or tag_type == '':
                if mtag != '(none)' and mtag != '':
                    mtag_mask_list.append(mask_item)
    else:
        mtag_mask_list = scene.renderItem.children(True, 'mask')
    return mtag_mask_list


def are_mask_equal(mask1, mask2):
    childrens1 = len(mask1.children(recursive=False, itemType='mask'))
    if childrens1 != 0:
        return False
    childrens2 = len(mask2.children(recursive=False, itemType='mask'))
    if childrens2 != 0:
        return False
    if get_item_mask(mask1) == get_item_mask(mask2):
        if get_ptag_type(mask1) == get_ptag_type(mask2):
            if get_ptag(mask1) == get_ptag(mask2):
                return True
    return False


def get_ptag_type(mask_item):
    ptyp = mask_item.channel('ptyp').get()
    if not ptyp:
        return EMPTY_PTAG
    return ptyp


def get_item_mask(mask_item):
    mask_item.select(True)
    item_mask = lx.eval('mask.setMesh ?')
    return item_mask


def get_ptag(mask_item):
    ptag = mask_item.channel('ptag').get()
    return ptag


def main():
    print('')
    print('start select_duplicated_mask.py ...')

    try:

        duplicated_mask_list = set()
        scene_mask_list = get_mask_list()
        tmp_scene_list = set(scene_mask_list)
        for mask in scene_mask_list:
            if mask in tmp_scene_list:
                tmp_scene_list.remove(mask)
            processed_list = set(tmp_scene_list)
            for compared_mask in processed_list:
                if are_mask_equal(mask, compared_mask):
                    tmp_scene_list.remove(compared_mask)
                    duplicated_mask_list.add(compared_mask)
        scene.deselect()
        for mask in duplicated_mask_list:
            mask.select()
        if len(duplicated_mask_list) > 0:
            lx.eval(f'item.editorColor {SELECTION_COLOR}')
    except LookupError:
        print('Error found.')
    finally:
        print('')
        print('select_duplicated_mask.py done.')


if __name__ == '__main__':
    scene = modo.Scene()
    main()
