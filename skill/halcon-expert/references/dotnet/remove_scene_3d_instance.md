# RemoveScene3dInstance (Operator)

## Name

`RemoveScene3dInstance` — Remove an object instance from a 3D scene.

## Signature

`static void HOperatorSet.RemoveScene3dInstance(HTuple scene3D, HTuple instanceIndex)`

`void HScene3D.RemoveScene3dInstance(HTuple instanceIndex)`

`void HScene3D.RemoveScene3dInstance(int instanceIndex)`

## Description

`RemoveScene3dInstance` removes the instance *`instanceIndex`*
from the 3D scene *`scene3D`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`scene3D`** (input_control)  scene_3d `→` [HScene3D](HScene3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D scene.

**`instanceIndex`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Index of the instance to remove.

## Result

`RemoveScene3dInstance` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## See also

`AddScene3dInstance`

## Module

3D Metrology
