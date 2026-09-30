# query_sheet_of_light_params (Operator)

## Name

`query_sheet_of_light_params` — For a given sheet-of-light model get the names of the generic iconic
or control parameters that can be used in the different
sheet-of-light operators.

## Signature

`query_sheet_of_light_params( : : SheetOfLightModelID, QueryName : GenParamName)`

## Description

The operator `query_sheet_of_light_params` returns the names of
the generic parameters that are supported by the following operators
[`create_sheet_of_light_model`](create_sheet_of_light_model.md), [`set_sheet_of_light_param`](set_sheet_of_light_param.md),
[`get_sheet_of_light_param`](get_sheet_of_light_param.md) and [`get_sheet_of_light_result`](get_sheet_of_light_result.md).
The parameter *`QueryName`* is used to select the desired
**parameter group**:

- ***'create_model_params'*:** —

  [`create_sheet_of_light_model`](create_sheet_of_light_model.md) - Parameters for adjusting
  the sheet-of-light model during its creation.
- ***'set_model_params'*:** —

  [`set_sheet_of_light_param`](set_sheet_of_light_param.md) - Parameters for adjusting
  the parameters of an available sheet-of-light model.
- ***'get_model_params'*:** —

  [`get_sheet_of_light_param`](get_sheet_of_light_param.md) - Parameters for querying
  the values of the parameters of a sheet-of-light model.
- ***'get_result_objects'*:** —

  [`get_sheet_of_light_result`](get_sheet_of_light_result.md) - Parameters for accessing
  the iconic objects resulting from the measurement.

The returned parameter list does not depend on the current state of the
model or its results.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SheetOfLightModelID`** (input_control)  sheet_of_light_model `→`  (handle)

Handle of the sheet-of-light model.

**`QueryName`** (input_control)  attribute.name `→`  (string)

Name of the parameter group.

Default:
'create_model_params'

List of values:
'create_model_params', 'get_model_params', 'get_result_objects', 'set_model_params'

**`GenParamName`** (output_control)  attribute.value-array `→`  (string)

List containing the names of the supported generic
parameters.

## Result

The operator `query_sheet_of_light_params` returns the value 2 (
H_MSG_TRUE)
if the given parameters are correct.
Otherwise, an exception will be raised.

## Possible Successors

`create_sheet_of_light_model`,
`set_sheet_of_light_param`,
`get_sheet_of_light_param`,
`get_sheet_of_light_result`

## Module

3D Metrology
