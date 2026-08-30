@echo off
title Generate RESHMA BANU 3D Animation Project
cd /d "%~dp0"

echo ================================================================
echo   Generating Cinematic 3D Typography Project: RESHMA BANU
echo ================================================================

where blender >nul 2>nul
if %ERRORLEVEL% equ 0 (
    blender --background --python generate_reshma_banu_blender_project.py
    echo.
    echo Project successfully created: reshma_banu_typography.blend
    echo Opening in Blender...
    start "" "reshma_banu_typography.blend"
) else (
    echo Blender executable not found in PATH.
    echo Looking in default Blender Foundation directory...
    if exist "C:\Program Files\Blender Foundation\Blender 5.2\blender.exe" (
        "C:\Program Files\Blender Foundation\Blender 5.2\blender.exe" --background --python generate_reshma_banu_blender_project.py
        start "" "C:\Program Files\Blender Foundation\Blender 5.2\blender.exe" "reshma_banu_typography.blend"
    ) else if exist "C:\Program Files\Blender Foundation\Blender 4.2\blender.exe" (
        "C:\Program Files\Blender Foundation\Blender 4.2\blender.exe" --background --python generate_reshma_banu_blender_project.py
        start "" "C:\Program Files\Blender Foundation\Blender 4.2\blender.exe" "reshma_banu_typography.blend"
    ) else (
        echo Please ensure Blender is installed or run this script from inside Blender.
    )
)

pause
