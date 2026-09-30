# edges_object_model_3d (Operator)

## Name

`edges_object_model_3d` — Find edges in a 3D object model.

## Signature

`edges_object_model_3d( : : ObjectModel3D, MinAmplitude, GenParamName, GenParamValue : ObjectModel3DEdges)`

## Description

`edges_object_model_3d` finds 3D edges in the 3D object model
*`ObjectModel3D`* and returns them in the 3D object model
*`ObjectModel3DEdges`*.

The operator supports edge extraction only from 3D object models that
contain a XYZ mapping, such as models that were created with
[`xyz_to_object_model_3d`](xyz_to_object_model_3d.md) or that were obtained with a sensor that
delivers the mapping.
*`MinAmplitude`* defines the minimum amplitude of a discontinuity in
order to be classified as an edge.
It is given in the same unit as used in *`ObjectModel3D`*.

The extracted edges are a subset of the points of the input object model.
In addition to the coordinates of the edges, the point normal vectors
in *`ObjectModel3DEdges`* contain the viewing direction of each
3D edge point from the viewpoint towards the edge point.
Also, the attributes *'edge_dir_x'*, *'edge_dir_y'* and
*'edge_dir_z'* contain a vector that is perpendicular to
the edge direction and to the viewing direction.
The attributes are set such that the 3D object model can be used
for edge-supported surface-based matching in [`find_surface_model`](find_surface_model.md).

Generic parameters can optionally be used to influence the edge extraction.
If desired, these parameters and their corresponding values can be specified
with *`GenParamName`* and *`GenParamValue`*.
The following values for *`GenParamName`* are possible:

- ***'max_gap'*:** —

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
- ***'estimate_viewpose'*:** —

  This parameter can be used to turn off the automatic viewpose
  estimation and set a manual viewpoint.

  Default:
   *'true'*.
- ***'viewpoint'*:** —

  This parameter only has an effect when *'estimate_viewpose'*
  is set to *'false'*. It specifies the viewpoint from which
  the 3D data is seen.
  It is used to determine the viewing directions and edge directions.
  It defaults to the origin *'0 0 0'* of the 3D data.
  If the projection center is at a different location, for example, if
  the 3D object model was transformed with
  [`rigid_trans_object_model_3d`](rigid_trans_object_model_3d.md) or if the 3D sensor performed a
  similar transformation, the original viewpoint must be set.
  For this, *`GenParamValue`* must contain a string consisting of
  the three coordinates (x, y and z) of the viewpoint, separated by spaces.
  The viewpoint is defined in the same coordinate frame as
  *`ObjectModel3D`*.
  Note that for use of this parameter, the values in the X-, Y-, and Z-
  images obtained from [`object_model_3d_to_xyz`](object_model_3d_to_xyz.md) must have increasing
  values from left to right, top to bottom, and for object parts further
  away from the camera, respectively.

  Default:
   *'0 0 0'*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator supports canceling timeouts and interrupts.

## Parameters

**`ObjectModel3D`** (input_control)  object_model_3d `→`  (handle)

Handle of the 3D object model whose edges should
be computed.

**`MinAmplitude`** (input_control)  number `→`  (real / integer)

Edge threshold.

**`GenParamName`** (input_control)  string(-array) `→`  (string)

Names of the generic parameters.

Default:
[]

List of values:
'estimate_viewpose', 'max_gap', 'viewpoint'

**`GenParamValue`** (input_control)  number(-array) `→`  (real / integer / string)

Values of the generic parameters.

Default:
[]

Suggested values:
'0 0 0', 10, 30, 100, 'true', 'false'

**`ObjectModel3DEdges`** (output_control)  object_model_3d `→`  (handle)

3D object model containing the edges.

## Result

`edges_object_model_3d` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Predecessors

`read_object_model_3d`,
`xyz_to_object_model_3d`

## Possible Successors

`find_surface_model`,
`find_surface_model_image`,
`refine_surface_model_pose`,
`refine_surface_model_pose_image`

## Module

3D Metrology
