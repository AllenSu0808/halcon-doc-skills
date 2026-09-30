# remove_scene_3d_camera (Operator)

## Name

`remove_scene_3d_camera` — Remove a camera from a 3D scene.

## Signature

`remove_scene_3d_camera( : : Scene3D, CameraIndex : )`

## Description

`remove_scene_3d_camera` removes the camera *`CameraIndex`* from
the 3D scene *`Scene3D`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Scene3D`** (input_control)  scene_3d `→`  (handle)

Handle of the 3D scene.

**`CameraIndex`** (input_control)  integer `→`  (integer)

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
