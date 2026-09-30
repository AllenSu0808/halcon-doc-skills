# create_calib_data (Operator)

## Name

`create_calib_data` — Create a HALCON calibration data model.

## Signature

`def create_calib_data(calib_setup: str, num_cameras: int, num_calib_objects: int) -> HHandle`

## Description

The operator `create_calib_data` creates a generic calibration
data model that stores

- the description of a camera calibration setup,
- settings for the calibration process,
- the calibration data, and
- the results of the camera calibration or the hand-eye calibration.

In the parameter *`calib_setup`*, you specify the calibration setup type.
Currently, five types are supported. A model of the type
*"calibration_object"* is used to calibrate the internal camera
parameters and the camera poses of one or more cameras based on the metric
information extracted from observations of calibration objects.

A model of type *"hand_eye_moving_cam"*,
*"hand_eye_stationary_cam"*, *"hand_eye_scara_moving_cam"*, or
*"hand_eye_scara_stationary_cam"* is used to perform a hand-eye
calibration based on observations of a calibration object and
corresponding poses of a robot tool in the robot base coordinate system.
The latter four model types on the one hand distinguish whether the camera
or the calibration object is moved by the robot and on the other hand
distinguish whether an articulated robot or a SCARA robot is calibrated.
The arm of an articulated robot has three rotary
joints typically covering 6 degrees of freedom (3 translations and 3
rotations). SCARA robots have two parallel rotary joints and one parallel
prismatic joint covering only 4 degrees of freedom (3 translations and 1
rotation). Loosely speaking, an articulated robot is able to tilt its
end effector while a SCARA robot is not.

*`num_cameras`* specifies the number of cameras that are
calibrated simultaneously in the setup. *`num_calib_objects`*
specifies the number of calibration objects observed by the cameras.
Please note that for camera calibrations with line scan cameras with
perspective lenses only a single calibration object is allowed
(*`num_calib_objects`*=1). For hand-eye calibrations, only two
setups are currently supported: either one area scan projective
camera and one calibration object (*`num_cameras`*=1,
*`num_calib_objects`*=1) or a general sensor with no calibration
object (*`num_cameras`*=0, *`num_calib_objects`*=0).
Attention:
 The four hand-eye calibration models do not support
telecentric cameras.

*`calib_data_id`* returns a handle of the new calibration data
model. You pass this handle to other operators to collect
the description of the camera setup, the calibration settings, and the
calibration data. For camera calibrations, you pass it to
[`calibrate_cameras`](calibrate_cameras.md), which performs the actual camera calibration
and stores the calibration results in the calibration data model.
For a detailed description of the preparation process, please refer to
the chapter [Calibration](toc_calibration.md).
For hand-eye calibrations, you pass it to [`calibrate_hand_eye`](calibrate_hand_eye.md), which
performs the actual hand-eye calibration and stores the calibration results
in the calibration data model. For a detailed description of the
preparation process, please refer to the operator [`calibrate_hand_eye`](calibrate_hand_eye.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`calib_setup`** (input_control)  string `→` str

Type of the calibration setup.

Default:
"calibration_object"

List of values:
"calibration_object", "hand_eye_moving_cam", "hand_eye_scara_moving_cam", "hand_eye_scara_stationary_cam", "hand_eye_stationary_cam"

**`num_cameras`** (input_control)  number `→` int

Number of cameras in the calibration setup.

Default:
1

Restriction:
`NumCameras >= 0`

**`num_calib_objects`** (input_control)  number `→` int

Number of calibration objects.

Default:
1

Restriction:
`NumCalibObjects >= 0`

**`calib_data_id`** (output_control)  calib_data `→` HHandle

Handle of the created calibration data model.

## Possible Successors

`set_calib_data_cam_param`,
`set_calib_data_calib_object`

## Module

Calibration
