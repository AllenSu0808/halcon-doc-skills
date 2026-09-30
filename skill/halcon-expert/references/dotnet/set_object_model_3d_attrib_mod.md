# SetObjectModel3dAttribMod (Operator)

## Name

`SetObjectModel3dAttribMod` — Set attributes of a 3D object model.

## Signature

`static void HOperatorSet.SetObjectModel3dAttribMod(HTuple objectModel3D, HTuple attribName, HTuple attachExtAttribTo, HTuple attribValues)`

`void HObjectModel3D.SetObjectModel3dAttribMod(HTuple attribName, string attachExtAttribTo, HTuple attribValues)`

`void HObjectModel3D.SetObjectModel3dAttribMod(string attribName, string attachExtAttribTo, double attribValues)`

## Description

`SetObjectModel3dAttribMod` sets the standard attributes or the
extended attributes given in *`attribName`* of a 3D object model
*`objectModel3D`* to the values in *`attribValues`*.
`SetObjectModel3dAttribMod` is
identical to [`SetObjectModel3dAttrib`](set_object_model_3d_attrib.md), with the exception that
it does not create a new 3D object model but modifies the given one.
It is possible to attach the values of extended attributes to
already existing standard attributes of the 3D object model by setting the
parameter *`attachExtAttribTo`*. For standard attributes,
*`attachExtAttribTo`* is ignored.

If the attributes in *`attribName`* do not exist, they are created if
possible.
If already existing attributes are set, the length of *`attribValues`*
must match the existing attribute values. In this case the existing attribute
values are replaced.
If extended attributes are attached to already existing standard
attributes with *`attachExtAttribTo`*, the length of *`attribValues`*
must match the existing attribute values.

For a detailed description see operator [`SetObjectModel3dAttrib`](set_object_model_3d_attrib.md).

## Attention

If multiple attributes are given in *`attribName`*,
*`attribValues`* is divided into sub-tuples of equal length.
Each sub-tuple is then assigned to one attribute.
E.g., if *`attribName`* and *`attribValues`* are set to

*`attribName`* := *["&attrib1","&attrib2","&attrib3"]*,

*`attribValues`* := *[0.0,1.0,2.0,3.0,4.0,5.0]*,

the following values are assigned to the individual attributes:

*"&attrib1"* = *[0.0,1.0]*,
*"&attrib2"* = *[2.0,3.0]*,
*"&attrib3"* = *[4.0,5.0]*.

Consequently,
it is not possible to set multiple attributes of different
lengths in one call.

`SetObjectModel3dAttribMod` modifies the content of an
already existing 3D object model. The operator
stores the input *`attribValues`* unmodified in the 3D object model.
Therefore, special attention must be paid to the consistency of the
input data, as most of the operators expect consistent 3D object models.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`objectModel3D`** (input_control)  object_model_3d `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D object model.

**`attribName`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Name of the attributes.

List of values:
"blue", "green", "lines", "original_point_indices", "point_coord_x", "point_coord_y", "point_coord_z", "point_normal_x", "point_normal_y", "point_normal_z", "polygons", "red", "score", "triangles", "xyz_mapping"

**`attachExtAttribTo`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Defines where extended attributes are attached to.

Default:
[]

List of values:
[], "lines", "object", "points", "polygons", "triangles"

**`attribValues`** (input_control)  real(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Attribute values.

## Result

If the parameters are valid, the operator
`SetObjectModel3dAttribMod` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Possible Predecessors

`GenEmptyObjectModel3d`

## Possible Successors

`GetObjectModel3dParams`

## Alternatives

`SetObjectModel3dAttrib`

## See also

`CopyObjectModel3d`,
`RemoveObjectModel3dAttribMod`

## Module

3D Metrology
