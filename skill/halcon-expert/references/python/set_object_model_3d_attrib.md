# set_object_model_3d_attrib (Operator)

## Name

`set_object_model_3d_attrib` — Set attributes of a 3D object model.

## Signature

`def set_object_model_3d_attrib(object_model_3d: HHandle, attrib_name: MaybeSequence[str], attach_ext_attrib_to: str, attrib_values: MaybeSequence[Union[float, int]]) -> HHandle`

## Description

`set_object_model_3d_attrib` sets the standard attributes or the
extended attributes given in *`attrib_name`* of a 3D object model
*`object_model_3d`* to the values in *`attrib_values`* and returns
a 3D object model with the new attribute values in *`object_model_3dout`*.
`set_object_model_3d_attrib` is identical to
[`set_object_model_3d_attrib_mod`](set_object_model_3d_attrib_mod.md) with the exception that it creates a
new 3D object model and leaves the original 3D object model unchanged.
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

### Standard attributes

The following standard attributes can be set:

- ***"point_coord_x"*:** —

  The x-coordinates of the 3D points are set with
  *`attrib_values`*. If the attribute does not exist, the
  x-, y- and z-coordinates must be set with *"point_coord_x"*,
  *"point_coord_y"*, and *"point_coord_z"* at once. The
  number of x-, y-, and z-coordinates must be identical.
- ***"point_coord_y"*:** —

  The y-coordinates of the 3D points are set with
  *`attrib_values`*. If the attribute does not exist, the
  x-, y- and z-coordinates must be set with *"point_coord_x"*,
  *"point_coord_y"*, and *"point_coord_z"* at once. The
  number of x-, y-, and z-coordinates must be identical.
- ***"point_coord_z"*:** —

  The z-coordinates of the 3D points are set with
  *`attrib_values`*. If the attribute does not exist, the
  x-, y- and z-coordinates must be set with *"point_coord_x"*,
  *"point_coord_y"*, and *"point_coord_z"* at once. The
  number of x-, y-, and z-coordinates must be identical.
- ***"point_normal_x"*:** —

  The x-components of the 3D point normals of the 3D points are
  set with *`attrib_values`*. If the attribute does not
  exist, the x-, y- and z-components of 3D point normals must be set
  with *"point_normal_x"*, *"point_normal_y"*, and
  *"point_normal_z"* at once. The number of x-, y-, and
  z-components must be identical
  to the number of 3D points. Note that the given 3D point normals will
  not be normalized to a length of 1.
- ***"point_normal_y"*:** —

  The y-components of the 3D point normals of the 3D points are
  set with *`attrib_values`*. If the attribute does not
  exist, the x-, y- and z-components of 3D point normals must be set
  with *"point_normal_x"*, *"point_normal_y"*, and
  *"point_normal_z"* at once. The number of x-, y-, and
  z-components must be identical
  to the number of 3D points. Note that the given 3D point normals will
  not be normalized to a length of 1.
- ***"point_normal_z"*:** —

  The z-components of the 3D point normals of the 3D points are
  set with *`attrib_values`*. If the attribute does not
  exist, the x-, y- and z-components of 3D point normals must be set
  with *"point_normal_x"*, *"point_normal_y"*, and
  *"point_normal_z"* at once. The number of x-, y-, and
  z-components must be identical
  to the number of 3D points. Note that the given 3D point normals will
  not be normalized to a length of 1.
- ***"triangles"*:** —

  The indices of the 3D points that represent triangles are set with
  *`attrib_values`* in the following order:
  The first three values of
  *`attrib_values`* (input values 0,1,2) represent the first triangle
  and contain the indices of the corresponding 3D points
  of the triangle corners.
  The second three values (input values 3,4,5) represent the
  second triangle etc.
  The direction of the triangles results from the
  order of the point indices.
- ***"polygons"*:** —

  The indices of the 3D points that represent polygons are set with
  *`attrib_values`* in the following order:
  The first value of *`attrib_values`* contains
  the number n of points of the first polygon. The following values
  (input values 1,2,..,n) contains the
  indices of the points of the first polygon. The next value
  (input value n+1) contains the number m of the points of the
  second polygon.
  The following m values (input values n+2,n+3,..,n+1+m)
  contain the indices of the points of the second polygon etc.
- ***"lines"*:** —

  The indices of the 3D points that represent polylines are set with
  *`attrib_values`* in the following order:
  The first value of *`attrib_values`* contains the number n
  of points of the first polyline. The following values
  (input values 1,2,..,n) represent the indices of the points
  of the first polyline.
  The next value (input value n+1) contains the number m of
  points of the second polyline. The following m values
  (input values n+2,n+3,..,n+1+m) represent the indices of the
  points of the second polyline etc. All indices correspond to
  already existing 3D points.
- ***"xyz_mapping"*:** —

  The mapping of 3D points to image
  coordinates is set with *`attrib_values`* in the following
  order: The first two values of
  *`attrib_values`* (input value 0 and 1) contain the width
  and height of the respective image. The following n
  values (input values 2,3,..,n+1, with n being the number
  of 3D points) represent the row coordinates of the n points
  given in image coordinates. The next n input values (input
  values n+2,n+3,..,n*2+1) represent the column coordinates of the
  n points in image coordinates. Hence, the total number of input
  values is n*2+2.

### Extended attributes

Extended attributes are attributes, that can be derived from standard
attributes by special operators (e.g., [`distance_object_model_3d`](distance_object_model_3d.md)),
or user-defined attributes. Predefined extended attributes can only be
set separately, for these attributes *`attach_ext_attrib_to`*
will be ignored. The names of user-defined extended attributes are arbitrary,
but must start with the prefix *'&'*, e.g., *"&my_attrib"*.
Extended attributes can have an arbitrary number of floating point
values.

The following predefined extended attributes can be set:

- ***"original_point_indices"*:** —

  The original points indices of the 3D points are set with
  *`attrib_values`*. The number of the original points indices must be
  identical to the number of 3D points.
- ***"score"*:** —

  The score of a 3D reconstruction of the 3D points are set with
  *`attrib_values`*. Since the score is evaluated separately for each
  3D point, the number of the score-components must be identical to the
  number of 3D points.
- ***"red"*:** —

  The red channel intensities of the 3D points are set with
  *`attrib_values`*. The number of color values must be identical
  to the number of 3D points.
- ***"green"*:** —

  The green channel intensities of the 3D points are set with
  *`attrib_values`*. The number of color values must be identical
  to the number of 3D points.
- ***"blue"*:** —

  The blue channel intensities of the 3D points are set with
  *`attrib_values`*. The number of color values must be identical
  to the number of 3D points.
- ***"edge_dir_x"*:** —

  The x-component of a vector that is perpendicular to the
  edge direction and the viewing direction.
- ***"edge_dir_y"*:** —

  The y-component of a vector that is perpendicular to the
  edge direction and the viewing direction.
- ***"edge_dir_z"*:** —

  The z-component of a vector that is perpendicular to the
  edge direction and the viewing direction.
- ***"edge_amplitude"*:** —

  Contains the amplitude of edge points.

Extended attributes can be attached to already existing standard attributes
of the 3D object model by setting the parameter *`attach_ext_attrib_to`*.
The following values of *`attach_ext_attrib_to`* are possible:

- ***"object"* or *[]*:** —

  If this value is set, the extended attribute specified in
  *`attrib_name`* is associated to the 3D object model as a whole.
  The number of values specified in *`attrib_values`* is not restricted.
- ***"points"*:** —

  If this value is set, the extended attribute specified in
  *`attrib_name`* is associated to the 3D points of the object model.
  The number of values specified in *`attrib_values`* must be the
  same as the number of already existing 3D points.
- ***"triangles"*:** —

  If this value is set, the extended attribute specified in
  *`attrib_name`* is associated to the triangles of the object model.
  The number of values specified in *`attrib_values`* must be the
  same as the number of already existing triangles.
- ***"polygons"*:** —

  If this value is set, the extended attribute specified in
  *`attrib_name`* is associated to the polygons of the object model.
  The number of values specified in *`attrib_values`* must be the
  same as the number of already existing polygons.
- ***"lines"*:** —

  If this value is set, the extended attribute specified in
  *`attrib_name`* is associated to the lines of the object model.
  The number of values specified in *`attrib_values`* must be the
  same as the number of already existing lines.

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

`set_object_model_3d_attrib` stores the input *`attrib_values`*
unmodified in the 3D object model. Therefore, special attention must
be paid to the consistency of the input data, as most of the operators
expect consistent 3D object models.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`object_model_3d`** (input_control)  object_model_3d `→` HHandle

Handle of the input 3D object model.

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

**`object_model_3dout`** (output_control)  object_model_3d `→` HHandle

Handle of the resulting 3D object model.

## Result

If the parameters are valid, the operator
`set_object_model_3d_attrib` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Possible Predecessors

`gen_empty_object_model_3d`

## Possible Successors

`get_object_model_3d_params`

## Alternatives

`set_object_model_3d_attrib_mod`

## See also

`copy_object_model_3d`,
`remove_object_model_3d_attrib`

## Module

3D Metrology
