# smooth_object_model_3d (Operator)

## Name

`smooth_object_model_3d` — Smooth the 3D points of a 3D object model.

## Signature

`smooth_object_model_3d( : : ObjectModel3D, Method, GenParamName, GenParamValue : SmoothObjectModel3D)`

## Description

The operator `smooth_object_model_3d` smoothes the 3D points in
*`ObjectModel3D`* and returns the smoothed points in
*`SmoothObjectModel3D`*.
Currently, the operator offers three methods for smoothing that can be
selected in *`Method`*: *'mls'*, *'xyz_mapping'* and
*'xyz_mapping_compute_normals'*. *'mls'* applies a Moving
Least Squares (MLS) algorithm on the 3D points. As a side effect of the
smoothing, the method extends *`SmoothObjectModel3D`* by
corresponding normals. *'xyz_mapping'* smoothes the coordinates
of the 3D points using a 2D filter and the 2D mapping contained in
*`ObjectModel3D`*. *'xyz_mapping_compute_normals'* applies
the same smoothing as *'xyz_mapping'*, but additionally extends
*`SmoothObjectModel3D`* by normals.

Additional parameters can be set with *`GenParamName`* and
*`GenParamValue`*. The parameter names settable for
*`Method`*=*'mls'* use the prefix *'mls'*.
Analogically, parameter names settable for
*`Method`*=*'xyz_mapping'* and
*`Method`*=*'xyz_mapping_compute_normals'* use the prefix
*'xyz_mapping'*.

### MLS smoothing

By selecting *`Method`*=*'mls'*, for each point P, the
MLS smoothing algorithm fits a planar surface or a higher order polynomial
surface to its `k`-neighborhood (the `k`
nearest points).
The surface fitting is essentially a standard *weighted least squares*
parameter estimation of the plane or polynomial surface parameters,
respectively.
The closest neighbors of P have higher contribution than the other
points, which is controlled by the following *weighting function*
with a parameter $\sigma$:
$$w(P') = exp\left(-\frac{\|P' - P\|^2}{\sigma^2}\right)$$ ![figure](../assets/51d97c8a44717904.svg)
The point is then projected on the surface. This process is repeated for
all points resulting in a smoothed point set. The fitted surfaces have
well defined normals (i.e., they can easily be computed from the
surface parameters). Therefore, the points are augmented by the
corresponding normals as side effect of the smoothing.

Additional parameters can be adjusted for the *MLS smoothing*
specifically using the following parameter names and values for
*`GenParamName`* and *`GenParamValue`*:

- ***'mls_kNN'*:** —

  Specify the number of nearest neighbors `k` that are
  used to fit the MLS surface to each point.

  Suggested values:
   *40*, *60*,
  *80*, *100*, *400*.

  Default:
   *60*.
- ***'mls_order'*:** —

  Specify the order of the MLS polynomial surface. For
  *'mls_order'*=*1* the surface is a plane.

  Suggested values:
   *1*, *2*,*3*.

  Default:
   *2*.
- ***'mls_abs_sigma'*:** —

  Specify the weighting parameter $\sigma$ as a
  fixed absolute value in meter. The value to be selected depends on the
  scale of the point data. As a rule of thumb,
  $\sigma$ can be selected to be the typical distance
  between a point P and its k/2-th neighbor
  $P_{k/2}$. Note that setting an absolute weighting
  parameter for point data with varying density might result in different
  smoothing results for points that are situated in parts of the point
  data with different densities.
  This problem can be avoided by using *'mls_relative_sigma'*
  instead that is scale independent, which makes it also a more
  convenient way to specify the neighborhood weighting. Note that if
  *'mls_abs_sigma'* is passed, any value set in
  *'mls_relative_sigma'* is ignored.

  Suggested values:
   *0.0001*, *0.001*,
  *0.01*, *0.1*, *1.0*.
- ***'mls_relative_sigma'*:** —

  Specify a multiplication factor $\sigma_{rel}$
  that is used to compute $\sigma_{P}$ for a point
  P by the formula:
  $$\sigma_{P}=\sigma_{rel}\|P_{k/2}-P\|,$$
  where $P_{k/2}$ is the k/2-th neighbor of
  P. Note that, unlike $\sigma$, which
  is a global parameter for all points, $\sigma_{P}$
  is computed for each point P and therefore adapts the
  weighting function to its neighborhood. This avoids problems that
  might appear while trying to set a global parameter
  $\sigma$ (*'mls_abs_sigma'*) to a point data
  with highly varying point density. Note however that if
  *'mls_abs_sigma'* is set, *'mls_relative_sigma'* is
  ignored.

  Suggested values:
   *0.1*, *0.5*, *1.0*,
  *1.5*, *2.0*.

  Default:
   *1.0*.
- ***'mls_force_inwards'*:** —

  If this parameter is set to *'true'*, all surface normals
  are oriented such that they point “in the direction of the
  origin”. Expressed mathematically, it is ensured that the
  scalar product between the normal vector and the vector from the
  respective surface point to the origin is positive. This may be
  necessary if the resulting *`SmoothObjectModel3D`* is used
  for surface-based matching, either as model in
  [`create_surface_model`](create_surface_model.md) or as 3D scene in
  find_surface_model, because here, the consistent orientation
  of the normals is important for the matching process. If
  *'mls_force_inwards'* is set to *'false'*, the
  normal vectors are oriented arbitrarily.

  List of values:
   *'true'*, *'false'*.

  Default:
   *'true'*.

### 2D mapping smoothing

By selecting *`Method`*=*'xyz_mapping'* or
*`Method`*=*'xyz_mapping_compute_normals'*, the coordinates
of the 3D points are smoothed using a 2D filter and the 2D mapping
contained in *`ObjectModel3D`*.
Additionally, for *`Method`*=*'xyz_mapping_compute_normals'*,
*`SmoothObjectModel3D`* is extended by normals computed from the
XYZ-mapping. If no 2D mapping is available, an exception is raised.
As the filter operates on the 2D depth image, using
*`Method`*=*'xyz_mapping'* or
*`Method`*=*'xyz_mapping_compute_normals'* is usually faster than
using *`Method`*=*'mls'*.
Invalid points (e.g., duplicated points with coordinates [0,0,0]) should be
removed from the 3D object model before applying the operator, e.g., by using
[`select_points_object_model_3d`](select_points_object_model_3d.md) with attribute *'point_coord_z'*
or *'num_neighbors_fast X'*.

Additional parameters can be adjusted for the *2D mapping smoothing*
specifically using the following parameter names and values for
*`GenParamName`* and *`GenParamValue`*:

- ***'xyz_mapping_filter'*:** —

  Specify the filter used for smoothing the 2D mapping.
  The sizes of the corresponding filter mask are set with
  *'xyz_mapping_mask_width'* and
  *'xyz_mapping_mask_height'*.

  In the default filter mode *'median_separate'*, the filter method
  used on the 2D image is comparable to [`median_separate`](median_separate.md). This mode
  is usually faster than *'median'*, but can also lead to less
  accurate results or artifacts at surface discontinuities.

  Using filter mode *'median'*, the used filter method is comparable
  to [`median_image`](median_image.md).

  List of values:
   *'median_separate'*, *'median'*.

  Default:
   *'median_separate'*.
- ***'xyz_mapping_mask_width'*,
  *'xyz_mapping_mask_height'*:** —

  Specify the width and height of the used filter mask.

  For *'xyz_mapping_filter'*=*'median_separate'* or
  *'xyz_mapping_filter'*=*'median'*, even values for
  *'xyz_mapping_mask_width'* or *'xyz_mapping_mask_height'*
  are increased to the next odd value automatically.

  For *'xyz_mapping_filter'*=*'median'*, the used filter mask
  must be quadratic (*'xyz_mapping_mask_width'* =
  *'xyz_mapping_mask_height'*). Thus, when setting only
  *'xyz_mapping_mask_width'* or
  *'xyz_mapping_mask_height'*, the other parameter is set to the same
  value automatically. If two different values are set, an error is raised.

  Suggested values:
   *3*, *5*, *7*, *9*.

  Default:
   *3*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator supports canceling timeouts and interrupts.

## Parameters

**`ObjectModel3D`** (input_control)  object_model_3d(-array) `→`  (handle)

Handle of the 3D object model containing 3D point
data.

**`Method`** (input_control)  string `→`  (string)

Smoothing method.

Default:
'mls'

List of values:
'mls', 'xyz_mapping', 'xyz_mapping_compute_normals'

**`GenParamName`** (input_control)  attribute.name-array `→`  (string)

Names of generic smoothing parameters.

Default:
[]

List of values:
'mls_abs_sigma', 'mls_force_inwards', 'mls_kNN', 'mls_order', 'mls_relative_sigma', 'xyz_mapping_filter', 'xyz_mapping_mask_height', 'xyz_mapping_mask_width'

**`GenParamValue`** (input_control)  attribute.value-array `→`  (real / integer / string)

Values of generic smoothing parameters.

Default:
[]

Suggested values:
10, 20, 40, 60, 0.1, 0.5, 1.0, 2.0, 0, 1, 2, 3, 5, 7, 9

**`SmoothObjectModel3D`** (output_control)  object_model_3d(-array) `→`  (handle)

Handle of the 3D object model with the smoothed 3D
point data.

## Alternatives

`surface_normals_object_model_3d`,
`sample_object_model_3d`,
`simplify_object_model_3d`

## Module

3D Metrology
