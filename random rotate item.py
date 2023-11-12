#!/usr/bin/python
# ================================
# (C)2019 Dmytro Golub
# heap3d@gmail.com
# --------------------------------
# modo python
# rotate selected items by random value
# can be absolute or incremental
# value of channel not changing if rng_* value set to None
# ================================
import modo
import random

scene = modo.scene.current()
absolute = True
rng_x = 360  # set None to skip
rng_y = None  # set None to skip
rng_z = None  # set None to skip

# print scene.selected
random.seed()

incremental = 0 if absolute else 1

for item in scene.selected:
    # print item.name, '...'
    cur_rot = modo.LocatorSuperType(item).rotation.get(degrees=True)
    # print cur_rot
    rnd_x = cur_rot[0]
    rnd_y = cur_rot[1]
    rnd_z = cur_rot[2]

    if rng_x is not None:
        rnd_x = cur_rot[0] * incremental + random.random() * rng_x
    if rng_y is not None:
        rnd_y = cur_rot[1] * incremental + random.random() * rng_y
    if rng_z is not None:
        rnd_z = cur_rot[2] * incremental + random.random() * rng_z

    modo.LocatorSuperType(item).rotation.set((rnd_x, rnd_y, rnd_z), degrees=True)
