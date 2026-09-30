# RemoveScene3dLight (Operator)

## Name

`RemoveScene3dLight` — Remove a light from a 3D scene.

## Signature

`static void HOperatorSet.RemoveScene3dLight(HTuple scene3D, HTuple lightIndex)`

`void HScene3D.RemoveScene3dLight(int lightIndex)`

## Description

`RemoveScene3dLight` removes the light *`lightIndex`*
from the 3D scene *`scene3D`* in future versions. Currently only one
light source is supported.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`scene3D`** (input_control)  scene_3d `→` [HScene3D](HScene3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D scene.

**`lightIndex`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Light to remove.

## Result

`RemoveScene3dLight` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## See also

`AddScene3dLight`

## Module

3D Metrology
