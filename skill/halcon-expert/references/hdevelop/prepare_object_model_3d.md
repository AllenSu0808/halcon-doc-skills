# prepare_object_model_3d (Operator)

## Name

`prepare_object_model_3d` — Prepare a 3D object model for a certain operation.

## Signature

`prepare_object_model_3d( : : ObjectModel3D, Purpose, OverwriteData, GenParamName, GenParamValue : )`

## Description

The operator `prepare_object_model_3d` prepares the 3D object model
*`ObjectModel3D`* for a following operation given in *`Purpose`*.
It computes values required for the operation and stores them in
*`ObjectModel3D`*, thus speeding up the following operation.
It is not necessary to call `prepare_object_model_3d`. However, if the
3D object model is to be used multiple times for the same operation, it
can be faster to do so.

The following values are possible for *`Purpose`*:

- ***'shape_based_matching_3d'*:** —

  The 3D object model is prepared to be used in
  [`create_shape_model_3d`](create_shape_model_3d.md). For this, there are no generic
  parameters to set.
- ***'segmentation'*:** —

  The 3D object model is prepared to be used in
  [`segment_object_model_3d`](segment_object_model_3d.md). For the preparation the 3D
  object model must have an attribute with the face triangles and
  an attribute with the 3D point coordinates.

  If the 3D object model has no attribute with the face triangles, a
  simple triangulation is performed (even if *`OverwriteData`*
  is set to *'false'*). For this, the
  3D object model must have an attribute with the 3D point
  coordinates and an attribute with the mapping from the point
  coordinates to image coordinates. Only points originating from
  neighboring pixels are triangulated. Additionally, holes in the
  image region can be filled with a Delaunay triangulation
  (see *'max_area_holes'* below). Only holes which are completely
  surrounded by the image region are closed.
- ***'distance_computation'*:** —

  The 3D object model is prepared to be used in
  [`distance_object_model_3d`](distance_object_model_3d.md).
- ***'gen_xyz_mapping'*:** —

  The XYZ-mapping information of a 3D object model containing an ordered
  point cloud is computed, i.e. image coordinates are assigned for each
  3D point. For this, either the generic parameter *'xyz_map_width'*
  or *'xyz_map_height'* must be set, to indicate whether the point
  cloud is ordered row-wise or column-wise and define the image dimensions
  (see *'xyz_map_width'* and *'xyz_map_height'* below).

  Note that in many cases, it is recommended to use the 2D mapping data,
  if available, for speed and robustness reasons. This is beneficial
  especially when using [`sample_object_model_3d`](sample_object_model_3d.md),
  [`surface_normals_object_model_3d`](surface_normals_object_model_3d.md), or when preparing a 3D object
  model for surface-based matching, e.g., smoothing, removing outliers, and
  reducing the domain.

The parameter *`OverwriteData`* defines if the existing data
of an already prepared 3D object model shall be removed. If
*`OverwriteData`* is set to *'true'*, the prepared data,
defined with the parameter *`Purpose`*, is overwritten. If
*`OverwriteData`* is set to *'false'*, the prepared data
is not overwritten. If there is no prepared data *`OverwriteData`*
is ignored and data is saved in a 3D object model.
The parameter *`OverwriteData`* can be used
for choosing another set of generic parameters *`GenParamName`*
and *`GenParamValue`*. The parameter *`OverwriteData`*
has no influence if the parameter *`Purpose`* is
set to *'shape_based_matching_3d'*, because for that, there
are no generic parameters to set.

The generic parameters can optionally be used to
influence the preparation. If desired, these parameters and their
corresponding values can be specified by using *`GenParamName`*
and *`GenParamValue`*, respectively. The following values for
*`GenParamName`* are possible:

- ***'max_area_holes'*:** —

  This parameter is only valid if
  *`Purpose`* is set to *'segmentation'*. The parameter
  specifies which area holes of the point coordinates are closed
  during a simple Delaunay triangulation. Only holes which are completely
  surrounded by the image region are closed.
  If *'max_area_holes'* is set to *0*,
  no holes are triangulated. If the parameter
  *'max_area_holes'* is set greater or equal than *1*
  pixel, the holes with an area less or equal than
  *'max_area_holes'* are closed by a meshing.

  Suggested values:
   *1*, *10*, *100*.

  Default:
   *10*.
- ***'distance_to'*:** —

  This parameter is only valid if
  *`Purpose`* is set to *'distance_computation'*.
  The parameter specifies the type of data to which the distance shall be
  computed to.
  It is described in more detail in the documentation of
  [`distance_object_model_3d`](distance_object_model_3d.md).

  List of values:
   *'auto'*, *'triangles'*,
  *'points'*, *'primitive'*.

  Default:
   *'auto'*.
- ***'method'*:** —

  This parameter is only valid if
  *`Purpose`* is set to *'distance_computation'*.
  The parameter specifies the method to be used for the distance computation.
  It is described in more detail in the documentation of
  [`distance_object_model_3d`](distance_object_model_3d.md).

  List of values:
   *'auto'*, *'kd-tree'*,
  *'voxel'*, *'linear'*.

  Default:
   *'auto'*.
- ***'max_distance'*:** —

  This parameter is only valid if
  *`Purpose`* is set to *'distance_computation'*.
  The parameter specifies the maximum distance of interest for the
  distance computation. If it is set to *0*, no maximum distance
  is used.
  It is described in more detail in the documentation of
  [`distance_object_model_3d`](distance_object_model_3d.md).

  Suggested values:
   *0*, *0.1*,
  *1*, *10*.

  Default:
   *0*.
- ***'sampling_dist_rel'*:** —

  This parameter is only valid if
  *`Purpose`* is set to *'distance_computation'*.
  The parameter specifies the relative sampling distance when computing
  the distance to triangles with the method *'voxel'*.
  It is described in more detail in the documentation of
  [`distance_object_model_3d`](distance_object_model_3d.md).

  Suggested values:
   *0.03*, *0.01*.

  Default:
   *0.03*.
- ***'sampling_dist_abs'*:** —

  This parameter is only valid if
  *`Purpose`* is set to *'distance_computation'*.
  The parameter specifies the absolute sampling distance when computing
  the distance to triangles with the method *'voxel'*.
  It is described in more detail in the documentation of
  [`distance_object_model_3d`](distance_object_model_3d.md).

  Suggested values:
   *1*, *5*, *10*.

  Default:
   None.
- ***'xyz_map_width'*:** —

  This parameter is only valid if
  *`Purpose`* is set to *'gen_xyz_mapping'*. The parameter
  indicates that the point cloud is ordered row-wise and the passed
  value is used as the width of the image. The height of the image is
  calculated automatically. Only one of the two parameters
  *'xyz_map_width'* and *'xyz_map_height'* can be set.

  Default:
   None.
- ***'xyz_map_height'*:** —

  This parameter is only valid if
  *`Purpose`* is set to *'gen_xyz_mapping'*. The parameter
  indicates that the point cloud is ordered column-wise and the passed
  value is used as the height of the image. The width of the image is
  calculated automatically. Only one of the two parameters
  *'xyz_map_width'* and *'xyz_map_height'* can be set.

  Default:
   None.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ObjectModel3D`** (input_control)  object_model_3d(-array) `→`  (handle)

Handle of the 3D object model.

**`Purpose`** (input_control)  string `→`  (string)

Purpose of the 3D object model.

Default:
'shape_based_matching_3d'

Suggested values:
'shape_based_matching_3d', 'segmentation', 'distance_computation', 'gen_xyz_mapping'

**`OverwriteData`** (input_control)  string `→`  (string)

Specify if already existing data should be overwritten.

Default:
'true'

List of values:
'false', 'true'

**`GenParamName`** (input_control)  attribute.name-array `→`  (string / real / integer)

Names of the generic parameters.

Default:
[]

List of values:
'distance_to', 'max_area_holes', 'max_distance', 'method', 'sampling_dist_abs', 'sampling_dist_rel', 'xyz_map_height', 'xyz_map_width'

**`GenParamValue`** (input_control)  attribute.value-array `→`  (string / real / integer)

Values of the generic parameters.

Default:
[]

Suggested values:
0, 1, 100, 'auto', 'triangles', 'points', 'primitive', 'kd-tree', 'voxel', 'linear', 0.01, 0.03

## Example (HDevelop)

```
read_object_model_3d ('object_model_3d', 'm', [], [], ObjectModel3D, Status)
prepare_object_model_3d (ObjectModel3D, 'gen_xyz_mapping', 'true',\
                         'xyz_map_width', Width)
object_model_3d_to_xyz (X, Y, Z, ObjectModel3D, 'from_xyz_map', [], [])
```

## Result

The operator `prepare_object_model_3d` returns the value
2 (
H_MSG_TRUE)
if the given parameters are correct. Otherwise, an exception
will be raised.

## Possible Predecessors

`read_object_model_3d`,
`xyz_to_object_model_3d`

## Possible Successors

`create_shape_model_3d`,
`create_surface_model`,
`distance_object_model_3d`,
`find_surface_model`,
`fit_primitives_object_model_3d`,
`refine_surface_model_pose`,
`segment_object_model_3d`,
`simplify_object_model_3d`,
`sample_object_model_3d`,
`surface_normals_object_model_3d`

## Module

3D Metrology
