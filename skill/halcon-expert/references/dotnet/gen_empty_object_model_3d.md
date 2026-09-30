# GenEmptyObjectModel3d (Operator)

## Name

`GenEmptyObjectModel3d` — Create an empty 3D object model.

## Signature

`static void HOperatorSet.GenEmptyObjectModel3d(out HTuple emptyObjectModel3D)`

`public HObjectModel3D()`

`void HObjectModel3D.GenEmptyObjectModel3d()`

## Description

`GenEmptyObjectModel3d` creates an empty 3D object model.
The handle of the 3D object model is returned by the parameter
*`emptyObjectModel3D`*. Attributes can be added using the operators
[`SetObjectModel3dAttrib`](set_object_model_3d_attrib.md) or
[`SetObjectModel3dAttribMod`](set_object_model_3d_attrib_mod.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`emptyObjectModel3D`** (output_control)  object_model_3d `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the new 3D object model.

## Result

`GenEmptyObjectModel3d` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

## Possible Successors

`SetObjectModel3dAttrib`,
`SetObjectModel3dAttribMod`

## See also

`GenBoxObjectModel3d`,
`GenCylinderObjectModel3d`,
`GenSphereObjectModel3d`,
`GenSphereObjectModel3dCenter`,
`GenPlaneObjectModel3d`

## Module

3D Metrology
