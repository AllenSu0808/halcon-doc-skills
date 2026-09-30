# GetSheetOfLightParam (Operator)

## Name

`GetSheetOfLightParam` — Get the value of a parameter, which has been set in a sheet-of-light model.

## Signature

`static void HOperatorSet.GetSheetOfLightParam(HTuple sheetOfLightModelID, HTuple genParamName, out HTuple genParamValue)`

`HTuple HSheetOfLightModel.GetSheetOfLightParam(string genParamName)`

## Description

The operator `GetSheetOfLightParam` is used to query the values
of the different parameters of a sheet-of-light model. The names of the
desired parameters are passed in the generic parameter
*`genParamName`*, the corresponding values are returned in
*`genParamValue`*.

It is not possible to query the values of several parameters with a single
operator call. In order to request the values of several parameters you have
to successively call of the operator `GetSheetOfLightParam`.

The possible parameters are listed and described
in [`SetSheetOfLightParam`](set_sheet_of_light_param.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`sheetOfLightModelID`** (input_control)  sheet_of_light_model `→` [HSheetOfLightModel](HSheetOfLightModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the sheet-of-light model.

**`genParamName`** (input_control)  attribute.name `→` [HTuple](HTuple.md) (*string*)

Name of the generic parameter that shall be queried.

Default:
"method"

List of values:
"ambiguity_solving", "calibration", "camera_parameter", "camera_pose", "lightplane_pose", "method", "min_gray", "movement_pose", "num_profiles", "offset_x", "offset_y", "offset_z", "scale", "scale_x", "scale_y", "scale_z", "score_type"

**`genParamValue`** (output_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Value of the model parameter that shall be queried.

## Result

The operator `GetSheetOfLightParam` returns the value 2 (
H_MSG_TRUE)
if the given parameters are correct.
Otherwise, an exception will be raised.

## Possible Predecessors

`QuerySheetOfLightParams`,
`SetSheetOfLightParam`

## Possible Successors

`MeasureProfileSheetOfLight`,
`SetSheetOfLightParam`,
`ApplySheetOfLightCalibration`

## Module

3D Metrology
