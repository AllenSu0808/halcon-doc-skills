# set_calib_data_cam_param (Operator)

## Name

`set_calib_data_cam_param` — Set type and initial parameters of a camera in a calibration data
model.

## Signature

`set_calib_data_cam_param( : : CalibDataID, CameraIdx, CameraType, CameraParam : )`

## Description

The operator `set_calib_data_cam_param` sets the initial
camera parameters *`CameraParam`* for the camera with the index
*`CameraIdx`* in the calibration data model
*`CalibDataID`*. The parameter *`CameraIdx`* must be
between 0 and `NumCameras`-1 (`NumCameras` is
specified during model creation with [`create_calib_data`](create_calib_data.md) and
can be queried with [`get_calib_data`](get_calib_data.md)). If a camera with
*`CameraIdx`* was already defined, its parameters are
overwritten by the current ones (the camera is substituted). In
this case, the selection which camera parameters are marked for
optimization is reset and maybe has to be set again. Note that all
`NumCameras` cameras must be set to perform
[`calibrate_cameras`](calibrate_cameras.md). The calibration procedure refines these
initial parameters. You can find further information about the calibration
process of different camera setups in [Calibration](toc_calibration.md).

The parameter *`CameraType`* is only provided for backwards
compatibility.
The information about the camera type is contained in the first element
of *`CameraParam`*.
Therefore, *`CameraType`* should be set either to its default value
*[]* (the recommended option) or to the same value as the
first element of *`CameraParam`*. In any other case an error is raised.

An overview of all available camera types and their
respective parameters is given in *`CameraParam`*.

The camera type can be queried later by calling
[`get_calib_data`](get_calib_data.md) with the arguments
`ItemType`=*'camera'* and
`DataName`=*'type'*. The initial camera parameters
can be queried by calling [`get_calib_data`](get_calib_data.md) with arguments
`ItemType`=*'camera'* and
`DataName`=*'init_params'*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- CalibDataID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`CalibDataID`** (input_control, state is modified)  calib_data `→`  (handle)

Handle of a calibration data model.

**`CameraIdx`** (input_control)  number-array `→`  (integer / string)

Camera index.

Default:
0

Suggested values:
'all', 0, 1, 2

**`CameraType`** (input_control)  string(-array) `→`  (string)

Type of the camera.

Default:
[]

List of values:
[]

**`CameraParam`** (input_control)  campar `→`  (real / integer / string)

Initial camera internal parameters.

## Possible Predecessors

`create_calib_data`,
`set_calib_data_calib_object`

## Possible Successors

`set_calib_data_calib_object`,
`set_calib_data_observ_points`,
`find_calib_object`

## Module

Calibration
