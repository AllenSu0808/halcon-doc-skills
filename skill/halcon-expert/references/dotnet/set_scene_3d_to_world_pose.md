# SetScene3dToWorldPose (Operator)

## Name

`SetScene3dToWorldPose` — Set the pose of a 3D scene.

## Signature

`static void HOperatorSet.SetScene3dToWorldPose(HTuple scene3D, HTuple toWorldPose)`

`void HScene3D.SetScene3dToWorldPose(HPose toWorldPose)`

## Description

`SetScene3dToWorldPose` sets the pose of the 3D scene
*`scene3D`* to *`toWorldPose`*.

See the documentation of [`CreateScene3d`](create_scene_3d.md) for more details on the
coordinate systems used in 3D scenes.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`scene3D`** (input_control)  scene_3d `→` [HScene3D](HScene3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D scene.

**`toWorldPose`** (input_control)  pose `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

New pose of the 3D scene.

## Result

`SetScene3dToWorldPose` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Predecessors

`CreateScene3d`

## See also

`SetScene3dInstancePose`

## Module

3D Metrology
