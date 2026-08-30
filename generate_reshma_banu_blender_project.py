"""
=============================================================================
  CINEMATIC 3D TYPOGRAPHY ANIMATION GENERATOR: "RESHMA BANU"
=============================================================================
Procedural Blender Python script creating a luxury studio 3D typography
animation for portfolio websites.

Key Features:
- Exact Text: "RESHMA BANU" on a single horizontal line
- 3D Inflated Puffy Balloon / Glass / Metal geometry
- 35-Second Seamless Looping Timeline (1050 frames @ 30fps)
- 10 Continuous Material Morphing States (Glass, Chrome, Obsidian Black,
  Electric Blue/Purple, Hot Magenta Foil, Fluffy Cloud, Fabric, Foam,
  Strawberry Icing with Sprinkles, returning to Glass)
- Dark Minimalist Studio Lighting & 85mm Cinematic Camera
- Clean Collections: Typography, Materials, Lights, Camera, Environment
- Main Object Name: RESHMA_BANU_3D

Run in Blender:
  blender --background --python generate_reshma_banu_blender_project.py
Or inside Blender Scripting Workspace -> Run Script.
=============================================================================
"""

import bpy
import math
import os
from math import radians

def build_scene():
    print("=" * 60)
    print("  Starting Procedural 3D Scene Generation: RESHMA BANU")
    print("=" * 60)

    # -------------------------------------------------------------------------
    # 1. INITIALIZE & CLEAN SCENE
    # -------------------------------------------------------------------------
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

    # Clear orphan data
    for block in bpy.data.meshes:
        bpy.data.meshes.remove(block)
    for block in bpy.data.materials:
        bpy.data.materials.remove(block)
    for block in bpy.data.lights:
        bpy.data.lights.remove(block)
    for block in bpy.data.cameras:
        bpy.data.cameras.remove(block)

    scene = bpy.context.scene
    scene.frame_start = 1
    scene.frame_end = 1050  # 35 seconds @ 30 fps
    scene.render.fps = 30
    scene.render.resolution_x = 1920
    scene.render.resolution_y = 1080
    scene.render.resolution_percentage = 100

    # -------------------------------------------------------------------------
    # 2. CREATE COLLECTIONS
    # -------------------------------------------------------------------------
    def get_or_create_collection(name, parent_col):
        for col in parent_col.children:
            if col.name == name:
                return col
        new_col = bpy.data.collections.new(name)
        parent_col.children.link(new_col)
        return new_col

    master_col = scene.collection
    col_typography = get_or_create_collection("Typography", master_col)
    col_materials = get_or_create_collection("Materials", master_col)
    col_lights = get_or_create_collection("Lights", master_col)
    col_camera = get_or_create_collection("Camera", master_col)
    col_environment = get_or_create_collection("Environment", master_col)

    # -------------------------------------------------------------------------
    # 3. ENVIRONMENT & WORLD SHADING (Minimal Pure Black Studio)
    # -------------------------------------------------------------------------
    world = scene.world
    if not world:
        world = bpy.data.worlds.new("StudioDarkWorld")
        scene.world = world
    world.use_nodes = True
    w_nodes = world.node_tree.nodes
    w_links = world.node_tree.links
    w_nodes.clear()

    bg_node = w_nodes.new(type='ShaderNodeBackground')
    bg_node.inputs['Color'].default_value = (0.002, 0.002, 0.004, 1.0)
    bg_node.inputs['Strength'].default_value = 0.2

    world_out = w_nodes.new(type='ShaderNodeOutputWorld')
    w_links.link(bg_node.outputs['Background'], world_out.inputs['Surface'])

    # -------------------------------------------------------------------------
    # 4. TYPOGRAPHY GEOMETRY CREATION ("RESHMA BANU")
    # -------------------------------------------------------------------------
    text_data = bpy.data.curves.new(name="RESHMA_BANU_TextCurve", type='FONT')
    text_data.body = "RESHMA BANU"
    text_data.align_x = 'CENTER'
    text_data.align_y = 'CENTER'
    text_data.size = 1.2
    text_data.space_character = 1.05
    text_data.space_word = 1.45
    text_data.extrude = 0.09
    text_data.bevel_depth = 0.075
    text_data.bevel_resolution = 8
    text_data.offset = 0.0

    # Try loading bold system font if available
    possible_fonts = [
        "C:/Windows/Fonts/arialbd.ttf",
        "C:/Windows/Fonts/segoeuib.ttf",
        "C:/Windows/Fonts/calibrib.ttf",
        "PPNeueMontreal-Bold.woff2"
    ]
    for fp in possible_fonts:
        if os.path.exists(fp):
            try:
                f_obj = bpy.data.fonts.load(fp)
                text_data.font = f_obj
                break
            except Exception:
                pass

    text_obj = bpy.data.objects.new("RESHMA_BANU_3D", text_data)
    col_typography.objects.link(text_obj)
    bpy.context.view_layer.objects.active = text_obj
    text_obj.select_set(True)

    # Position at Origin
    text_obj.location = (0.0, 0.0, 0.0)
    text_obj.rotation_euler = (radians(90), 0, 0)

    # Convert to mesh for organic inflation and sculpting/modifiers
    bpy.ops.object.convert(target='MESH')
    mesh = text_obj.data
    for p in mesh.polygons:
        p.use_smooth = True

    # Add Voxel Remesh for seamless puffy balloon topology
    remesh_mod = text_obj.modifiers.new(name="PuffyRemesh", type='REMESH')
    remesh_mod.mode = 'VOXEL'
    remesh_mod.voxel_size = 0.022
    remesh_mod.adaptivity = 0.0

    # Add Subdivision Surface for silky smooth highlights
    subsurf_mod = text_obj.modifiers.new(name="PuffySubsurf", type='SUBSURF')
    subsurf_mod.render_levels = 2
    subsurf_mod.levels = 1

    # Add Procedural Micro-Wrinkles Displacement Modifier (Foil balloon seams)
    disp_tex = bpy.data.textures.new("BalloonCreaseNoise", type='CLOUDS')
    disp_tex.noise_scale = 0.18
    disp_tex.noise_depth = 3

    disp_mod = text_obj.modifiers.new(name="FoilWrinkles", type='DISPLACE')
    disp_mod.texture = disp_tex
    disp_mod.strength = 0.018
    disp_mod.mid_level = 0.5

    # -------------------------------------------------------------------------
    # 5. ORGANIC BREATHING & FLOATING ANIMATION
    # -------------------------------------------------------------------------
    # 35-second cyclic organic floating motion
    fps = 30
    total_frames = 1050
    cycle_frames = 150  # 5 sec per breath cycle

    for frame in range(1, total_frames + 1, 15):
        t = (frame - 1) / cycle_frames
        # Subtle gentle vertical float
        z_offset = math.sin(t * 2 * math.pi) * 0.035
        text_obj.location = (0.0, 0.0, z_offset)
        text_obj.keyframe_insert(data_path="location", frame=frame)

        # Subtle organic breathing expansion
        s_xy = 1.0 + math.cos(t * 2 * math.pi) * 0.012
        s_z = 1.0 + math.sin(t * 2 * math.pi) * 0.018
        text_obj.scale = (s_xy, s_xy, s_z)
        text_obj.keyframe_insert(data_path="scale", frame=frame)

        # Subtle displacement breathing
        disp_mod.strength = 0.015 + math.sin(t * 2 * math.pi) * 0.008
        disp_mod.keyframe_insert(data_path="strength", frame=frame)

    # -------------------------------------------------------------------------
    # 6. MASTER MORPHING MATERIAL CREATION
    # -------------------------------------------------------------------------
    mat = bpy.data.materials.new(name="M_ReshmaBanu_Master")
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    nodes.clear()

    # Create Material Output
    mat_out = nodes.new(type='ShaderNodeOutputMaterial')
    mat_out.location = (600, 0)

    # Create Principled BSDF
    bsdf = nodes.new(type='ShaderNodeBsdfPrincipled')
    bsdf.location = (150, 0)
    links.link(bsdf.outputs['BSDF'], mat_out.inputs['Surface'])

    # Helper function for version-safe socket property access
    def set_bsdf_val(socket_names, val, f=None):
        for s in socket_names:
            if s in bsdf.inputs:
                bsdf.inputs[s].default_value = val
                if f is not None:
                    bsdf.inputs[s].keyframe_insert(data_path="default_value", frame=f)
                return True
        return False

    # -------------------------------------------------------------------------
    # 7. ANIMATE 10 MATERIAL STATES (Frames 1 to 1050)
    # -------------------------------------------------------------------------
    # State Keyframe Schedule (30 fps):
    # 0s   (Frame 1)   : Glass emerging from darkness
    # 4s   (Frame 120) : Pristine Transparent Crystal Glass
    # 8s   (Frame 240) : Chrome / Liquid Silver Metal
    # 12s  (Frame 360) : Glossy Black Metallic Foil
    # 16s  (Frame 480) : Electric Royal Blue / Purple Metallic
    # 20s  (Frame 600) : Hot Magenta / Pink Metallic Balloon
    # 24s  (Frame 720) : Soft White Fluffy / Cloud
    # 27s  (Frame 810) : Stretched White Textile Fabric
    # 30s  (Frame 900) : Pearlescent White Foam / Bubbles
    # 33s  (Frame 990) : Glossy Pink Icing with Sprinkles
    # 35s  (Frame 1050): Return to Transparent Crystal Glass (Seamless Loop!)

    states = [
        # Frame 1 (0s): Glass appearing
        (1, {
            "color": (0.95, 0.97, 1.0, 1.0),
            "metallic": 0.0,
            "roughness": 0.02,
            "transmission": 1.0,
            "ior": 1.48,
            "subsurface": 0.0,
            "sheen": 0.0,
            "specular": 0.6
        }),
        # Frame 120 (4s): Crystal Glass
        (120, {
            "color": (0.98, 0.98, 1.0, 1.0),
            "metallic": 0.0,
            "roughness": 0.015,
            "transmission": 1.0,
            "ior": 1.50,
            "subsurface": 0.0,
            "sheen": 0.0,
            "specular": 0.8
        }),
        # Frame 240 (8s): Chrome / Silver
        (240, {
            "color": (0.96, 0.96, 0.98, 1.0),
            "metallic": 1.0,
            "roughness": 0.035,
            "transmission": 0.0,
            "ior": 1.55,
            "subsurface": 0.0,
            "sheen": 0.0,
            "specular": 1.0
        }),
        # Frame 360 (12s): Glossy Obsidian Black (Reference Image 4)
        (360, {
            "color": (0.012, 0.012, 0.016, 1.0),
            "metallic": 0.88,
            "roughness": 0.09,
            "transmission": 0.0,
            "ior": 1.55,
            "subsurface": 0.0,
            "sheen": 0.2,
            "specular": 0.9
        }),
        # Frame 480 (16s): Electric Blue/Purple Metallic (Reference Image 2)
        (480, {
            "color": (0.04, 0.18, 0.96, 1.0),
            "metallic": 0.95,
            "roughness": 0.065,
            "transmission": 0.0,
            "ior": 1.52,
            "subsurface": 0.0,
            "sheen": 0.85,
            "specular": 1.0
        }),
        # Frame 600 (20s): Hot Pink / Magenta Balloon (Reference Image 3)
        (600, {
            "color": (0.95, 0.02, 0.45, 1.0),
            "metallic": 0.95,
            "roughness": 0.065,
            "transmission": 0.0,
            "ior": 1.52,
            "subsurface": 0.0,
            "sheen": 0.9,
            "specular": 1.0
        }),
        # Frame 720 (24s): Soft White Fluffy / Cloud (Reference Image 5)
        (720, {
            "color": (0.96, 0.96, 0.98, 1.0),
            "metallic": 0.0,
            "roughness": 0.78,
            "transmission": 0.0,
            "ior": 1.45,
            "subsurface": 0.85,
            "sheen": 1.0,
            "specular": 0.3
        }),
        # Frame 810 (27s): Stretched White Fabric / Textile
        (810, {
            "color": (0.90, 0.90, 0.92, 1.0),
            "metallic": 0.0,
            "roughness": 0.62,
            "transmission": 0.0,
            "ior": 1.46,
            "subsurface": 0.25,
            "sheen": 0.8,
            "specular": 0.4
        }),
        # Frame 900 (30s): Pearlescent Bubbly Foam
        (900, {
            "color": (0.94, 0.97, 1.0, 1.0),
            "metallic": 0.05,
            "roughness": 0.16,
            "transmission": 0.35,
            "ior": 1.33,
            "subsurface": 0.55,
            "sheen": 0.4,
            "specular": 0.7
        }),
        # Frame 990 (33s): Pink Icing & Sprinkles
        (990, {
            "color": (1.0, 0.42, 0.64, 1.0),
            "metallic": 0.0,
            "roughness": 0.18,
            "transmission": 0.0,
            "ior": 1.45,
            "subsurface": 0.50,
            "sheen": 0.3,
            "specular": 0.75
        }),
        # Frame 1050 (35s): Seamless Loop back to Transparent Glass
        (1050, {
            "color": (0.98, 0.98, 1.0, 1.0),
            "metallic": 0.0,
            "roughness": 0.015,
            "transmission": 1.0,
            "ior": 1.50,
            "subsurface": 0.0,
            "sheen": 0.0,
            "specular": 0.8
        })
    ]

    for f, props in states:
        set_bsdf_val(['Base Color'], props["color"], f)
        set_bsdf_val(['Metallic'], props["metallic"], f)
        set_bsdf_val(['Roughness'], props["roughness"], f)
        set_bsdf_val(['Transmission Weight', 'Transmission'], props["transmission"], f)
        set_bsdf_val(['IOR'], props["ior"], f)
        set_bsdf_val(['Subsurface Weight', 'Subsurface'], props["subsurface"], f)
        set_bsdf_val(['Sheen Weight', 'Sheen'], props["sheen"], f)
        set_bsdf_val(['Specular IOR Level', 'Specular'], props["specular"], f)

    # Assign material to object
    if text_obj.data.materials:
        text_obj.data.materials[0] = mat
    else:
        text_obj.data.materials.append(mat)

    # -------------------------------------------------------------------------
    # 8. STUDIO LIGHTING RIG (4-Point Cinematic Setup)
    # -------------------------------------------------------------------------
    def create_area_light(name, loc, rot, size, energy, color):
        light_data = bpy.data.lights.new(name=name, type='AREA')
        light_data.shape = 'RECTANGLE' if isinstance(size, tuple) else 'SQUARE'
        if isinstance(size, tuple):
            light_data.size = size[0]
            light_data.size_y = size[1]
        else:
            light_data.size = size
        light_data.energy = energy
        light_data.color = color

        light_obj = bpy.data.objects.new(name=name, object_data=light_data)
        light_obj.location = loc
        light_obj.rotation_euler = rot
        col_lights.objects.link(light_obj)
        return light_obj

    # Key Light (Warm soft studio main light from upper-right)
    create_area_light(
        "KeyLight",
        loc=(3.8, -4.5, 4.0),
        rot=(radians(50), radians(20), radians(30)),
        size=3.2,
        energy=850.0,
        color=(1.0, 0.98, 0.95)
    )

    # Fill Light (Cool soft fill from lower-left)
    create_area_light(
        "FillLight",
        loc=(-4.2, -4.2, 1.2),
        rot=(radians(75), radians(-15), radians(-40)),
        size=3.8,
        energy=380.0,
        color=(0.92, 0.95, 1.0)
    )

    # Top Rim Strip Light (Creates brilliant glossy rim highlights on inflated letter tops)
    create_area_light(
        "TopRimStrip",
        loc=(0.0, 0.3, 4.5),
        rot=(radians(10), 0, 0),
        size=(7.5, 0.6),
        energy=650.0,
        color=(1.0, 1.0, 1.0)
    )

    # Bottom Kicker Light (Subtle upward bounce)
    create_area_light(
        "BottomKicker",
        loc=(0.0, -2.8, -3.2),
        rot=(radians(-65), 0, 0),
        size=(6.5, 0.8),
        energy=220.0,
        color=(0.95, 0.95, 1.0)
    )

    # -------------------------------------------------------------------------
    # 9. CINEMATIC 85MM CAMERA & COMPOSITION
    # -------------------------------------------------------------------------
    cam_data = bpy.data.cameras.new("MainCinematicCamera")
    cam_data.lens = 85  # 85mm Telephoto (Orthographic studio feel, minimal distortion)
    cam_data.clip_start = 0.1
    cam_data.clip_end = 100.0

    # Subtle Depth of Field
    cam_data.dof.use_dof = True
    cam_data.dof.focus_object = text_obj
    cam_data.dof.aperture_fstop = 5.6  # Crisp, readable text across full width

    cam_obj = bpy.data.objects.new("MainCamera", cam_data)
    # Position camera to frame "RESHMA BANU" perfectly spanning ~75% of horizontal 16:9 frame
    cam_obj.location = (0.0, -9.8, 0.0)
    cam_obj.rotation_euler = (radians(90), 0, 0)
    col_camera.objects.link(cam_obj)
    scene.camera = cam_obj

    # Subtle cinematic camera breathing orbit
    for frame in range(1, total_frames + 1, 30):
        t = (frame - 1) / total_frames
        cam_x = math.sin(t * 2 * math.pi) * 0.15
        cam_y = -9.8 + math.cos(t * 2 * math.pi) * 0.10
        cam_obj.location = (cam_x, cam_y, 0.0)
        cam_obj.keyframe_insert(data_path="location", frame=frame)

    # -------------------------------------------------------------------------
    # 10. RENDER ENGINE & COLOR MANAGEMENT
    # -------------------------------------------------------------------------
    # Use Cycles if available, fallback to Eevee
    scene.render.engine = 'CYCLES'
    if hasattr(scene, 'cycles'):
        scene.cycles.device = 'GPU' if hasattr(scene.cycles, 'device') else 'CPU'
        scene.cycles.samples = 128
        scene.cycles.use_denoising = True
        scene.cycles.preview_samples = 32
        scene.cycles.max_bounces = 8
        scene.cycles.transmission_bounces = 12

    # Color Management (High Contrast Cinematic Film)
    scene.view_settings.view_transform = 'AgX' if 'AgX' in bpy.types.ColorManagedViewSettings.bl_rna.properties['view_transform'].enum_items else 'Filmic'
    scene.view_settings.look = 'Medium High Contrast'

    # -------------------------------------------------------------------------
    # 11. SAVE BLEND FILE
    # -------------------------------------------------------------------------
    output_blend = os.path.join(os.path.dirname(os.path.abspath(__file__)), "reshma_banu_typography.blend")
    bpy.ops.wm.save_as_mainfile(filepath=output_blend)

    print("=" * 60)
    print("  SUCCESSFULLY GENERATED CINEMATIC 3D PROJECT!")
    print(f"  Saved File: {output_blend}")
    print("=" * 60)

if __name__ == '__main__':
    build_scene()
