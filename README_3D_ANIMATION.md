# 🎬 RESHMA BANU — Cinematic 3D Typography Animation

Procedural luxury 3D typography project designed for high-end portfolio websites, built in Blender with physically based material morphing.

---

## 📌 Project Overview
- **Main Text**: `"RESHMA BANU"` on a single horizontal line
- **Geometry**: Inflated 3D puffy foil balloon / crystal glass typography with realistic edge bevels, voxel remesh, subsurf smoothing, and procedural micro-crease displacement
- **Scene Collections**:
  - `Typography`: Contains `RESHMA_BANU_3D` mesh
  - `Materials`: Master material node tree `M_ReshmaBanu_Master`
  - `Lights`: 4-point dark studio lighting rig (Key, Fill, Top Rim Strip, Bottom Kicker)
  - `Camera`: 85mm cinematic camera with subtle breathing motion and depth of field
  - `Environment`: Minimal pure black studio environment
- **Timeline**: 35 seconds (1050 frames @ 30 fps)
- **Seamless Loop**: Frame 1050 connects seamlessly back into Frame 1 / Frame 120

---

## 🎨 10 Material States & Animation Timeline

| Time Range | Frame Range | Material State | Description |
|---|---|---|---|
| **0.0s – 4.0s** | 1 – 120 | **Transparent Glass / Crystal** | High-refraction crystal glass emerging from dark studio void |
| **4.0s – 8.0s** | 120 – 240 | **Polished Chrome / Silver** | Ultra-reflective liquid mirror chrome with high specular highlights |
| **8.0s – 12.0s** | 240 – 360 | **Glossy Obsidian Black** | Deep metallic black foil with subtle seam creases |
| **12.0s – 16.0s** | 360 – 480 | **Electric Blue / Purple** | Vibrant royal blue metallic foil with iridescent violet sheen |
| **16.0s – 20.0s** | 480 – 600 | **Hot Pink / Magenta Balloon** | Glossy electric magenta balloon with sharp studio reflections |
| **20.0s – 24.0s** | 600 – 720 | **Soft White Fluffy / Cloud** | Volumetric subsurface scattering cloud/fluff texture |
| **24.0s – 27.0s** | 720 – 810 | **Stretched White Fabric** | Matte textile textile with velvet sheen |
| **27.0s – 30.0s** | 810 – 900 | **Pearlescent Bubbly Foam** | Translucent pearlescent foam with micro scatter |
| **30.0s – 33.0s** | 900 – 990 | **Pink Icing & Sprinkles** | Glossy strawberry frosting with micro sprinkle accents |
| **33.0s – 35.0s** | 990 – 1050 | **Return to Crystal Glass** | Smooth fluid morphing back to transparent glass (**Seamless Loop**) |

---

## 🚀 How to Run & Generate

### Option 1: One-Click Batch File
Double-click `generate_blend.bat` in this folder. It will generate `reshma_banu_typography.blend` and open it directly in Blender.

### Option 2: Command Line (Headless Generation)
```bash
blender --background --python generate_reshma_banu_blender_project.py
```

### Option 3: Inside Blender
1. Open Blender.
2. Go to the **Scripting** workspace tab at the top.
3. Open `generate_reshma_banu_blender_project.py`.
4. Click **Run Script** (or press `Alt + P`).

---

## 🎥 Rendering Video Output
Inside Blender:
1. Set the Output format to **FFmpeg Video** (H.264 / MP4) under Output Properties.
2. Press **Ctrl + F12** (or Render -> Render Animation).
3. The rendered 35-second looping video can be embedded directly into the portfolio hero background!
