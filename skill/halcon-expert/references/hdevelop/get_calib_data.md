# get_calib_data (Operator)

## Name

`get_calib_data` — Query data stored or computed in a calibration data model.

## Signature

`get_calib_data( : : CalibDataID, ItemType, ItemIdx, DataName : DataValue)`

## Description

With the operator `get_calib_data`, you can query data of the
calibration data model *`CalibDataID`*.

Note that in the following, all 'pose'-related data is given in relation to
the coordinate system of the model's *reference camera*, which can be
set with [`set_calib_data`](set_calib_data.md) and queried with `get_calib_data`. By
default, the first camera (camera index 0) is used as reference camera.

The calibration data model contains various kinds of data. How to query
specific data of the calibration data model is described for different
categories of data:

- Model-related data (*`ItemType`* *'model'*)
- Camera-related data (*`ItemType`* *'camera'*)
- Data related to calibration objects (*`ItemType`* *'calib_obj'*)
- Data related to calibration object poses (*`ItemType`* *'calib_obj_pose'*)
- Hand-eye calibration related data (different values for *`ItemType`*)

Before we describe the individual data you can query in detail, we provide
you with an overview on which data is available after the individual steps of
the calibration processes. When calibrating cameras or a hand-eye system,
several operators are called that step by step fill the calibration data
model with content. In the following, for each operator a table lists the
data that is added to the model. Additionally, you find information about the
combinations of the values for *`ItemType`*, *`ItemIdx`*, and
*`DataName`* that are needed to query the information with
`get_calib_data`. For the different indices that are used within the
tables the following abbreviations (or potential variable names) are used:

- Camera index: `CameraIdx`
- Calibration object index: `CalibObjIdx`
- Calibration object pose index: `CalibObjPoseIdx`

Detailed descriptions of the data that can be queried can then be found in
the specific sections that handle the different categories of data
individually.

To get detailed information about the calibration process of
your camera setup see the chapter [Calibration](toc_calibration.md).

### Content of Calibration Data Model When Calibrating Cameras

For each operator that extends the calibration model, a table is provided
to give an overview on the respective data:

- [`create_calib_data`](create_calib_data.md):

  |  |  |  |  |
  | --- | --- | --- | --- |
  | Data added to the model | *`ItemType`* | *`ItemIdx`* | *`DataName`* |
  | **Type of the calibration data model** | *'model'* | *'general'* | *'type'* |
  | **Number of cameras** | *'model'* | *'general'* | *'num_cameras'* |
  | **Number of calibration objects** | *'model'* | *'general'* | *'num_calib_objs'* |
- [`set_calib_data_cam_param`](set_calib_data_cam_param.md):

  |  |  |  |  |
  | --- | --- | --- | --- |
  | Data added to the model | *`ItemType`* | *`ItemIdx`* | *`DataName`* |
  | **Camera types** | *'camera'* | `CameraIdx` | *'type'* |
  | **Initial internal camera parameters** | *'camera'* | `CameraIdx` | *'init_params'* |
- [`set_calib_data_calib_object`](set_calib_data_calib_object.md):

  |  |  |  |  |
  | --- | --- | --- | --- |
  | Data added to the model | *`ItemType`* | *`ItemIdx`* | *`DataName`* |
  | **Numbers of calibration marks** of the calibration objects | *'calib_obj'* | `CalibObjIdx` | *'num_marks'* |
  | **Coordinates of the calibration marks** of the calibration objects relative to their calibration object coordinate systems | *'calib_obj'* | `CalibObjIdx` | *'x'*, *'y'*, *'z'* |

For standard HALCON calibration plates, further calibration plate specific
information is added to the model, which is not accessible with
`get_calib_data` but can be obtained directly from the corresponding
calibration plate description files instead (for details about the
description files see [`create_caltab`](create_caltab.md) for a calibration plate with
hexagonally arranged marks and [`gen_caltab`](gen_caltab.md) for a calibration plate
with rectangularly arranged marks).

- [`find_calib_object`](find_calib_object.md) (for standard HALCON calibration plates):

  |  |  |
  | --- | --- |
  | Data added to the model | accessible with |
  | **Observed image coordinates** of the calibration marks | [`get_calib_data_observ_points`](get_calib_data_observ_points.md) |
  | **Observed contours** of the calibration marks | [`get_calib_data_observ_contours`](get_calib_data_observ_contours.md) |
  | **Observed poses** of the calibration plate relative to the camera coordinate system | [`get_calib_data_observ_pose`](get_calib_data_observ_pose.md) or [`get_calib_data_observ_points`](get_calib_data_observ_points.md) |
- [`set_calib_data_observ_points`](set_calib_data_observ_points.md) (for other calibration objects than the HALCON calibration plates):

  |  |  |
  | --- | --- |
  | Data added to the model | accessible with |
  | **Observed image coordinates** of the calibration marks | [`get_calib_data_observ_points`](get_calib_data_observ_points.md) |
- [`set_calib_data`](set_calib_data.md):

  |  |  |  |  |
  | --- | --- | --- | --- |
  | Data added to the model | *`ItemType`* | *`ItemIdx`* | *`DataName`* |
  | **Reference camera** | *'model'* | *'general'* | *'reference_camera'* |
  | **Internal and external camera parameters** to calibrate | *'camera'* | *'general'* or `CameraIdx` | *'calib_settings'* |
  | **Internal and external camera parameters** to be excluded from the calibration | *'camera'* | *'general'* or `CameraIdx` | *'excluded_settings'* |
  | For stereo setups with telecentric line scan cameras: Do the cameras have a **common motion vector**? | *'model'* | *'general'* | *'common_motion_vector'* |
  | **Calibration object pose settings** to be optimized | *'calib_obj_pose'* | *'general'* or `[CalibObjIdx, CalibObjPoseIdx]` | *'calib_settings'* |
  | **Calibration object pose settings** to be excluded from the calibration | *'calib_obj_pose'* | *'general'* or `[CalibObjIdx, CalibObjPoseIdx]` | *'excluded_settings'* |
- [`calibrate_cameras`](calibrate_cameras.md):

  |  |  |  |  |
  | --- | --- | --- | --- |
  | Data added to the model | *`ItemType`* | *`ItemIdx`* | *`DataName`* |
  | **Camera setup model** (needed for multi-view stereo reconstruction) | *'model'* | *'general'* | *'camera_setup_model'* |
  | **Optimized internal camera parameters** | *'camera'* | `CameraIdx` | *'params'* |
  | **Standard deviations** of the optimized internal camera parameters | *'camera'* | `CameraIdx` | *'params_deviations'* |
  | **Covariance matrices** of the optimized internal camera parameters | *'camera'* | `CameraIdx` | *'params_covariances'* |
  | **Labels for the internal camera parameters** | *'camera'* | `CameraIdx` | *'params_labels'* |
  | **Initial external camera parameters** (camera poses) | *'camera'* | `CameraIdx` | *'init_pose'* |
  | **Optimized external camera parameters** (camera poses) | *'camera'* | `CameraIdx` | *'pose'* |
  | **Labels for the external camera parameters** (camera poses) | *'camera'* | `CameraIdx` | *'pose_labels'* |
  | **Initial calibration object poses** | *'calib_obj_pose'* | `[CalibObjIdx, CalibObjPoseIdx]` | *'init_pose'* |
  | **Optimized calibration object poses** | *'calib_obj_pose'* | `[CalibObjIdx, CalibObjPoseIdx]` | *'pose'* |
  | **Labels for the calibration object pose parameters** | *'calib_obj_pose'* | `[CalibObjIdx, CalibObjPoseIdx]` | *'pose_labels'* |

### Content of Calibration Data Model When Performing Hand-Eye Calibration

For each operator that extends the calibration model when performing
hand-eye calibration, a table is provided to give an overview on the
respective data:

- [`create_calib_data`](create_calib_data.md):

  See the section **'Content of Calibration Data Model When Calibrating Cameras'**.
- [`set_calib_data`](set_calib_data.md):

  |  |  |  |  |
  | --- | --- | --- | --- |
  | Data added to the model | *`ItemType`* | *`ItemIdx`* | *`DataName`* |
  | **Optimization method** | *'model'* | *'general'* | *'optimization_method'* |
  | **Poses of the robot tool in robot base coordinates** | *'tool'* | `CalibObjPoseIdx` | *'tool_in_base_pose'* |
- [`set_calib_data_observ_pose`](set_calib_data_observ_pose.md) (observations obtained by 3D sensors):

  |  |  |
  | --- | --- |
  | Data added to the model | accessible with |
  | **Observed calibration object poses** | [`get_calib_data_observ_pose`](get_calib_data_observ_pose.md) |
- [`set_calib_data_cam_param`](set_calib_data_cam_param.md),
  [`set_calib_data_calib_object`](set_calib_data_calib_object.md), and
  [`find_calib_object`](find_calib_object.md) or [`set_calib_data_observ_points`](set_calib_data_observ_points.md)
  (observations obtained by cameras):

  See the section `'Content of Calibration Data Model When Calibrating Cameras'`.
- [`calibrate_hand_eye`](calibrate_hand_eye.md):

  Moving camera scenario:

  |  |  |  |  |
  | --- | --- | --- | --- |
  | Data added to the model | *`ItemType`* | *`ItemIdx`* | *`DataName`* |
  | **Pose of robot tool** in camera coordinate system | *'camera'* | *0* | *'tool_in_cam_pose'* |
  | **Pose of calibration object** in robot base coordinate system | *'calib_obj'* | *0* | *'obj_in_base_pose'* |
  | **Standard deviations** of the Pose of the robot tool in camera coordinate system | *'camera'* | *0* | *'tool_in_cam_pose_deviations'* |
  | **Covariance matrices** of the Pose of the robot tool in camera coordinate system | *'camera'* | *0* | *'tool_in_cam_pose_covariances'* |
  | **Standard deviations** of the Pose of the calibration object in robot base coordinate system | *'calib_obj'* | *0* | *'obj_in_base_pose_deviations'* |
  | **Covariance matrices** of the Pose of the calibration object in robot base coordinate system | *'calib_obj'* | *0* | *'obj_in_base_pose_covariances'* |

  Stationary camera scenario:

  |  |  |  |  |
  | --- | --- | --- | --- |
  | Data added to the model | *`ItemType`* | *`ItemIdx`* | *`DataName`* |
  | **Pose of robot base** in camera coordinate system | *'camera'* | *0* | *'base_in_cam_pose'* |
  | **Pose of calibration object** in robot tool coordinate system | *'calib_obj'* | *0* | *'obj_in_tool_pose'* |
  | **Standard deviations** of the Pose of the robot base in camera coordinate system | *'camera'* | *0* | *'base_in_cam_pose_deviations'* |
  | **Covariance matrices** of the Pose of the robot base in camera coordinate system | *'camera'* | *0* | *'base_in_cam_pose_covariances'* |
  | **Standard deviations** of the Pose of the calibration object in robot tool coordinate system | *'calib_obj'* | *0* | *'obj_in_tool_pose_deviations'* |
  | **Covariance matrices** of the Pose of the calibration object in robot tool coordinate system | *'calib_obj'* | *0* | *'obj_in_tool_covariances'* |

  Both hand-eye scenarios:

  |  |  |  |  |
  | --- | --- | --- | --- |
  | Data added to the model | *`ItemType`* | *`ItemIdx`* | *`DataName`* |
  | **Calibrated poses of the calibration object** in camera coordinate system (not available for SCARA robots) | *'calib_obj_pose'* | *[0, CalibObjPoseIdx]* | *'pose'* |
  | **Root mean square error (RMSE)** of the back projection after the optimization of the camera system | *'model'* | *'general'* | *'camera_calib_error'* |
  | **Pose error of the complete chain of transformations** | *'model'* | *'general'* | *'hand_eye_calib_error'* |
  | **Camera setup model** (needed for multi-view stereo reconstruction) | *'model'* | *'general'* | *'camera_setup_model'* |

  Both hand-eye scenarios, if *'optimization_method'* is set to *'stochastic'*:

  |  |  |  |  |
  | --- | --- | --- | --- |
  | Data added to the model | *`ItemType`* | *`ItemIdx`* | *`DataName`* |
  | **Root mean square error (RMSE)** of the back projection into camera images, via pose chain using corrected tool poses | *'model'* | *'general'* | *'camera_calib_error_corrected_tool'* |
  | **Pose error of the complete chain of transformations** using corrected tool poses | *'model'* | *'general'* | *'hand_eye_calib_error_corrected_tool'* |
  | **Standard deviations** of the input poses of the robot tool in robot base coordinates | *'tool'* | *'general'* | *'tool_translation_deviation'*, *'tool_rotation_deviation'* |
  | **Corrected poses of the robot tool in robot base coordinates** | *'tool'* | `CalibObjPoseIdx` | *'tool_in_base_pose_corrected'* |

  The following sections describe the parameters for the specific categories of
  data in more detail.

### Model-Related Data

- ***`ItemType`*=*'model'*:** —

  *`ItemIdx`* must be set to *'general'*.

  Depending on the selection
  in *`DataName`*, the following model-related data is then
  returned in *`DataValue`*:

  - ***'type'*:** —

    Type of the calibration data model. Currently, the five types
    *'calibration_object'*,
    *'hand_eye_stationary_cam'*,
    *'hand_eye_moving_cam'*,
    *'hand_eye_scara_stationary_cam'*, and
    *'hand_eye_scara_moving_cam'* are supported.
  - ***'reference_camera'*:** —

    Index of the reference camera for the calibration model. All
    poses stored in the calibration data model are specified in the
    coordinate system of this reference camera.
  - ***'num_cameras'*:** —

    Number of cameras in the calibration data model (see
    [`create_calib_data`](create_calib_data.md)).
  - ***'num_calib_objs'*:** —

    Number of calibration objects in the calibration data model (see
    [`create_calib_data`](create_calib_data.md)).
  - ***'common_motion_vector'*:** —

    For stereo setups with telecentric line scan cameras, a string
    with a Boolean value (i.e., *'true'* or *'false'*)
    that determines whether the cameras have a common motion vector.
  - ***'camera_setup_model'*:** —

    A handle to a camera setup model containing the poses and the
    internal parameters for the calibrated cameras from the current
    calibration setup.
  - ***'camera_calib_error'*:** —

    The root mean square error (RMSE) of the back projection of the
    optimization of the camera system. Typically, this error is
    queried after a hand-eye calibration
    ([`calibrate_hand_eye`](calibrate_hand_eye.md)) was performed, where internally the
    camera system is calibrated without returning the error of the
    camera calibration. The returned error is identical to the error
    returned by [`calibrate_cameras`](calibrate_cameras.md), except for
    *'optimization_method'* set to *'stochastic'*, which
    refines hand-eye poses and camera parameters simultaneously for
    articulated robots.
  - ***'hand_eye_calib_error'*:** —

    After a successful hand-eye calibration, the pose error of the
    complete chain of transformations is returned. To be more
    precise, a tuple with four elements is returned, where the first
    element is the root-mean-square error of the translational part,
    the second element is the root-mean-square error of the
    rotational part, the third element is the maximum translational
    error and the fourth element is the maximum rotational
    error. The returned errors are identical to the errors returned
    by [`calibrate_hand_eye`](calibrate_hand_eye.md).
  - ***'optimization_method'*:** —

    Optimization method that was set for the hand-eye calibration
    (see [`set_calib_data`](set_calib_data.md)).
  - ***'camera_calib_error_corrected_tool'*:** —

    The root mean square error (RMSE) of the back projection of
    the calibration mark centers into camera images, via the pose chain
    using corrected tool poses. By contrast,
    *'camera_calib_error'* uses the direct back projection
    of *'calib_obj_pose'*. This parameter is only available
    if *'optimization_method'* is set to *'stochastic'*.
  - ***'hand_eye_calib_error_corrected_tool'*:** —

    After a successful hand_eye calibration, the pose error of the
    complete chain of transformations using corrected tool poses
    is returned. By contrast, *'hand_eye_calib_error'*
    uses the input tool poses. This parameter is only available
    if *'optimization_method'* is set to *'stochastic'*.

  The parameters *'reference_camera'*,
  *'common_motion_vector'*, and *'optimization_method'*
  can be set with [`set_calib_data`](set_calib_data.md). The other parameters are set
  during the model creation or are a result of the calibration process
  and cannot be modified.

### Camera-Related Data

- ***`ItemType`*=*'camera'*:** —

  *`ItemIdx`* determines, if data is queried for all cameras in
  general or for a specific camera. With *`ItemIdx`*=*'general'*,
  the default value of a parameter for all cameras is returned. In contrast,
  if you pass a valid camera index instead, i.e., a number between 0 and
  `NumCameras`-1 (`NumCameras` is specified during model
  creation with [`create_calib_data`](create_calib_data.md)), only the parameter value of the
  specified camera is returned.

  By selecting the following parameters in *`DataName`*, you can
  query which camera parameters are (or have been) optimized during
  the calibration performed by [`calibrate_cameras`](calibrate_cameras.md):

  - ***'calib_settings'*:** —

    List of the camera parameters that are marked for calibration.
  - ***'excluded_settings'*:** —

    List of camera parameters that are excluded from the
    calibration.

  These parameters can be modified by a corresponding call to
  [`set_calib_data`](set_calib_data.md).

  The following parameters can only be queried for a specific camera,
  i.e., you must pass a valid camera index in *`ItemIdx`*:

  - ***'type'*:** —

    The camera type that was set with [`set_calib_data_cam_param`](set_calib_data_cam_param.md).
  - ***'init_params'*:** —

    Initial internal camera parameters (set with
    [`set_calib_data_cam_param`](set_calib_data_cam_param.md)).
  - ***'params'*:** —

    Optimized internal camera parameters.
  - ***'params_deviations'*:** —

    Standard deviations of the optimized camera parameters, as
    estimated at the end of the camera calibration. Note that if the
    tuple returned for *'params'* contains $n$
    elements, the tuple returned for *'params_deviations'*
    contains $(n-1)$ elements since the camera parameter
    tuple contains the camera type in the first element of the
    tuple, whereas the tuple returned for
    *'params_deviations'* does not contain the camera type.
  - ***'params_covariances'*:** —

    Covariance matrix of the optimized camera parameters, as
    estimated at the end of the camera calibration. Note that if
    the tuple returned for *'params'* contains $n$
    elements, the tuple returned for *'params_covariances'*
    contains $(n-1)\times(n-1)$ elements since
    the camera parameter tuple contains the camera type in the first
    element of the tuple, whereas the tuple returned for
    *'params_covariances'* does not contain the camera type.
  - ***'params_labels'*:** —

    A convenience list of labels for the entries returned by
    *'params'*. This list is camera-type specific. Note that
    this list contains the label *'camera_type'* in its first
    position. If the first element of the tuple is removed, the
    list refers to the labels of *'params_deviations'* and
    the labels of the rows and columns of
    *'params_covariances'*.
  - ***'init_pose'*:** —

    Initial camera pose, relative to the current reference
    camera. It is computed internally based on observation poses
    during the calibration process (see [Calibration](toc_calibration.md)).
  - ***'pose'*:** —

    Optimized camera pose, relative to the current reference camera.
    If one single telecentric camera is calibrated, the translation
    along the z-axis is set to the value 0.0. If more than one
    telecentric camera is calibrated, the camera poses are moved in
    direction of their z-axis until they all lie on a sphere
    centered at the first observed calibration plate. The radius of
    the sphere corresponds to the longest distance of a camera to
    the first observed calibration plate. If this calculated
    distance is smaller than 1 m, the radius is set to 1 m.
  - ***'pose_labels'*:** —

    A convenience list of labels for the entries returned by
    *'pose'*.

  The calibrated camera parameters (*'params'* and
  *'pose'*) can be queried only after a successful execution of
  [`calibrate_cameras`](calibrate_cameras.md). The initial internal camera parameters
  *'init_params'* can be queried after a successful call to
  [`set_calib_data_cam_param`](set_calib_data_cam_param.md).

### Data Related to Calibration Objects

- ***`ItemType`*=*'calib_obj'*:** —

  *`ItemIdx`* must be set to a valid calibration object index
  (number between 0 and `NumCalibObjects`-1).
  `NumCalibObjects` is specified during the model creation with
  [`create_calib_data`](create_calib_data.md).

  The following parameters can be queried with
  *`DataName`* and are returned in *`DataValue`*:

  - ***'num_marks'*:** —

    Number of calibration marks of the calibration object.
  - ***'x'*, *'y'*, *'z'*:** —

    Coordinates of the calibration marks relative to the calibration
    object coordinate system.

  These parameters can be modified with
  [`set_calib_data_calib_object`](set_calib_data_calib_object.md).

### Data Related to Calibration Object Poses

- ***`ItemType`*=*'calib_obj_pose'*:** —

  *`ItemIdx`* determines, if data is queried for all
  calibration object poses in general or for a specific calibration object
  pose. With *`ItemIdx`*=*'general'*, the default value of a
  parameter for all calibration object poses is returned. In contrast, if
  you pass a valid calibration object index instead, i.e., a tuple
  containing a valid index pair `[CalibObjIdx, CalibObjPoseIdx]`,
  only the parameter value of the specified calibration object pose is
  returned.

  By selecting the following parameters in *`DataName`*, you can
  query which calibration object pose parameters are (or have been)
  optimized during the calibration performed by
  [`calibrate_cameras`](calibrate_cameras.md):

  - ***'calib_settings'*:** —

    List of calibration object pose parameters marked for
    calibration.
  - ***'excluded_settings'*:** —

    List of calibration object pose parameters excluded from
    calibration.

  These parameters can be set with [`set_calib_data`](set_calib_data.md).

  The following parameters can only be queried for a specific
  calibration object pose, i.e., you must pass a valid index pair
  `[CalibObjIdx, CalibObjPoseIdx]` in *`ItemIdx`*:

  - ***'init_pose'*:** —

    Initial calibration object pose. It is computed internally based
    on observation poses during the calibration process (see
    [Calibration](toc_calibration.md)). This pose is relative to the current
    reference camera.
  - ***'pose'*:** —

    Optimized calibration object pose, relative to current reference
    camera.
  - ***'pose_labels'*:** —

    A convenience list of labels for the entries returned by
    *'pose'*.

  These parameters cannot be explicitly modified and can only be
  queried after [`calibrate_cameras`](calibrate_cameras.md) was executed.

### Hand-Eye Calibration Related Data

- ***`ItemType`*=*'tool'*:** —

  The following parameters can be queried with
  *`DataName`* and are returned in *`DataValue`*:

  - ***'tool_in_base_pose'*:** —

    Pose of the robot tool in robot base coordinates with Index
    *`ItemIdx`*. These poses were previously set using
    [`set_calib_data`](set_calib_data.md) and served as input for
    the hand-eye calibration algorithm.
  - ***'tool_in_base_pose_corrected'*:** —

    Corrected pose of the robot tool in robot base coordinates of the
    input *'tool_in_base_pose'* with Index *`ItemIdx`*.
    This parameter is only available if *'optimization_method'*
    is set to *'stochastic'* and after [`calibrate_hand_eye`](calibrate_hand_eye.md) was executed.
  - ***'tool_translation_deviation'*, *'tool_rotation_deviation'*:** —

    Standard deviations of the input poses of the robot tool in robot base
    coordinates. *`ItemIdx`* has to be set to *'general'*.
    This parameter is only available if *'optimization_method'*
    is set to *'stochastic'* and after [`calibrate_hand_eye`](calibrate_hand_eye.md) was executed.

After performing a successful hand-eye calibration using
[`calibrate_hand_eye`](calibrate_hand_eye.md), the following poses can be queried for a
calibration data model of type:

- ***'hand_eye_moving_cam'*,
  *'hand_eye_scara_moving_cam'*:** —

  For *`ItemType`*=*'camera'* and
  *`DataName`*=*'tool_in_cam_pose'*, the pose of the
  robot tool in the camera coordinate system is returned in
  *`DataValue`*. For *`ItemType`*=*'calib_obj'*
  and *`DataName`*=*'obj_in_base_pose'*, the pose of
  the calibration object in the robot base coordinate system is
  returned in *`DataValue`*.

  Note that when calibrating SCARA robots, it is not possible to
  determine the Z translation of *'obj_in_base_pose'*.
  To eliminate this ambiguity the Z translation
  *'obj_in_base_pose'* is internally set to 0.0 and the
  *'tool_in_cam_pose'* is calculated accordingly. It is
  necessary to determine the true translation in Z after the
  calibration (see [`calibrate_hand_eye`](calibrate_hand_eye.md)).

  The standard deviations and the covariance matrices of the 6
  pose parameters of both poses can be queried with
  *'tool_in_cam_pose_deviations'*,
  *'tool_in_cam_pose_covariances'* (*`ItemType`*=*'camera'*),
  *'obj_in_base_pose_deviations'*, and
  *'obj_in_base_pose_covariances'* (*`ItemType`*=*'calib_obj'*). Like poses, they are
  specified in the units [m] and [°].
- ***'hand_eye_stationary_cam'*,
  *'hand_eye_scara_stationary_cam'*:** —

  For *`ItemType`*=*'camera'* and
  *`DataName`*=*'base_in_cam_pose'*, the pose of the
  robot base in the camera coordinate system is returned in
  *`DataValue`*. For
  *`ItemType`*=*'calib_obj'* and
  *`DataName`*=*'obj_in_tool_pose'*, the pose of the
  calibration object in the robot tool coordinate system is returned
  in *`DataValue`*.

  Note that when calibrating SCARA robots, it is not possible to
  determine the Z translation of *'obj_in_tool_pose'*. To
  eliminate this ambiguity the Z translation of
  *'obj_in_tool_pose'* is internally set to 0.0 and the
  *'base_in_cam_pose'* is calculated accordingly. It is
  necessary to determine the true translation in Z after the
  calibration (see [`calibrate_hand_eye`](calibrate_hand_eye.md)).

  The standard deviations and the covariance matrices of the 6
  pose parameters of both poses can be queried with
  *'base_in_cam_pose_deviations'*,
  *'base_in_cam_pose_covariances'* (*`ItemType`*=*'camera'*),
  *'obj_in_tool_pose_deviations'*, and
  *'obj_in_tool_pose_covariances'* (*`ItemType`*=*'calib_obj'*). Like poses, they are
  specified in the units [m] and [°].

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`CalibDataID`** (input_control)  calib_data `→`  (handle)

Handle of a calibration data model.

**`ItemType`** (input_control)  string `→`  (string)

Type of calibration data item.

Default:
'camera'

List of values:
'calib_obj', 'calib_obj_pose', 'camera', 'model', 'tool'

**`ItemIdx`** (input_control)  integer(-array) `→`  (integer / string)

Index of the affected item (depending on the
selected *`ItemType`*).

Default:
0

Suggested values:
0, 1, 2, 'general'

**`DataName`** (input_control)  attribute.name(-array) `→`  (string)

The name of the inspected data.

Default:
'params'

List of values:
'base_in_cam_pose', 'base_in_cam_pose_covariances', 'base_in_cam_pose_deviations', 'calib_settings', 'camera_calib_error', 'camera_calib_error_corrected_tool', 'camera_setup_model', 'common_motion_vector', 'excluded_settings', 'hand_eye_calib_error', 'hand_eye_calib_error_corrected_tool', 'init_params', 'init_pose', 'num_calib_objs', 'num_cameras', 'num_marks', 'obj_in_base_pose', 'obj_in_base_pose_covariances', 'obj_in_base_pose_deviations', 'obj_in_tool_pose', 'obj_in_tool_pose_covariances', 'obj_in_tool_pose_deviations', 'optimization_method', 'params', 'params_covariances', 'params_deviations', 'params_labels', 'pose', 'pose_labels', 'reference_camera', 'tool_in_base_pose', 'tool_in_base_pose_corrected', 'tool_in_cam_pose', 'tool_in_cam_pose_covariances', 'tool_in_cam_pose_deviations', 'tool_rotation_deviation', 'tool_translation_deviation', 'type', 'x', 'y', 'z'

**`DataValue`** (output_control)  attribute.value(-array) `→`  (real / integer / string)

Requested data.

## Example (HDevelop)

```
* Get the camera type of camera 0.
get_calib_data (CalibDataID, 'camera', 0, 'type', CameraType)

* Get the optimized (calibrated) pose of pose 1 of the
* calibration object 2.
get_calib_data (CalibDataID, 'calib_obj_pose', [2,1], 'pose', CalobjPose)
```

## Possible Predecessors

`calibrate_cameras`,
`calibrate_hand_eye`,
`create_calib_data`,
`read_calib_data`

## Module

Calibration
