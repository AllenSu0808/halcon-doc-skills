# set_scene_3d_instance_pose (Operator)

## Name

`set_scene_3d_instance_pose` — Set the pose of an instance in a 3D scene.

## Signature

`set_scene_3d_instance_pose( : : Scene3D, InstanceIndex, Pose : )`

## Description

`set_scene_3d_instance_pose` sets the pose of the instance
*`InstanceIndex`* in the 3D scene *`Scene3D`* to *`Pose`*.
It's possible to set one pose for multiple instances or one pose for
each instance.

See the documentation of [`create_scene_3d`](create_scene_3d.md) for more details on the
coordinate systems used in 3D scenes.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Scene3D`** (input_control)  scene_3d `→`  (handle)

Handle of the 3D scene.

**`InstanceIndex`** (input_control)  integer(-array) `→`  (integer)

Index of the instance.

**`Pose`** (input_control)  pose(-array) `→`  (real / integer)

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
