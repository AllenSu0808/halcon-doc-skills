# DistanceObjectModel3d (Operator)

## Name

`DistanceObjectModel3d` — Compute the distances of the points of one 3D object model to another
3D object model.

## Signature

`static void HOperatorSet.DistanceObjectModel3d(HTuple objectModel3DFrom, HTuple objectModel3DTo, HTuple pose, HTuple maxDistance, HTuple genParamName, HTuple genParamValue)`

`void HObjectModel3D.DistanceObjectModel3d(HObjectModel3D objectModel3DTo, HPose pose, HTuple maxDistance, HTuple genParamName, HTuple genParamValue)`

`void HObjectModel3D.DistanceObjectModel3d(HObjectModel3D objectModel3DTo, HPose pose, double maxDistance, string genParamName, string genParamValue)`

## Description

The operator `DistanceObjectModel3d` computes the distances of
the points in the 3D object model *`objectModel3DFrom`* to the
points, triangles, polygons, or primitive in the 3D object model
*`objectModel3DTo`*. The distances are stored as an extended attribute
named *"&distance"* in the 3D object model
*`objectModel3DFrom`*. This attribute can subsequently be queried with
[`GetObjectModel3dParams`](get_object_model_3d_params.md) or be processed with
[`SelectPointsObjectModel3d`](select_points_object_model_3d.md) or other operators that use
extended attributes.

The target data (points, triangles, polygons, or primitive) is selected
based on the attributes contained in *`objectModel3DTo`*.
It is selected based on the presence of the data in the following precedence:
Primitive, triangles, polygons, and points.
As alternative to this automatic target data selection, the target data
type can also be set with the generic parameter *"distance_to"*
(see below).
Generic, non-triangular polygons are internally triangulated by the operator
before the distance to the resulting triangles is calculated. Thus,
calling the operator with triangulated objects is faster than calling
it with objects having different polygon faces.

*`maxDistance`* can be used to limit the range of the distance values
to be computed. If *`maxDistance`* is set to *0*, all distances
are computed. If *`maxDistance`* is set to another value, points whose
distance would exceed *`maxDistance`* are not processed and set to
*`maxDistance`*. Thus, setting *`maxDistance`* to a value different
than *0* can significantly speed up the execution of this operator.

If *`pose`* is a non-empty tuple, it must contain a pose which is
applied to the points in *`objectModel3DFrom`* before
computing the distances. The pose can be inverted using the generic
parameter *"invert_pose"* (see below).

Depending on the target data type (points, triangles, or primitive), several
methods for computing the distances are available.
Some of these methods compute a data structure on the elements of
*`objectModel3DTo`* to speed up the distance computation.
Those data structures can be precomputed using the operator
[`PrepareObjectModel3d`](prepare_object_model_3d.md). This allows multiple calls to
`DistanceObjectModel3d` to re-use the data structure, thus saving
the time to re-compute it for each call. For objects with non-triangular
polygon faces, the operator [`PrepareObjectModel3d`](prepare_object_model_3d.md) can additionally
perform the triangulation and save it to the object to further speed-up
the `DistanceObjectModel3d` operator. This triangulation is only
performed when the generic parameter *"distance_to"* is set to
*"triangles"*. Note that this triangulation, contrary to that of the
operator [`TriangulateObjectModel3d`](triangulate_object_model_3d.md), does not clear out the
polygons attribute.

When computing the distance to points or to triangles, the operator
can optionally return the index of the closest point or triangle for each
point in *`objectModel3DFrom`* by setting the generic parameter
*"store_closest_index"* to *"true"* (see below).
The index is stored as extended attribute named
*"&closest_index"* in the 3D object model *`objectModel3DFrom`*.
Note that the closest index can not be computed when using the
*"voxel"* method.
If a point's distance to its closest element exceeds the maximum distance
set in *`maxDistance`*, the closest index is set to -1.

Optionally, signed distances to points, triangles or to a primitive can be
calculated. Therefore, the generic parameter *"signed_distances"* has
to be set to *"true"*.
Note that signed distances can not be computed when using the
*"voxel"* method in combination with point to point distances.

In the following, the different target types and methods are explained,
and their advantages and disadvantages are described. Note that
the operator automatically selects a default method depending on
the target data type. This method can be overridden using the
generic parameter *"method"*.

- **Distance to points:** —

  The following methods are available to compute
  the distances from points to points:

  - **Linear search:** —

    For each point in *`objectModel3DFrom`*,
    the distances to all points in *`objectModel3DTo`* are computed,
    and the smallest distance is used.
    This method requires no precomputed data structure, and is the
    fastest for a small number of points in *`objectModel3DTo`*.
  - **KD-Tree:** —

    The points in *`objectModel3DTo`* are organized in
    a KD-Tree, which speeds up the search for the closest point.
    The construction of the tree is very efficient.
    The search time is approximately logarithmic to the number of
    points in *`objectModel3DTo`*.
    However, the search time is not constant, and can vary significantly
    depending on the position of the query points in
    *`objectModel3DFrom`*.
  - **Voxel:** —

    The points in *`objectModel3DTo`* are organized in a
    voxel structure.
    This voxel structure allows searching in almost constant time, i.e.,
    independent from the position of the query points in
    *`objectModel3DFrom`* and the number of points
    in *`objectModel3DTo`*.

    Note that the preparation of this data structure takes several seconds
    or minutes. However, it is possible to perform a precomputation using
    [`PrepareObjectModel3d`](prepare_object_model_3d.md) on *`objectModel3DTo`*
    with `purpose` set to *"distance_computation"*.
- **Distance to triangles:** —

  For computing the distances to triangles,
  the following methods are supported:

  - **Linear search:** —

    For each point in *`objectModel3DFrom`*,
    the distances to all triangles in *`objectModel3DTo`* are computed,
    and the smallest distance is used.
    This method requires no precomputed data structure, and is the
    fastest for a small number of triangles in *`objectModel3DTo`*.
  - **KD-Tree:** —

    The triangles in *`objectModel3DTo`* are organized in
    a KD-Tree, which speeds up the search for the closest triangle.
    The construction of the tree is efficient.
    The search time is approximately logarithmic to the number of
    triangles in *`objectModel3DTo`*.
    However, the search time is not constant, and can vary significantly
    depending on the position of the query points in
    *`objectModel3DFrom`*.
  - **Voxel:** —

    The triangles in *`objectModel3DTo`* are organized in a
    voxel structure.
    This voxel structure allows searching in almost constant time, i.e.,
    independent from the position of the query points in
    *`objectModel3DFrom`* and the number of triangles
    in *`objectModel3DTo`*.

    Note that the preparation of this data structure takes several seconds
    or minutes. However, it is possible to perform a precomputation using
    [`PrepareObjectModel3d`](prepare_object_model_3d.md) on *`objectModel3DTo`*
    with `purpose` set to *"distance_computation"*.
    For creating the voxel data structure, the triangles are sampled.
    The corresponding sampling distance can be set with the generic
    parameters *"sampling_dist_rel"* and *"sampling_dist_abs"*.

    By default, a relative sampling distance of *0.03* is used.
    See below for a more detailed description of the sampling distance.
    Note that this data structure is only approximate. It is possible that
    some of the distances are off by around 10% of the sampling distance.
    In these cases, the returned distances will always be larger than the
    actual distances.
- **Distance to primitive:** —

  Since *`objectModel3DTo`* can contain
  only one primitive, the distances from the query points to this primitive
  are computed linearly.
  The creation or usage of a data structure is not possible.

  Note that computing the distance to primitive planes fitted with
  [`SegmentObjectModel3d`](segment_object_model_3d.md) or [`FitPrimitivesObjectModel3d`](fit_primitives_object_model_3d.md)
  can be slow, since those planes contain a complex convex hull of the
  points that were used to fit the plane.
  If only the distance to the plane is required, and the boundary should
  be ignored, it is recommended to obtain the plane pose using
  [`GetObjectModel3dParams`](get_object_model_3d_params.md) with parameter
  *"primitive_parameter_pose"* and create a new plane
  using [`GenPlaneObjectModel3d`](gen_plane_object_model_3d.md).

The following table lists the different target data types, methods, and their
properties. The search time is the approximate time per point in
*`objectModel3DFrom`*. N is the number of target elements
in *`objectModel3DTo`*.

| Target Data | Method | Creation Time | Approximate Search Time | Properties |
| --- | --- | --- | --- | --- |
| points | linear | 0 | $O(N)$ | - No precomputation |
|  |  |  |  | - Fastest for small $N$ |
|  |  |  |  | - Default for $N<100$ |
|  |  |  |  |  |
| points | kd-tree | $O(N\log (N))$ | $O(\log (N))$ | - Fast structure creation |
|  |  |  |  | - Non-constant search time |
|  |  |  |  | - Default for $N\ge100$ |
|  |  |  |  |  |
| points | voxel | $O(N\log (N))$ | $O(\log (\log (N)))$ | - Slow structure creation |
|  |  |  |  | - Very fast search |
|  |  |  |  | - Default for precomputation with [`PrepareObjectModel3d`](prepare_object_model_3d.md) |
|  |  |  |  |  |
|  |  |  |  |  |
| triangles | linear | 0 | $O(N)$ | - No precomputation |
|  |  |  |  | - Fastest for small $N$ |
|  |  |  |  | - Default |
|  |  |  |  |  |
| triangles | kd-tree | $O(N\log (N))$ | $O(\log (N))$ | - Fast structure creation |
|  |  |  |  | - Non-constant search time |
|  |  |  |  |  |
| triangles | voxel | $O(N\log (N))$ | $O(\log (\log (N)))$ | - Slow structure creation |
|  |  |  |  | - Requires sampling distance |
|  |  |  |  | - Very fast search |
|  |  |  |  | - Small errors possible |
|  |  |  |  | - Default for precomputation with [`PrepareObjectModel3d`](prepare_object_model_3d.md) |
|  |  |  |  |  |
|  |  |  |  |  |
| primitive | linear | 0 | $O(1)$ |  |

Additionally to the parameters described above, the following parameters can
be set to influence the distance computation.
If desired, these parameters and their
corresponding values can be specified by using *`genParamName`*
and *`genParamValue`*, respectively.
All of the following parameters are optional.

- ***"distance_to"*** —

  This parameter can be used to explicitly set
  the target data to which the distances are computed.

  - ***"auto"*** —

    (Default) Automatically set the target data.
    The following list of attributes is queried, and the first appearing
    attribute from the list is used as target data: Primitive, Triangle,
    Point.
  - ***"primitive"*** —

    Compute the distance to the primitive contained
    in *`objectModel3DTo`*.
  - ***"triangles"*** —

    Compute the distance to the triangles contained
    in *`objectModel3DTo`*.
  - ***"points"*** —

    Compute the distance to the points contained
    in *`objectModel3DTo`*.
- ***"method"*** —

  This parameter can be used to explicitly set
  the method to be used for the distance computation. Note that not all
  methods are available for all target data types. For the list of possible
  pairs of target data type and method, see above.

  - ***"auto"*** —

    (Default) Use the default method for the used
    target data type.
  - ***"linear"*** —

    Use a linear search for computing the distances.
  - ***"kd-tree"*** —

    Use a KD-Tree for computing the distances.
  - ***"voxel"*** —

    Use a voxel structure for computing the distances.
- ***"invert_pose"*** —

  This parameter can be used to invert the pose
  given in *`pose`*.

  - ***"false"*** —

    (Default) The pose is not inverted.
  - ***"true"*** —

    The pose is inverted.
- ***"output_attribute"*** —

  This parameter can be used to set the name
  of the attribute in which the distances are stored.
  By default, the distances are stored in an extended attribute named
  *"&distance"* in *`objectModel3DFrom`*.
  However, if the same 3D object model is used for different calls of this
  operator, the result of the previous call would be overwritten.
  This can be avoided by changing the name of the extended attribute.
  Valid extended attribute names start with a *'&'*.
- ***"sampling_dist_rel"*, *"sampling_dist_abs"*** —

  These parameters are used when computing the distances to triangles
  using the voxel method.
  For this, the triangles need to be sampled.
  The sampling distance can be set either in absolute terms, using
  *"sampling_dist_abs"*, or relative to the diameter of the
  axis aligned bounding box, using *"sampling_dist_rel"*.
  By default, *"sampling_dist_rel"* is set to 0.03.
  Only one of the two parameters can be set.
  The diameter of the axis aligned bounding box can be queried using
  [`GetObjectModel3dParams`](get_object_model_3d_params.md).
  Note that the creation of the voxel data structure is very time
  consuming, and is usually performed offline using
  [`PrepareObjectModel3d`](prepare_object_model_3d.md) (see above).
- ***"store_closest_index"*** —

  This parameter can be used to
  return the index of the closest point or triangle in the extended
  attribute '&closest_index'.

  - ***"false"*** —

    (Default) The index is not returned.
  - ***"true"*** —

    The index is returned.
- ***"signed_distances"*** —

  This parameter can be used to calculate signed distances of the points
  in the 3D object model *`objectModel3DFrom`* to the points, triangles
  or primitive in the 3D object model *`objectModel3DTo`*.

  - ***"false"*** —

    (Default) Unsigned distances are returned.
  - ***"true"*** —

    Signed distances are returned.

  Dependent on the available target data (points, triangles or primitive)
  the following particularities have to be considered:

  - **Distance to points:** —

    The computation of signed distances is only
    supported for the methods *"kd-tree"* and *"linear"*.
    However, signed distances can only be calculated if point normals
    are available for the points in the 3D object model or attached via the
    operator [`SetObjectModel3dAttribMod`](set_object_model_3d_attrib_mod.md).
  - **Distance to triangles:** —

    Signed distances can be calculated for all
    methods listed above. The operator returns a negative distance, if the dot
    product with the normal vector of the triangle is less than zero.
    Otherwise, the distance is positive.
  - **Distance to primitive:** —

    When calculating signed distances to a
    cylindrical, spherical or box-shaped primitive, the points of the 3D
    object model *`objectModel3DFrom`* inside the primitive obtain a
    negative distance, whereas all others have a positive distance.
    When calculating signed distances to planes, all points beneath the
    plane obtain a negative distance, whereas all others have a positive one.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`objectModel3DFrom`** (input_control)  object_model_3d `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the source 3D object model.

**`objectModel3DTo`** (input_control)  object_model_3d `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the target 3D object model.

**`pose`** (input_control)  pose `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

Pose of the source 3D object model in the target
3D object model.

Default:
[]

**`maxDistance`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Maximum distance of interest.

Default:
0

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Names of the generic input parameters.

Default:
[]

List of values:
"distance_to", "invert_pose", "method", "output_attribute", "sampling_dist_abs", "sampling_dist_rel", "signed_distances", "store_closest_index"

**`genParamValue`** (input_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Values of the generic input parameters.

Default:
[]

List of values:
"auto", "false", "kd-tree", "linear", "points", "polygons", "primitive", "triangles", "true", "voxel"

## Result

`DistanceObjectModel3d` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

## Possible Predecessors

`PrepareObjectModel3d`,
`ReadObjectModel3d`,
`FindSurfaceModel`,
`XyzToObjectModel3d`

## Possible Successors

`GetObjectModel3dParams`,
`RenderObjectModel3d`,
`DispObjectModel3d`,
`ClearObjectModel3d`

## See also

`PrepareObjectModel3d`

## Module

3D Metrology
