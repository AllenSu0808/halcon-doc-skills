# ProjectObjectModel3d (Operator)

## Name

`ProjectObjectModel3d` — Project a 3D object model into image coordinates.

## Signature

`static void HOperatorSet.ProjectObjectModel3d(out HObject modelContours, HTuple objectModel3D, HTuple camParam, HTuple pose, HTuple genParamName, HTuple genParamValue)`

`HXLDCont HObjectModel3D.ProjectObjectModel3d(HCamPar camParam, HPose pose, HTuple genParamName, HTuple genParamValue)`

`HXLDCont HObjectModel3D.ProjectObjectModel3d(HCamPar camParam, HPose pose, string genParamName, string genParamValue)`

`HXLDCont HCamPar.ProjectObjectModel3d(HObjectModel3D objectModel3D, HPose pose, HTuple genParamName, HTuple genParamValue)`

`HXLDCont HCamPar.ProjectObjectModel3d(HObjectModel3D objectModel3D, HPose pose, string genParamName, string genParamValue)`

`HXLDCont HPose.ProjectObjectModel3d(HObjectModel3D objectModel3D, HCamPar camParam, HTuple genParamName, HTuple genParamValue)`

`HXLDCont HPose.ProjectObjectModel3d(HObjectModel3D objectModel3D, HCamPar camParam, string genParamName, string genParamValue)`

## Description

The operator `ProjectObjectModel3d` projects a
3D object model into the image coordinate system and returns the
projected contours in *`modelContours`*. This operator is
particularly useful for the visualization of 3D object models.
Note that primitives are not projected but silently ignored.
The coordinates of the 3D object model are given in the model coordinate
system (*mcs*), a 3D world coordinate system.
First, they are transformed into the camera coordinate system (*ccs*)
using the given *`pose`*.
Then, these coordinates are projected into the
image coordinate system based on the internal camera parameters
*`camParam`*.
Thereby the pose is needed in the form
$\mathrm{ccs} \mathbf{P}_{\mathrm{mcs}}$ ![figure](../assets/36630faf4c6dcd27.svg), see [Transformations / Poses](toc_transformations_poses.md)
and `“Solution Guide III-C - 3D Vision”`.
Thus, the *`pose`* describes the position
and orientation of the world coordinate system with respect to the
camera coordinate system.
The internal camera parameters *`camParam`* describe the
projection characteristics of the camera (see
[Calibration](toc_calibration.md)).

There are some generic parameters that can optionally be used to
influence the projection. If desired, these parameters and their
corresponding values can be specified by using *`genParamName`*
and *`genParamValue`*, respectively. The following values for
*`genParamName`* are possible:

- ***"data"*:** —

  This parameter specifies which geometric data
  of the 3D object model should be projected. If *"data"* is set
  to *"faces"*, the faces of the 3D object model are projected.
  The faces are represented by their border lines in
  *`modelContours`*. If *"data"* is set
  to *"lines"*, the 3D lines of the 3D object model are projected.
  If *"data"* is set to
  *"points"*, the points of the 3D object model are
  projected. The projected points can be represented in
  *`modelContours`* in different ways. The point representation
  can be selected by using the generic parameter *"point_shape"*
  (see below). Finally, if *"data"* is set to *"auto"*,
  HALCON automatically chooses the most descriptive geometry data
  that is available in the 3D object model for visualization.

  List of values:
   *"auto"*, *"faces"*,
  *"lines"*, *"points"*.

  Default:
   *"auto"*.
- ***"point_shape"*:** —

  This parameter specifies how
  points are represented in the output contour *`modelContours`*.
  Consequently, this parameter only has an effect if the points of the
  3D object model are selected for projection (see above).
  If *"point_shape"* is set to *"circle"*, points are
  represented by circles, whereas if *"point_shape"* is set to
  *"cross"*, points are represented by crosses. In both cases
  the size of the points (i.e., the size of the circles or the size
  of the crosses) can be specified by the generic parameter
  *"point_size"* (see below). The orientation of the crosses
  can be specified by the generic parameter
  *"point_orientation"* (see below).

  List of values:
   *"circle"*, *"cross"*.

  Default:
   *"circle"*.
- ***"point_size"*:** —

  This parameter specifies the size
  of the point representation in the output contour
  *`modelContours`*, i.e., the size of the circles or the size
  of the crosses depending on the selected *"point_shape"*.
  Consequently, this parameter only has an effect if the points of
  the 3D object model are selected for projection (see above).
  The size must be given in pixel units. If *"point_size"*
  is set to *0*, each point is represented by a contour
  that contains a single contour point.

  Suggested values:
   *0*, *2*, *4*.

  Default:
   *4*.
- ***"point_orientation"*:** —

  This parameter specifies the
  orientation of the crosses in radians. Consequently, this
  parameter only has an effect if the points of the 3D object model
  are selected for projection and *"point_shape"* is set
  to *"cross"* (see above).

  Suggested values:
   *0*, *0.39*, *0.79*.

  Default:
   *0.79*.
- ***"union_adjacent_contours"*:** —

  This parameter specifies if
  adjacent projected contours should be joined or not.
  Activating this option is equivalent to calling
  [`UnionAdjacentContoursXld`](union_adjacent_contours_xld.md) after this operator, but significantly
  faster.

  List of values:
   *"true"*, *"false"*.

  Default:
   *"true"*.
- ***"hidden_surface_removal"*:** —

  This parameter can be
  used to switch on or off the removal of hidden surfaces. If
  *"hidden_surface_removal"* is set to *"true"*, only those
  projected edges are returned that are not hidden by faces of the 3D
  object model. If *"hidden_surface_removal"* is set to
  *"false"*, all projected edges are returned. This is faster
  than a projection with *"hidden_surface_removal"* set to
  *"true"*.

  If the system variable (see [`SetSystem`](set_system.md))
  *"opengl_hidden_surface_removal_enable"* is set to *"true"*
  (which is the default if it is available) and *"hidden_surface_removal"*
  is set to *"true"*, the projection of the model is accelerated
  using the graphics card.
  Depending on the graphics card this is significantly faster than the non
  accelerated algorithm. Be aware that the results of the OpenGL projection
  are slightly different compared to the analytic projection. Notable, only
  the contours visible through *`camParam`* are projected in this
  mode.

  List of values:
   *"true"*, *"false"*.

  Default:
   *"true"*.
- ***"min_face_angle"*:** —

  3D edges are only projected if the
  angle between the two 3D faces that are incident with the 3D edge
  is at least *"min_face_angle"*. If *"min_face_angle"*
  is set to *0.0*, all edges are projected. If
  *"min_face_angle"* is set to $\pi$ (equivalent to
  180 degrees), only the silhouette of the 3D object model is returned.
  This parameter can be used to suppress edges within curved
  surfaces, e.g., the surface of a cylinder or cone.

  Suggested values:
   *0.17*, *0.26*,
  *0.35*, *0.52*.

  Default:
   *0.52*.

## Attention

Cameras with hypercentric lenses are not supported.
For displaying large faces with a non-zero distortion
in *`camParam`*, note that the distortion is only applied to the
points of the model. In the projection, these points are subsequently
connected by straight lines. For a good approximation of the distorted
lines, please use a triangulation with sufficiently small triangles.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`modelContours`** (output_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Projected model contours.

**`objectModel3D`** (input_control)  object_model_3d `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D object model.

**`camParam`** (input_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

Internal camera parameters.

**`pose`** (input_control)  pose `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

3D pose of the world coordinate system in camera
coordinates.

Number of elements:
Pose == 7

**`genParamName`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Name of the generic parameter.

Default:
[]

List of values:
"data", "false", "hidden_surface_removal", "min_face_angle", "point_orientation", "point_shape", "point_size", "true", "union_adjacent_contours"

**`genParamValue`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Value of the generic parameter.

Default:
[]

Suggested values:
0.17, 0.26, 0.35, 0.52, "true", "false", "auto", "points", "faces", "lines", "circle", "cross", 1, 2, 3, 4, 0.785398

## Result

`ProjectObjectModel3d` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised. If the geometric
data that was selected for the projection is not available in the
3D object model, the error 9514 is raised.

## Possible Predecessors

`ReadObjectModel3d`,
`AffineTransObjectModel3d`,
`PrepareObjectModel3d`

## Possible Successors

`ClearObjectModel3d`

## See also

`ProjectShapeModel3d`,
`ObjectModel3dToXyz`

## Module

3D Metrology
