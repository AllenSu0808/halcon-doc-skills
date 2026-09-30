# set_scene_3d_camera_pose (Operator)

## Name

`set_scene_3d_camera_pose` — Set the pose of a camera in a 3D scene.

## Signature

`set_scene_3d_camera_pose( : : Scene3D, CameraIndex, Pose : )`

## Description

`set_scene_3d_camera_pose` sets the *`Pose`* of the camera
*`CameraIndex`* in the 3D scene *`Scene3D`*.

See [`create_scene_3d`](create_scene_3d.md) for more details on the coordinate systems used
in 3D scenes.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Scene3D`** (input_control)  scene_3d `→`  (handle)

Handle of the 3D scene.

**`CameraIndex`** (input_control)  integer `→`  (integer)

Index of the camera.

**`Pose`** (input_control)  pose `→`  (real / integer)

New pose of the camera.

## Result

`set_scene_3d_camera_pose` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Predecessors

`add_scene_3d_camera`

## See also

`set_scene_3d_to_world_pose`,
`set_scene_3d_instance_pose`

## Module

3D Metrology
