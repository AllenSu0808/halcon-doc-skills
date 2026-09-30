# add_scene_3d_camera (Operator)

## Name

`add_scene_3d_camera` — Add a camera to a 3D scene.

## Signature

`add_scene_3d_camera( : : Scene3D, CameraParam : CameraIndex)`

## Description

`add_scene_3d_camera` adds a new camera to the 3D scene
*`Scene3D`* and returns the index of this camera in
*`CameraIndex`*. The camera parameters of the camera must be
given in *`CameraParam`*. By default the new camera is located
at the origin of the world coordinate system. The pose of the camera
*`CameraIndex`* can be set with [`set_scene_3d_camera_pose`](set_scene_3d_camera_pose.md).

## Attention

Cameras with hypercentric lenses are not supported.
For displaying large faces (or primitives) with a non-zero distortion
in *`CameraParam`*, note that the distortion is only applied to the
points of the model. In the projection, these points are subsequently
connected by straight lines. For a good approximation of the distorted
lines, please use a triangulation with sufficiently small triangles.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Scene3D`** (input_control)  scene_3d `→`  (handle)

Handle of the 3D scene.

**`CameraParam`** (input_control)  campar `→`  (real / integer / string)

Parameters of the new camera.

**`CameraIndex`** (output_control)  integer `→`  (integer)

Index of the new camera in the 3D scene.

## Result

`add_scene_3d_camera` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Predecessors

`create_scene_3d`

## Possible Successors

`set_scene_3d_camera_pose`,
`display_scene_3d`

## Module

3D Metrology
