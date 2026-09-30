# get_sheet_of_light_param (Operator)

## Name

`get_sheet_of_light_param` — Get the value of a parameter, which has been set in a sheet-of-light model.

## Signature

`def get_sheet_of_light_param(sheet_of_light_model_id: HHandle, gen_param_name: str) -> Sequence[Union[int, float, str]]`

`def get_sheet_of_light_param_s(sheet_of_light_model_id: HHandle, gen_param_name: str) -> Union[int, float, str]`

## Description

The operator `get_sheet_of_light_param` is used to query the values
of the different parameters of a sheet-of-light model. The names of the
desired parameters are passed in the generic parameter
*`gen_param_name`*, the corresponding values are returned in
*`gen_param_value`*.

It is not possible to query the values of several parameters with a single
operator call. In order to request the values of several parameters you have
to successively call of the operator `get_sheet_of_light_param`.

The possible parameters are listed and described
in [`set_sheet_of_light_param`](set_sheet_of_light_param.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`sheet_of_light_model_id`** (input_control)  sheet_of_light_model `→` HHandle

Handle of the sheet-of-light model.

**`gen_param_name`** (input_control)  attribute.name `→` str

Name of the generic parameter that shall be queried.

Default:
"method"

List of values:
"ambiguity_solving", "calibration", "camera_parameter", "camera_pose", "lightplane_pose", "method", "min_gray", "movement_pose", "num_profiles", "offset_x", "offset_y", "offset_z", "scale", "scale_x", "scale_y", "scale_z", "score_type"

**`gen_param_value`** (output_control)  attribute.value(-array) `→` Sequence[Union[int, float, str]]

Value of the model parameter that shall be queried.

## Result

The operator `get_sheet_of_light_param` returns the value 2 (
H_MSG_TRUE)
if the given parameters are correct.
Otherwise, an exception will be raised.

## Possible Predecessors

`query_sheet_of_light_params`,
`set_sheet_of_light_param`

## Possible Successors

`measure_profile_sheet_of_light`,
`set_sheet_of_light_param`,
`apply_sheet_of_light_calibration`

## Module

3D Metrology
