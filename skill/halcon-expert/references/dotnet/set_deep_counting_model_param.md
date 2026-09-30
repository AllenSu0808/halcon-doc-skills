# SetDeepCountingModelParam (Operator)

## Name

`SetDeepCountingModelParam` — Set selected parameters of the Deep Counting model.

## Signature

`static void HOperatorSet.SetDeepCountingModelParam(HTuple deepCountingHandle, HTuple genParamName, HTuple genParamValue)`

`void HDlModelCounting.SetDeepCountingModelParam(HTuple genParamName, HTuple genParamValue)`

`void HDlModelCounting.SetDeepCountingModelParam(string genParamName, double genParamValue)`

## Description

The operator `SetDeepCountingModelParam` sets the selected parameters
*`genParamName`* in the Deep Counting handle *`deepCountingHandle`* to
the values passed in *`genParamValue`*.

The possible parameters are listed and described in
[`GetDeepCountingModelParam`](get_deep_counting_model_param.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- deepCountingHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`deepCountingHandle`** (input_control, state is modified)  deep_counting `→` [HDlModelCounting](HDlModelCounting.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the Deep Counting model.

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Parameter names.

Default:
"min_score"

List of values:
"angle_end", "angle_start", "angle_step", "backbone_model", "device", "max_overlap", "min_score", "scale_max", "scale_min", "scale_step"

**`genParamValue`** (input_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*double* / int / long / string)

Parameter values.

Default:
0.5

## Result

If the parameters are valid, the operator `SetDeepCountingModelParam`
returns the value 2 (
H_MSG_TRUE)
. If necessary an exception is raised.

## Possible Predecessors

`CreateDeepCountingModel`,
`GetDeepCountingModelParam`

## Possible Successors

`PrepareDeepCountingModel`,
`ApplyDeepCountingModel`

## See also

`GetDeepCountingModelParam`

## Module

Matching
