# set_object_model_3d_attrib_mod (Operator)

## Name

`set_object_model_3d_attrib_mod` — Set attributes of a 3D object model.

## Signature

`set_object_model_3d_attrib_mod( : : ObjectModel3D, AttribName, AttachExtAttribTo, AttribValues : )`

## Description

`set_object_model_3d_attrib_mod` sets the standard attributes or the
extended attributes given in *`AttribName`* of a 3D object model
*`ObjectModel3D`* to the values in *`AttribValues`*.
`set_object_model_3d_attrib_mod` is
identical to [`set_object_model_3d_attrib`](set_object_model_3d_attrib.md), with the exception that
it does not create a new 3D object model but modifies the given one.
It is possible to attach the values of extended attributes to
already existing standard attributes of the 3D object model by setting the
parameter *`AttachExtAttribTo`*. For standard attributes,
*`AttachExtAttribTo`* is ignored.

If the attributes in *`AttribName`* do not exist, they are created if
possible.
If already existing attributes are set, the length of *`AttribValues`*
must match the existing attribute values. In this case the existing attribute
values are replaced.
If extended attributes are attached to already existing standard
attributes with *`AttachExtAttribTo`*, the length of *`AttribValues`*
must match the existing attribute values.

For a detailed description see operator [`set_object_model_3d_attrib`](set_object_model_3d_attrib.md).

## Attention

If multiple attributes are given in *`AttribName`*,
*`AttribValues`* is divided into sub-tuples of equal length.
Each sub-tuple is then assigned to one attribute.
E.g., if *`AttribName`* and *`AttribValues`* are set to

*`AttribName`* := *['&attrib1','&attrib2','&attrib3']*,

*`AttribValues`* := *[0.0,1.0,2.0,3.0,4.0,5.0]*,

the following values are assigned to the individual attributes:

*'&attrib1'* = *[0.0,1.0]*,
*'&attrib2'* = *[2.0,3.0]*,
*'&attrib3'* = *[4.0,5.0]*.

Consequently,
it is not possible to set multiple attributes of different
lengths in one call.

`set_object_model_3d_attrib_mod` modifies the content of an
already existing 3D object model. The operator
stores the input *`AttribValues`* unmodified in the 3D object model.
Therefore, special attention must be paid to the consistency of the
input data, as most of the operators expect consistent 3D object models.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ObjectModel3D`** (input_control)  object_model_3d `→`  (handle)

Handle of the 3D object model.

**`AttribName`** (input_control)  string(-array) `→`  (string)

Name of the attributes.

List of values:
'blue', 'green', 'lines', 'original_point_indices', 'point_coord_x', 'point_coord_y', 'point_coord_z', 'point_normal_x', 'point_normal_y', 'point_normal_z', 'polygons', 'red', 'score', 'triangles', 'xyz_mapping'

**`AttachExtAttribTo`** (input_control)  string `→`  (string)

Defines where extended attributes are attached to.

Default:
[]

List of values:
[], 'lines', 'object', 'points', 'polygons', 'triangles'

**`AttribValues`** (input_control)  real(-array) `→`  (real / integer)

Attribute values.

## Result

If the parameters are valid, the operator
`set_object_model_3d_attrib_mod` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Possible Predecessors

`gen_empty_object_model_3d`

## Possible Successors

`get_object_model_3d_params`

## Alternatives

`set_object_model_3d_attrib`

## See also

`copy_object_model_3d`,
`remove_object_model_3d_attrib_mod`

## Module

3D Metrology
