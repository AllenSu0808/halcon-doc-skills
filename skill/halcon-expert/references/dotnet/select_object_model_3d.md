# SelectObjectModel3d (Operator)

## Name

`SelectObjectModel3d` — Select 3D object models from an array of 3D object models according
to global features.

## Signature

`static void HOperatorSet.SelectObjectModel3d(HTuple objectModel3D, HTuple feature, HTuple operation, HTuple minValue, HTuple maxValue, out HTuple objectModel3DSelected)`

`static HObjectModel3D[] HObjectModel3D.SelectObjectModel3d(HObjectModel3D[] objectModel3D, HTuple feature, string operation, HTuple minValue, HTuple maxValue)`

`HObjectModel3D HObjectModel3D.SelectObjectModel3d(string feature, string operation, double minValue, double maxValue)`

## Description

`SelectObjectModel3d` selects 3D object models from an array of
3D object models for which the values of specified global features lie
within a specified range.
The list of possible features that may be specified in *`feature`* are:

- ***"mean_points_x"*:** —

  The mean x-coordinate of the points in the 3D object model.
- ***"mean_points_y"*:** —

  The mean y-coordinate of the points in the 3D object model.
- ***"mean_points_z"*:** —

  The mean z-coordinate of the points in the 3D object model.
- ***"diameter_axis_aligned_bounding_box"*:** —

  The diameter of the set of 3D points, defined as the length of
  the diagonal of the smallest enclosing axis-parallel cuboid.
- ***"diameter_bounding_box"*:** —

  The diameter of the set of 3D points, defined as the length of
  the diagonal of the smallest enclosing oriented cuboid. This feature has
  a high calculation complexity.
- ***"diameter_object"*:** —

  The diameter of the set of 3D points, defined as the length of
  the distance between two points.
- ***"volume"*:** —

  The volume of the triangulation of the 3D object model over the
  x-y plane in the coordinate origin. This corresponds to the default
  parametrization of [`VolumeObjectModel3dRelativeToPlane`](volume_object_model_3d_relative_to_plane.md)
  with the plane [0,0,0,0,0,0,0]. The plane con not be changed here.
- ***"volume_axis_aligned_bounding_box"*:** —

  The volume of the smallest enclosing axis-parallel cuboid.
- ***"area"*:** —

  The area of the triangulation of the 3D object model.
- ***"central_moment_2_x"*:** —

  The x-value of the second central moment of the 3D object model.
- ***"central_moment_2_y"*:** —

  The y-value of the second central moment of the 3D object model.
- ***"central_moment_2_z"*:** —

  The z-value of the second central moment of the 3D object model.
- ***"central_moment_2_xy"*:** —

  The xy-value of the second central moment of the 3D object model.
- ***"central_moment_2_xz"*:** —

  The xz-value of the second central moment of the 3D object model.
- ***"central_moment_2_yz"*:** —

  The yz-value of the second central moment of the 3D object model.
- ***"num_points"*:** —

  The number of points.
- ***"num_triangles"*:** —

  The number of triangles.
- ***"num_faces"*:** —

  The number of faces.
- ***"num_lines"*:** —

  The number of polylines.
- ***"has_points"*:** —

  The existence of 3D points.
- ***"has_point_normals"*:** —

  The existence of 3D point normals.
- ***"has_triangles"*:** —

  The existence of triangles.
- ***"has_faces"*:** —

  The existence of faces or polygons.
- ***"has_lines"*:** —

  The existence of lines.
- ***"has_xyz_mapping"*:** —

  The existence of a mapping of the 3D points to image
  coordinates.
- ***"has_shape_based_matching_3d_data"*:** —

  The existence of a shape model for shape-based 3D matching.
- ***"has_surface_based_matching_data"*:** —

  The existence of data for the surface-based 3D matching.
- ***"has_segmentation_data"*:** —

  The existence of data for a 3D segmentation.
- ***"has_primitive_data"*:** —

  The existence of a 3D primitive.

For all features listed in *`feature`* a minimal and maximal
threshold must be specified in *`minValue`* and *`maxValue`*.
This range is then used to select all given
3D object models that fulfill the given conditions. These are copied
to *`objectModel3DSelected`*. For logical parameters
(e.g., *"has_points"*, *"has_point_normals"*, ...),
*`minValue`* and *`maxValue`* can both be set to *"true"*
to select all 3D object models that have the respective attribute or to
*"false"* to select all that do not have it.
*`minValue`* and *`maxValue`* can be set to *"min"* and
*"max"* accordingly to ignore the respective threshold.

The parameter *`operation`* defines the logical operation
that is used to combine different features in
*`feature`*. It can be either a logical *"or"* or
*"and"*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`objectModel3D`** (input_control)  object_model_3d(-array) `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handles of the available 3D object models to
select.

**`feature`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

List of features a test is performed on.

Default:
"has_triangles"

List of values:
"area", "central_moment_2_x", "central_moment_2_xy", "central_moment_2_xz", "central_moment_2_y", "central_moment_2_yz", "central_moment_2_z", "diameter_axis_aligned_bounding_box", "diameter_bounding_box", "diameter_object", "has_faces", "has_lines", "has_point_normals", "has_points", "has_primitive_data", "has_segmentation_data", "has_shape_based_matching_3d_data", "has_surface_based_matching_data", "has_triangles", "has_xyz_mapping", "mean_points_x", "mean_points_y", "mean_points_z", "num_faces", "num_lines", "num_points", "num_triangles", "volume", "volume_axis_aligned_bounding_box"

**`operation`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Logical operation to combine the features given in
*`feature`*.

Default:
"and"

List of values:
"and", "or"

**`minValue`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long / string)

Minimum value for the given feature.

Default:
1

Suggested values:
0, 1, 100, 0.1, "true", "false", "min"

**`maxValue`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long / string)

Maximum value for the given feature.

Default:
1

Suggested values:
0, 1, 10, 100, 0.1, "true", "false", "max"

**`objectModel3DSelected`** (output_control)  object_model_3d(-array) `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

A subset of *`objectModel3D`* fulfilling
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

`SelectObjectModel3d` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

## Possible Predecessors

`ReadObjectModel3d`,
`SelectPointsObjectModel3d`,
`ConnectionObjectModel3d`,
`GetObjectModel3dParams`,
`VolumeObjectModel3dRelativeToPlane`,
`AreaObjectModel3d`,
`MaxDiameterObjectModel3d`,
`MomentsObjectModel3d`

## Possible Successors

`ProjectObjectModel3d`,
`ObjectModel3dToXyz`

## See also

`VolumeObjectModel3dRelativeToPlane`,
`AreaObjectModel3d`,
`MaxDiameterObjectModel3d`,
`MomentsObjectModel3d`,
`GetObjectModel3dParams`

## Module

3D Metrology
