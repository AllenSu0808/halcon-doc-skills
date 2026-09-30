# remove_scene_3d_instance (Operator)

## Name

`remove_scene_3d_instance` — Remove an object instance from a 3D scene.

## Signature

`def remove_scene_3d_instance(scene_3d: HHandle, instance_index: MaybeSequence[int]) -> None`

## Description

`remove_scene_3d_instance` removes the instance *`instance_index`*
from the 3D scene *`scene_3d`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`scene_3d`** (input_control)  scene_3d `→` HHandle

Handle of the 3D scene.

**`instance_index`** (input_control)  integer(-array) `→` MaybeSequence[int]

Index of the instance to remove.

## Result

`remove_scene_3d_instance` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## See also

`add_scene_3d_instance`

## Module

3D Metrology
