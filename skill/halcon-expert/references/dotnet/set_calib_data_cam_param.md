# SetCalibDataCamParam (Operator)

## Name

`SetCalibDataCamParam` — Set type and initial parameters of a camera in a calibration data
model.

## Signature

`static void HOperatorSet.SetCalibDataCamParam(HTuple calibDataID, HTuple cameraIdx, HTuple cameraType, HTuple cameraParam)`

`void HCalibData.SetCalibDataCamParam(HTuple cameraIdx, HTuple cameraType, HCamPar cameraParam)`

`void HCalibData.SetCalibDataCamParam(HTuple cameraIdx, string cameraType, HCamPar cameraParam)`

`void HCamPar.SetCalibDataCamParam(HCalibData calibDataID, HTuple cameraIdx, HTuple cameraType)`

`void HCamPar.SetCalibDataCamParam(HCalibData calibDataID, HTuple cameraIdx, string cameraType)`

## Description

The operator `SetCalibDataCamParam` sets the initial
camera parameters *`cameraParam`* for the camera with the index
*`cameraIdx`* in the calibration data model
*`calibDataID`*. The parameter *`cameraIdx`* must be
between 0 and `numCameras`-1 (`numCameras` is
specified during model creation with [`CreateCalibData`](create_calib_data.md) and
can be queried with [`GetCalibData`](get_calib_data.md)). If a camera with
*`cameraIdx`* was already defined, its parameters are
overwritten by the current ones (the camera is substituted). In
this case, the selection which camera parameters are marked for
optimization is reset and maybe has to be set again. Note that all
`numCameras` cameras must be set to perform
[`CalibrateCameras`](calibrate_cameras.md). The calibration procedure refines these
initial parameters. You can find further information about the calibration
process of different camera setups in [Calibration](toc_calibration.md).

The parameter *`cameraType`* is only provided for backwards
compatibility.
The information about the camera type is contained in the first element
of *`cameraParam`*.
Therefore, *`cameraType`* should be set either to its default value
*[]* (the recommended option) or to the same value as the
first element of *`cameraParam`*. In any other case an error is raised.

An overview of all available camera types and their
respective parameters is given in *`cameraParam`*.

The camera type can be queried later by calling
[`GetCalibData`](get_calib_data.md) with the arguments
`itemType`=*"camera"* and
`dataName`=*"type"*. The initial camera parameters
can be queried by calling [`GetCalibData`](get_calib_data.md) with arguments
`itemType`=*"camera"* and
`dataName`=*"init_params"*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- calibDataID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`calibDataID`** (input_control, state is modified)  calib_data `→` [HCalibData](HCalibData.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of a calibration data model.

**`cameraIdx`** (input_control)  number-array `→` [HTuple](HTuple.md) (*int* / long / string)

Camera index.

Default:
0

Suggested values:
"all", 0, 1, 2

**`cameraType`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Type of the camera.

Default:
[]

List of values:
[]

**`cameraParam`** (input_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

Initial camera internal parameters.

## Possible Predecessors

`CreateCalibData`,
`SetCalibDataCalibObject`

## Possible Successors

`SetCalibDataCalibObject`,
`SetCalibDataObservPoints`,
`FindCalibObject`

## Module

Calibration
