# add_scene_3d_instance (Operator)

## Name

`add_scene_3d_instance` — Add an instance of a 3D object model to a 3D scene.

## Signature

`def add_scene_3d_instance(scene_3d: HHandle, object_model_3d: MaybeSequence[HHandle], pose: Sequence[Union[float, int]]) -> int`

## Description

`add_scene_3d_instance` adds an instance of the 3D model
*`object_model_3d`* to the 3D scene *`scene_3d`* and returns
its index in *`instance_index`*. If multiple 3D object models are
supplied, it is possible to set one pose for all instances or one pose
for every instance.

The pose of the object instance in the scene coordinate system must be
given in *`pose`*. The operator
[`set_scene_3d_instance_pose`](set_scene_3d_instance_pose.md) can be used to change this pose.
As long as no global scene pose is set with
[`set_scene_3d_to_world_pose`](set_scene_3d_to_world_pose.md), this pose is evaluated relative to
the world coordinate system.

Parameters of the instance, such as its color, are set with the
operator [`set_scene_3d_instance_param`](set_scene_3d_instance_param.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`scene_3d`** (input_control)  scene_3d `→` HHandle

Handle of the 3D scene.

**`object_model_3d`** (input_control)  object_model_3d(-array) `→` MaybeSequence[HHandle]

Handle of the 3D object model.

**`pose`** (input_control)  pose(-array) `→` Sequence[Union[float, int]]

Pose of the 3D object model.

Number of elements:
7

**`instance_index`** (output_control)  integer `→` int

Index of the new instance in the 3D scene.

## Result

`add_scene_3d_instance` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Predecessors

`create_scene_3d`

## Possible Successors

`set_scene_3d_instance_param`,
`set_scene_3d_instance_pose`

## See also

`remove_scene_3d_instance`

## Module

3D Metrology
