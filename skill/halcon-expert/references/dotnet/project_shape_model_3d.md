# ProjectShapeModel3d (Operator)

## Name

`ProjectShapeModel3d` — Project the edges of a 3D shape model into image coordinates.

## Signature

`static void HOperatorSet.ProjectShapeModel3d(out HObject modelContours, HTuple shapeModel3DID, HTuple camParam, HTuple pose, HTuple hiddenSurfaceRemoval, HTuple minFaceAngle)`

`HXLDCont HShapeModel3D.ProjectShapeModel3d(HCamPar camParam, HPose pose, string hiddenSurfaceRemoval, HTuple minFaceAngle)`

`HXLDCont HShapeModel3D.ProjectShapeModel3d(HCamPar camParam, HPose pose, string hiddenSurfaceRemoval, double minFaceAngle)`

`HXLDCont HCamPar.ProjectShapeModel3d(HShapeModel3D shapeModel3DID, HPose pose, string hiddenSurfaceRemoval, HTuple minFaceAngle)`

`HXLDCont HCamPar.ProjectShapeModel3d(HShapeModel3D shapeModel3DID, HPose pose, string hiddenSurfaceRemoval, double minFaceAngle)`

`HXLDCont HPose.ProjectShapeModel3d(HShapeModel3D shapeModel3DID, HCamPar camParam, string hiddenSurfaceRemoval, HTuple minFaceAngle)`

`HXLDCont HPose.ProjectShapeModel3d(HShapeModel3D shapeModel3DID, HCamPar camParam, string hiddenSurfaceRemoval, double minFaceAngle)`

## Description

The operator `ProjectShapeModel3d` projects the edges of
the 3D object model that was used to create the 3D shape model
*`shapeModel3DID`* into the image coordinate system and returns
the projected edges in *`modelContours`*. The coordinates of
the 3D object model are given in the 3D world coordinate
system (*mcs*). First, they are transformed into the camera
coordinate system (*ccs*) using the external camera parameters given
in *`pose`*.
Then, these coordinates are projected into the image coordinate system
based on the internal camera parameters *`camParam`*.

The internal camera parameters *`camParam`* describe the
projection characteristics of the camera (see
[Calibration](toc_calibration.md)).
The *`pose`* is in the form $\mathrm{ccs} \mathbf{P}_{\mathrm{mcs}}$ ![figure](../assets/36630faf4c6dcd27.svg),
see [Transformations / Poses](toc_transformations_poses.md) and
`“Solution Guide III-C - 3D Vision”`.
Hence, it describes the position and orientation of the model coordinate
system defined by the 3D object model relative to the camera coordinate
system.

The parameter *`hiddenSurfaceRemoval`* can be used to switch on
or to switch off the removal of hidden surfaces. If
*`hiddenSurfaceRemoval`* is set to *"true"*, only those
projected edges are returned that are not hidden by faces of the 3D
object model. If *`hiddenSurfaceRemoval`* is set to
*"false"*, all projected edges are returned. This is faster
than a projection with *`hiddenSurfaceRemoval`* set to
*"true"*.

If the system variable (see [`SetSystem`](set_system.md))
*"opengl_hidden_surface_removal_enable"* is set to *"true"*
(which is default if it is available) and *`hiddenSurfaceRemoval`* is
set to *"true"*, the projection of the model is accelerated using
the graphics card.
Depending on the graphics card this is significantly faster than the non
accelerated algorithm. Be aware that the results of the OpenGL projection
are slightly different compared to the analytic projection. Notable, only
the contours visible through *`camParam`* are projected in this mode.

3D edges are only projected if the angle between the two 3D faces
that are incident with the 3D edge is at least
*`minFaceAngle`*. If *`minFaceAngle`* is set to
*0.0*, all edges are projected. If *`minFaceAngle`* is
set to $\pi$ (equivalent to 180 degrees), only the
silhouette of the 3D object model is returned. This parameter can be
used to suppress edges within curved surfaces, e.g., the surface of
a cylinder.

If for the model creation with [`CreateShapeModel3d`](create_shape_model_3d.md) the parameter
*"union_adjacent_contours"* was activated, adjacent contours
are joined.

`ProjectShapeModel3d` and [`ProjectObjectModel3d`](project_object_model_3d.md)
return the same result if the 3D object model that was used to
create the 3D shape model is passed to
[`ProjectObjectModel3d`](project_object_model_3d.md).

`ProjectShapeModel3d` is especially useful in order to
visualize the matches that are returned by
[`FindShapeModel3d`](find_shape_model_3d.md) in the case that the underlying 3D
object model is no longer available.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`modelContours`** (output_object)  xld_cont-array `→` [HXLDCont](HXLDCont.md)

Contour representation of the model view.

**`shapeModel3DID`** (input_control)  shape_model_3d `→` [HShapeModel3D](HShapeModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D shape model.

**`camParam`** (input_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

Internal camera parameters.

**`pose`** (input_control)  pose `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

3D pose of the 3D shape model in the world
coordinate system.

**`hiddenSurfaceRemoval`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Remove hidden surfaces?

Default:
"true"

List of values:
"false", "true"

**`minFaceAngle`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double* / int / long)

Smallest face angle for which the edge is displayed

Default:
0.523599

Suggested values:
0.17, 0.26, 0.35, 0.52

## Result

If the parameters are valid, the operator
`ProjectShapeModel3d` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`CreateShapeModel3d`,
`ReadShapeModel3d`,
`GetShapeModel3dParams`,
`FindShapeModel3d`

## Alternatives

`ProjectObjectModel3d`

## See also

`ConvertPoint3dCartToSpher`,
`ConvertPoint3dSpherToCart`,
`CreateCamPoseLookAtPoint`,
`TransPoseShapeModel3d`

## Module

3D Metrology
