# FuseObjectModel3d (Operator)

## Name

`FuseObjectModel3d` — Fuse 3D object models into a surface.

## Signature

`static void HOperatorSet.FuseObjectModel3d(HTuple objectModel3D, HTuple boundingBox, HTuple resolution, HTuple surfaceTolerance, HTuple minThickness, HTuple smoothing, HTuple normalDirection, HTuple genParamName, HTuple genParamValue, out HTuple objectModel3DFusion)`

`static HObjectModel3D HObjectModel3D.FuseObjectModel3d(HObjectModel3D[] objectModel3D, HTuple boundingBox, HTuple resolution, HTuple surfaceTolerance, HTuple minThickness, HTuple smoothing, HTuple normalDirection, HTuple genParamName, HTuple genParamValue)`

`HObjectModel3D HObjectModel3D.FuseObjectModel3d(HTuple boundingBox, double resolution, double surfaceTolerance, double minThickness, double smoothing, string normalDirection, HTuple genParamName, HTuple genParamValue)`

## Description

`FuseObjectModel3d` fuses multiple point clouds representing an
object surface into a watertight surface *`objectModel3DFusion`*.
The operator can be used to simplify the postprocessing step of point clouds
that are already registered in the same coordinate system.
In particular, unification, suppression of outliers, trade-off between
smoothing and preservation of edges, equidistant
sub-sampling, hole filling, and meshing of the output surface can often
be handled nicely and in high quality.
On the other hand, these advantages come at the price of a high runtime.

If you want to fuse 3D point clouds acquired by stereo reconstruction,
you should use [`ReconstructSurfaceStereo`](reconstruct_surface_stereo.md) instead of
`FuseObjectModel3d`.

### Workflow

1. Acquire point clouds and transform them into a common coordinate
   system, for example using [`RegisterObjectModel3dPair`](register_object_model_3d_pair.md)
   and [`RegisterObjectModel3dGlobal`](register_object_model_3d_global.md).
2. If not already available, compute triangles or point normals for
   the point clouds using [`TriangulateObjectModel3d`](triangulate_object_model_3d.md) or
   [`SurfaceNormalsObjectModel3d`](surface_normals_object_model_3d.md). A triangulation is more
   suitable if you have surfaces with many outliers or holes that should
   be closed. Otherwise, for clean surfaces, you can work with normals.
3. Inspect the normals of the input models using
   `visualize_object_model_3d` with *`genParamName`*
   *"disp_normals"* or `dev_inspect_ctrl`.
   The point or triangle normals have to be oriented consistently towards
   the inside or outside of the object. Set *`normalDirection`*
   accordingly to *"inwards"* or *"outwards"*.
4. Specify the volume of interest in *`boundingBox`*. To obtain
   a first guess for *`boundingBox`*, use
   [`GetObjectModel3dParams`](get_object_model_3d_params.md) with *`genParamName`* set to
   *"bounding_box1"*.
5. Specify an initial set of parameters: a rough *`resolution`*
   (e.g., 1/100 of the diameter of the *`boundingBox`*),
   *`surfaceTolerance`* at least a bit larger
   (e.g., 5**`resolution`*),
   *`minThickness`* as the minimum thickness of the object
   (if the input point clouds represent the object only from one side,
   set it very high, so that the object is cut off at the
   *`boundingBox`*), *`smoothing`* set to *1.0*.
6. Apply `FuseObjectModel3d` and readjust the parameters to
   improve the results with respect to quality and runtime, see below.
   Use a *`resolution`* just fine enough to make out the details of
   your object while tuning the other parameters, in order to avoid long
   runtimes. Also consider using the additional parameters in
   *`genParamName`*.

### Parameter Description

See the HDevelop example `fuse_object_model_3d_workflow` for an
explanation how to fine-tune the parameters for your application.

The input point clouds *`objectModel3D`* have to lie in a common
coordinate system and add up to the initial surface.
Furthermore, they must contain triangles or point normals.
If both attributes are present, normals are used
as a default due to speed advantages.
If triangles should be used, use [`CopyObjectModel3d`](copy_object_model_3d.md) to obtain only
point and triangle information.
Surfaces with many outliers or holes to be closed should be used with a
triangulation, clean surfaces with normals.
The point or triangle normals have to be oriented consistently towards the
inside or outside of the object.

*`normalDirection`* is used to specify whether the point or triangle
normals point *"inwards"* or *"outwards"*. If only one value
is specified, it is applied to all input models. Otherwise, the number of
values has to equal the number of input models.

*`boundingBox`* specifies the volume of interest to be taken into
account for input and output.
Note that points outside the bounding box are discarded. Triangles of the
input point cloud with a point outside the *`boundingBox`* are
discarded, not clipped. The *`boundingBox`* is specified as
a tuple `[x1,y1,z1,x2,y2,z2]` assigning two opposite corner points
`P1=[x1,y1,z1]` and `P2=[x2,y2,z2]` of the rectangular cuboid
(with edges parallel to the coordinate axes).
For a valid bounding box, `P1` must be the point on the front
lower left corner and `P2` on the back upper right corner of the
bounding box, i.e., `x1<x2`, `y1<y2` and `z1<z2`.
Note that the operator will try to produce a closed surface.
If the input point clouds represent the object from only one point of view,
one wants the bounding box usually to cut off the unknown part,
wherefore *`minThickness`* should be set
e.g., to a value larger than or equal to the length of the diagonal of the
bounding box (which can be obtained by using
[`GetObjectModel3dParams`](get_object_model_3d_params.md) with the parameter
*"diameter_axis_aligned_bounding_box"*). An object cut off
by a surface of the bounding box has no points at this specific surface,
thus has a hole. Note also that you may have to rotate the input point
clouds in order make the bounding box cut off the unknown part in the right
place, since the edges of the bounding box are always parallel to the
coordinate axes. This can be achieved e.g., using
[`AffineTransObjectModel3d`](affine_trans_object_model_3d.md) or [`RigidTransObjectModel3d`](rigid_trans_object_model_3d.md).

*`resolution`* specifies the
distance of neighboring grid points in each coordinate direction in
the discretization of the *`boundingBox`*. *`resolution`* is set
in the same unit as used in *`objectModel3D`*. Too small values will
unnecessarily increase the runtime, so it is recommended to begin with a
coarse resolution.
Too large values will lead to a reconstruction with high loss of details.
*`smoothing`* may need to be adapted when *`resolution`*
is changed.
*`resolution`* should always be a bit smaller than
*`surfaceTolerance`* in order to avoid discretization artifacts.

*`surfaceTolerance`*
specifies how much noise in the input point cloud should be combined
to the surface from its inside and outside.
Sole exemption when *`surfaceTolerance`* is larger than
*"distance_in_front"*, in that case *"distance_in_front"*
determines the surface thickness to the front of the object.
*`surfaceTolerance`* is set in the same unit as used in
*`objectModel3D`*.
Points in the interior of the object as specified by
*`normalDirection`* (and also
*`genParamName`*=*"angle_threshold"*) are considered surely
inside the object if their distance to the initial surface exceeds
*`surfaceTolerance`* but is smaller than *`minThickness`*.
*`surfaceTolerance`* always has to be smaller
than *`minThickness`*.
*`surfaceTolerance`* should always be a bit larger than
*`resolution`* in order to avoid discretization artifacts.

*`minThickness`* specifies the thickness of the object in normal
direction of the initial surfaces. *`minThickness`* is set
in the same unit as used in *`objectModel3D`*.
Points which are specified by *`normalDirection`* (and also
*`genParamName`*=*"angle_threshold"*) to be in the interior of
the object are only considered as being inside if their distance to the
initial surface does not exceed *`minThickness`*. Note that this can
lead to a hollow part of the object.
*`minThickness`* always has to be larger than
*`surfaceTolerance`*.
For point clouds representing the object from different sides,
*`minThickness`* is best set as the thickness
of the objects narrowest part.
Note that the operator will try to produce a closed surface.
If the input point clouds represent the object only from one side, this
parameter should be set very large, so that the object is cut off at the
bounding box.
The backside of the objects is not observed and thus its
reconstruction will probably be incorrect.
If you observe several distinct objects from only one side, you may want
to reduce the parameter *`minThickness`* to restrict the
depth of reconstructed objects and thus keep them from being smudged into
one surface.
Too small values can result in holes or double walls in the fused point
cloud. Too large values can result in a distorted point cloud or
blow up the surface towards the outside of the object (if the surface is
blown up beyond the bounding box, no points will be returned).

|  |  |
| --- | --- |
| ![figure](../assets/19d6ba7bde1d62df.svg) | ![figure](../assets/98c256506e4ce2ac.svg) |
| ( 1) | ( 2) |

Schematic view of the parameters *`surfaceTolerance`*,
*`minThickness`* and the value *"distance_in_front"*
with the aid of an example surface (_.):
`o` are points taken as outside,
`s` are points of the surface,
`i` are points surely inside the object,
`c` are points also considered for the evaluation of the surface.
(1): *"distance_in_front"* smaller than *`surfaceTolerance`*
(2): *"distance_in_front"* larger than *`surfaceTolerance`*.

*`smoothing`*
determines how important a small total
variation of the distance function is compared to data fidelity. Thus,
*`smoothing`* regulates the 'jumpiness' of the resulting surface.
Note that the actual value of *`smoothing`* for a given data to
result in an appropriate and visually pleasing surface has to be found by
trial and error.
Too small values lead to integrating many outliers into the surface even
if the surface then exhibits many jumps. Too large values lead to lost
fidelity towards the input point clouds (how the
algorithm views distances to the input point clouds depends heavily on
*`surfaceTolerance`* and *`minThickness`*).
*`smoothing`* may need to be adapted when *`resolution`*
is changed.

By setting *`genParamName`* to the following values, the additional
parameters can be set with *`genParamValue`*:

- ***"distance_in_front"*** —

  Points in the exterior of the object as specified by
  *`normalDirection`*
  (and also *`genParamName`*=*"angle_threshold"*)
  are only considered as part of the
  object if their distance to the initial surface does not exceed
  *"distance_in_front"*.
  This is the outside analogous to *`minThickness`* of the interior,
  except that *"distance_in_front"* does not have to be larger
  than *`surfaceTolerance`*.
  In case *"distance_in_front"* is smaller than
  *`surfaceTolerance`* it determines the surface thickness to the
  front.
  This parameter is useful if holes in the surface should be closed along
  a jump in the surface
  (for example along the viewing direction of the sensor). In this case,
  *"distance_in_front"* can be set to a small value in order to
  avoid a wrong initialization of the distance field.
  *"distance_in_front"* is set in the same unit as used in
  *`objectModel3D`*.
  *"distance_in_front"* should always be a bit larger than
  *`resolution`* in order to avoid discretization artifacts.
  Per default, *"distance_in_front"* is set to a value larger than
  the bounding box diameter, therewith all points outside of the object
  in the bounding box are considered.

  Suggested values:
   *0.001*, *0.1*, *1*,
  *10*.

  Default:
   Larger than the bounding box diameter.

  Restriction:
   *"distance_in_front"* > 0
- ***"angle_threshold"*** —

  specifies the angle of a cone around a surface normal.
  *"angle_threshold"* is set in [rad]. When determining
  the distance information for data fidelity, only points are considered
  lying in such a cone starting at their closest surface point.
  For example, if distances to
  triangles are considered, *"angle_threshold"* can be set to
  *0.0*, so that only the volume directly above the triangle
  is considered (thus a right prism).
  If point normals are used and thus distances to normals are considered,
  *"angle_threshold"* has to be set to a higher value.
  When outliers disrupt the result, decreasing *"angle_threshold"*
  may help.
  If holes in the surface should be closed along a
  jump in the surface (for example along the viewing direction of the
  sensor), enlarging *"angle_threshold"* may help.

  Suggested values:
   *"rad(0.0)"*, *"rad(10.0)"*,
  *"rad(30.0)"*.

  Default:
   *"rad(10.0)"*.

  Restriction:
   *"angle_threshold"* >= 0
- ***"point_meshing"*** —

  determines whether the output points should be triangulated with the
  algorithm 'marching tetrahedra', which can be activated by setting
  *"point_meshing"* to *"isosurface"*.
  Note that there are more points in *`objectModel3DFusion`* if
  meshing of the isosurface is enabled even if the used
  *`resolution`* is the same.

  List of values:
   *"none"*, *"isosurface"*.

  Default:
   *"isosurface"*.

### Fusion algorithm

The algorithm will produce a watertight, closed surface (which is maybe
cut off at the *`boundingBox`*). The goal is to obtain
a preferably smooth surface while keeping form fidelity. To this end,
the bounding box is sampled and each sample point is assigned an initial
distance to a so-called isosurface (consisting of points with distance 0).
The final distance values (and thus the isosurface) are obtained by
minimizing an error function based on fidelity to the initial point clouds
on the one hand and total variation ('jumpiness') of the distance function
on the other hand. This leads to a fusion of the input point clouds
(see paper in References below).

The calculation of the isosurface can be influenced with
the parameters of the operator.
The distance between sample points in the bounding box (in each
coordinate direction) can be set with the parameter *`resolution`*.

Fidelity to the initial point clouds is grasped as the signed distances of
sample points, lying on the grid, in the bounding box to their nearest
neighbors (points or triangles) on the input point clouds.
Whether a sample point in the bounding box is considered to lie outside
or inside the object (the sign of the distance) is determined by the
normal of its nearest neighbor on the initial surface and the set
*`normalDirection`*.
To determine if a sample point is surely inside or
outside the object with respect to an input point cloud, the
distance to its nearest neighbor on the initial surface is determined.
A point on the inside is considered surely inside if the distance
exceeds *`surfaceTolerance`* but not *`minThickness`*, while
a point on the outside counts as exteriorly if the distance exceeds
*"distance_in_front"*.

Fidelity to the initial point clouds is only considered for those sample
points lying within *`minThickness`* inside or within
*`genParamName`* *"distance_in_front"* outside the initial
surface.

Furthermore, fidelity is not maintained for a given sample point lying
outside a cone around *`genParamName`* *"angle_threshold"*.
Thus it is not maintained if the line from
the sample point to its nearest neighbor on the initial surface differs
from the surface normal of the nearest neighbor by an angle more than
*`genParamName`* *"angle_threshold"*.
Note that the distances to nearest neighboring triangles will
often yield more satisfying results while distances to nearest points can
be calculated much faster.

The subsequent optimization of the distance values is the same as
the one used in [`ReconstructSurfaceStereo`](reconstruct_surface_stereo.md) with
`method`=*"surface_fusion"*.

The parameter *`smoothing`* regulates the 'jumpiness' of the
distance function by weighing the two terms in the error function:
Fidelity to the initial point clouds
on the one hand, total variation of the distance function on the other
hand. Note that the actual value of *`smoothing`* for a given data
set to be visually pleasing has to be found by trial and error.

Each 3D point of the object model returned in *`objectModel3DFusion`*
is extracted from the isosurface where the distance function equals zero.
Its normal vector is calculated from the gradient of the distance
function. The so-obtained point cloud can also be meshed using the
algorithm 'marching tetrahedra' by setting the *`genParamName`*
*"point_meshing"* to the *`genParamValue`*
*"isosurface"*.

### Troubleshooting

Please follow the workflow above. If the results are not
satisfactory, please consult the following hints and ideas:

- ***Quality of the input point clouds*** —

  The input point clouds should represent the entire object surface. If
  point normals are used, the points should be dense on the entire
  surface, not only along edges of the object. In particular, for CAD-data
  typically triangulation has to be used.
- ***Used attribute*** —

  Using triangles instead of point normals will typically yield results
  of higher quality. If both attributes are present, point normals are
  used per default. If triangles should be used, use
  [`CopyObjectModel3d`](copy_object_model_3d.md) to obtain only point and triangle
  information.
- ***Outliers*** —

  If outliers of the input models disturb the output surface even for
  high values of *`smoothing`*, try to decrease *`genParamName`*
  *"angle_threshold"*. If wanted, outliers of the input models
  can also be removed, for example using
  [`ConnectionObjectModel3d`](connection_object_model_3d.md). With reduced influence also
  modifying *`genParamName`* *"distance_in_front"* may help
  to reduce certain outliers.
- ***Closing of holes*** —

  If holes in the surface are not closed even for
  high values of *`smoothing`* (for example a jump in the surface
  along the viewing direction of the sensor), try to decrease
  *`genParamName`* *"distance_in_front"*. Enlarging
  *`genParamName`* *"angle_threshold"* may help the algorithm
  to close the gap. Note that [`TriangulateObjectModel3d`](triangulate_object_model_3d.md) can
  close gaps when triangulating sensor data which contains a 2D mapping.
- ***Empty output*** —

  If the output contains no point, try to decrease *`smoothing`*. If
  there is no output even for very low values of *`smoothing`*,
  you may want to check if *`minThickness`* is set too large and
  if the set *`normalDirection`* is correct.

### Runtime

In order to improve the runtime, consider the following hints:

- ***Extent of the bounding box*** —

  The bounding box should be tight around the volume of interest. Else,
  the runtime will increase drastically but without any benefit.
- ***Resolution*** —

  Enlarging the parameter *`resolution`* will speed up the execution
  considerably.
- ***Used attribute*** —

  Using point normals instead of triangles will speed up the execution.
  If both, normals and triangles, are present in the input models,
  normals are used per default.
- ***Density of input point clouds*** —

  The input point clouds can be thinned out using
  [`SampleObjectModel3d`](sample_object_model_3d.md) (if normals are used) or
  [`SimplifyObjectModel3d`](simplify_object_model_3d.md) with *`genParamName`*
  *"avoid_triangle_flips"* set to *"true"*
  (if triangles are used).
- ***Distances to surface*** —

  Make sure that *`minThickness`* and *`genParamName`*
  *"distance_in_front"* are not set unnecessarily large,
  since this can slow down the preparation and distance computation.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`objectModel3D`** (input_control)  object_model_3d(-array) `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handles of the 3D object models.

**`boundingBox`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

The two opposite bound box corners.

**`resolution`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Used resolution within the bounding box.

Default:
1.0

Suggested values:
1.0, 1.1, 1.5, 10.0, 100.0

**`surfaceTolerance`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Distance of expected noise to surface.

Default:
1.0

Suggested values:
1.0, 1.1, 1.5, 10.0, 100.0

**`minThickness`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Minimum thickness of the object in direction
of the surface normal.

Default:
1.0

Suggested values:
1.0, 1.1, 1.5, 10.0, 100.0

**`smoothing`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Weight factor for data fidelity.

Default:
1.0

Suggested values:
1.0, 1.1, 1.5, 10.0, 100.0

**`normalDirection`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Direction of normals of the input models.

Default:
"inwards"

List of values:
"inwards", "outwards"

**`genParamName`** (input_control)  attribute.name-array `→` [HTuple](HTuple.md) (*string*)

Name of the generic parameter.

Default:
[]

List of values:
"angle_threshold", "distance_in_front", "point_meshing"

**`genParamValue`** (input_control)  attribute.value-array `→` [HTuple](HTuple.md) (*string* / double / int / long)

Value of the generic parameter.

Default:
[]

Suggested values:
"isosurface", "none", 0.0, 0.1, 0.175, 0.524

**`objectModel3DFusion`** (output_control)  object_model_3d `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the fused 3D object model.

## Result

`FuseObjectModel3d` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

## Possible Predecessors

`ReadObjectModel3d`,
`RegisterObjectModel3dPair`,
`RegisterObjectModel3dGlobal`,
`SurfaceNormalsObjectModel3d`,
`TriangulateObjectModel3d`,
`SimplifyObjectModel3d`,
`GetObjectModel3dParams`

## Possible Successors

`WriteObjectModel3d`,
`CreateSurfaceModel`

## See also

`ReconstructSurfaceStereo`

## References

C. Zach, T. Pock, and H. Bischof: “A globally optimal algorithm for robust
TV-L1 range image integration.”
Proceedings of IEEE International Conference on Computer Vision (ICCV 2007).

## Module

3D Metrology
