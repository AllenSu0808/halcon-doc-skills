# sample_object_model_3d (Operator)

## Name

`sample_object_model_3d` — Sample a 3D object model.

## Signature

`sample_object_model_3d( : : ObjectModel3D, Method, SamplingParam, GenParamName, GenParamValue : SampledObjectModel3D)`

## Description

`sample_object_model_3d` creates a sampled version of the 3D object
model *`ObjectModel3D`* and returns it in *`SampledObjectModel3D`*.
Depending on the method used, *`SamplingParam`* controls the minimum
distance or the number of points in *`SampledObjectModel3D`*.
The created 3D object model is returned in *`SampledObjectModel3D`*.

Using `sample_object_model_3d` is recommended if complex point clouds
are to be thinned out for faster postprocessing or if primitives are to be
converted to point clouds.
Note that if the 3D object model is triangulated and should be simplified by
preserving its original geometry as good as possible,
[`simplify_object_model_3d`](simplify_object_model_3d.md) should be used instead.

If the input object model *`ObjectModel3D`* contains only points,
several sampling methods are available which can be selected using
the parameter *`Method`*:

- ***'fast'*:** —

  The default method *'fast'* adds
  all points from the input model which are not
  closer than *`SamplingParam`* to any point that was earlier added to
  the output model.
  If present, normals, XYZ-mapping and extended point attributes are copied to
  the output model.
- ***'fast_compute_normals'*:** —

  The method *'fast_compute_normals'* selects the same points
  as the method *'fast'*, but additionally calculates the
  normals for all points that were selected.
  For this, the input object model must either contain normals, which are
  copied, or it must contain a XYZ-mapping attribute from which the
  normals are computed. The z-component of the calculated normal
  vectors is always positive. The XYZ-mapping is created by
  [`xyz_to_object_model_3d`](xyz_to_object_model_3d.md).
- ***'accurate'*:** —

  The method *'accurate'* goes through the points of the 3D object
  model *`ObjectModel3D`* and calculates whether any other points are
  within a sphere with the radius *`SamplingParam`* around the
  examined point.
  If there are no other points, the original point is stored
  in *`SampledObjectModel3D`*.
  If there are other points, the center of gravity of these
  points (including the original point) is stored in
  *`SampledObjectModel3D`*.
  This procedure is repeated with the remaining points until there
  are no points left.
  Extended attributes of the input 3D object model are not copied, but
  normals and XYZ-mapping are copied.
  For this method, a noise removal is possible by specifying a
  value for *'min_num_points'*
  in *`GenParamName`* and *`GenParamValue`*, which removes all
  interpolated points that had less than the specified number of neighbor
  points in the original model.
- ***'accurate_use_normals'*:** —

  The method *'accurate_use_normals'* requires normals in the
  input 3D object model and interpolates only points with similar
  normals.
  The similarity depends on the angle between the normals. The threshold
  of the angle can be specified in *`GenParamName`* and
  *`GenParamValue`* with *'max_angle_diff'*.
  The default value is *180* degrees.
  Additionally, outliers can be removed as described in the method
  *'accurate'*, by setting the generic parameter
  *'min_num_points'*.
- ***'xyz_mapping'*:** —

  The method *'xyz_mapping'* can only be applied to 3D object models
  that contain an XYZ-mapping (for example, if it was created using
  [`xyz_to_object_model_3d`](xyz_to_object_model_3d.md)).
  This mapping stores for each 3D point its original image coordinates.
  The method *'xyz_mapping'* subdivides those original images into
  squares with side length *`SamplingParam`* (which is given in
  pixel) and selects one 3D point per square.

  The method behaves similar to applying [`zoom_image_factor`](zoom_image_factor.md) onto
  the original XYZ-images.
  Note that this method does not use the 3D-coordinates of the points for
  the point selection, only their 2D image coordinates.

  It is important to notice that for this method, the parameter
  *`SamplingParam`* corresponds to a distance in pixels, not to a
  distance in 3D space.
- ***'xyz_mapping_compute_normals'*:** —

  The method *'xyz_mapping_compute_normals'* selects the same points
  as the method *'xyz_mapping'*, but additionally calculates the
  normals for all points that were selected. The z-component of the normal
  vectors is always positive.
  If the input object model contains normals, those normals are copied
  to the output.
  Otherwise, the normals are computed based on the XYZ-mapping.
- ***'furthest_point'*:** —

  The method *'furthest_point'* iteratively adds the point of the
  input object to the output object that is furthest from all points
  already added to the output model. This usually leads to a reasonably
  uniform sampling.
  For this method, the desired number of points in the output model is
  passed in *`SamplingParam`*.
  If that number exceeds the number of points in the input object,
  then all points of the input object are returned.

  The first point added to the output object is the point that is
  furthest away from the center of the axis aligned bounding box
  around the points of the input object.
- ***'furthest_point_compute_normals'*:** —

  The method *'furthest_point_compute_normals'* selects the same points
  as the method *'furthest_point'*, but additionally calculates the
  normals for all points that were selected.
  The number of desired points in the output object is passed in
  *`SamplingParam`*.

  To compute the normals, the input object model must either contain normals,
  which are copied, or it must contain a XYZ-mapping attribute from which the
  normals are computed. The z-component of the calculated normal
  vectors is always positive. The XYZ-mapping is created by
  [`xyz_to_object_model_3d`](xyz_to_object_model_3d.md).

If the input object model contains faces (triangles or polygons) or is
a 3D primitive, the surface is sampled with the given
distance.
In this case, the method specified in *`Method`* is ignored.
The directions of the computed normals depend on the face orientation of the
model. Usually, the orientation of the faces does not vary within one
CAD model, which results in a set of normals that is either pointing inwards
or outwards.
Note that planes and cylinders must have finite extent.
If the input object model contains lines, the lines are sampled with the
given distance *`SamplingParam`*.

The sampling process approximates surfaces by creating new points in the
output object model.
Therefore, any extended attributes from the input object model are discarded.

For mixed input object models, the sampling priority is (from top to
bottom) faces, lines, primitives and points, i.e., only the objects
of the highest priority are sampled.

The parameter *`SamplingParam`* accepts either one value, which is
then used for all 3D object models passed in *`ObjectModel3D`*, or one
value per input object model. If *`SamplingParam`* is a distance in 3D
space the unit is the usual HALCON-internal unit *'m'*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator supports canceling timeouts and interrupts.

## Parameters

**`ObjectModel3D`** (input_control)  object_model_3d(-array) `→`  (handle)

Handle of the 3D object model to be sampled.

**`Method`** (input_control)  string `→`  (string)

Selects between the different subsampling methods.

Default:
'fast'

List of values:
'accurate', 'accurate_use_normals', 'fast', 'fast_compute_normals', 'furthest_point', 'furthest_point_compute_normals', 'xyz_mapping', 'xyz_mapping_compute_normals'

**`SamplingParam`** (input_control)  real(-array) `→`  (real / integer)

Sampling distance or number of points.

Number of elements:
SamplingParam == 1 || SamplingParam == ObjectModel3D

Default:
0.05

**`GenParamName`** (input_control)  string-array `→`  (string)

Names of the generic parameters that can be adjusted.

Default:
[]

List of values:
'max_angle_diff', 'min_num_points'

**`GenParamValue`** (input_control)  number-array `→`  (real / integer / string)

Values of the generic parameters that can be
adjusted.

Default:
[]

Suggested values:
1, 2, 5, 10, 20, 0.1, 0.25, 0.5

**`SampledObjectModel3D`** (output_control)  object_model_3d(-array) `→`  (handle)

Handle of the 3D object model that contains the
sampled points.

Number of elements:
SampledObjectModel3D == ObjectModel3D

## Example (HDevelop)

```
gen_box_object_model_3d ([0,0,0,0,0,0,0],3,2,1, ObjectModel3D)
sample_object_model_3d (ObjectModel3D, 'fast', 0.05, [], [], \
                        SampledObjectModel3D)
dev_get_window (WindowHandle)
visualize_object_model_3d (WindowHandle, SampledObjectModel3D, \
                           [], [], [], [], [], [], [], PoseOut)
```

## Result

`sample_object_model_3d` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

## Possible Predecessors

`read_object_model_3d`,
`gen_plane_object_model_3d`,
`gen_sphere_object_model_3d`,
`gen_cylinder_object_model_3d`,
`gen_box_object_model_3d`,
`gen_sphere_object_model_3d_center`,
`xyz_to_object_model_3d`

## Possible Successors

`get_object_model_3d_params`,
`clear_object_model_3d`

## Alternatives

`simplify_object_model_3d`,
`smooth_object_model_3d`

## Module

3D Metrology
