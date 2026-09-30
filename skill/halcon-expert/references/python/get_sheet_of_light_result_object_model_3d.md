# get_sheet_of_light_result_object_model_3d (Operator)

## Name

`get_sheet_of_light_result_object_model_3d` — Get the result of a calibrated measurement performed with the
sheet-of-light technique as a 3D object model.

## Signature

`def get_sheet_of_light_result_object_model_3d(sheet_of_light_model_id: HHandle) -> HHandle`

## Description

The operator `get_sheet_of_light_result_object_model_3d` returns the
result of a fully calibrated sheet-of-light measurement as a 3D object
model. The handle of the sheet-of-light model with which the
measurement is performed must be passed to *`sheet_of_light_model_id`*.
The calibration extent of the sheet-of-light model (*"calibration"*)
must have been set to *"xyz"* or *"offset_scale"*
before applying the measurement,
otherwise the computed coordinates cannot be returned as a 3D object model
and an exception is raised.

The handle of the 3D object model resulting from the measurement is returned
in *`object_model_3d`*. For the 3D points within this 3D object model
no triangular meshing is available, therefore no faces are stored in the 3D
object model. If a 3D object model with triangular meshing is required for
the subsequent processing, use the operator [`get_sheet_of_light_result`](get_sheet_of_light_result.md)
in order to retrieve the *"x"*, *"y"*, and *"z"*
coordinates from the sheet-of-light model and then call the operator
[`xyz_to_object_model_3d`](xyz_to_object_model_3d.md) with suitable parameters. Refer to
[`xyz_to_object_model_3d`](xyz_to_object_model_3d.md) for more information about 3D object models.

The unit of the returned coordinates depends on the value of the parameter
*"scale"* that was set for the sheet-of-light model before applying
the measurement.
See [`create_sheet_of_light_model`](create_sheet_of_light_model.md) and [`set_sheet_of_light_param`](set_sheet_of_light_param.md)
for details on the possible values of the model parameter *"scale"*.
The operator `get_sheet_of_light_result_object_model_3d` returns a
handle to an empty 3D object model if the desired result has not been
measured yet.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`sheet_of_light_model_id`** (input_control)  sheet_of_light_model `→` HHandle

Handle for accessing the sheet-of-light model.

**`object_model_3d`** (output_control)  object_model_3d `→` HHandle

Handle of the resulting 3D object model.

## Result

The operator `get_sheet_of_light_result_object_model_3d` returns the
value 2 (
H_MSG_TRUE)
if the given parameters are correct.
Otherwise, an exception will be raised.

## Possible Predecessors

`create_sheet_of_light_model`,
`measure_profile_sheet_of_light`,
`calibrate_sheet_of_light`

## Possible Successors

`clear_object_model_3d`

## Module

3D Metrology
