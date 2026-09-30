# SetScene3dInstancePose (Operator)

## Name

`SetScene3dInstancePose` — Set the pose of an instance in a 3D scene.

## Signature

`static void HOperatorSet.SetScene3dInstancePose(HTuple scene3D, HTuple instanceIndex, HTuple pose)`

`void HScene3D.SetScene3dInstancePose(HTuple instanceIndex, HPose[] pose)`

`void HScene3D.SetScene3dInstancePose(int instanceIndex, HPose pose)`

## Description

`SetScene3dInstancePose` sets the pose of the instance
*`instanceIndex`* in the 3D scene *`scene3D`* to *`pose`*.
It's possible to set one pose for multiple instances or one pose for
each instance.

See the documentation of [`CreateScene3d`](create_scene_3d.md) for more details on the
coordinate systems used in 3D scenes.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`scene3D`** (input_control)  scene_3d `→` [HScene3D](HScene3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D scene.

**`instanceIndex`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Index of the instance.

**`pose`** (input_control)  pose(-array) `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

New pose of the instance.

## Result

`SetScene3dInstancePose` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Predecessors

`AddScene3dInstance`

## See also

`SetScene3dToWorldPose`,
`SetScene3dCameraPose`

## Module

3D Metrology
