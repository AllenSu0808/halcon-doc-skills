# calibrate_hand_eye (Operator)

## Name

`calibrate_hand_eye` — Perform a hand-eye calibration.

## Signature

`def calibrate_hand_eye(calib_data_id: HHandle) -> Sequence[float]`

## Description

The operator `calibrate_hand_eye` determines the 3D pose of a robot
(“hand”) relative to a camera or 3D sensor (“eye”) based on the
calibration data model *`calib_data_id`*. With the determined 3D poses,
the poses of the calibration object in the camera coordinate system can be
transformed into the coordinate system of the robot which can then, e.g.,
grasp an inspected part. There are two possible configurations of
robot-camera (hand-eye) systems:
The camera can be mounted on the robot or be stationary and observe the
robot. Note that the term robot is used in place of a mechanism that moves
objects. Thus, you can use `calibrate_hand_eye` to calibrate many
different systems, from pan-tilt heads to multi-axis manipulators.

In essence, systems suitable for hand-eye calibration are described by a
closed chain of four Euclidean transformations. In this chain two
non-consecutive transformations are either known from the robot controller
or computed from camera data, e.g., calibration object poses observed by
a camera. The two unknown constant transformations are computed by the
hand-eye calibration procedure.

A hand-eye calibration is performed similarly to the calibration of the
external camera parameters (see [Calibration](toc_calibration.md)): You
acquire a set of poses of a calibration object in the camera coordinate
system, and a corresponding set of poses of the tool in robot base
coordinates and set them in the calibration data model *`calib_data_id`*.

In contrast to the camera calibration, the calibration object is not moved
manually. This task is delegated to the robot. Basically, two hand-eye
calibration scenarios can be distinguished. A robot either moves the camera
(moving camera) or it moves the calibration object (stationary camera).
The robot's movements are assumed to be known. They are used
as an input for the hand-eye calibration and are set in the calibration
data model *`calib_data_id`* using [`set_calib_data`](set_calib_data.md).

The results of a hand-eye calibration are two poses: For the
moving camera scenario, the 3D pose of the tool in the camera
coordinate system (*"tool_in_cam_pose"*) and the 3D pose of the
calibration object in the robot base coordinate system
(*"obj_in_base_pose"*) are computed. For the stationary camera
scenario, the 3D pose of the robot base in the camera coordinate system
(*"base_in_cam_pose"*) and the 3D pose of the calibration object
in the tool coordinate system (*"obj_in_tool_pose"*) are computed.
Their pose type is identical to the pose type of the input poses. If the
input poses have different pose types, poses of type 0 are returned.

The two hand-eye calibration scenarios are discussed in more detail below,
followed by general information about the data for and the preparation of
the calibration data model.

### Moving camera (mounted on a robot)

In this configuration, the calibration object remains stationary. The
camera is mounted on the robot and is moved to different positions by
the robot. The main idea behind the hand-eye calibration is that the
information extracted from an observation of the calibration object,
i.e., the pose of the calibration object relative to the camera,
can be seen as a chain of poses or homogeneous transformation matrices from
the calibration object via the base of the robot to its tool (end-effector)
and finally to the camera:

Moving camera: camera_H_cal = camera_H_tool * (base_H_tool)^(-1) * base_H_cal
| | | |
'obj_in_cam_pose' 'tool_in_cam_pose' 'tool_in_base_pose' 'obj_in_base_pose'

From the set of calibration object poses (*"obj_in_cam_pose"*) and
the poses of the tool in the robot base coordinate system
(*"tool_in_base_pose"*), the operator `calibrate_hand_eye`
determines the two missing transformations at the ends of the chain, i.e.,
the pose of the robot tool in the camera coordinate system
(![figure](../assets/2d0f630af62efd3c.svg),
*"tool_in_cam_pose"*) and the pose of the calibration object in
the robot base coordinate system
($\text{base} H_{\text{cal}}$ ![figure](../assets/b3b3145d09179bb6.svg), *"obj_in_base_pose"*).
These two poses are constant.

In contrast, the transformation in the middle of the chain,
$base H tool$ ![figure](../assets/8cfc6599aff0f07e.svg), is known but changes
for each observation of the calibration object, because it describes
the pose of the tool with respect to the robot base coordinate system.
In the equation the inverted transformation matrix is used. The inversion
is performed internally.

Note that when calibrating SCARA robots, it is not possible to determine
the Z translation of *"obj_in_base_pose"*. To eliminate this
ambiguity the Z translation *"obj_in_base_pose"* is internally
set to 0.0 and the *"tool_in_cam_pose"* is calculated accordingly.
It is necessary to determine the true translation in Z after the
calibration by moving the robot to a pose of
known height in the camera coordinate system. For this, the following
approach can be applied: The calibration plate is placed at an arbitrary
position. The robot is then moved such that the camera can observe the
calibration plate. Now, an image of the calibration plate is acquired and
the current robot pose is queried (*ToolInBasePose1*). From the
image, the pose of the calibration plate in the camera coordinate system can
be determined (*ObjInCamPose1*). Afterwards, the tool of the robot
is manually moved to the origin of the calibration plate and the robot
pose is queried again (*ToolInBasePose2*). These three poses and
the result of the calibration (*ToolInCamPose*) can be used to fix
the Z ambiguity by using the following lines of code:

|  |
| --- |
| [`pose_invert(ToolInCamPose, CamInToolPose)`](pose_invert.md) |
| [`pose_compose(CamInToolPose, ObjInCamPose1, ObjInToolPose1)`](pose_compose.md) |
| [`pose_invert(ToolInBasePose1, BaseInToolPose1)`](pose_invert.md) |
| [`pose_compose(BaseInToolPose1, ToolInBasePose2, Tool2InTool1Pose)`](pose_compose.md) |
| `ZCorrection := ObjInToolPose1[2]-Tool2InTool1Pose[2]` |
| [`set_origin_pose(ToolInCamPose, 0, 0, ZCorrection, ToolInCamPoseFinal)`](set_origin_pose.md) |

The *"optimization_method"* *"stochastic"* also estimates the
uncertainty of observations. Besides the input poses described above,
it also uses the extracted calibration marks and is thus only available
for use with a camera and a calibration plate, not for use with a 3D sensor.
For articulated robots, the hand-eye poses and camera parameters are refined
simultaneously.

### Stationary camera

In this configuration, the robot grasps the calibration object and moves
it in front of the camera. Again, the information extracted from an
observation of the calibration object, i.e., the pose of the calibration
object in the camera coordinate system (e.g., the external camera
parameters), are equal to a chain of poses or homogeneous transformation
matrices, this time from the calibration object via the robot's tool to
its base and finally to the camera:

Stationary camera: camera_H_cal = camera_H_base * base_H_tool * tool_H_cal
| | | |
'obj_in_cam_pose' 'base_in_cam_pose' 'tool_in_base_pose' 'obj_in_tool_pose'

Analogously to the configuration with a moving camera, the operator
`calibrate_hand_eye` determines the two transformations at the ends
of the chain, here the pose of the robot base coordinate system in camera
coordinates ($H_{base}$ ![figure](../assets/cbc3848736101be4.svg),
*"base_in_cam_pose"*) and the pose of the calibration object
relative to the robot tool ($H_{cal}$ ![figure](../assets/c9f2354c5c71269c.svg),
*"obj_in_tool_pose"*).

The transformation in the middle of the chain,
$base H tool$ ![figure](../assets/8cfc6599aff0f07e.svg), describes the pose of
the tool relative to the robot base coordinate system. The transformation
![figure](../assets/5f39a69878f30ae7.svg) describes the pose of the
calibration object relative to the camera coordinate system.

Note that when calibrating SCARA robots, it is not possible to determine
the Z translation of *"obj_in_tool_pose"*. To eliminate this
ambiguity the Z translation of *"obj_in_tool_pose"* is internally
set to 0.0 and the *"base_in_cam_pose"* is calculated accordingly.
It is necessary to determine the true translation in Z after the
calibration by moving the robot to a pose of
known height in the camera coordinate system. For this, the following
approach can be applied: A calibration plate (that is not attached to the
robot) is placed at an arbitrary position such that it can be observed by
the camera. The pose of the calibration plate must then be determined in
the camera coordinate system (*ObjInCamPose*). Afterwards the tool
of the robot is manually moved to the origin of the calibration plate
and the robot pose is queried (*ToolInBasePose*). The two
poses and the result of the calibration (*BaseInCamPose*) can be used
to fix the Z ambiguity by using the following lines of code:

|  |
| --- |
| [`pose_invert(BaseInCamPose, CamInBasePose)`](pose_invert.md) |
| [`pose_compose(CamInBasePose, ObjInCamPose, ObjInBasePose)`](pose_compose.md) |
| `ZCorrection := ObjInBasePose[2]-ToolInBasePose[2]` |
| [`set_origin_pose(BaseInCamPose, 0, 0, ZCorrection, BaseInCamPoseFinal)`](set_origin_pose.md) |

The *"optimization_method"* *"stochastic"* also estimates the
uncertainty of observations. Besides the input poses described above,
it also uses the extracted calibration marks and is thus only available
for use with a camera and a calibration plate, not for use with a 3D sensor.
For articulated robots, the hand-eye poses and camera parameters are refined
simultaneously.

### Preparing the calibration input data

Before calling `calibrate_hand_eye`, you must create and fill the
calibration data model with the following steps:

1. **Create a calibration data model** with the operator
   [`create_calib_data`](create_calib_data.md), specifying the number of cameras in the setup
   and the number of used calibration objects. Depending on your scenario,
   `calib_setup` has to be set to *"hand_eye_moving_camera"*,
   *"hand_eye_stationary_camera"*,
   *"hand_eye_scara_moving_camera"*, or
   *"hand_eye_scara_stationary_camera"*. These four scenarios on the
   one hand distinguish whether the camera or the calibration object is
   moved by the robot and on the other hand distinguish whether an
   articulated robot or a SCARA robot is calibrated. The arm of an
   articulated robot has three rotary joints typically covering 6 degrees
   of freedom (3 translations and 3 rotations). SCARA robots have two
   parallel rotary joints and one parallel prismatic joint covering only
   4 degrees of freedom (3 translations and 1 rotation). Loosely speaking,
   an articulated robot is able to tilt its end effector while a SCARA robot
   is not.
2. **Specify the optimization method** with the operator
   [`set_calib_data`](set_calib_data.md). For the parameter
   `data_name`=*"optimization_method"*, three options for
   `data_value` are available, `data_value`=*"linear"*,
   `data_value`=*"nonlinear"*
   and `data_value`=*"stochastic"*
   (see paragraph 'Performing the actual hand-eye calibration').
3. **Specify the poses of the calibration object**

   1. For each observation of the calibration object,
      the 3D pose can be set directly using the operator
      [`set_calib_data_observ_pose`](set_calib_data_observ_pose.md). This operator is
      intended to be used with generic 3D sensors that observe the
      calibration object.
   2. The pose of the calibration object can also be estimated using
      camera images. The calibration object has to be set in the
      calibration data model *`calib_data_id`* with the operator
      [`set_calib_data_calib_object`](set_calib_data_calib_object.md). Initial camera parameters have
      to be set with the operator [`set_calib_data_cam_param`](set_calib_data_cam_param.md).
      If a standard HALCON calibration plate is used, the operator
      [`find_calib_object`](find_calib_object.md) determines the pose of the
      calibration plate relative to the camera and saves it in the
      calibration data model *`calib_data_id`*.

      The operator `calibrate_hand_eye` for articulated (i.e.,
      non-SCARA) robots in this case calibrates the camera
      before performing the hand-eye calibration.
      If *"optimization_method"* is set to *"stochastic"*,
      the hand-eye poses and camera parameters are then refined simultaneously.
      If the provided
      camera parameters are already calibrated, the camera calibration
      can be switched off by calling
      `set_calib_data(CalibDataID,'camera','general','excluded_settings','params')`.

      In contrast, for SCARA robots `calibrate_hand_eye` always
      assumes that the provided camera parameters are already calibrated.
      Therefore, in this case the internal camera calibration
      is never performed automatically during hand-eye calibration.
      This is because the internal camera parameters cannot
      be calibrated reliably without significantly tilting the calibration
      plate with respect to the camera. For hand-eye calibration,
      the calibration plate is often approximately parallel to the
      image plane. Therefore, for SCARA robots all camera poses are
      approximately parallel. Therefore, the camera must be calibrated
      beforehand by using a different set of calibration images.
4. **Specify the poses of the tool** in robot base coordinates.
   For each pose of the calibration object in the camera coordinate system, the
   corresponding pose of the tool in the robot base coordinate system has to be
   set with the operator
   `set_calib_data(CalibDataID,'tool', PoseNumber, 'tool_in_base_pose', ToolInBasePose)`.

### Performing the actual hand-eye calibration

The operator `calibrate_hand_eye` can perform the calibration in three
different ways. In all cases, all provided calibration object poses in
camera coordinates and the corresponding poses of the tool in robot base
coordinates are used for the calibration. The method *"stochastic"*
also uses the extracted calibration marks, and is thus only available for
use with a camera and a calibration plate, not for use with a 3D sensor.
The method to be used is specified with [`set_calib_data`](set_calib_data.md).

For the parameter combination
`data_name`=*"optimization_method"* and
`data_value`=*"linear"*, the calibration is performed using a
linear algorithm which is fast but in many practical situations not accurate
enough.

For the parameter
`data_name`=*"optimization_method"* and
`data_value`=*"nonlinear"*, the calibration is performed using
a non-linear algorithm, which results in more accurately calibrated poses.

For the parameter
`data_name`=*"optimization_method"* and
`data_value`=*"stochastic"*, the calibration algorithm
models the uncertainty of all measured observations including the input robot
poses, which results in more robustly calibrated hand-eye poses. The estimation
will be better the more input poses are used. However, the method
is only available for use with a camera and a calibration plate, not for use
with a 3D sensor. For articulated robots, the hand-eye poses and camera
parameters are refined simultaneously.

### Checking the success of the calibration

The operator `calibrate_hand_eye` returns the pose error of the
complete chain of transformations in *`errors`*.
To be more precise, a tuple with four elements is returned, where the first
element is the root-mean-square error of the translational part, the second
element is the root-mean-square error of the rotational part, the third element
is the maximum translational error and the fourth element is the maximum
rotational error. Using these error measures, it can be determined,
whether the calibration was successful.

The *`errors`* are returned in the same units in which the input
poses were given, i.e., the translational errors are typically given
in meters and the rotational errors are always given in degrees.

If *"optimization_method"* is set to *"stochastic"*,
[`get_calib_data`](get_calib_data.md) can be used to obtain
*"hand_eye_calib_error_corrected_tool"*, which differs from
*`errors`* only in that it uses the corrected robot tool poses instead
of the input robot tool poses.

For articulated robots, [`get_calib_data`](get_calib_data.md) can be used to obtain
the *"camera_calib_error"* of the camera calibration,
the root mean square error (RMSE) of the direct back projection of
calibration mark centers into camera images.
If *"optimization_method"* is set to *"stochastic"*,
*"camera_calib_error_corrected_tool"* returns the back
projection error via the pose chain using corrected tool poses.

### Getting the calibration results

The poses that are computed with the operator `calibrate_hand_eye`
can be queried with [`get_calib_data`](get_calib_data.md).
For the moving camera scenario, the 3D pose of the tool in the camera
coordinate system (*"tool_in_cam_pose"*) and the 3D pose of the
calibration object in the robot base coordinate system
(*"obj_in_base_pose"*) can be obtained. For the stationary camera
scenario, the 3D pose of the robot base in the camera coordinate system
(*"base_in_cam_pose"*) and the 3D pose of the calibration object
in the coordinate system of the tool (*"obj_in_tool_pose"*) can
be obtained.

### Querying the input data

If the poses of the calibration object relative to a camera were computed
with [`find_calib_object`](find_calib_object.md), then for articulated (i.e., non-SCARA) robots
they are used in an internal camera
calibration step preceding the hand-eye calibration and are calibrated
as well. For *"optimization_method"* set to *"stochastic"*,
the hand-eye poses and camera parameters are refined simultaneously,
the poses of the calibration object are then updated relative to the
resulting new camera parameters.
The calibrated 3D poses can be queried using [`get_calib_data`](get_calib_data.md)
with the parameter `item_type`=*"calib_obj_pose"*.

If the poses
of the calibration object were observed with a generic 3D sensor, they cannot
be calibrated and are set by [`set_calib_data_observ_pose`](set_calib_data_observ_pose.md). These raw
3D poses can be queried using [`get_calib_data_observ_pose`](get_calib_data_observ_pose.md).

The corresponding 3D poses of the tool in the coordinate system of the robot
base can be queried using [`get_calib_data`](get_calib_data.md).

### Acquiring a suitable set of observations

The following conditions, especially if using a standard calibration plate,
should be considered:

- The position of the calibration object (moving camera: relative to the
  robot's base; stationary camera: relative to the robot's tool) and
  the position of the camera (moving camera: relative to the
  robot's tool; stationary camera: relative to the robot's base)
  must not be changed between the calibration poses.
- Even though a lower limit of three calibration object poses is
  theoretically possible, it is recommended to acquire 10 or
  more poses, in which the pose of the camera or the
  robot hand are sufficiently different. If *"optimization_method"*
  is set to *"stochastic"*, at least 25 poses
  are recommended. The estimation will be better the more poses are used.

  For articulated (i.e., non-SCARA) robots the amount of rotation between
  the calibration object poses is essential and should be at least 30
  degrees or better 60 degrees.
  The rotations between the poses must exhibit at least two different
  axes of rotation. Very different orientations lead to more precise
  results of the hand-eye calibration. For SCARA robots there is only one
  axis of rotation. The amount of rotation between the images should also
  be large.
- For cameras, the internal camera parameters
  must be constant during and after the calibration.
  Note that changes of the image size, the focal length, the aperture,
  or the focus cause a change of the internal camera parameters.
- As mentioned, the camera must not be modified between the acquisition
  of the individual images. Please make sure that the focus is sufficient
  for the expected changes of the camera to calibration plate distance.
  Therefore, bright lighting conditions for the calibration plate are
  important, because then you can use smaller apertures, which result in
  a larger depth of focus.

### Obtaining the poses of the robot tool

We recommend to create the robot poses in a separate program and save them
in files using [`write_pose`](write_pose.md). In the calibration program you can then
import them and set them in the calibration data model *`calib_data_id`*.

Via the Cartesian interface of the robot, you can typically obtain the pose
of the tool in robot base coordinates in a notation that corresponds to the
pose representations with the codes 0 or 2 (`order_of_rotation` =
*"gba"* or *"abg"*, see [`create_pose`](create_pose.md)). In this case,
you can directly use the pose values obtained from the robot as input for
[`create_pose`](create_pose.md).

If the Cartesian interface of your robot describes the orientation in a
different way, e.g., with the representation ZYZ ($\mathbf{R}_{z}(\varphi1)\cdot\mathbf{R}_{y}(\varphi2)\cdot\mathbf{R}_{z}(\varphi3)$), you can create the
corresponding homogeneous transformation matrix step by step using the
operators [`hom_mat3d_rotate`](hom_mat3d_rotate.md) and [`hom_mat3d_translate`](hom_mat3d_translate.md) and then
convert the resulting matrix into a pose using [`hom_mat3d_to_pose`](hom_mat3d_to_pose.md).
The following example code creates a pose from the ZYZ representation
described above:

|  |
| --- |
| [`hom_mat3d_identity(HomMat3DIdent)`](hom_mat3d_identity.md) |
| [`hom_mat3d_rotate(HomMat3DIdent, phi3, "z", 0, 0, 0, HomMat3DRotZ)`](hom_mat3d_rotate.md) |
| [`hom_mat3d_rotate(HomMat3DRotZ, phi2, "y", 0, 0, 0, HomMat3DRotZY)`](hom_mat3d_rotate.md) |
| [`hom_mat3d_rotate(HomMat3DRotZY, phi1, "z", 0, 0, 0, HomMat3DRotZYZ)`](hom_mat3d_rotate.md) |
| [`hom_mat3d_translate(HomMat3DRotZYZ, Tx, Ty, Tz, base_H_tool)`](hom_mat3d_translate.md) |
| [`hom_mat3d_to_pose(base_H_tool, RobPose)`](hom_mat3d_to_pose.md) |

Please note that the hand-eye calibration only works if the poses of the
tool in robot base coordinates are specified with high accuracy. Of the
provided methods, *"optimization_method"* set to *"stochastic"*
will yield the most robust results with respect to noise on the poses of the
tool in robot base coordinates. The estimation will be better the more
input poses are used.

Please note that this operator supports canceling timeouts and interrupts
if *"optimization_method"* is set to *"stochastic"*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator supports canceling timeouts and interrupts.

This operator modifies the state of the following input parameter:

- calib_data_id

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`calib_data_id`** (input_control, state is modified)  calib_data `→` HHandle

Handle of a calibration data model.

**`errors`** (output_control)  number-array `→` Sequence[float]

Average residual error of the optimization.

## Possible Predecessors

`create_calib_data`,
`set_calib_data_cam_param`,
`set_calib_data_calib_object`,
`set_calib_data_observ_pose`,
`find_calib_object`,
`set_calib_data`,
`remove_calib_data`,
`remove_calib_data_observ`

## Possible Successors

`get_calib_data`

## References

K. Daniilidis: “Hand-Eye Calibration Using Dual Quaternions”;
International Journal of Robotics Research, Vol. 18, No. 3,
pp. 286-298; 1999.
  
M. Ulrich, C. Steger: “Hand-Eye Calibration of SCARA Robots Using Dual
Quaternions”; Pattern Recognition and Image Analysis, Vol. 26, No. 1,
pp. 231-239; January 2016.
  
M. Ulrich, M. Hillemann: “Generic Hand–Eye Calibration of Uncertain
Robots”; 2021 IEEE International Conference on Robotics and
Automation (ICRA), pp. 11060-11066; 2021.

## Module

Calibration
