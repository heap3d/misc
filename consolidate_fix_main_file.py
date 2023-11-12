#!/usr/bin/python
# ================================
# (C)2019 Dmytro Holub
# heap3d@gmail.com
# --------------------------------
# modo python
# channel set setup value - workaround for consolidate bug
# ================================

import modo

print 20*'-'
print

items = modo.scene.current().items('locator')
for item in items:
    print '{} :: {}'.format(item.name, item)
    try:
        for transform in item.transforms:
            edit_val = transform.get(action='edit')
            transform.set(edit_val, action='setup')
            setup_val = transform.get(action='setup')
            print '{}{} : {}'.format(3*' ', transform.name, setup_val)
    except:
        print '{}{} : --- error ---'.format(3*' ', item.name)

    try:
        for channel in item.channels:
            edit_val = channel.get(action='edit')
            channel.set(edit_val, action='setup')
            setup_val = channel.get(action='setup')
            print '{}{} : {}'.format(3 * ' ', channel.name, edit_val)
    except:
        print '{}{} : --- error ---'.format(3*' ', item.name)
