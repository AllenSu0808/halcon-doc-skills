# get_sheet_of_light_param (Operator)

## Name

`get_sheet_of_light_param` — Get the value of a parameter, which has been set in a sheet-of-light model.

## Signature

`get_sheet_of_light_param( : : SheetOfLightModelID, GenParamName : GenParamValue)`

## Description

The operator `get_sheet_of_light_param` is used to query the values
of the different parameters of a sheet-of-light model. The names of the
desired parameters are passed in the generic parameter
*`GenParamName`*, the corresponding values are returned in
*`GenParamValue`*.

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

**`SheetOfLightModelID`** (input_control)  sheet_of_light_model `→`  (handle)

Handle of the sheet-of-light model.

**`GenParamName`** (input_control)  attribute.name `→`  (string)

Name of the generic parameter that shall be queried.

Default:
'method'

List of values:
'ambiguity_solving', 'calibration', 'camera_parameter', 'camera_pose', 'lightplane_pose', 'method', 'min_gray', 'movement_pose', 'num_profiles', 'offset_x', 'offset_y', 'offset_z', 'scale', 'scale_x', 'scale_y', 'scale_z', 'score_type'

**`GenParamValue`** (output_control)  attribute.value(-array) `→`  (string / integer / real)

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
