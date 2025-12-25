import bpy
for obj in bpy.data.objects:
    if obj.name.startswith(("Cube", "Circle")):
        bpy.data.objects.remove(obj, do_unlink=True)




bpy.ops.mesh.primitive_cube_add(location=(0,0,0.75))
cube=bpy.context.active_object
cube.name="Cube"
cube_mat = bpy.data.materials.new(name="Cube_Mat")
cube_mat.use_nodes = True
cube_mat.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = (1, 0, 0, 1)
cube.data.materials.append(cube_mat)


cube.keyframe_insert(data_path="location",frame=1)

cube.location.z=5

cube.keyframe_insert(data_path="location",frame=100)

cube.hide_viewport=False
cube.hide_render=False

cube.keyframe_insert(data_path="hide_viewport",frame=100)
cube.keyframe_insert(data_path="hide_render",frame=100)

cube.hide_viewport=True
cube.hide_render=True

cube.keyframe_insert(data_path="hide_viewport",frame=119)
cube.keyframe_insert(data_path="hide_viewport",frame=119)



bpy.ops.mesh.primitive_cylinder_add(location=(0,0,5))
circle=bpy.context.active_object
circle.name="Circle"
circle_mat = bpy.data.materials.new(name="Circle_Mat")
circle_mat.use_nodes = True
circle_mat.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = (0, 0, 1, 1)
circle.data.materials.clear()
circle.data.materials.append(circle_mat)



circle.hide_viewport=True
circle.hide_render=True

circle.keyframe_insert(data_path="hide_viewport",frame=119)
circle.keyframe_insert(data_path="hide_render",frame=119)

circle.hide_viewport=False
circle.hide_render=False

circle.keyframe_insert(data_path="hide_viewport",frame=120)
circle.keyframe_insert(data_path="hide_render",frame=120)

circle.location = (0, 0, 5)
circle.keyframe_insert("location", frame=120)

circle.location = (5, 0, -5)
circle.keyframe_insert("location", frame=180)
