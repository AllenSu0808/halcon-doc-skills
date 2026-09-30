# EdgesObjectModel3d (Operator)

## Name

`EdgesObjectModel3d` — Find edges in a 3D object model.

## Signature

`static void HOperatorSet.EdgesObjectModel3d(HTuple objectModel3D, HTuple minAmplitude, HTuple genParamName, HTuple genParamValue, out HTuple objectModel3DEdges)`

`HObjectModel3D HObjectModel3D.EdgesObjectModel3d(HTuple minAmplitude, HTuple genParamName, HTuple genParamValue)`

`HObjectModel3D HObjectModel3D.EdgesObjectModel3d(double minAmplitude, string genParamName, double genParamValue)`

## Description

`EdgesObjectModel3d` finds 3D edges in the 3D object model
*`objectModel3D`* and returns them in the 3D object model
*`objectModel3DEdges`*.

The operator supports edge extraction only from 3D object models that
contain a XYZ mapping, such as models that were created with
[`XyzToObjectModel3d`](xyz_to_object_model_3d.md) or that were obtained with a sensor that
delivers the mapping.
*`minAmplitude`* defines the minimum amplitude of a discontinuity in
order to be classified as an edge.
It is given in the same unit as used in *`objectModel3D`*.

The extracted edges are a subset of the points of the input object model.
In addition to the coordinates of the edges, the point normal vectors
in *`objectModel3DEdges`* contain the viewing direction of each
3D edge point from the viewpoint towards the edge point.
Also, the attributes *"edge_dir_x"*, *"edge_dir_y"* and
*"edge_dir_z"* contain a vector that is perpendicular to
the edge direction and to the viewing direction.
The attributes are set such that the 3D object model can be used
for edge-supported surface-based matching in [`FindSurfaceModel`](find_surface_model.md).

Generic parameters can optionally be used to influence the edge extraction.
If desired, these parameters and their corresponding values can be specified
with *`genParamName`* and *`genParamValue`*.
The following values for *`genParamName`* are possible:

- ***"max_gap"*:** —

  This parameter specifies the maximum gap size in pixels in the
  XYZ-images that are closed.
  Gaps larger than this value will contain edges at their
  boundary, while gaps smaller than this value will not.
  This suppresses edges around smaller patches that were not
  reconstructed by the sensor as well as edges at the more
  distant part of a discontinuity.
  For sensors with very large resolutions, the value should be
  increased to avoid spurious edges.

  Default:
   *30*.
- ***"estimate_viewpose"*:** —

  This parameter can be used to turn off the automatic viewpose
  estimation and set a manual viewpoint.

  Default:
   *"true"*.
- ***"viewpoint"*:** —

  This parameter only has an effect when *"estimate_viewpose"*
  is set to *"false"*. It specifies the viewpoint from which
  the 3D data is seen.
  It is used to determine the viewing directions and edge directions.
  It defaults to the origin *"0 0 0"* of the 3D data.
  If the projection center is at a different location, for example, if
  the 3D object model was transformed with
  [`RigidTransObjectModel3d`](rigid_trans_object_model_3d.md) or if the 3D sensor performed a
  similar transformation, the original viewpoint must be set.
  For this, *`genParamValue`* must contain a string consisting of
  the three coordinates (x, y and z) of the viewpoint, separated by spaces.
  The viewpoint is defined in the same coordinate frame as
  *`objectModel3D`*.
  Note that for use of this parameter, the values in the X-, Y-, and Z-
  images obtained from [`ObjectModel3dToXyz`](object_model_3d_to_xyz.md) must have increasing
  values from left to right, top to bottom, and for object parts further
  away from the camera, respectively.

  Default:
   *"0 0 0"*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator supports canceling timeouts and interrupts.

## Parameters

**`objectModel3D`** (input_control)  object_model_3d `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D object model whose edges should
be computed.

**`minAmplitude`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Edge threshold.

**`genParamName`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Names of the generic parameters.

Default:
[]

List of values:
"estimate_viewpose", "max_gap", "viewpoint"

**`genParamValue`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long / string)

Values of the generic parameters.

Default:
[]

Suggested values:
"0 0 0", 10, 30, 100, "true", "false"

**`objectModel3DEdges`** (output_control)  object_model_3d `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

3D object model containing the edges.

## Result

`EdgesObjectModel3d` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Predecessors

`ReadObjectModel3d`,
`XyzToObjectModel3d`

## Possible Successors

`FindSurfaceModel`,
`FindSurfaceModelImage`,
`RefineSurfaceModelPose`,
`RefineSurfaceModelPoseImage`

## Module

3D Metrology
