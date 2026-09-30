# AddScene3dInstance (Operator)

## Name

`AddScene3dInstance` — Add an instance of a 3D object model to a 3D scene.

## Signature

`static void HOperatorSet.AddScene3dInstance(HTuple scene3D, HTuple objectModel3D, HTuple pose, out HTuple instanceIndex)`

`int HScene3D.AddScene3dInstance(HObjectModel3D[] objectModel3D, HPose[] pose)`

`int HScene3D.AddScene3dInstance(HObjectModel3D objectModel3D, HPose pose)`

## Description

`AddScene3dInstance` adds an instance of the 3D model
*`objectModel3D`* to the 3D scene *`scene3D`* and returns
its index in *`instanceIndex`*. If multiple 3D object models are
supplied, it is possible to set one pose for all instances or one pose
for every instance.

The pose of the object instance in the scene coordinate system must be
given in *`pose`*. The operator
[`SetScene3dInstancePose`](set_scene_3d_instance_pose.md) can be used to change this pose.
As long as no global scene pose is set with
[`SetScene3dToWorldPose`](set_scene_3d_to_world_pose.md), this pose is evaluated relative to
the world coordinate system.

Parameters of the instance, such as its color, are set with the
operator [`SetScene3dInstanceParam`](set_scene_3d_instance_param.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`scene3D`** (input_control)  scene_3d `→` [HScene3D](HScene3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D scene.

**`objectModel3D`** (input_control)  object_model_3d(-array) `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D object model.

**`pose`** (input_control)  pose(-array) `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

Pose of the 3D object model.

Number of elements:
7

**`instanceIndex`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Index of the new instance in the 3D scene.

## Result

`AddScene3dInstance` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Predecessors

`CreateScene3d`

## Possible Successors

`SetScene3dInstanceParam`,
`SetScene3dInstancePose`

## See also

`RemoveScene3dInstance`

## Module

3D Metrology
