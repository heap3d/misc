#!/usr/bin/python
import modo

scene = modo.Scene()
scene.deselect()
items = scene.items()

meshrefs = set()
for item in items:
    if ":" not in item.id:
        continue
    if "OP10Parts:" in item.id:
        continue
    if "OP20Parts:" in item.id:
        continue
    if "VSC250DUO_MeshRef_01:" in item.id:
        continue
    if "HydraulicGuides_MeshRef:" in item.id:
        continue
    if "Tools:" in item.id:
        continue
    if "RingGear_Parts_Raw_Finished_MeshRef:" in item.id:
        continue

    if item.type == "videoStill":
        continue
    if item.type == "translation":
        continue
    if item.type == "rotation":
        continue
    if item.type == "scale":
        continue

    print(item.id, item.type)
    meshrefs.add(item.id.split(":")[0])
    # scene.removeItems(item)
    # scene.removeItems(item, children=True)

print("\n".join(meshrefs))
