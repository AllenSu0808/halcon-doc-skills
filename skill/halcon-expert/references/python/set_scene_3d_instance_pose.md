# set_scene_3d_instance_pose (Operator)

## Name

`set_scene_3d_instance_pose` — Set the pose of an instance in a 3D scene.

## Signature

`def set_scene_3d_instance_pose(scene_3d: HHandle, instance_index: MaybeSequence[int], pose: MaybeSequence[Union[float, int]]) -> None`

## Description

`set_scene_3d_instance_pose` sets the pose of the instance
*`instance_index`* in the 3D scene *`scene_3d`* to *`pose`*.
It's possible to set one pose for multiple instances or one pose for
each instance.

See the documentation of [`create_scene_3d`](create_scene_3d.md) for more details on the
coordinate systems used in 3D scenes.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`scene_3d`** (input_control)  scene_3d `→` HHandle

Handle of the 3D scene.

**`instance_index`** (input_control)  integer(-array) `→` MaybeSequence[int]

Index of the instance.

**`pose`** (input_control)  pose(-array) `→` MaybeSequence[Union[float, int]]

New pose of the instance.

## Result

`set_scene_3d_instance_pose` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Predecessors

`add_scene_3d_instance`

## See also

`set_scene_3d_to_world_pose`,
`set_scene_3d_camera_pose`

## Module

3D Metrology
