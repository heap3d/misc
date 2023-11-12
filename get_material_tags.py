import modo

scene = modo.scene.current()

selectedMeshes = scene.selectedByType('mesh')  # selected meshes
# selectedMeshes = scene.items('mesh')  # all meshes
print selectedMeshes

tagSet = set()  # python sets - Set elements are unique. Duplicate elements are not allowed
for mesh in selectedMeshes:
    print mesh.name
    meshSet = set()
    for poly in mesh.geometry.polygons:
        meshSet.add(poly.materialTag)
    for mTag in meshSet:
        print '   <{}>'.format(mTag)

    tagSet = tagSet | meshSet
    print tagSet
