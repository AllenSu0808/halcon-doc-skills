# remove_scene_3d_label (Operator)

## Name

`remove_scene_3d_label` — Remove a text label from a 3D scene.

## Signature

`def remove_scene_3d_label(scene_3d: HHandle, label_index: MaybeSequence[int]) -> None`

## Description

`remove_scene_3d_label` removes the text label *`label_index`*
from the 3D scene *`scene_3d`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`scene_3d`** (input_control)  scene_3d `→` HHandle

Handle of the 3D scene.

**`label_index`** (input_control)  integer(-array) `→` MaybeSequence[int]

Index of the text label to remove.

## Result

`remove_scene_3d_label` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## See also

`add_scene_3d_label`

## Module

3D Metrology
