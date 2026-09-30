# project_shape_model_3d (Operator)

## Name

`project_shape_model_3d` — Project the edges of a 3D shape model into image coordinates.

## Signature

`def project_shape_model_3d(shape_model_3did: HHandle, cam_param: Sequence[Union[int, float, str]], pose: Sequence[Union[int, float]], hidden_surface_removal: str, min_face_angle: Union[int, float]) -> HObject`

## Description

The operator `project_shape_model_3d` projects the edges of
the 3D object model that was used to create the 3D shape model
*`shape_model_3did`* into the image coordinate system and returns
the projected edges in *`model_contours`*. The coordinates of
the 3D object model are given in the 3D world coordinate
system (*mcs*). First, they are transformed into the camera
coordinate system (*ccs*) using the external camera parameters given
in *`pose`*.
Then, these coordinates are projected into the image coordinate system
based on the internal camera parameters *`cam_param`*.

The internal camera parameters *`cam_param`* describe the
projection characteristics of the camera (see
[Calibration](toc_calibration.md)).
The *`pose`* is in the form $\mathrm{ccs} \mathbf{P}_{\mathrm{mcs}}$ ![figure](../assets/36630faf4c6dcd27.svg),
see [Transformations / Poses](toc_transformations_poses.md) and
`“Solution Guide III-C - 3D Vision”`.
Hence, it describes the position and orientation of the model coordinate
system defined by the 3D object model relative to the camera coordinate
system.

The parameter *`hidden_surface_removal`* can be used to switch on
or to switch off the removal of hidden surfaces. If
*`hidden_surface_removal`* is set to *"true"*, only those
projected edges are returned that are not hidden by faces of the 3D
object model. If *`hidden_surface_removal`* is set to
*"false"*, all projected edges are returned. This is faster
than a projection with *`hidden_surface_removal`* set to
*"true"*.

If the system variable (see [`set_system`](set_system.md))
*"opengl_hidden_surface_removal_enable"* is set to *"true"*
(which is default if it is available) and *`hidden_surface_removal`* is
set to *"true"*, the projection of the model is accelerated using
the graphics card.
Depending on the graphics card this is significantly faster than the non
accelerated algorithm. Be aware that the results of the OpenGL projection
are slightly different compared to the analytic projection. Notable, only
the contours visible through *`cam_param`* are projected in this mode.

3D edges are only projected if the angle between the two 3D faces
that are incident with the 3D edge is at least
*`min_face_angle`*. If *`min_face_angle`* is set to
*0.0*, all edges are projected. If *`min_face_angle`* is
set to $\pi$ (equivalent to 180 degrees), only the
silhouette of the 3D object model is returned. This parameter can be
used to suppress edges within curved surfaces, e.g., the surface of
a cylinder.

If for the model creation with [`create_shape_model_3d`](create_shape_model_3d.md) the parameter
*"union_adjacent_contours"* was activated, adjacent contours
are joined.

`project_shape_model_3d` and [`project_object_model_3d`](project_object_model_3d.md)
return the same result if the 3D object model that was used to
create the 3D shape model is passed to
[`project_object_model_3d`](project_object_model_3d.md).

`project_shape_model_3d` is especially useful in order to
visualize the matches that are returned by
[`find_shape_model_3d`](find_shape_model_3d.md) in the case that the underlying 3D
object model is no longer available.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`model_contours`** (output_object)  xld_cont-array `→` HObject

Contour representation of the model view.

**`shape_model_3did`** (input_control)  shape_model_3d `→` HHandle

Handle of the 3D shape model.

**`cam_param`** (input_control)  campar `→` Sequence[Union[int, float, str]]

Internal camera parameters.

**`pose`** (input_control)  pose `→` Sequence[Union[int, float]]

3D pose of the 3D shape model in the world
coordinate system.

**`hidden_surface_removal`** (input_control)  string `→` str

Remove hidden surfaces?

Default:
"true"

List of values:
"false", "true"

**`min_face_angle`** (input_control)  angle.rad `→` Union[int, float]

Smallest face angle for which the edge is displayed

Default:
0.523599

Suggested values:
0.17, 0.26, 0.35, 0.52

## Result

If the parameters are valid, the operator
`project_shape_model_3d` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`create_shape_model_3d`,
`read_shape_model_3d`,
`get_shape_model_3d_params`,
`find_shape_model_3d`

## Alternatives

`project_object_model_3d`

## See also

`convert_point_3d_cart_to_spher`,
`convert_point_3d_spher_to_cart`,
`create_cam_pose_look_at_point`,
`trans_pose_shape_model_3d`

## Module

3D Metrology
