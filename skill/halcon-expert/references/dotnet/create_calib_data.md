# CreateCalibData (Operator)

## Name

`CreateCalibData` — Create a HALCON calibration data model.

## Signature

`static void HOperatorSet.CreateCalibData(HTuple calibSetup, HTuple numCameras, HTuple numCalibObjects, out HTuple calibDataID)`

`public HCalibData(string calibSetup, int numCameras, int numCalibObjects)`

`void HCalibData.CreateCalibData(string calibSetup, int numCameras, int numCalibObjects)`

## Description

The operator `CreateCalibData` creates a generic calibration
data model that stores

- the description of a camera calibration setup,
- settings for the calibration process,
- the calibration data, and
- the results of the camera calibration or the hand-eye calibration.

In the parameter *`calibSetup`*, you specify the calibration setup type.
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

*`numCameras`* specifies the number of cameras that are
calibrated simultaneously in the setup. *`numCalibObjects`*
specifies the number of calibration objects observed by the cameras.
Please note that for camera calibrations with line scan cameras with
perspective lenses only a single calibration object is allowed
(*`numCalibObjects`*=1). For hand-eye calibrations, only two
setups are currently supported: either one area scan projective
camera and one calibration object (*`numCameras`*=1,
*`numCalibObjects`*=1) or a general sensor with no calibration
object (*`numCameras`*=0, *`numCalibObjects`*=0).
Attention:
 The four hand-eye calibration models do not support
telecentric cameras.

*`calibDataID`* returns a handle of the new calibration data
model. You pass this handle to other operators to collect
the description of the camera setup, the calibration settings, and the
calibration data. For camera calibrations, you pass it to
[`CalibrateCameras`](calibrate_cameras.md), which performs the actual camera calibration
and stores the calibration results in the calibration data model.
For a detailed description of the preparation process, please refer to
the chapter [Calibration](toc_calibration.md).
For hand-eye calibrations, you pass it to [`CalibrateHandEye`](calibrate_hand_eye.md), which
performs the actual hand-eye calibration and stores the calibration results
in the calibration data model. For a detailed description of the
preparation process, please refer to the operator [`CalibrateHandEye`](calibrate_hand_eye.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`calibSetup`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Type of the calibration setup.

Default:
"calibration_object"

List of values:
"calibration_object", "hand_eye_moving_cam", "hand_eye_scara_moving_cam", "hand_eye_scara_stationary_cam", "hand_eye_stationary_cam"

**`numCameras`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Number of cameras in the calibration setup.

Default:
1

Restriction:
`NumCameras >= 0`

**`numCalibObjects`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Number of calibration objects.

Default:
1

Restriction:
`NumCalibObjects >= 0`

**`calibDataID`** (output_control)  calib_data `→` [HCalibData](HCalibData.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the created calibration data model.

## Possible Successors

`SetCalibDataCamParam`,
`SetCalibDataCalibObject`

## Module

Calibration
