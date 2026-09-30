# remove_scene_3d_camera (Operator)

## Name

`remove_scene_3d_camera` — Remove a camera from a 3D scene.

## Signature

`def remove_scene_3d_camera(scene_3d: HHandle, camera_index: int) -> None`

## Description

`remove_scene_3d_camera` removes the camera *`camera_index`* from
the 3D scene *`scene_3d`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`scene_3d`** (input_control)  scene_3d `→` HHandle

Handle of the 3D scene.

**`camera_index`** (input_control)  integer `→` int

Index of the camera to remove.

## Result

`remove_scene_3d_camera` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## See also

`add_scene_3d_camera`

## Module

3D Metrology
