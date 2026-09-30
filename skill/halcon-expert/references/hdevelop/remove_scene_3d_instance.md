# remove_scene_3d_instance (Operator)

## Name

`remove_scene_3d_instance` — Remove an object instance from a 3D scene.

## Signature

`remove_scene_3d_instance( : : Scene3D, InstanceIndex : )`

## Description

`remove_scene_3d_instance` removes the instance *`InstanceIndex`*
from the 3D scene *`Scene3D`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Scene3D`** (input_control)  scene_3d `→`  (handle)

Handle of the 3D scene.

**`InstanceIndex`** (input_control)  integer(-array) `→`  (integer)

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
