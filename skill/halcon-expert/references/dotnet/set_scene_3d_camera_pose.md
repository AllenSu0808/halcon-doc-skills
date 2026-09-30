# SetScene3dCameraPose (Operator)

## Name

`SetScene3dCameraPose` — Set the pose of a camera in a 3D scene.

## Signature

`static void HOperatorSet.SetScene3dCameraPose(HTuple scene3D, HTuple cameraIndex, HTuple pose)`

`void HScene3D.SetScene3dCameraPose(int cameraIndex, HPose pose)`

## Description

`SetScene3dCameraPose` sets the *`pose`* of the camera
*`cameraIndex`* in the 3D scene *`scene3D`*.

See [`CreateScene3d`](create_scene_3d.md) for more details on the coordinate systems used
in 3D scenes.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`scene3D`** (input_control)  scene_3d `→` [HScene3D](HScene3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D scene.

**`cameraIndex`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Index of the camera.

**`pose`** (input_control)  pose `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

New pose of the camera.

## Result

`SetScene3dCameraPose` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Predecessors

`AddScene3dCamera`

## See also

`SetScene3dToWorldPose`,
`SetScene3dInstancePose`

## Module

3D Metrology
