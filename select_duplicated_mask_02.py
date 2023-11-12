#!/usr/bin/python
# ================================
# (C)2020 Dmytro Holub
# heap3d@gmail.com
# --------------------------------
# modo python
# select duplicated material mask, keep topmost unselected
# ================================

import modo
import lx
import os

scene = modo.scene.current()

compare_by_material_tag = False
compare_by_selection_set_tag = False
compare_by_part_tag = False
compare_by_item_mask = False
compare_by_all = False
clear_selection = False
delete_material_mask = False

cbl_all = 'all'
cbl_material = 'material'
cbl_selection_set = 'selection set'
cbl_part = 'part'
cbl_item_mask = 'item mask'

# comparedBy user.value
userVal_compareBy_name = 'h3d_select_duplicated_compareBy'
userVal_compareBy_username = 'select duplicated material mask by'
userVal_compareBy_dialogname = 'choose selection filter'
userVal_compareBy_list = '{0};{1};{2};{3};{4}'.format(cbl_all, cbl_item_mask, cbl_material, cbl_selection_set, cbl_part)

# clear_selection user.value
userVal_clear_selection_name = 'h3d_select_duplicated_clear_selection'
userVal_clear_selection_username = 'clear selection'
userVal_clear_selection_dialogname = 'turn ON to clear selection'

# delete_material_mask user.value
userVal_delete_material_mask_name = 'h3d_select_duplicated_delete_material_mask'
userVal_delete_material_mask_username = 'delete material mask'
userVal_delete_material_mask_dialogname = 'turn ON to delete material mask'

fileLogName = os.path.join(os.path.dirname(scene.filename), (os.path.splitext(os.path.basename(scene.filename))[0])+'_select_duplicated_mask_02'+'.log')  # get log file name
f_log = open(fileLogName, 'w')  # define log file (override)


# print decorator
def print_log_decorator(func):
    def wrap(text='', enabled=True, line_div=''):
        if enabled:
            func(text)
            if line_div != '':
                func(line_div)
    return wrap
@print_log_decorator
def print_log(text, enabled=True, line_div=''):
    print >> f_log, text


def get_mask_list():
    mtag_mask_list = []
    if compare_by_material_tag:
        # include mask with Polygon Tag Type <Material> only and polygon tag not <(all)>
        for mask_item in scene.renderItem.children(True, 'mask'):
            tag_type = mask_item.channel('ptyp').get()
            mtag = mask_item.channel('ptag').get()
            if tag_type == 'Material' or tag_type == '':
                if mtag != '(none)' and mtag != '':
                    mtag_mask_list.append(mask_item)
    else:
        mtag_mask_list = scene.renderItem.children(True, 'mask')
    return mtag_mask_list


def get_ptag(mask_item):
    ptag = mask_item.channel('ptag').get()
    return ptag


def get_ptag_type(mask_item):
    ptyp = mask_item.channel('ptyp').get()
    return ptyp


def get_item_mask(mask_item):
    mask_item.select(True)
    item_mask = lx.eval('mask.setMesh ?')
    # print ('mask: {} item mask: <{}>'.format(mask_item.name, item_mask))
    return item_mask


def are_mask_equal(mask1, mask2):
    print_log('  comparing to <{}>'.format(mask2.name))
    childrens1 = len(mask1.children(recursive=False, itemType='mask'))
    if childrens1 != 0:
        # print('<{}> has {} children(s)'.format(mask1.name, childrens1))
        return False
    childrens2 = len(mask2.children(recursive=False, itemType='mask'))
    if childrens2 != 0:
        # print('<{}> has {} children(s)'.format(mask2.name, childrens2))
        return False
    if get_item_mask(mask1) == get_item_mask(mask2):
        if get_ptag_type(mask1) == get_ptag_type(mask2):
            if get_ptag(mask1) == get_ptag(mask2):
                # print('EQUAL')
                return True
    return False


print_log('----------')
print_log('start...')
print('----------')
print('start...')

# comparedBy user.value
if not lx.eval('query scriptsysservice userValue.isDefined ? {%s}' % userVal_compareBy_name):
    lx.eval('user.defNew {%s} integer life:config' % userVal_compareBy_name)
lx.eval('user.def {%s} list {%s}' % (userVal_compareBy_name, userVal_compareBy_list))
lx.eval('user.def {%s} username {%s}' % (userVal_compareBy_name, userVal_compareBy_username))
lx.eval('user.def {%s} dialogname {%s}' % (userVal_compareBy_name, userVal_compareBy_dialogname))

# clear_selection user.value
if not lx.eval('query scriptsysservice userValue.isDefined ? {%s}' % userVal_clear_selection_name):
    lx.eval('user.defNew {%s} boolean life:config' % userVal_clear_selection_name)

# delete_material_mask user.value
if not lx.eval('query scriptsysservice userValue.isDefined ? {%s}' % userVal_delete_material_mask_name):
    lx.eval('user.defNew {%s} boolean life:config' % userVal_delete_material_mask_name)

try:
    lx.eval('user.value {%s}' % userVal_compareBy_name)
except:
    print 'aborted.'
    f_log.close()
    exit()

compareBy_value = lx.eval('user.value {%s} ?' % userVal_compareBy_name)
# print('compareBy index: {}   list: {}'.format(compareBy_value, userVal_compareBy_list))
compare_by_material_tag = compareBy_value == cbl_material
compare_by_selection_set_tag = compareBy_value == cbl_selection_set
compare_by_part_tag = compareBy_value == cbl_part
compare_by_item_mask = compareBy_value == cbl_item_mask
compare_by_all = compareBy_value == cbl_all

try:

    # keep top mask unselected
    duplicated_mask_list = set()
    # processed_tag_list = {}
    scene_mask_list = get_mask_list()
    print_log('scene_mask_list[{}]: <{}>'.format(len(scene_mask_list), scene_mask_list))
    tmp_scene_list = set(scene_mask_list)
    print_log('tmp_scene_list[{}]: <{}>'.format(len(tmp_scene_list), tmp_scene_list))
    for mask in scene_mask_list:
        print_log('current mask: <{}>'.format(mask.name))
        if mask in tmp_scene_list:
            tmp_scene_list.remove(mask)
        print_log('tmp_scene_list remove(mask)[{}]: <{}>'.format(len(tmp_scene_list), tmp_scene_list))
        processed_list = set(tmp_scene_list)
        print_log('processed_list[{}]: <{}>'.format(len(processed_list), processed_list))
        for compared_mask in processed_list:
            print_log('compared_mask: <{}>'.format(compared_mask))
            if are_mask_equal(mask, compared_mask):
                print_log('  --> equal')
                tmp_scene_list.remove(compared_mask)
                duplicated_mask_list.add(compared_mask)
                print_log('tmp_scene_list remove compared_mask[{}]: <{}>'.format(len(tmp_scene_list), tmp_scene_list))
    # clear selection
    scene.deselect()
    # select duplicated masks
    for mask in duplicated_mask_list:
        mask.select()
    if len(duplicated_mask_list) > 0:
        lx.eval('item.editorColor yellow')
    print_log('{} duplicated mask selected'.format(len(duplicated_mask_list)))
except LookupError:
    print_log('Error found.')
finally:
    print_log('done.')
    print('done.')
    f_log.close()
