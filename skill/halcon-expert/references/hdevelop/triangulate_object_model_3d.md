# triangulate_object_model_3d (Operator)

## Name

`triangulate_object_model_3d` — Create a surface triangulation for a 3D object model.

## Signature

`triangulate_object_model_3d( : : ObjectModel3D, Method, GenParamName, GenParamValue : TriangulatedObjectModel3D, Information)`

## Description

The operator `triangulate_object_model_3d` generates a surface of
triangular faces for the 3D object model *`ObjectModel3D`* and
returns the resulting surface in *`TriangulatedObjectModel3D`*.
Currently, the operator offers four methods for the triangulation that
can be selected in *`Method`*: *'polygon_triangulation'*,
*'xyz_mapping'*, *'greedy'* and *'implicit'*.
*'polygon_triangulation'*
is a simple method for the conversion of a polygonal to a triangular face
representation in a 3D object model.
*'xyz_mapping'* triangulates the points in 2D according to a 2D
mapping. The other two methods are rather
complex algorithms that are used to calculate triangular faces from pure
3D point data with unknown surface topology. A detailed comparison of
the *'greedy'* and *'implicit'* algorithm is provided in the
paragraph *"Comparison of the triangulation methods"* below.

### Polygon triangulation

By selecting *`Method`*=*'polygon_triangulation'*,
all polygons in *`ObjectModel3D`* are triangulated.
No generic parameters are supported for this method. If no polygons are
available, an exception is raised. A triangular mesh representing the
same surface as *`ObjectModel3D`* is returned in
*`TriangulatedObjectModel3D`*.

### 2D mapping triangulation

By selecting *`Method`*=*'xyz_mapping'*, the points are
triangulated in 2D according to a 2D mapping contained in
*`ObjectModel3D`*. The used method is the same as in
[`prepare_object_model_3d`](prepare_object_model_3d.md) for Purpose='segmentation'.
If no 2D mapping is available, an exception is raised.

As a post-processing step, triangles whose normal differs
strongly from a specified direction can be removed,
refer to the description of *`GenParamName`* below.
This is helpful in cases where the 2D neighborhood used for
the triangulation does not reflect the 3D neighborhood well,
e.g., when parts of the surface are hidden along the viewing direction
of the sensor, or to remove typical noise along the viewing direction
of the sensor.

By setting *`GenParamName`* to the following value, the additional
parameter specific for the *2D mapping triangulation* can be set with
*`GenParamValue`*:

- ***'xyz_mapping_max_area_holes'*** —

  specifies which area holes of the point coordinates are closed during
  a simple Delaunay triangulation. Only holes which are completely
  surrounded by the image region are closed. If
  *'xyz_mapping_max_area_holes'* is set to 0, no holes are triangulated.
  The parameter corresponds to the `GenParamName`
  *'max_area_holes'* of [`prepare_object_model_3d`](prepare_object_model_3d.md).

  Suggested values:
   *1*, *10*, *100*.

  Default:
   *10*.
- ***'xyz_mapping_max_view_angle'*** —

  specifies the maximum allowed angle difference between the triangle
  normal and the viewing direction of the sensor. The smaller this value
  is set, the fewer triangles are returned. The viewing direction of the
  sensor is assumed to be the z-axis in the coordinate system of
  *`ObjectModel3D`* if not specified differently using
  *`GenParamName`* set to *'xyz_mapping_max_view_dir_x'*,
  *'xyz_mapping_max_view_dir_y'*, and
  *'xyz_mapping_max_view_dir_z'*.
  The angle has to be specified between 0 and 90 degrees.

  Suggested values:
   *'rad(60)'*, *'rad(85)'*,
  *'rad(90)'*.

  Default:
   *'rad(90)'*.
- ***'xyz_mapping_max_view_dir_x'*,
  *'xyz_mapping_max_view_dir_y'*,
  *'xyz_mapping_max_view_dir_z'*** —

  specify the viewing direction of the sensor for use with the
  *`GenParamName`* *'xyz_mapping_max_view_angle'*, in the
  coordinate system of *`ObjectModel3D`*.
  If not all three coordinate directions are set simultaneously or
  the direction equals the zero vector, an exception is raised.

  Suggested values:
   *[1, 0, 0]*, *[0, 0, 1]*.

  Default:
   *[0, 0, 1]*.
- ***'xyz_mapping_output_all_points'*** —

  controls, if all input points are returned, regardless whether they
  were used in the output triangulation or not. Mainly provided for
  reasons of backward compatibility. When
  *'xyz_mapping_output_all_points'* is set to
  *'false'*, the old point indices are stored as an extended
  attribute named *'original_point_indices'* in the 3D object model
  *`TriangulatedObjectModel3D`*. This attribute can subsequently be
  queried with [`get_object_model_3d_params`](get_object_model_3d_params.md) or be processed with
  other operators that use extended attributes.

  List of values:
   *'false'*, *'true'*.

  Default:
   *'false'*.

  |  |
  | --- |
  | ![figure](../assets/f3aa5c6b410de9b4.svg) |
  | ( 1) |
  | ![figure](../assets/8564fd18381fc9ea.svg) |
  | ( 2) |

  (1) In order to triangulate the 3D object model, a 2D mapping of the
  model is used.
  The triangulation is based on the respective 2D neighborhood.
  Thereby it is possible, that unwanted triangles are created
  along the sensor's direction of view, e.g., because of hidden
  object parts or clutter data.
  (2) Whether or not a triangle is returned, is decided by computing
  the difference between the normal direction of each triangle
  and the viewing direction. The maximum deviation is specified
  in *'xyz_mapping_max_view_angle'*.

### Greedy triangulation

By selecting *`Method`*=*'greedy'*, a so called greedy
triangulation algorithm is invoked. It requires 3D point data containing
normals. If *`ObjectModel3D`* does not contain the normals, they are
calculated internally, in an identical manner to calling
[`surface_normals_object_model_3d`](surface_normals_object_model_3d.md) with its default parameters before
triangulation. The algorithm constructs a surface, which passes through the
points and whose surface normals must be conform to the corresponding point
normals up to a given tolerance. The surface is represented by triangular
faces, which are constructed from triplets of *neighboring* points.
In order to determine which triplets qualify for a surface triangle, the
algorithm applies for each point pair the following local neighborhood test,
denoted as **surface neighborhood criteria (SNC)**:

If a point P is lying on a surface, with N being the
orientation (normal) of the surface, then a point P' with normal
N' is considered to lay on this surface if:

1. the distance between both points is smaller or equal to
   `r`, i.e.,
   $\Delta(P,P^{\prime})\le r$
2. both normals have similar orientation, i.e., the angle
   $\mathcal{L}\bigl(N, N^{\prime}\bigr) \leq \alpha$ ![figure](../assets/c2249f77dc35ca20.svg)
   or - if no strict consistency of the normals is enforced -
   $\angle (N,-N') \leq \alpha$ ![figure](../assets/dc0f0886ede03ec3.svg)
3. the vector $\delta P=P^{\prime}-P$ is close to orthogonal
   with respect to N, i.e., the angle
   $\left|90^{\circ}-\angle(N,\delta P)\right|\leq \beta$ ![figure](../assets/003695d145917d19.svg)
4. if P' does not meet 3. but it is not further away from
   the plane defined by [P,N] than `d`,
   then it is accepted as well.

The four parameters `r` (see *'greedy_radius_type'*
and *'greedy_radius_value'*), $\alpha$
(see *'greedy_neigh_orient_tol'*), $\beta$
(see *'greedy_neigh_latitude_tol'*), and `d`
(see *'greedy_neigh_vertical_tol'*) control the criteria and have
the following meaning:

The parameter $\alpha$ essentially controls the
curvature of the generated surface: for small values of
$\alpha$ the generated surface will be locally
flatter; larger values of $\alpha$ permit the
generation of more curved surface fragments.

The other three parameters define a portion of a sphere that defines
the valid SNC neighborhood. The sphere has a radius `r`,
it is centered in P, and its equatorial plane is incident with
the plane [P,N]. Only points that are within the sphere
(first SNC criteria) are considered. Furthermore, they need to have a
latitude within [-$\beta$; $\beta$]
(third SNC criteria) with respect to the equator unless they are lying
within the thin layer defined on the both sides of the equatorial plane
by the distance parameter `d` (fourth SNC criteria).
In contrast, points lying in any of both pole segments of the
sphere (i.e., with higher latitude than $\beta$ and
a distance from the equatorial plane beyond `d`)
are not considered as neighbors.

The parameter `r` prevents the algorithm from constructing
too big triangles. This is particularly important for point sets that
represent several disconnected surface pieces or a surface with holes
that must not be closed. The latitude window defined by
$\beta$ enables neighbors which deviate from
[P,N] due to noise or curvature to be considered as well.
Similarly, the parameter `d` enables neighbors
right "above" or "below" the equatorial plane to be accepted, which
essentially accounts for data noise.

Here is some advice for selecting the appropriate values for these
parameters:

- If the resulting surface triangulation looks very disconnected or
  exhibits many holes, this might be a hint that `r`
  is too small and thus restricts the generation of triangles that
  are large enough to close the holes. Try to increase
  `r`.
- If the normals data is noisy (i.e., neighboring normals are
  deviating to a large extend from each other), then
  increase $\alpha$. The source of noisy normals
  is typically caused either by the sensor, which delivers both the
  point and the normals data, or an imprecise normals estimation
  routine, which computes the normals from the point data.
- If the point data represents a very curved surface, i.e., it
  exhibits a very fine structure like, e.g., little buckles, fine
  waves or folds, or sharp turns, then make sure the generation of
  curved data is facilitated by an increasing
  $\alpha$ and/or $\beta$.
- In contrast, if the data is rather planar but has lots of outliers
  (i.e., points laying next to the surface, which have completely
  different orientations and thus most probably do not belong to it),
  then decrease $\alpha$ to exclude them from
  the surface generation.
- If the point data is very noisy and resembles more a crust than a
  single-layer surface, then increase $\beta$
  and/or `d` to make sure that neighbors for
  P can still be found even if they are further away from
  the optimal plane [P,N].
- In contrast, if the data is rather noise-free, but two surfaces are
  running close to each other and are nearly parallel, e.g., surfaces
  representing the front and the back side of a thin, plate-like
  object, then decrease $\beta$ and
  `d` to avoid interference between the surfaces.

The **greedy triangulation** algorithm starts by initializing a
surface with one triangle constructed from three SNC-eligible, neighboring
points. If all valid neighborhoods show local inconsistencies like collinear
or 'double' points, an error will be raised. A prior call of
[`sample_object_model_3d`](sample_object_model_3d.md) with Method set to 'fast' and a small
SamplingParam will remove most local inconsistencies from
*`ObjectModel3D`*. Having found one triangle, the algorithm
then greedily constructs new triangles as long as further
points can be reached by the SNC rules from any point on the surface
boundaries. If no points can be reached from the current surface, but
there are unprocessed points in the 3D object model, a new surface is
initialized. Because the SNC rules are essentially defined only in the
small local neighborhoods of the points, the resulting surface can have
global topological artifacts like holes and flips. The latter occur,
when - while it is growing - a surface meets itself but with inverted
face orientations (i.e., the surface was *flipped* somewhere while
it was growing). These artifacts are handled in special post-processing
steps: *hole filling* and *flip resolving*, respectively.

Finally, a *mesh morphology* can be performed to additionally remove
artifacts that occurred on the final surface boundaries. The mesh morphology
consists of several mesh erosion cycles and several subsequent mesh
dilation cycles. With each erosion cycle, all triangles reachable from the
surface boundaries are removed and the surface boundaries shrink. Then, with
each dilation cycle all triangles reachable from the surface boundaries are
appended again to the surface and the boundaries expand. Note that this is
only possible for triangles, which were removed by an erosion cycle before
that. Therefore, once the original boundaries of the surface (i.e., those
which existed before the mesh erosion cycles) are reached, the dilation
cannot advance any further and hence the dilation cycles cannot be more
than the erosion cycles. Applying mesh erosion and dilation subsequently is
analogous to performing opening to standard HALCON regions. At last, the
mesh morphology can delete surface pieces which have too few triangles.

The individual algorithm steps are summarized here:

1. Triangulation of all points reachable by SNC
2. Hole filling (see *'greedy_hole_filling'*)
3. Flip resolving (see *'greedy_fix_flips'*)
4. Mesh morphology (see *'greedy_mesh_erosion'*,
   *'greedy_mesh_dilation'*, and
   *'greedy_remove_small_surfaces'*)

By setting *`GenParamName`* to one of the following values, additional
parameters specific for the *greedy triangulation* can be set with
*`GenParamValue`*:

- ***'greedy_kNN'*** —

  specifies the size `k` of the neighborhood. While
  looking for reachable SNC neighbors for a surface boundary point, the
  algorithm considers only its closest `k` neighbors.

  Suggested values:
   *20*, *30*, *40*,
  *50*, *60*.

  Default:
   *40*.
- ***'greedy_radius_type'*:** —

  if set to *'fixed'*,*'greedy_radius_value'* specifies the
  SNC radius `r` in meter units.

  If set to *'z_factor'*, `r` is calculated for
  each point P by multiplying its z-coordinate by the value
  specified by *'greedy_radius_value'*. This representation of
  `r` is appropriate for data where the density of the
  points correlates with their distance from the sensor they were
  recorded with. This is typically the case with depth sensors or TOF
  cameras.

  If set to *'auto'*, the algorithm determines internally whether
  to use a *'fixed'* or a *'z_factor'* radius and estimates
  its value. The estimated value is then multiplied by the value specified
  in *'greedy_radius_value'*. This way, the user specifies a scale
  factor for the estimated radius.

  List of values:
   *'auto'*,
  *'fixed'*, *'z_factor'*.

  Default:
   *'auto'*.
- ***'greedy_radius_value'*:** —

  see *'greedy_radius_type'*.

  Suggested values:
   *0.01*, *0.05*, *0.5*,
  *0.66*, *1.0*, *1.5*,
  *2.0*, *3.0*, *4.0*
- ***'greedy_neigh_orient_tol'*:** —

  sets the SNC parameter $\alpha$ in degree units.
  $\alpha$ controls the surface curvature as described
  with the SNC rules above.

  Suggested values:
   *10*, *20*, *30*,
  *40*.

  Default:
   *30*.
- ***'greedy_neigh_orient_consistent'*:** —

  enforces that the normals of two neighboring points have the same
  orientation (i.e., they do not show in opposite directions). If
  enabled, this parameter disables the second part of the SNC criteria
  for $\alpha$, i.e., if
  $\langle (N, N^{\prime})\rangle > \alpha$ ![figure](../assets/a5d5be35e45cd032.svg),
  the criteria fails even if
  $\angle (N,-N') \leq \alpha$ ![figure](../assets/dc0f0886ede03ec3.svg).

  List of values:
   *'true'*, *'false'*.

  Default:
   *'false'*.
- ***'greedy_neigh_latitude_tol'*:** —

  sets the SNC parameter $\beta$ in degree units.
  $\beta$ controls the surface neighborhood latitude
  window as described with the SNC rules above.

  Suggested values:
   *10*, *20*, *30*
  *40*.

  Default:
   *30*.
- ***'greedy_neigh_vertical_tol'*:** —

  sets the SNC parameter `d` as a factor of the radius
  `r`.

  Suggested values:
   *0.01*, *0.1*,
  *0.2*, *0.3*.

  Default:
   *0.1*.
- ***'greedy_hole_filling'*:** —

  sets the length of surface boundaries (in number of point vertices)
  that should be considered for the hole filling. If *'false'* is
  specified, then the hole filling step is disabled.

  Suggested values:
   *'false'*,
  *20*, *40*, *60*.

  Default:
   *40*.
- ***'greedy_fix_flips'*:** —

  enables/disables the flip resolving step of the algorithm.

  List of values:
   *'true'*, *'false'*.

  Default:
   *'true'*.
- ***'greedy_prefetch_neighbors'*:** —

  enables/disables prefetching of lists of the k nearest neighbors for all
  points. This prefetching improves the algorithm speed, but has high
  memory requirements (O(k*n), where `k`
  is the number specified by *'greedy_kNN'*, and
  `n` is the number of points in *`ObjectModel3D`*).
  For very large data, it might be impossible to preallocate such a big
  amount of memory, results in a memory error message. In such a case the
  prefetching must be disabled.

  List of values:
   *'true'*, *'false'*
  Default:
   *'true'*.
- ***'greedy_mesh_erosion'*:** —

  specifies the number of erosion cycles applied to the final mesh.

  Suggested values:
   *0*, *1*, *2*,
  *3*.

  Default:
   *0*.
- ***'greedy_mesh_dilation'*:** —

  specifies the number of dilation cycles. The mesh dilation is applied
  after the mesh erosion. If *'greedy_mesh_dilation'* is set to a
  greater value than *'greedy_mesh_erosion'*, it will be reduced
  internally to the value of *'greedy_mesh_erosion'*.

  Suggested values:
   *0*, *1*, *2*,
  *3*
  Default:
   *0*.
- ***'greedy_remove_small_surfaces'*:** —

  controls the criteria for removing small surface pieces.
  If set to *'false'*, the small surface removal is disabled. If
  set to a value between *0.0* and *1.0*, all surfaces
  having less triangles than
  *'greedy_remove_small_surfaces'*x`num_triangles`
  will be removed, where `num_triangles` is the total number
  of triangles generated by the algorithm.
  If set to a value greater than *1*, all surfaces having less
  triangles than *'greedy_remove_small_surfaces'* will be removed.

  Suggested values:
   *'false'*,
  *0.01*, *0.05*, *0.1*,
  *10*, *100*, *1000*, *10000*.

  Default:
   *'false'*.
- ***'greedy_timeout'*:** —

  using a timeout, it is possible to interrupt the operator after a
  defined period of time in seconds. This is especially useful in cases,
  where a maximum cycle time has to be ensured. The temporal accuracy of
  this interrupt is about 10 ms. Passing values less then zero is not
  valid. Setting *'greedy_timeout'* to *'false'* deactivates
  the timeout, which corresponds to the default. The temporal accuracy
  depends on several factors including
  the size of the model, the speed of your computer, and the
  *'timer_mode'* set via [`set_system`](set_system.md).

  Suggested values:
   *'false'*,
  *0.1*, *0.5*, *1*, *10*, *100*.

  Default:
   *'false'*.
- ***'greedy_suppress_timeout_error'*:** —

  by default, if a timeout occurs the operator returns a timeout error
  code. By setting *'greedy_suppress_timeout_error'* to
  *'true'* instead, the operator returns no error and the
  intermediate results of the triangulation are returned in
  *`TriangulatedObjectModel3D`*. With the error suppressed, the
  occurrence of a timeout can be checked by querying the list of values
  returned in *`Information`* (in *'verbose'* mode) by
  looking for the value corresponding to *'timeout_occured'*.

  List of values:
   *'false'*, *'true'*.

  Default:
   *'false'*.
- ***'greedy_output_all_points'*:** —

  controls, if all input points are returned, regardless whether they
  were used in the output triangulation or not. Mainly provided for
  reasons of backward compatibility. When
  *'greedy_output_all_points'* is set to
  *'false'*, the old point indices are stored as an extended
  attribute named *'original_point_indices'* in the 3D object model
  *`TriangulatedObjectModel3D`*. This attribute can subsequently be
  queried with [`get_object_model_3d_params`](get_object_model_3d_params.md) or be processed with
  other operators that use extended attributes.

  List of values:
   *'false'*, *'true'*.

  Default:
   *'false'*.
- ***'information'*:** —

  specifies, which intermediate results shall be reported in
  *`Information`*. By default
  (*'information'*=*'num_triangles'*), the number of
  generated triangles is reported. For
  *'information'*=*'verbose'*, a list of name-value
  information pairs is returned. Currently, the following information
  is reported:

  | Name | Value | Description |
  | --- | --- | --- |
  | *'num_triangles'* | <number of triangles> | returns the number of generated triangular faces. |
  | *'specified_radius_type'* | *'auto'* | *'fixed'* | *'z_factor'* | *'none'* | returns the radius type as specified by the user. |
  | *'specified_radius_value'* | <specified radius value> | returns the radius value specified by the user. |
  | *'used_radius_type'* | *'fixed'* | *'z_factor'* | *'sampling'* | returns the radius type used internally; |
  |  |  | if the user specified *'auto'* for *'specified_radius_type'*, this field returns the radius type that was selected internally;   if *`ObjectModel3D`* is a 3D primitive, the user specified radius value is internally used as a sampling step and *'used_radius_type'* returns *'sampling'*. |
  | *'used_radius_value'* | <used radius value> | returns the radius value used internally; |
  |  |  | if *'used_radius_type'*=*'fixed'*, the absolute neighborhood radius in meters is reported;   if *'used_radius_type'*=*'z_factor'*, the multiplication factor is reported, which is used to compute the neighborhood radius from the z-coordinate of the neighborhood center point;   if *'used_radius_type'*=*'sampling'*, then the sub-sampling factor is reported, which is used to generate the triangulation of 3D primitives, in particular: cylinder and sphere. |
  | *'neigh_orient_tol'* | <$\alpha$> | returns the surface curvature parameter $\alpha$ in degrees that was used for the triangulation. |
  | *'neigh_latitude_tol'* | <$\beta$> | returns the angular tolerance window in degrees that was used to select surface neighbors. |
  | *'neigh_vertical_tol'* | <$d$> | returns the neighborhood parameter $d$ as a factor of the used radius. |
  | *'fix_flips'* | *'true'* | *'false'* | returns whether the flip fixing was enabled. |
  | *'hole_filling'* | *'false'* | <max hole boundary length> | returns *'false'* when the hole filling was disabled, or the specified maximal hole boundary length in number of points. |
  | *'timeout'* | *'false'* | <timeout> | *'false'* when the timeout was disabled, or the specified timeout in seconds. |
  | *'timeout_occured'* | *'yes'* | *'no'* | returns whether a timeout occurred. |
  |  |

  List of values:
   *'num_triangles'*,
  *'verbose'*.

  Default:
   *'num_triangles'*.

### Implicit triangulation

By selecting *`Method`*=*'implicit'* an implicit triangulation
algorithm based on a Poisson solver (see the paper in References) is
invoked. It constructs a water-tight surface, i.e., it is completely closed.
The implicit triangulation requires 3D point data containing normals.
Additionally, it is required that the 3D normals are pointing strictly
inwards or strictly outwards regarding the volume enclosed by the surface
to be reconstructed. Unlike the *'greedy'* algorithm, the
*'implicit'* algorithm does not construct the surface through the
input 3D points. Instead, it constructs a surface that approximates the
original 3D data and creates a new set of 3D points lying on this surface.

First, the algorithm organizes the point data in an adaptive octree
structure: the volume of the bounding box containing the point data is split
in the middle in each dimension resulting in eight sub-volumes, or
*octree voxels*. Voxels still containing enough point data can
be split in further eight sub-voxels. Voxels that contain no or just
few points must not be split further. This splitting is repeated
recursively in regions of dense 3D point data until the resulting
voxels contain no or just few points. The recursion level of the voxel
splits, reached with the smallest voxels, is denoted as *depth*
of the octree.

In the next step, the algorithm estimates the values of the so-called
*implicit indicator function* of the surface, based on the assumption
that the points from *`ObjectModel3D`* are lying on the surface of an
object and the normals of the points in *`ObjectModel3D`* are pointing
inwards that object (see the paper in References). This assumption explains
the requirement of mutually consistent normal orientations. The implicit
function has a value of 1 in voxel corners that are strictly inside the
body and 0 for voxel corners strictly outside of it. Due to noisy data,
voxel corners that are close to the boundary of the object cannot be
'labeled' unambiguously. Therefore, they receive a value between 0 and 1.

The *implicit surface* defined by the indicator function is a
surface, such that each point lying on it has an indicator value of
0.5. The implicit algorithm uses a standard *marching cubes
algorithm* to compute the intersection points of the implicit surface with
the sides of the octree voxels. The intersection points result in the
new set of 3D points spanning the surface returned in
*`TriangulatedObjectModel3D`*. As a consequence, the resolution of
the surface details reconstructed in *`TriangulatedObjectModel3D`*
depends directly on the resolution of the octree (i.e., on its
*depth*).

By setting *`GenParamName`* to one of the following values, additional
parameters specific for the *implicit triangulation* can be set with
*`GenParamValue`*:

- ***'implicit_octree_depth'*:** —

  sets the depth of the octree. The octree depth controls the resolution
  of the surface generation - a higher depth leads to a higher surface
  resolution. The octree depth has an exponential effect on the
  runtime and an exponential effect on the memory requirements
  of the octree. Therefore, the depth is limited to *12*.

  Restriction:
   *5* $\le$
  *'implicit_octree_depth'*
  $\le$ *12*.

  Suggested values:
   *5*, *6*, *8*,
  *10*, *11*, *12*.

  Default:
   *6*.
- ***'implicit_solver_depth'*:** —

  enables an alternative algorithm, which can prepare the implicit
  function up to a user specified octree depth, before the original
  algorithm takes over the rest of the computations. This algorithm
  requires less memory than the original one, but is a bit slower.

  Restriction:
   *'implicit_solver_depth'*
  $\le$ *'implicit_octree_depth'*.

  Suggested values:
   *2*, *4*, *6*, *8*,
  *10*, *11*, *12*.

  Default:
   *6*.
- ***'implicit_min_num_samples'*:** —

  sets the minimal number of point samples required per octree voxel
  node. If the number of points in a voxel is less than this value, the
  voxel is not split any further. For noise free data, this value can be
  set low (e.g., between 1-5). For noisy data, this value should be
  set higher (e.g., 10-20), such that the noisy data is accumulated
  in single voxel nodes to smooth the noise.

  Suggested values:
   *1* *5*, *10*, *15*,
  *20*, *30*.

  Default:
   *1*.
- ***'information'*:** —
  specifies, which intermediate results shall be reported in
  *`Information`*. By default
  (*'information'*=*'num_triangles'*), the number of
  generated triangles is reported. For
  *'information'*=*'verbose'*, a list of name-value
  information pairs is returned. Currently, the following information
  is reported:

  | Name | Value | Description |
  | --- | --- | --- |
  | *'num_triangles'* | <number of triangles> | returns the number of generated triangular faces. |
  | *'num_points'* | <number of points> | returns the number of generated points. |

  List of values:
   *'num_triangles'*,
  *'verbose'*.

  Default:
   *'num_triangles'*.

### Comparison of the triangulation methods

In this paragraph, a simple comparison of both supported triangulation
methods is provided:

| Property | Greedy triangulation | Implicit triangulation |
| --- | --- | --- |
| required data: | 3D points with 3D normals | 3D points with 3D normals, the normals must point consistently inwards |
| resulting surface: | open, triangulation of the input points | closed (water-tight), approximation of the input points |
| resulting point data: | the input point data is preserved | new point data is generated |
| noise handling: | moderate point and normal noise handled properly | point and normal noise handled implicitly; moderate and high noise levels are accepted |
| triangulation resolution: | explicit, controlled by surface neighborhood parameters | implicit, controlled by octree depth and minimal number of point samples per node |
| time complexity: | $O(Nk\log N)$ | $O(ND^{3})$ |
| memory complexity: | $O(Nk)$, with neighborhood prefetching | $O(D^{3})$ |
|  | $O(N)$, without neighborhood prefetching |  |
|  |  |  |
|  |  | *where:* |
|  |  | $N$: *number of points* |
|  |  | $k$: *size of the neighborhood* |
|  |  | $D$: *depth of the octree* |

Depending on the number of points in *`ObjectModel3D`*, noise, and
specific structure of the data, both algorithms deliver different results
and perform with different time and memory complexity. The greedy algorithm
works fast, requires less memory, and returns a high level of details in
the reconstructed surface for rather small data sets (up to, e.g., 500.000
points). Since the algorithm must basically process every single point
in the data, its time performance cannot be decoupled from the point number
and it can be rather time consuming for more than 500.000 points.
If large point sets need to be triangulated with this method anyway, it
is recommended to first sub-sample them via [`sample_object_model_3d`](sample_object_model_3d.md).

In contrast, as described above, the implicit algorithm organizes
all points in an underlying octree. Therefore, the details returned by it,
its speed, and its memory consumption are dominated by the depth of the
octree. While higher levels of surface details can only be achieved
at disproportionately higher time and memory costs, the octree offers the
advantage that it handles large point sets more efficiently. With the
octree, the performance of the implicit algorithm depends mostly on
the depth of the octree and to a lesser degree on the number of points
to be processed. One further disadvantage of the implicit algorithm is its
requirement that the adjacent point normals are strictly consistent. This
requirement can seldom be fulfilled by usual normal estimation routines.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`ObjectModel3D`** (input_control)  object_model_3d(-array) `→`  (handle)

Handle of the 3D object model containing 3D
point data.

**`Method`** (input_control)  string `→`  (string)

Triangulation method.

Default:
'greedy'

List of values:
'greedy', 'implicit', 'polygon_triangulation', 'xyz_mapping'

**`GenParamName`** (input_control)  attribute.name-array `→`  (string)

Names of the generic triangulation parameters.

Default:
[]

List of values:
'greedy_fix_flips', 'greedy_hole_filling', 'greedy_kNN', 'greedy_mesh_dilation', 'greedy_mesh_erosion', 'greedy_neigh_latitude_tol', 'greedy_neigh_orient_consistent', 'greedy_neigh_orient_tol', 'greedy_neigh_vertical_tol', 'greedy_output_all_points', 'greedy_prefetch_neighbors', 'greedy_radius_type', 'greedy_radius_value', 'greedy_remove_small_surfaces', 'greedy_suppress_timeout_error', 'greedy_timeout', 'implicit_min_num_samples', 'implicit_octree_depth', 'implicit_solver_depth', 'information', 'xyz_mapping_max_area_holes', 'xyz_mapping_max_view_angle', 'xyz_mapping_max_view_dir_x', 'xyz_mapping_max_view_dir_y', 'xyz_mapping_max_view_dir_z', 'xyz_mapping_output_all_points'

**`GenParamValue`** (input_control)  attribute.value-array `→`  (real / integer / string)

Values of the generic triangulation parameters.

Default:
[]

Suggested values:
6, 8, 12, 'true', 'false', 'auto', 'fixed', 'z_factor', 'verbose', 'num_triangles'

**`TriangulatedObjectModel3D`** (output_control)  object_model_3d(-array) `→`  (handle)

Handle of the 3D object model with the
triangulated surface.

**`Information`** (output_control)  number(-array) `→`  (integer / string)

Additional information about the triangulation
process.

## Possible Predecessors

`read_object_model_3d`,
`gen_plane_object_model_3d`,
`gen_sphere_object_model_3d`,
`gen_cylinder_object_model_3d`,
`gen_box_object_model_3d`,
`gen_sphere_object_model_3d_center`,
`sample_object_model_3d`

## Possible Successors

`write_object_model_3d`,
`render_object_model_3d`,
`project_object_model_3d`,
`simplify_object_model_3d`

## References

M. Kazhdan, M. Bolitho, and H. Hoppe: “Poisson Surface Reconstruction.”
Symposium on Geometry Processing (June 2006).

## Module

3D Metrology
