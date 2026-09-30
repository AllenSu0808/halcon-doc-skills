# set_scene_3d_to_world_pose (Operator)

## Name

`set_scene_3d_to_world_pose` — Set the pose of a 3D scene.

## Signature

`def set_scene_3d_to_world_pose(scene_3d: HHandle, to_world_pose: MaybeSequence[Union[float, int]]) -> None`

## Description

`set_scene_3d_to_world_pose` sets the pose of the 3D scene
*`scene_3d`* to *`to_world_pose`*.

See the documentation of [`create_scene_3d`](create_scene_3d.md) for more details on the
coordinate systems used in 3D scenes.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`scene_3d`** (input_control)  scene_3d `→` HHandle

Handle of the 3D scene.

**`to_world_pose`** (input_control)  pose `→` MaybeSequence[Union[float, int]]

New pose of the 3D scene.

## Result

`set_scene_3d_to_world_pose` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Predecessors

`create_scene_3d`

## See also

`set_scene_3d_instance_pose`

## Module

3D Metrology
