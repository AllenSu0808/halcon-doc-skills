# RemoveObjectModel3dAttribMod (Operator)

## Name

`RemoveObjectModel3dAttribMod` — Remove attributes of a 3D object model.

## Signature

`static void HOperatorSet.RemoveObjectModel3dAttribMod(HTuple objectModel3D, HTuple attributes)`

`void HObjectModel3D.RemoveObjectModel3dAttribMod(HTuple attributes)`

`void HObjectModel3D.RemoveObjectModel3dAttribMod(string attributes)`

## Description

`RemoveObjectModel3dAttribMod` removes the standard and/or extended
attributes given in *`attributes`* of a 3D object model
*`objectModel3D`*.
Doing so changes the 3D object model. This is in contrast to the
operator [`RemoveObjectModel3dAttrib`](remove_object_model_3d_attrib.md), which creates a new model
but functions identically otherwise.

If the *`attributes`* do not exist in *`objectModel3D`*, no
exception is raised.

For a detailed description of *`attributes`* see operator
[`RemoveObjectModel3dAttrib`](remove_object_model_3d_attrib.md).

## Attention

`RemoveObjectModel3dAttribMod` removes *`attributes`*
unchecked from the 3D object model. Special attention must be paid
to retain a consistent 3D object model, as most of the operators expect
consistent 3D object models. Furthermore, the mapping of the 3D points to
image coordinates should not be removed because it speeds up the
computation of many operators.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`objectModel3D`** (input_control)  object_model_3d `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the input 3D object model.

**`attributes`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Name of the attributes to be removed.

Default:
"extended_attribute"

List of values:
"all", "blue", "distance_computation_data", "extended_attribute", "green", "lines", "original_point_indices", "point_normal", "polygons", "primitive_box", "primitive_cylinder", "primitive_plane", "primitive_sphere", "primitives_all", "red", "score", "shape_based_matching_3d_data", "triangles", "xyz_mapping"

## Result

If the parameters are valid, the operator
`RemoveObjectModel3dAttribMod` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Possible Predecessors

`SetObjectModel3dAttribMod`

## Possible Successors

`GetObjectModel3dParams`

## Alternatives

`RemoveObjectModel3dAttrib`

## See also

`CopyObjectModel3d`,
`SetObjectModel3dAttribMod`

## Module

3D Metrology
