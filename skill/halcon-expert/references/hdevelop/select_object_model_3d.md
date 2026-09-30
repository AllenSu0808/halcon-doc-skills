# select_object_model_3d (Operator)

## Name

`select_object_model_3d` — Select 3D object models from an array of 3D object models according
to global features.

## Signature

`select_object_model_3d( : : ObjectModel3D, Feature, Operation, MinValue, MaxValue : ObjectModel3DSelected)`

## Description

`select_object_model_3d` selects 3D object models from an array of
3D object models for which the values of specified global features lie
within a specified range.
The list of possible features that may be specified in *`Feature`* are:

- ***'mean_points_x'*:** —

  The mean x-coordinate of the points in the 3D object model.
- ***'mean_points_y'*:** —

  The mean y-coordinate of the points in the 3D object model.
- ***'mean_points_z'*:** —

  The mean z-coordinate of the points in the 3D object model.
- ***'diameter_axis_aligned_bounding_box'*:** —

  The diameter of the set of 3D points, defined as the length of
  the diagonal of the smallest enclosing axis-parallel cuboid.
- ***'diameter_bounding_box'*:** —

  The diameter of the set of 3D points, defined as the length of
  the diagonal of the smallest enclosing oriented cuboid. This feature has
  a high calculation complexity.
- ***'diameter_object'*:** —

  The diameter of the set of 3D points, defined as the length of
  the distance between two points.
- ***'volume'*:** —

  The volume of the triangulation of the 3D object model over the
  x-y plane in the coordinate origin. This corresponds to the default
  parametrization of [`volume_object_model_3d_relative_to_plane`](volume_object_model_3d_relative_to_plane.md)
  with the plane [0,0,0,0,0,0,0]. The plane con not be changed here.
- ***'volume_axis_aligned_bounding_box'*:** —

  The volume of the smallest enclosing axis-parallel cuboid.
- ***'area'*:** —

  The area of the triangulation of the 3D object model.
- ***'central_moment_2_x'*:** —

  The x-value of the second central moment of the 3D object model.
- ***'central_moment_2_y'*:** —

  The y-value of the second central moment of the 3D object model.
- ***'central_moment_2_z'*:** —

  The z-value of the second central moment of the 3D object model.
- ***'central_moment_2_xy'*:** —

  The xy-value of the second central moment of the 3D object model.
- ***'central_moment_2_xz'*:** —

  The xz-value of the second central moment of the 3D object model.
- ***'central_moment_2_yz'*:** —

  The yz-value of the second central moment of the 3D object model.
- ***'num_points'*:** —

  The number of points.
- ***'num_triangles'*:** —

  The number of triangles.
- ***'num_faces'*:** —

  The number of faces.
- ***'num_lines'*:** —

  The number of polylines.
- ***'has_points'*:** —

  The existence of 3D points.
- ***'has_point_normals'*:** —

  The existence of 3D point normals.
- ***'has_triangles'*:** —

  The existence of triangles.
- ***'has_faces'*:** —

  The existence of faces or polygons.
- ***'has_lines'*:** —

  The existence of lines.
- ***'has_xyz_mapping'*:** —

  The existence of a mapping of the 3D points to image
  coordinates.
- ***'has_shape_based_matching_3d_data'*:** —

  The existence of a shape model for shape-based 3D matching.
- ***'has_surface_based_matching_data'*:** —

  The existence of data for the surface-based 3D matching.
- ***'has_segmentation_data'*:** —

  The existence of data for a 3D segmentation.
- ***'has_primitive_data'*:** —

  The existence of a 3D primitive.

For all features listed in *`Feature`* a minimal and maximal
threshold must be specified in *`MinValue`* and *`MaxValue`*.
This range is then used to select all given
3D object models that fulfill the given conditions. These are copied
to *`ObjectModel3DSelected`*. For logical parameters
(e.g., *'has_points'*, *'has_point_normals'*, ...),
*`MinValue`* and *`MaxValue`* can both be set to *'true'*
to select all 3D object models that have the respective attribute or to
*'false'* to select all that do not have it.
*`MinValue`* and *`MaxValue`* can be set to *'min'* and
*'max'* accordingly to ignore the respective threshold.

The parameter *`Operation`* defines the logical operation
that is used to combine different features in
*`Feature`*. It can be either a logical *'or'* or
*'and'*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ObjectModel3D`** (input_control)  object_model_3d(-array) `→`  (handle)

Handles of the available 3D object models to
select.

**`Feature`** (input_control)  string(-array) `→`  (string)

List of features a test is performed on.

Default:
'has_triangles'

List of values:
'area', 'central_moment_2_x', 'central_moment_2_xy', 'central_moment_2_xz', 'central_moment_2_y', 'central_moment_2_yz', 'central_moment_2_z', 'diameter_axis_aligned_bounding_box', 'diameter_bounding_box', 'diameter_object', 'has_faces', 'has_lines', 'has_point_normals', 'has_points', 'has_primitive_data', 'has_segmentation_data', 'has_shape_based_matching_3d_data', 'has_surface_based_matching_data', 'has_triangles', 'has_xyz_mapping', 'mean_points_x', 'mean_points_y', 'mean_points_z', 'num_faces', 'num_lines', 'num_points', 'num_triangles', 'volume', 'volume_axis_aligned_bounding_box'

**`Operation`** (input_control)  string `→`  (string)

Logical operation to combine the features given in
*`Feature`*.

Default:
'and'

List of values:
'and', 'or'

**`MinValue`** (input_control)  number(-array) `→`  (real / integer / string)

Minimum value for the given feature.

Default:
1

Suggested values:
0, 1, 100, 0.1, 'true', 'false', 'min'

**`MaxValue`** (input_control)  number(-array) `→`  (real / integer / string)

Maximum value for the given feature.

Default:
1

Suggested values:
0, 1, 10, 100, 0.1, 'true', 'false', 'max'

**`ObjectModel3DSelected`** (output_control)  object_model_3d(-array) `→`  (handle)

A subset of *`ObjectModel3D`* fulfilling
the given conditions.

## Example (HDevelop)

```
gen_object_model_3d_from_points (rand(20)-1.0, rand(20)-1.0,\
                                    rand(20)-1.0, ObjectModel3D1)
gen_object_model_3d_from_points (rand(20), rand(20),\
                                    rand(20), ObjectModel3D2)
select_object_model_3d ([ObjectModel3D1, ObjectModel3D2],\
                        'mean_points_x', 'and', 0, 1, ObjectModel3DSelected)
```

## Result

`select_object_model_3d` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

## Possible Predecessors

`read_object_model_3d`,
`select_points_object_model_3d`,
`connection_object_model_3d`,
`get_object_model_3d_params`,
`volume_object_model_3d_relative_to_plane`,
`area_object_model_3d`,
`max_diameter_object_model_3d`,
`moments_object_model_3d`

## Possible Successors

`project_object_model_3d`,
`object_model_3d_to_xyz`

## See also

`volume_object_model_3d_relative_to_plane`,
`area_object_model_3d`,
`max_diameter_object_model_3d`,
`moments_object_model_3d`,
`get_object_model_3d_params`

## Module

3D Metrology
