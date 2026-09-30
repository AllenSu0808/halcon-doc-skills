# remove_scene_3d_light (Operator)

## Name

`remove_scene_3d_light` — Remove a light from a 3D scene.

## Signature

`remove_scene_3d_light( : : Scene3D, LightIndex : )`

## Description

`remove_scene_3d_light` removes the light *`LightIndex`*
from the 3D scene *`Scene3D`* in future versions. Currently only one
light source is supported.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Scene3D`** (input_control)  scene_3d `→`  (handle)

Handle of the 3D scene.

**`LightIndex`** (input_control)  integer `→`  (integer)

Light to remove.

## Result

`remove_scene_3d_light` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## See also

`add_scene_3d_light`

## Module

3D Metrology
