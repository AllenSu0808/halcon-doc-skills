# RemoveObjectModel3dAttrib (Operator)

## Name

`RemoveObjectModel3dAttrib` — Remove attributes of a 3D object model.

## Signature

`static void HOperatorSet.RemoveObjectModel3dAttrib(HTuple objectModel3D, HTuple attributes, out HTuple objectModel3DOut)`

`HObjectModel3D HObjectModel3D.RemoveObjectModel3dAttrib(HTuple attributes)`

`HObjectModel3D HObjectModel3D.RemoveObjectModel3dAttrib(string attributes)`

## Description

`RemoveObjectModel3dAttrib` copies the 3d object model
*`objectModel3D`* and removes within this copy the standard and/or
extended attributes given in *`attributes`*.
The new 3d object model is returned in *`objectModel3DOut`*.
Doing so does not modify the 3d object model *`objectModel3D`* but a
new model is created. This is in contrast to the
operator [`RemoveObjectModel3dAttribMod`](remove_object_model_3d_attrib_mod.md), which modifies the input
model but functions identically otherwise.

If the *`attributes`* do not exist in *`objectModel3D`*, no
exception is raised.

### Standard attributes

The following values for the parameter *`attributes`* are possible:

- ***"point_normal"*:** —

  This value specifies that the
  attribute with the 3D point normals and the attribute with the
  3D point coordinates are removed.
- ***"triangles"*:** —

  This value specifies that the
  attribute with the face triangles is removed.
- ***"polygons"*:** —

  This value specifies that the
  attribute with the face polygon is removed.
- ***"lines"*:** —

  This value specifies that the
  attribute with the lines is removed.
- ***"xyz_mapping"*:** —

  This value specifies that the
  attribute with the mapping to image coordinates is removed.
- ***"extended_attribute"*:** —

  This value specifies that all
  user-defined extended attributes are removed.
- ***"primitives_all"*:** —

  This value specifies that the
  attribute with the parameters of the primitive (including an empty
  primitive) is removed (e.g., obtained from
  the operator [`FitPrimitivesObjectModel3d`](fit_primitives_object_model_3d.md)).
- ***"primitive_plane"*:** —

  This value specifies that the
  attribute with the primitive plane is removed (e.g., obtained from
  the operator [`FitPrimitivesObjectModel3d`](fit_primitives_object_model_3d.md)).
- ***"primitive_sphere"*:** —

  This value specifies that the
  attribute with the primitive sphere is removed (e.g., obtained from
  the operator [`FitPrimitivesObjectModel3d`](fit_primitives_object_model_3d.md)).
- ***"primitive_cylinder"*:** —

  This value specifies that the
  attribute with the primitive cylinder is removed (e.g., obtained from
  the operator [`FitPrimitivesObjectModel3d`](fit_primitives_object_model_3d.md)).
- ***"primitive_box"*:** —

  This value specifies that the
  attribute with the primitive cylinder is removed.
- ***"shape_based_matching_3d_data"*:** —

  This value
  specifies that the attribute with the prepared shape model for
  shape-based 3D matching is removed.
- ***"distance_computation_data"*:** —

  This value
  specifies that the attribute with the distance computation data
  structure is removed.
  The distance computation data can be created with
  [`PrepareObjectModel3d`](prepare_object_model_3d.md), and can be used with
  [`DistanceObjectModel3d`](distance_object_model_3d.md).
- ***"all"*:** —

  This value specifies that all available
  attributes are removed except for the point coordinates. That is, the
  attributes are the point normals, the face triangles, the face polygons,
  the mapping to image coordinates, the shape model for matching, the
  parameter of a primitive, and the extended attributes.

### Extended attributes

Extended attributes are attributes, that can be derived from
standard attributes by special operators (e.g.,
[`DistanceObjectModel3d`](distance_object_model_3d.md)), or user-defined attributes
(set with [`SetObjectModel3dAttrib`](set_object_model_3d_attrib.md) or
[`SetObjectModel3dAttribMod`](set_object_model_3d_attrib_mod.md)).
The extended attributes can be removed by setting their names in
*`attributes`*.

The following predefined extended attributes can be removed:

- ***"original_point_indices"*:** —

  This value specifies that the
  attribute with the original point indices is removed. Original point
  indices may be obtained from the operator
  [`TriangulateObjectModel3d`](triangulate_object_model_3d.md).
- ***"score"*:** —

  This value specifies that the
  attribute with the scores is removed. Scores may be obtained from the
  operator [`ReconstructSurfaceStereo`](reconstruct_surface_stereo.md).
- ***"red"*:** —

  This value specifies that the attribute containing
  the red color is removed.
- ***"green"*:** —

  This value specifies that the attribute containing
  the green color is removed.
- ***"blue"*:** —

  This value specifies that the attribute containing
  the blue color is removed.
- ***"edge_dir_x"*:** —

  This value specifies that the vector for the X axis is removed.
- ***"edge_dir_y"*:** —

  This value specifies that the vector for the Y axis is removed.
- ***"edge_dir_z"*:** —

  This value specifies that the vector for the Z axis is removed.
- ***"edge_amplitude"*:** —

  This value specifies that the vector for the amplitude is removed.

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

**`objectModel3DOut`** (output_control)  object_model_3d `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the resulting 3D object model.

## Result

If the parameters are valid, the operator
`RemoveObjectModel3dAttrib` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Possible Predecessors

`SetObjectModel3dAttrib`

## Possible Successors

`GetObjectModel3dParams`

## Alternatives

`RemoveObjectModel3dAttribMod`

## See also

`CopyObjectModel3d`,
`SetObjectModel3dAttrib`

## Module

3D Metrology
