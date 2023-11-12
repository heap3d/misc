#!/usr/bin/python
# ================================
# (C)2019 Dmytro Holub
# heap3d@gmail.com
# --------------------------------
# modo python
# rename selected items by adding prefix and suffix
# ================================
import modo

replace_enable = False
remove_prefix_enable = False
remove_suffix_enable = True
strip_enable = True
suffix_enable = False
suffix_numbering_enable = True
prefix = ''
suffix_base = ' #'
suffix_template = '{}{}'
suffix_start_number = 1
str_find = ''
str_replace = ''
remove_prefix = '] '  # truncate name to position of char sequence
remove_suffix = ' ['  # truncate name from position of char sequence

scene = modo.scene.current()
# print scene.selected

if str_find == '':
    replace_enable = False
if remove_prefix == '':
    remove_prefix_enable = False
if remove_suffix == '':
    remove_suffix_enable = False
suffix = ''  # variable declaration
i = suffix_start_number
for item in scene.selected:
    print item.name
    p_name = item.name
    if suffix_enable:
        suffix = suffix_base
        if suffix_numbering_enable:
            suffix = suffix_template.format(suffix_base, i)
    if remove_prefix_enable:
        rp_pos = p_name.find(remove_prefix)
        if rp_pos >= 0:
            p_name = p_name[rp_pos+len(remove_prefix):]
        print 'removed prefix: {}'.format(p_name)
    if remove_suffix_enable:
        rs_pos = p_name.rfind(remove_suffix)
        if rs_pos >= 0:
            p_name = p_name[:rs_pos]
        print 'removed suffix: {}'.format(p_name)
    if replace_enable:
        p_name = p_name.replace(str_find, str_replace)
        print 'replaced: {}'.format(p_name)
    if strip_enable:
        p_name = p_name.strip()
    item.name = prefix + p_name + suffix
    i += 1
