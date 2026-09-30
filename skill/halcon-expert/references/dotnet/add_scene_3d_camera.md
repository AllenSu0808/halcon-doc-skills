# AddScene3dCamera (Operator)

## Name

`AddScene3dCamera` — Add a camera to a 3D scene.

## Signature

`static void HOperatorSet.AddScene3dCamera(HTuple scene3D, HTuple cameraParam, out HTuple cameraIndex)`

`int HCamPar.AddScene3dCamera(HScene3D scene3D)`

`int HScene3D.AddScene3dCamera(HCamPar cameraParam)`

## Description

`AddScene3dCamera` adds a new camera to the 3D scene
*`scene3D`* and returns the index of this camera in
*`cameraIndex`*. The camera parameters of the camera must be
given in *`cameraParam`*. By default the new camera is located
at the origin of the world coordinate system. The pose of the camera
*`cameraIndex`* can be set with [`SetScene3dCameraPose`](set_scene_3d_camera_pose.md).

## Attention

Cameras with hypercentric lenses are not supported.
For displaying large faces (or primitives) with a non-zero distortion
in *`cameraParam`*, note that the distortion is only applied to the
points of the model. In the projection, these points are subsequently
connected by straight lines. For a good approximation of the distorted
lines, please use a triangulation with sufficiently small triangles.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`scene3D`** (input_control)  scene_3d `→` [HScene3D](HScene3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D scene.

**`cameraParam`** (input_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

Parameters of the new camera.

**`cameraIndex`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Index of the new camera in the 3D scene.

## Result

`AddScene3dCamera` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Predecessors

`CreateScene3d`

## Possible Successors

`SetScene3dCameraPose`,
`DisplayScene3d`

## Module

3D Metrology
