# RemoveScene3dCamera (Operator)

## Name

`RemoveScene3dCamera` — Remove a camera from a 3D scene.

## Signature

`static void HOperatorSet.RemoveScene3dCamera(HTuple scene3D, HTuple cameraIndex)`

`void HScene3D.RemoveScene3dCamera(int cameraIndex)`

## Description

`RemoveScene3dCamera` removes the camera *`cameraIndex`* from
the 3D scene *`scene3D`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`scene3D`** (input_control)  scene_3d `→` [HScene3D](HScene3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D scene.

**`cameraIndex`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Index of the camera to remove.

## Result

`RemoveScene3dCamera` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## See also

`AddScene3dCamera`

## Module

3D Metrology
