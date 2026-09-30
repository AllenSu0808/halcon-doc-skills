# set_surface_model_param (Operator)

## Name

`set_surface_model_param` — Set parameters and properties of a surface model.

## Signature

`set_surface_model_param( : : SurfaceModelID, GenParamName, GenParamValue : )`

## Description

The operator `set_surface_model_param` sets parameters and
properties of the surface model *`SurfaceModelID`*.
The surface model must have been created by [`create_surface_model`](create_surface_model.md)
or [`read_surface_model`](read_surface_model.md).
The names of the desired properties are passed in the generic parameter
*`GenParamName`*, the corresponding values are passed in
*`GenParamValue`*.

The possible values for *`GenParamName`* are listed below.

- **Defining cameras for image-based refinement.**
  The following parameters allow to set and clear camera parameters and
  poses. Those are used by the operators [`find_surface_model_image`](find_surface_model_image.md)
  and [`refine_surface_model_pose_image`](refine_surface_model_pose_image.md) to project the surface
  model into the passed image.

  Note that the camera parameters must be set before the camera pose.

  - ***'camera_parameter'*:** —
  - ***'camera_parameter X'*:** —

    Sets the camera parameters for camera number X, where X is a zero-based
    index for the cameras. If not given, X defaults zero (first camera).
    The camera parameters are used by the operators
    [`find_surface_model_image`](find_surface_model_image.md) and
    [`refine_surface_model_pose_image`](refine_surface_model_pose_image.md),
    which use the images corresponding to the camera for the 3D pose
    refinement.
    Cameras must be added in increasing order.
  - ***'camera_pose'*:** —
  - ***'camera_pose X'*:** —

    Sets the camera pose for camera number X, where X is a zero-based
    index for the cameras. If not given, X defaults zero (first camera).
    The pose defaults to the zero-pose *[0,0,0,0,0,0,0]* when adding
    a new camera with *'camera_parameter'*.
    This usually means that camera and 3D sensor have the same point of
    origin.
  - ***'clear_cameras'*:** —

    Removes all previously set cameras from the surface model.
- **Defining Object Symmetries.**
  The following parameters can be used to define symmetries of the 3D
  object which was used for the creation of the surface model.
  If the 3D object is symmetric, that information can be used to speed up
  the surface-based matching.
  Note that for surface models created with the *'train_3d_edges'*
  parameter enabled, no symmetries can be set.

  By default, no symmetry is active.

  Note that for performance reasons, when changing the symmetry with any
  of the parameters below, certain internal data structures of the surface
  model are re-created, which can take a few seconds.

  - ***'symmetry_axis_direction'*:** —

    Set the direction of the symmetry axis of the model.
    *`GenParamValue`* must be a tuple with three numbers, containing
    the x-, y- and z-value of the axis direction.
    The model is modified to use this symmetry information for speeding
    up the matching process.

    To remove the symmetry information, pass an empty tuple in
    *`GenParamValue`*.
    Note that either a symmetry axis or symmetry poses can be set, but
    not both.

    ![figure](../assets/06ac3224559d6775.svg)

    An object (cylinder) with the symmetry axis direction
    *[0,0,1]*.

    In case that *'symmetry_axis_direction'* is used
    in combination with a restriction of the pose range as described below,
    the value of *'symmetry_axis_direction'* is also used as if set
    with the parameter *'pose_restriction_allowed_axis_direction'*.
  - ***'symmetry_axis_origin'*:** —

    Set a point on the symmetry axis of the model.
    *`GenParamValue`* must be a tuple with three numbers, which
    represent a point in model coordinates that lies on the symmetry
    axis of the model.
    This parameter is optional and defaults to the center of the
    model as returned by [`get_surface_model_param`](get_surface_model_param.md).

    In case that *'symmetry_axis_origin'* is used
    in combination with a restriction of the pose range as described below,
    the value of *'symmetry_axis_origin'* is also used as if set
    with the parameter *'pose_restriction_allowed_axis_origin'*.
  - ***'symmetry_poses'*:** —

    Set one or more symmetry poses of the model (see [`create_pose`](create_pose.md)).
    The model must be identical when transformed with any of those
    poses.
    The model is modified to use this symmetry information for speeding
    up the matching process.

    When setting one or more symmetry poses, `set_surface_model_param`
    will internally create all poses that can be created by chaining and
    inverting the passed poses. To obtain all internally created poses,
    use [`get_surface_model_param`](get_surface_model_param.md) with the argument
    *'symmetry_poses_all'*.
    If more than 100 poses are created internally, an error is returned,
    which indicates that the passed symmetry poses are invalid.

    To remove the symmetry poses, pass an empty tuple in
    *`GenParamValue`*.
    Note that either a symmetry axis or symmetry poses can be set, but
    not both.

    ![figure](../assets/8dfe8fe4f14ad70a.svg)

    An object with a discontinuous symmetry. The symmetry pose for this
    object is *[0,0,0, 0,0,360.0/5, 0]*.
- **Restrict the pose range.**
  The following parameters can be used to restrict the range of rotations
  in which the surface model is searched for by [`find_surface_model`](find_surface_model.md),
  or the allowed range of rotations for the refinement with
  [`refine_surface_model_pose`](refine_surface_model_pose.md).

  By default, no pose range restriction is active.

  Note that for performance reasons, when changing the pose range with any
  of the parameters below, certain internal data structures of the surface
  model are re-created, which can take a few seconds.

  - ***'pose_restriction_reference_pose'*:** —

    Set a reference pose of the model.
    The reference pose can be used along with
    *'pose_restriction_max_angle_diff'*,
    to restrict the allowed range of rotations of the model.

    If *`GenParamValue`* is an empty tuple, any previously set
    reference pose is cleared and no pose range restriction will be active
    for the model.

    Otherwise, *`GenParamValue`* must be a pose (see
    [`create_pose`](create_pose.md)).
    Note that the translation part of the pose is ignored.
    Also note that both *'pose_restriction_reference_pose'* and
    *'pose_restriction_max_angle_diff'* must be set in order for
    the pose restriction to be active.
  - ***'pose_restriction_max_angle_diff'*:** —

    Set by how much the rotation of a pose found with
    [`find_surface_model`](find_surface_model.md) or refined with
    [`refine_surface_model_pose`](refine_surface_model_pose.md) may deviate from the rotation set
    with *'pose_restriction_reference_pose'*, in radians.

    If *`GenParamValue`* is an empty tuple, any previously set
    maximum deviation angle is cleared and no pose range restriction will
    be active for the model.

    Otherwise, *`GenParamValue`* must be an angle, which
    indicates by how much the rotations of a detected pose *'P'*
    and the reference pose *'R'* set with
    *'pose_restriction_reference_pose'* may differ.
    The comparison is performed for every model point using the formula
    $\angle (R_v, P_v) \leq \max\_angle\_diff$ ![figure](../assets/1a29adb1a83caeab.svg),
    where $\mathbf{v}$ is the 3D point vector.
  - ***'pose_restriction_allowed_axis_direction'*:** —

    Set an axis for which rotations are ignored when evaluating the pose
    range (see *'pose_restriction_reference_pose'* and
    *'pose_restriction_max_angle_diff'*).
    If *`GenParamValue`* is an empty tuple, any previously set
    axis is cleared.

    Otherwise, *`GenParamValue`* must contain a tuple of three numbers
    which are the direction of the axis in model coordinates.

    If such an axis is set, then a pose is considered to be within the
    allowed range if the angle between the axis in the reference pose
    and the compared pose is smaller than the allowed angle, using
    $\angle(R\!axis, P\!axis) \leq \mathrm{max\_angle\_diff}$ ![figure](../assets/c7eb78128707c2a9.svg).
  - ***'pose_restriction_allowed_axis_origin'*:** —

    Set a point on the allowed rotation axis of the model.
    *`GenParamValue`* must be a tuple with three numbers, which
    represent a point in model coordinates that lies on the symmetry
    axis of the model.
    This parameter is optional and defaults to the center of the
    model as returned by [`get_surface_model_param`](get_surface_model_param.md).
  - ***'pose_restriction_filter_final_poses_only'*:** —

    This flag allows to switch between two different modes for the pose
    range restriction.

    If *`GenParamValue`* is *'false'* (default), poses outside the
    defined pose range are removed early in the matching process.
    Use this setting if the object pose in the scene is always within the
    defined rotation range, but the object is sometimes found with incorrect
    rotations.
    Note that with this setting, [`find_surface_model`](find_surface_model.md) might return
    poses that the algorithm considers to be locally suboptimal, because the
    locally more optimal poses are outside the allowed pose range.
    Also note that with this setting, the pose restriction is observed
    strictly.
    When passing an input pose to [`refine_surface_model_pose`](refine_surface_model_pose.md)
    that is outside the allowed pose range, it will be transformed to be
    within the allowed pose range.

    If *`GenParamValue`* is *'true'*, only the final poses
    are filtered before returning them.
    This allows removing poses that are valid object poses, but are not
    needed by the application because, for example, the object cannot be
    picked up by the robot in a certain orientation.
    Note that in this setting, less poses than requested might be returned
    by [`find_surface_model`](find_surface_model.md) if one or more of the final poses
    are outside the allowed pose range.
- **Modifying self-similarities.**
  The following parameters can be used to adapt the optimization regarding
  self-similar poses, i.e., poses under which the model is almost
  symmetric.
  The parameters can only be set if the parameter
  *'train_self_similar_poses'* was activated during the call
  of [`create_surface_model`](create_surface_model.md).

  Note that for performance reasons, when changing the self-similarity search
  with any of the parameters below, certain internal data structures of the surface
  model are re-created, which can take a few seconds.

  - ***'self_similar_poses'*:** —

    Set the self-similar poses of the model.
    Those are poses under which the model is very similar to itself
    and which can be confused during search.

    [`find_surface_model`](find_surface_model.md) will find such poses automatically
    if the parameter *'use_self_similar_poses'* is activated.
    The poses can be obtained with [`get_surface_model_param`](get_surface_model_param.md).
    If the automatically determined poses are not sufficient to
    resolve self-similarities, the self-similar poses can be adapted
    with this parameter.
    It is usually not recommended to modify this parameter.

    *`GenParamValue`* must contain a list of poses.
    The identity pose will automatically be added to the list of poses,
    if it is not already contained in it.

## Attention

Note that in some cases, if this operator encounters an error condition
while modifying the surface model, such as an out-of-memory error, the
model might be left in an inconsistent, partly changed state.
In such cases, it is recommended to clear the surface model and to no
longer use it.

This does not apply to error codes due to invalid parameters, which are
checked before performing any model modification.

Also note that setting some of the options requires re-generation of
internal data structures and can take as long as the original
[`create_surface_model`](create_surface_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator modifies the state of the following input parameter:

- SurfaceModelID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`SurfaceModelID`** (input_control, state is modified)  surface_model `→`  (handle)

Handle of the surface model.

**`GenParamName`** (input_control)  attribute.name `→`  (string)

Name of the parameter.

Default:
'camera_parameter'

List of values:
'camera_parameter', 'camera_pose', 'clear_cameras', 'pose_restriction_allowed_axis_direction', 'pose_restriction_allowed_axis_origin', 'pose_restriction_filter_final_poses_only', 'pose_restriction_max_angle_diff', 'pose_restriction_reference_pose', 'self_similar_poses', 'symmetry_axis_direction', 'symmetry_axis_origin', 'symmetry_poses'

**`GenParamValue`** (input_control)  attribute.value(-array) `→`  (real / string / integer)

Value of the parameter.

Suggested values:
'true', 'false', [], [0,0,0,0,0,0,0], [0,0,1]

## Result

`set_surface_model_param` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Predecessors

`create_surface_model`,
`read_surface_model`,
`get_surface_model_param`

## Possible Successors

`find_surface_model`,
`refine_surface_model_pose`,
`write_surface_model`,
`find_surface_model_image`,
`refine_surface_model_pose_image`

## See also

`create_surface_model`,
`get_surface_model_param`

## Module

3D Metrology
