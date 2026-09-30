# QuerySheetOfLightParams (Operator)

## Name

`QuerySheetOfLightParams` — For a given sheet-of-light model get the names of the generic iconic
or control parameters that can be used in the different
sheet-of-light operators.

## Signature

`static void HOperatorSet.QuerySheetOfLightParams(HTuple sheetOfLightModelID, HTuple queryName, out HTuple genParamName)`

`HTuple HSheetOfLightModel.QuerySheetOfLightParams(string queryName)`

## Description

The operator `QuerySheetOfLightParams` returns the names of
the generic parameters that are supported by the following operators
[`CreateSheetOfLightModel`](create_sheet_of_light_model.md), [`SetSheetOfLightParam`](set_sheet_of_light_param.md),
[`GetSheetOfLightParam`](get_sheet_of_light_param.md) and [`GetSheetOfLightResult`](get_sheet_of_light_result.md).
The parameter *`queryName`* is used to select the desired
**parameter group**:

- ***"create_model_params"*:** —

  [`CreateSheetOfLightModel`](create_sheet_of_light_model.md) - Parameters for adjusting
  the sheet-of-light model during its creation.
- ***"set_model_params"*:** —

  [`SetSheetOfLightParam`](set_sheet_of_light_param.md) - Parameters for adjusting
  the parameters of an available sheet-of-light model.
- ***"get_model_params"*:** —

  [`GetSheetOfLightParam`](get_sheet_of_light_param.md) - Parameters for querying
  the values of the parameters of a sheet-of-light model.
- ***"get_result_objects"*:** —

  [`GetSheetOfLightResult`](get_sheet_of_light_result.md) - Parameters for accessing
  the iconic objects resulting from the measurement.

The returned parameter list does not depend on the current state of the
model or its results.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`sheetOfLightModelID`** (input_control)  sheet_of_light_model `→` [HSheetOfLightModel](HSheetOfLightModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the sheet-of-light model.

**`queryName`** (input_control)  attribute.name `→` [HTuple](HTuple.md) (*string*)

Name of the parameter group.

Default:
"create_model_params"

List of values:
"create_model_params", "get_model_params", "get_result_objects", "set_model_params"

**`genParamName`** (output_control)  attribute.value-array `→` [HTuple](HTuple.md) (*string*)

List containing the names of the supported generic
parameters.

## Result

The operator `QuerySheetOfLightParams` returns the value 2 (
H_MSG_TRUE)
if the given parameters are correct.
Otherwise, an exception will be raised.

## Possible Successors

`CreateSheetOfLightModel`,
`SetSheetOfLightParam`,
`GetSheetOfLightParam`,
`GetSheetOfLightResult`

## Module

3D Metrology
