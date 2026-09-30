# gen_empty_object_model_3d (Operator)

## Name

`gen_empty_object_model_3d` — Create an empty 3D object model.

## Signature

`def gen_empty_object_model_3d() -> HHandle`

## Description

`gen_empty_object_model_3d` creates an empty 3D object model.
The handle of the 3D object model is returned by the parameter
*`empty_object_model_3d`*. Attributes can be added using the operators
[`set_object_model_3d_attrib`](set_object_model_3d_attrib.md) or
[`set_object_model_3d_attrib_mod`](set_object_model_3d_attrib_mod.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`empty_object_model_3d`** (output_control)  object_model_3d `→` HHandle

Handle of the new 3D object model.

## Result

`gen_empty_object_model_3d` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

## Possible Successors

`set_object_model_3d_attrib`,
`set_object_model_3d_attrib_mod`

## See also

`gen_box_object_model_3d`,
`gen_cylinder_object_model_3d`,
`gen_sphere_object_model_3d`,
`gen_sphere_object_model_3d_center`,
`gen_plane_object_model_3d`

## Module

3D Metrology
