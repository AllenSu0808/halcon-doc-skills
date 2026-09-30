# set_object_model_3d_attrib_mod (Operator)

## Name

`set_object_model_3d_attrib_mod` — Set attributes of a 3D object model.

## Signature

`def set_object_model_3d_attrib_mod(object_model_3d: HHandle, attrib_name: MaybeSequence[str], attach_ext_attrib_to: str, attrib_values: MaybeSequence[Union[float, int]]) -> None`

## Description

`set_object_model_3d_attrib_mod` sets the standard attributes or the
extended attributes given in *`attrib_name`* of a 3D object model
*`object_model_3d`* to the values in *`attrib_values`*.
`set_object_model_3d_attrib_mod` is
identical to [`set_object_model_3d_attrib`](set_object_model_3d_attrib.md), with the exception that
it does not create a new 3D object model but modifies the given one.
It is possible to attach the values of extended attributes to
already existing standard attributes of the 3D object model by setting the
parameter *`attach_ext_attrib_to`*. For standard attributes,
*`attach_ext_attrib_to`* is ignored.

If the attributes in *`attrib_name`* do not exist, they are created if
possible.
If already existing attributes are set, the length of *`attrib_values`*
must match the existing attribute values. In this case the existing attribute
values are replaced.
If extended attributes are attached to already existing standard
attributes with *`attach_ext_attrib_to`*, the length of *`attrib_values`*
must match the existing attribute values.

For a detailed description see operator [`set_object_model_3d_attrib`](set_object_model_3d_attrib.md).

## Attention

If multiple attributes are given in *`attrib_name`*,
*`attrib_values`* is divided into sub-tuples of equal length.
Each sub-tuple is then assigned to one attribute.
E.g., if *`attrib_name`* and *`attrib_values`* are set to

*`attrib_name`* := *["&attrib1","&attrib2","&attrib3"]*,

*`attrib_values`* := *[0.0,1.0,2.0,3.0,4.0,5.0]*,

the following values are assigned to the individual attributes:

*"&attrib1"* = *[0.0,1.0]*,
*"&attrib2"* = *[2.0,3.0]*,
*"&attrib3"* = *[4.0,5.0]*.

Consequently,
it is not possible to set multiple attributes of different
lengths in one call.

`set_object_model_3d_attrib_mod` modifies the content of an
already existing 3D object model. The operator
stores the input *`attrib_values`* unmodified in the 3D object model.
Therefore, special attention must be paid to the consistency of the
input data, as most of the operators expect consistent 3D object models.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`object_model_3d`** (input_control)  object_model_3d `→` HHandle

Handle of the 3D object model.

**`attrib_name`** (input_control)  string(-array) `→` MaybeSequence[str]

Name of the attributes.

List of values:
"blue", "green", "lines", "original_point_indices", "point_coord_x", "point_coord_y", "point_coord_z", "point_normal_x", "point_normal_y", "point_normal_z", "polygons", "red", "score", "triangles", "xyz_mapping"

**`attach_ext_attrib_to`** (input_control)  string `→` str

Defines where extended attributes are attached to.

Default:
[]

List of values:
[], "lines", "object", "points", "polygons", "triangles"

**`attrib_values`** (input_control)  real(-array) `→` MaybeSequence[Union[float, int]]

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
