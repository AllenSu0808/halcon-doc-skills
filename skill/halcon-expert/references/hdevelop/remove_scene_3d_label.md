# remove_scene_3d_label (Operator)

## Name

`remove_scene_3d_label` — Remove a text label from a 3D scene.

## Signature

`remove_scene_3d_label( : : Scene3D, LabelIndex : )`

## Description

`remove_scene_3d_label` removes the text label *`LabelIndex`*
from the 3D scene *`Scene3D`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Scene3D`** (input_control)  scene_3d `→`  (handle)

Handle of the 3D scene.

**`LabelIndex`** (input_control)  integer(-array) `→`  (integer)

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
