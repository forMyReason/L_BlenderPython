import bpy
import bmesh

mesh_obj = bpy.context.active_object

# this mesh must be in edit mode
bm = bmesh.from_edit_mesh(mesh_obj.data)

selected_verts = []

selected_verts = [vert for vert in bm.verts if vert.select]

#for vert in bm.verts:
#    if vert.select:
#        selected_verts.append(vert)

print("selected vert:")
for vert in selected_verts:
    print(f"{vert.index}")

# Modify the BMesh, can do anything here...
#for v in bm.verts:
#    v.co.x += 1.0

# Show the updates in the viewport
# and recalculate n-gon tessellation.
#bmesh.update_edit_mesh(me, loop_triangles=True)

bm.free()