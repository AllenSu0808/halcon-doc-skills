# remove_scene_3d_light (Operator)

## Name

`remove_scene_3d_light` — Remove a light from a 3D scene.

## Signature

`def remove_scene_3d_light(scene_3d: HHandle, light_index: int) -> None`

## Description

`remove_scene_3d_light` removes the light *`light_index`*
from the 3D scene *`scene_3d`* in future versions. Currently only one
light source is supported.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`scene_3d`** (input_control)  scene_3d `→` HHandle

Handle of the 3D scene.

**`light_index`** (input_control)  integer `→` int

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
