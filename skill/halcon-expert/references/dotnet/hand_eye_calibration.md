# HandEyeCalibration (Operator)

## Name

`HandEyeCalibration` — Perform a hand-eye calibration.

## Signature

`static void HOperatorSet.HandEyeCalibration(HTuple x, HTuple y, HTuple z, HTuple row, HTuple col, HTuple numPoints, HTuple robotPoses, HTuple cameraParam, HTuple method, HTuple qualityType, out HTuple cameraPose, out HTuple calibrationPose, out HTuple quality)`

`HPose HCamPar.HandEyeCalibration(HTuple x, HTuple y, HTuple z, HTuple row, HTuple col, HTuple numPoints, HPose[] robotPoses, string method, HTuple qualityType, out HPose calibrationPose, out HTuple quality)`

`HPose HCamPar.HandEyeCalibration(HTuple x, HTuple y, HTuple z, HTuple row, HTuple col, HTuple numPoints, HPose[] robotPoses, string method, string qualityType, out HPose calibrationPose, out double quality)`

`static HPose HPose.HandEyeCalibration(HTuple x, HTuple y, HTuple z, HTuple row, HTuple col, HTuple numPoints, HPose[] robotPoses, HCamPar cameraParam, string method, HTuple qualityType, out HPose calibrationPose, out HTuple quality)`

`static HPose HPose.HandEyeCalibration(HTuple x, HTuple y, HTuple z, HTuple row, HTuple col, HTuple numPoints, HPose[] robotPoses, HCamPar cameraParam, string method, string qualityType, out HPose calibrationPose, out double quality)`

## Description

The operator `HandEyeCalibration` determines the 3D pose of a robot
(“hand”) relative to a camera (“eye”). With this information, the
results of image processing can be transformed into the coordinate system of
the robot which can then, e.g., grasp an inspected part.
Please note that the operator `HandEyeCalibration` does not support
3D sensors. A hand-eye calibration including 3D sensors is only supported
by the operator [`CalibrateHandEye`](calibrate_hand_eye.md). That operator furthermore
provides a more user-friendly interface to the hand-eye calibration than the
operator `HandEyeCalibration`, since the reference coordinate
systems are explicitly indicated.

There are two possible configurations of robot-camera (hand-eye) systems:
The camera can be mounted on the robot or be stationary and observe the
robot. Note that the term robot is used in place for a mechanism that moves
objects. Thus, you can use `HandEyeCalibration` to calibrate many
different systems, from pan-tilt heads to multi-axis manipulators.

In essence, systems suitable for hand-eye calibration are described by a
closed chain of four Euclidean transformations. In this chain two
non-consecutive transformations are either known from the robot controller
or computed from calibration points seen by a camera system. The two other
constant transformations are computed by the hand-eye calibration procedure.

A hand-eye calibration is performed similarly to the calibration of the
external camera parameters (see [`CameraCalibration`](camera_calibration.md)): You acquire a
set of images of a calibration object, determine correspondences between
known calibration points and their projection in the images and pass them to
`HandEyeCalibration` via the parameters *`x`*, *`y`*,
*`z`*, *`row`*, *`col`*, and *`numPoints`*. If
you use the standard calibration plate, the correspondences can be determined
very easily with the operators [`FindCaltab`](find_caltab.md) and
[`FindMarksAndPose`](find_marks_and_pose.md). Furthermore, the camera is identical for
the complete calibration sequence and is specified by the internal camera
parameters in *`cameraParam`*. The internal camera parameters are
calibrated beforehand deploying the operator [`CalibrateCameras`](calibrate_cameras.md) or
[`CameraCalibration`](camera_calibration.md).

In contrast to the camera calibration, the calibration object is not moved
manually. This task is delegated to the robot, which either moves the camera
(mounted camera) or the calibration object (stationary camera). The robot's
movements are assumed to be known and therefore are also used as an input for
the calibration (parameter *`robotPoses`*).

The output of `HandEyeCalibration` are the two poses
*`cameraPose`* and *`calibrationPose`*. Their pose type is
identical to the pose type of the first input robot pose.

Basically, two hand-eye configurations can be distinguished and are
discussed in more detail below, followed by general information about the
process of hand-eye calibration.

### Moving camera (mounted on a robot)

In this configuration, the calibration object remains stationary and the
camera is moved to different positions by the robot. The main idea behind the
hand-eye calibration is that the information extracted from a calibration
image, i.e., the pose of the calibration object relative to the camera (i.e.,
the external camera parameters), can be seen as a chain of poses or
homogeneous transformation matrices, from the calibration object via the base
of the robot to its tool (end-effector) and finally to the camera:

Moving camera: cam_H_cal = cam_H_tool * tool_H_base * base_H_cal
| | |
*`cameraPose`* *`robotPoses`* *`calibrationPose`*

From the set of calibration images, the operator `HandEyeCalibration`
determines the two transformations at the ends of the chain, i.e., the pose
of the robot tool in camera coordinates
(${\\mathcal{H}}$ ![figure](../assets/6968e1ee0e568d37.svg),*`cameraPose`*) and
the pose of the calibration object in the robot base coordinate system
($\text{base} H_{\text{cal}}$ ![figure](../assets/b3b3145d09179bb6.svg),*`calibrationPose`*).

In contrast, the transformation in the middle of the chain,
$\text{tool} \mathcal{H}_{\mathrm{base}}$ ![figure](../assets/b525ea73a5e57d88.svg), is known but changes for each
calibration image, because it describes the pose of the robot moving the
camera, or to be more exact its inverse pose (pose of the base coordinate
system in robot tool coordinates). You must specify the inverse robot poses
in the calibration images in the parameter *`robotPoses`*.

Note that when calibrating SCARA robots it is not possible to
determine the Z translation of *`calibrationPose`*. To eliminate
this ambiguity the Z translation of *`calibrationPose`* is internally
set to 0.0 and the *`cameraPose`* is calculated accordingly.
It is necessary to determine the true translation in Z after
the calibration (see [`CalibrateHandEye`](calibrate_hand_eye.md)).

### Stationary camera

In this configuration, the robot grasps the calibration object and moves
it in front of the camera. Again, the information extracted from a
calibration image, i.e., the pose of the calibration object in camera
coordinates (the external camera parameters), are equal to a chain of
poses or homogeneous transformation matrices, this time from the
calibration object via the robot's tool to its base and finally to
the camera:

Stationary camera: cam_H_cal = cam_H_base * base_H_tool * tool_H_cal
| | |
*`cameraPose`* *`robotPoses`* *`calibrationPose`*

Analogously to the configuration with a moving camera, the operator
`HandEyeCalibration` determines the two transformations at the ends
of the chain, here the pose of the robot base coordinate system in camera
coordinates
($\text{cam} \mathrm{H}_{\mathrm{base}}$ ![figure](../assets/d3c9d1f0fffab79f.svg),*`cameraPose`*)
and the pose of the calibration object relative to the robot tool
($H_{cal}$ ![figure](../assets/c9f2354c5c71269c.svg),*`calibrationPose`*).

The transformation in the middle of the chain,
$base H tool$ ![figure](../assets/8cfc6599aff0f07e.svg), describes the pose of the
robot moving the calibration object, i.e., the pose of the tool relative to
the base coordinate system. You must specify the robot poses in the
calibration images in the parameter *`robotPoses`*.

Note that when calibrating SCARA robots it is not possible to
determine the Z translation of *`calibrationPose`*. To eliminate
this ambiguity the Z translation of *`calibrationPose`* is internally
set to 0.0 and the *`cameraPose`* is calculated accordingly.
It is necessary to determine the true translation in Z after
the calibration (see [`CalibrateHandEye`](calibrate_hand_eye.md)).

### Additional information about the calibration process

The following sections discuss individual questions arising from the
use of `HandEyeCalibration`. They are intended to be a guideline
for using the operator in an application, as well as to help
understanding the operator.

- **How do I get 3D calibration points and their projections?** —

  3D calibration points given in the world coordinate system (*`x`*,
  *`y`*, *`z`*) and their associated projections in the image
  (*`row`*, *`col`*) form the basis of the hand-eye calibration.
  In order to be able to perform a successful hand-eye calibration, you need
  at least three images of the 3D calibration points that were obtained under
  different poses of the manipulator. In each image at least four points must
  be available, in order to compute internally the pose transferring the
  calibration points from their world coordinate system into the camera
  coordinate system.

  In principle, you can use arbitrary known points for the calibration.
  However, it is usually most convenient to use the standard calibration plate,
  e.g., the one that can be generated with [`GenCaltab`](gen_caltab.md). In this
  case, you can use the operators [`FindCaltab`](find_caltab.md) and
  [`FindMarksAndPose`](find_marks_and_pose.md) to extract the position of the calibration plate
  and of the calibration marks and the operator [`CaltabPoints`](caltab_points.md) to read
  the 3D coordinates of the calibration marks (see also the description of
  [`CameraCalibration`](camera_calibration.md)).

  The parameter *`numPoints`* specifies the number of 3D calibration
  points used for each pose of the manipulator, i.e., for each image.
  With this, the 3D calibration points which are stored in a linearized
  fashion in *`x`*, *`y`*, *`z`*, and their corresponding
  projections (*`row`*, *`col`*) can be associated with the
  corresponding pose of the manipulator (*`robotPoses`*). Note that
  in contrast to the operator [`CameraCalibration`](camera_calibration.md) the 3D coordinates
  of the calibration points must be specified for each calibration image,
  not only once, and thus can vary for each image of the sequence.
- **How do I acquire a suitable set of images?** —

  The following conditions, especially if using a standard calibration plate,
  should be considered:

  - The position of the calibration marks (moving camera: relative to the
    robot's base; stationary camera: relative to the robot's tool) and
    the position of the camera (moving camera: relative to the
    robot's tool; stationary camera: relative to the robot's base)
    must not be changed between the images.
  - The internal camera parameters (*`cameraParam`*) must be
    constant and must be determined in a previous camera calibration step
    (see [`CameraCalibration`](camera_calibration.md)). Note that changes of the image size,
    the focal length, the aperture, or the focus cause a change of the
    internal camera parameters.
  - The theoretical lower limit of the number of image to acquire is three.
    Nevertheless, it is recommended to have 10 or more images at hand, in
    which the position of the camera or the robot hand are
    sufficiently different.

    For articulated (i.e., non-SCARA) robots the amount of rotation between
    the images is essential and should be at least 30 degrees or better
    60 degrees. The rotations between the images must exhibit at least
    two different axes of rotation. Very different orientations lead to
    precise calibration results. For SCARA robots there is only one
    axis of rotation. The amount of rotation between the images should also
    be large.
  - In each image, the calibration plate must be completely visible
    (including its border).
  - Reflections or other disturbances should not impair the detection of the
    calibration plate and its calibration marks.
  - If individual calibration marks instead of the standard
    calibration plate are used at least four marks must be present in
    each image.
  - In each image, the calibration plate should at least fill one
    quarter of the entire image for a precise computation of the
    calibration to camera transformation, which is performed internally
    during hand-eye calibration.
  - As mentioned, the camera must not be modified between the acquisition of
    the individual images. Please make sure that the focus is sufficient for
    the expected changes of the camera to calibration plate distance.
    Therefore, bright lighting conditions for the calibration plate are
    important, because then you can use smaller apertures, which result in
    a larger depth of focus.
- **How do I obtain the poses of the robot?** —

  In the parameter *`robotPoses`* you must pass the poses of the robot in
  the calibration images (moving camera: pose of the robot base in robot tool
  coordinates; stationary camera: pose of the robot tool in robot base
  coordinates) in a linearized fashion. We recommend to create the robot poses
  in a separate program and save in files using [`WritePose`](write_pose.md). In the
  calibration program you can then read and accumulate them in a tuple as shown
  in the example program below. In addition, we recommend to save the pose of
  the robot tool in robot base coordinates independent of the hand-eye
  configuration. When using a moving camera, you then invert the read poses
  before accumulating them. This is also shown in the example program.

  Via the Cartesian interface of the robot, you can typically obtain the pose
  of the tool in base coordinates in a notation that corresponds to the pose
  representations with the codes 0 or 2 (`orderOfRotation` =
  *"gba"* or *"abg"*, see [`CreatePose`](create_pose.md)). In this case, you
  can directly use the pose values obtained from the robot as input for
  [`CreatePose`](create_pose.md).

  If the Cartesian interface of your robot describes the orientation in a
  different way, e.g., with the representation ZYZ ($\mathbf{R}_{z}(\varphi1)\cdot\mathbf{R}_{y}(\varphi2)\cdot\mathbf{R}_{z}(\varphi3)$), you can create the
  corresponding homogeneous transformation matrix step by step using the
  operators [`HomMat3dRotate`](hom_mat3d_rotate.md) and [`HomMat3dTranslate`](hom_mat3d_translate.md) and then
  convert the matrix into a pose using [`HomMat3dToPose`](hom_mat3d_to_pose.md). The following
  example code creates a pose from the ZYZ representation described above:

  |  |
  | --- |
  | [`HomMat3dIdentity(HomMat3DIdent)`](hom_mat3d_identity.md) |
  | [`HomMat3dRotate(HomMat3DIdent, phi3, "z", 0, 0, 0, HomMat3DRotZ)`](hom_mat3d_rotate.md) |
  | [`HomMat3dRotate(HomMat3DRotZ, phi2, "y", 0, 0, 0, HomMat3DRotZY)`](hom_mat3d_rotate.md) |
  | [`HomMat3dRotate(HomMat3DRotZY, phi1, "z", 0, 0, 0, HomMat3DRotZYZ)`](hom_mat3d_rotate.md) |
  | [`HomMat3dTranslate(HomMat3DRotZYZ, Tx, Ty, Tz, base_H_tool)`](hom_mat3d_translate.md) |
  | [`HomMat3dToPose(base_H_tool, RobPose)`](hom_mat3d_to_pose.md) |

  Please note that the hand-eye calibration only works if the robot poses
  *`robotPoses`* are specified with high accuracy!
- **What is the order of the individual parameters?** —

  The length of the tuple *`numPoints`* corresponds to the number of
  different positions of the manipulator and thus to the number of calibration
  images. The parameter *`numPoints`* determines the number of
  calibration points used in the individual positions. If the standard
  calibration plate is used, this means 49 points per position (image).
  If, for example, 15 images were acquired, *`numPoints`* is a tuple
  of length 15, where all elements of the tuple have the value 49.

  The number of images in the sequence, which is determined by the length of
  *`numPoints`*, must also be taken into account for the tuples of
  the 3D calibration points and the extracted 2D marks, respectively. Hence,
  for 15 calibration images with 49 calibration points each, the tuples
  *`x`*, *`y`*, *`z`*, *`row`*, and *`col`* must
  contain $15\cdot49=735$ values each. These tuples
  are ordered according to the image the respective points lie in, i.e.,
  the first 49 values correspond to the 49 calibration points in the first
  image. The order of the 3D calibration points and the extracted 2D
  calibration points must be the same in each image.

  The length of the tuple *`robotPoses`* also depends on the number of
  calibration images. If, for example, 15 images and therefore 15 poses
  are used, the length of the tuple *`robotPoses`* is
  $15\cdot7=105$ (15 times 7 pose parameters).
  The first seven parameters thus determine the pose of the manipulator
  in the first image, and so on.
- **Algorithm and output parameters** —

  The parameter *`method`* determines the type of algorithm used for the
  hand-eye calibration: With *"linear"* a linear algorithm is chosen,
  which is fast but in many practical situations not accurate enough.
  *"nonlinear"* selects a non-linear algorithm, which results in
  the most accurately calibrated poses and which is the method of choice.

  For the calibration of SCARA robots the parameter *`method`* must
  be set to *"scara_linear"* or *"scara_nonlinear"*,
  respectively. While the arm of an articulated robot has three rotary
  joints typically covering 6 degrees of freedom (3 translations and 3
  rotations), SCARA robots have two parallel rotary joints and one parallel
  prismatic joint covering only 4 degrees of freedom (3 translations and 1
  rotation). Loosely speaking, an articulated robot is able to tilt its
  end effector while a SCARA robot is not.

  The parameter *`qualityType`* switches between different possibilities
  for assessing the quality of the calibration result returned in
  *`quality`*. *"error_pose"* stands for the pose error of the
  complete chain of transformations. To be more precise, a tuple with four
  elements is returned, where the first element is the root-mean-square error
  of the translational part, the second element is the root-mean-square error
  of the rotational part, the third element is the maximum translational
  error and the fourth element is the maximum rotational error.
  With *"standard_deviation"*, a tuple with 12 elements containing the
  standard deviations of the two poses is returned: The first six elements
  refer to the camera pose and the others to the pose of the calibration
  points. With *"covariance"*, the full 12x12 covariance matrix of
  both poses is returned. Like poses, the standard deviations and the
  covariances are specified in the units [m] and [°].
  Note that selecting *"linear"* or *"scara_linear"* for
  the parameter *`method`* enables only the output of the pose error
  (*"error_pose"*).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`x`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Linear list containing all the x coordinates of the
calibration points (in the order of the images).

**`y`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Linear list containing all the y coordinates of the
calibration points (in the order of the images).

**`z`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Linear list containing all the z coordinates of the
calibration points (in the order of the images).

**`row`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Linear list containing all row coordinates of the
calibration points (in the order of the images).

**`col`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Linear list containing all the column coordinates of
the calibration points (in the order of the images).

**`numPoints`** (input_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Number of the calibration points for each image.

**`robotPoses`** (input_control)  pose-array `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

Known 3D pose of the robot for each image (moving
camera: robot base in robot tool coordinates;
stationary camera: robot tool in robot base
coordinates).

**`cameraParam`** (input_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

Internal camera parameters.

**`method`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Method of hand-eye calibration.

Default:
"nonlinear"

List of values:
"linear", "nonlinear", "scara_linear", "scara_nonlinear"

**`qualityType`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Type of quality assessment.

Default:
"error_pose"

List of values:
"covariance", "error_pose", "standard_deviation"

**`cameraPose`** (output_control)  pose `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

Computed relative camera pose: 3D pose of the robot tool
(moving camera) or robot base (stationary camera),
respectively, in camera coordinates.

**`calibrationPose`** (output_control)  pose `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

Computed 3D pose of the calibration points in robot base
coordinates (moving camera) or in robot tool coordinates
(stationary camera), respectively.

**`quality`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Quality assessment of the result.

## Example (HDevelop)

```
* Note that, in order to use this code snippet, you must provide
* the camera parameters, the calibration plate description file,
* the calibration images, and the robot poses.
read_cam_par('campar.dat', CameraParam)
CalDescr := 'caltab.descr'
caltab_points(CalDescr, X, Y, Z)
* Process all calibration images.
for i := 0 to NumImages-1 by 1
  read_image(Image, 'calib_'+i$'02d')
  * Find marks on the calibration plate in every image.
  find_caltab(Image, CalPlate, CalDescr, 3, 150, 5)
  find_marks_and_pose(Image, CalPlate, CalDescr, CameraParam, 128, 10, 18, \
                      0.9, 15, 100, RCoordTmp, CCoordTmp, StartPose)
  * Accumulate 2D and 3D coordinates of the marks.
  RCoord := [RCoord, RCoordTmp]
  CCoord := [CCoord, CCoordTmp]
  XCoord := [XCoord, X]
  YCoord := [YCoord, Y]
  ZCoord := [ZCoord, Z]
  NumMarker := [NumMarker, |RCoordTmp|]
  * Read pose of the robot tool in robot base coordinates.
  read_pose('robpose_'+i$'02d'+'.dat', RobPose)
  * Moving camera? Invert pose.
  if (IsMovingCameraConfig == 'true')
    pose_to_hom_mat3d(RobPose, base_H_tool)
    hom_mat3d_invert(base_H_tool, tool_H_base)
    hom_mat3d_to_pose(tool_H_base, RobPose)
  endif
  * Accumulate robot poses.
  RobotPoses := [RobotPoses, RobPose]
endfor
*
* Perform hand-eye calibration.
*
hand_eye_calibration(XCoord, YCoord, ZCoord, RCoord, CCoord, NumMarker, \
                     RobotPoses, CameraParam, 'nonlinear', 'error_pose', \
                     CameraPose, CalibrationPose, Error)
```

## Result

The operator `HandEyeCalibration` returns the value 2 (
H_MSG_TRUE)
if the given parameters are correct. Otherwise, an exception will be raised.

## Possible Predecessors

`FindMarksAndPose`,
`CameraCalibration`,
`CalibrateCameras`

## Possible Successors

`WritePose`,
`ConvertPoseType`,
`PoseToHomMat3d`,
`DispCaltab`,
`SimCaltab`

## Alternatives

`CalibrateHandEye`

## See also

`FindCaltab`,
`FindMarksAndPose`,
`DispCaltab`,
`SimCaltab`,
`WriteCamPar`,
`ReadCamPar`,
`CreatePose`,
`ConvertPoseType`,
`WritePose`,
`ReadPose`,
`PoseToHomMat3d`,
`HomMat3dToPose`,
`CaltabPoints`,
`GenCaltab`,
`CalibrateHandEye`

## References

K. Daniilidis: “Hand-Eye Calibration Using Dual Quaternions”;
International Journal of Robotics Research, Vol. 18, No. 3,
pp. 286-298; 1999.
  
M. Ulrich, C. Steger: “Hand-Eye Calibration of SCARA Robots Using Dual
Quaternions”; Pattern Recognition and Image Analysis, Vol. 26, No. 1,
pp. 231-239; January 2016.

## Module

Calibration
