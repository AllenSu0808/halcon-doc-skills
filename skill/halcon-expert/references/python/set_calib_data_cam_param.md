# set_calib_data_cam_param (Operator)

## Name

`set_calib_data_cam_param` — Set type and initial parameters of a camera in a calibration data
model.

## Signature

`def set_calib_data_cam_param(calib_data_id: HHandle, camera_idx: Sequence[Union[int, str]], camera_type: MaybeSequence[str], camera_param: Sequence[Union[float, int, str]]) -> None`

## Description

The operator `set_calib_data_cam_param` sets the initial
camera parameters *`camera_param`* for the camera with the index
*`camera_idx`* in the calibration data model
*`calib_data_id`*. The parameter *`camera_idx`* must be
between 0 and `num_cameras`-1 (`num_cameras` is
specified during model creation with [`create_calib_data`](create_calib_data.md) and
can be queried with [`get_calib_data`](get_calib_data.md)). If a camera with
*`camera_idx`* was already defined, its parameters are
overwritten by the current ones (the camera is substituted). In
this case, the selection which camera parameters are marked for
optimization is reset and maybe has to be set again. Note that all
`num_cameras` cameras must be set to perform
[`calibrate_cameras`](calibrate_cameras.md). The calibration procedure refines these
initial parameters. You can find further information about the calibration
process of different camera setups in [Calibration](toc_calibration.md).

The parameter *`camera_type`* is only provided for backwards
compatibility.
The information about the camera type is contained in the first element
of *`camera_param`*.
Therefore, *`camera_type`* should be set either to its default value
*[]* (the recommended option) or to the same value as the
first element of *`camera_param`*. In any other case an error is raised.

An overview of all available camera types and their
respective parameters is given in *`camera_param`*.

The camera type can be queried later by calling
[`get_calib_data`](get_calib_data.md) with the arguments
`item_type`=*"camera"* and
`data_name`=*"type"*. The initial camera parameters
can be queried by calling [`get_calib_data`](get_calib_data.md) with arguments
`item_type`=*"camera"* and
`data_name`=*"init_params"*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- calib_data_id

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`calib_data_id`** (input_control, state is modified)  calib_data `→` HHandle

Handle of a calibration data model.

**`camera_idx`** (input_control)  number-array `→` Sequence[Union[int, str]]

Camera index.

Default:
0

Suggested values:
"all", 0, 1, 2

**`camera_type`** (input_control)  string(-array) `→` MaybeSequence[str]

Type of the camera.

Default:
[]

List of values:
[]

**`camera_param`** (input_control)  campar `→` Sequence[Union[float, int, str]]

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
