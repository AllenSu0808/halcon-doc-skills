# RemoveScene3dLabel (Operator)

## Name

`RemoveScene3dLabel` — Remove a text label from a 3D scene.

## Signature

`static void HOperatorSet.RemoveScene3dLabel(HTuple scene3D, HTuple labelIndex)`

`void HScene3D.RemoveScene3dLabel(HTuple labelIndex)`

`void HScene3D.RemoveScene3dLabel(int labelIndex)`

## Description

`RemoveScene3dLabel` removes the text label *`labelIndex`*
from the 3D scene *`scene3D`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`scene3D`** (input_control)  scene_3d `→` [HScene3D](HScene3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D scene.

**`labelIndex`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Index of the text label to remove.

## Result

`RemoveScene3dLabel` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## See also

`AddScene3dLabel`

## Module

3D Metrology
