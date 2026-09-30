# copy_object_model_3d (Operator)

## Name

`copy_object_model_3d` — Copy a 3D object model.

## Signature

`def copy_object_model_3d(object_model_3d: HHandle, attributes: MaybeSequence[Union[str, float, int]]) -> HHandle`

## Description

A 3D object model consists of a set of attributes.
The operator `copy_object_model_3d` creates a new 3D object
model and copies the selected attributes of the input 3D object
model to this new output 3D object model. The input 3D object
model is defined by a handle *`object_model_3d`*. The
operator returns the handle *`copied_object_model_3d`*
of the new 3D object model.
The operator can be used to save memory
space by removing not needed attributes. Access to the attributes of
the 3D object model is possible, e.g., with the operator
[`get_object_model_3d_params`](get_object_model_3d_params.md).

The parameter *`attributes`* determines which attributes
should be copied. In addition, attributes can be excluded from
copying by using the prefix ~. In order to remove
attributes from a 3D object model, the operator
[`remove_object_model_3d_attrib`](remove_object_model_3d_attrib.md) can be used instead.

Note that because a 3D object model itself consists of a
set of attributes, even the point coordinates are an attribute
of the model. This means, that at least this one attribute must be
selected for `copy_object_model_3d` else the object model
to be copied would be empty. So if only
a 3D object model representing a point cloud shall be copied
without further attributes, *`attributes`* must be set
to *"point_coord"*.
If an attribute to be copied is not available or no attribute
is selected, an exception is raised.

The following
values for the parameter *`attributes`* are possible:

- ***"point_coord"*:** —

  This value specifies that the
  attribute with the 3D point coordinates is copied.
- ***"point_normal"*:** —

  This value specifies that the
  attribute with the 3D point normals and the attribute with the
  3D point coordinates are copied.
- ***"triangles"*:** —

  This value specifies that the
  attribute with the face triangles and attribute with the
  3D point coordinates are copied.
- ***"polygons"*:** —

  This value specifies that the
  attribute with the face polygons and the attribute with the
  3D point coordinates are copied.
- ***"lines"*:** —

  This value specifies that the
  attribute with the lines and the attribute with the
  3D point coordinates are copied.
- ***"xyz_mapping"*:** —

  This value specifies that the
  attribute with the mapping to image coordinates and the attribute
  with the 3D point coordinates are copied.
- ***"extended_attribute"*:** —

  This value specifies that all
  extended attributes are copied. If it is necessary to copy further
  attributes that are related to the extended attributes, these
  attributes are copied, too. These further attributes
  could be, e.g., 3D point coordinates, face triangles, face polygons,
  or lines.
- ***"primitives_all"*:** —

  This value specifies that the
  attribute with the parameters of the primitive (including an empty
  primitive) is copied (e.g., obtained from
  the operator [`fit_primitives_object_model_3d`](fit_primitives_object_model_3d.md)).
- ***"primitive_plane"*:** —

  This value specifies that the
  attribute with the primitive plane is copied (e.g., obtained from
  the operator [`fit_primitives_object_model_3d`](fit_primitives_object_model_3d.md)).
- ***"primitive_sphere"*:** —

  This value specifies that the
  attribute with the primitive sphere is copied (e.g., obtained from
  the operator [`fit_primitives_object_model_3d`](fit_primitives_object_model_3d.md)).
- ***"primitive_cylinder"*:** —

  This value specifies that the
  attribute with the primitive cylinder is copied (e.g., obtained from
  the operator [`fit_primitives_object_model_3d`](fit_primitives_object_model_3d.md)).
- ***"primitive_box"*:** —

  This value specifies that the
  attribute with the primitive cylinder is copied.
- ***"shape_based_matching_3d_data"*:** —

  This value
  specifies that the attribute with the prepared shape model for
  shape-based 3D matching is copied.
- ***"distance_computation_data"*:** —

  This value
  specifies that the attribute with the distance computation data
  structure is copied.
  The distance computation data can be created with
  [`prepare_object_model_3d`](prepare_object_model_3d.md), and can be used with
  [`distance_object_model_3d`](distance_object_model_3d.md).
  If this attribute is selected, then the corresponding target
  data attribute of the distance computation is copied as well.
  For example, if the distance computation was prepared for triangles,
  the triangles and the vertices are copied.
- ***"surface_based_matching_data"*:** —

  This value specifies
  that the data for surface based matching are copied. The
  attributes with the 3D point coordinates and the attribute with the
  point normals are copied. If the attribute with point normals is
  not available, the attribute with the mapping from the 3D point
  coordinates to the image coordinates is copied. If the attribute
  with the mapping from the 3D point coordinates to the image coordinates
  is not available, the attribute with the face triangles is copied.
  If the attribute with face triangles is not available, too,
  the attribute with the face polygons is copied.
  If none of these attributes is available, an exception is raised.
- ***"segmentation_data"*:** —

  This value specifies that the
  data for a 3D segmentation is copied. The attributes with the
  3D point coordinates and the attribute with the face triangles are
  copied. If the attribute with the face triangles is not
  available, the attribute with the mapping from the 3D point coordinates
  to the image coordinates is copied. If none of these attributes is
  available, an exception is raised.
- ***"score"*:** —

  This value specifies that the
  attribute with the scores and the attribute with the 3D point coordinates
  are copied. Scores may be obtained from the operator
  [`reconstruct_surface_stereo`](reconstruct_surface_stereo.md).
- ***"red"*:** —

  This value specifies that the attribute containing
  the red color and the attribute with the 3D point coordinates are copied.
- ***"green"*:** —

  This value specifies that the attribute containing
  the green color and the attribute with the 3D point coordinates are copied.
- ***"blue"*:** —

  This value specifies that the attribute containing
  the blue color and the attribute with the 3D point coordinates are copied.
- ***"original_point_indices"*:** —

  This value specifies that the
  attribute with the original point indices and the attribute with the 3D
  point coordinates are copied.
  Original point indices may be obtained from the operator
  [`triangulate_object_model_3d`](triangulate_object_model_3d.md).
- ***"all"*:** —

  This value specifies that all available
  attributes are copied. That is, the attributes are the point
  coordinates, the point normals, the face triangles, the face
  polygons, the mapping to image coordinates, the shape model for
  matching, the parameter of a primitive, and the extended attributes.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`object_model_3d`** (input_control)  object_model_3d `→` HHandle

Handle of the input 3D object model.

**`attributes`** (input_control)  string(-array) `→` MaybeSequence[Union[str, float, int]]

Attributes to be copied.

Default:
"all"

List of values:
"all", "blue", "distance_computation_data", "extended_attribute", "green", "original_point_indices", "point_coord", "point_normal", "polygons", "primitive_box", "primitive_cylinder", "primitive_plane", "primitive_sphere", "primitives_all", "red", "score", "segmentation_data", "shape_based_matching_3d_data", "surface_based_matching_data", "triangles", "xyz_mapping"

**`copied_object_model_3d`** (output_control)  object_model_3d `→` HHandle

Handle of the copied 3D object model.

## Result

`copy_object_model_3d` returns 2 (
H_MSG_TRUE)
if all parameter values
are correct. If necessary, an exception is raised.

## Possible Predecessors

`read_object_model_3d`,
`xyz_to_object_model_3d`

## Possible Successors

`get_object_model_3d_params`

## See also

`remove_object_model_3d_attrib`,
`set_object_model_3d_attrib`

## Module

3D Metrology
