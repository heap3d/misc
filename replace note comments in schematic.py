#!/usr/bin/python
# ================================
# (C)2020 Dmytro Holub
# heap3d@gmail.com
# --------------------------------
# modo python
# replace comment in schematic notes
# ================================

import modo

selection = modo.scene.current().selected
for item in selection:
    print item.name
    for channel in item.iterChannels():
        if channel.name == 'comment':
            value = channel.get()
            channel.set(value.replace('30.5', '30.6'))
        print '{}: <{}>'.format(channel.name, channel.get())
