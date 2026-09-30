# SetDlPruningParam (Operator)

## Name

`SetDlPruningParam` — Set parameter in a pruning data handle.

## Signature

`static void HOperatorSet.SetDlPruningParam(HTuple DLPruningHandle, HTuple genParamName, HTuple genParamValue)`

`void HDlPrune.SetDlPruningParam(string genParamName, HTuple genParamValue)`

`void HDlPrune.SetDlPruningParam(string genParamName, double genParamValue)`

## Description

`SetDlPruningParam` sets the parameter *`genParamName`* in the
pruning handle *`DLPruningHandle`* to the value *`genParamValue`*.

An overview as well as a description of the settable parameters is given in
[`GetDlModelParam`](get_dl_model_param.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DLPruningHandle`** (input_control)  dl_pruning `→` [HDlPrune](HDlPrune.md), [HTuple](HTuple.md) (*IntPtr*)

Pruning data handle.

**`genParamName`** (input_control)  attribute.name `→` [HTuple](HTuple.md) (*string*)

Name of the generic parameter.

Default:
"percentage"

List of values:
"mode", "percentage"

**`genParamValue`** (input_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*double* / string / int / long)

Value of the generic parameter.

Default:
10

Suggested values:
"oracle", 10, 20, 30, 40, 50

## Result

If the parameters are valid, the operator
`SetDlPruningParam` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`CreateDlPruning`,
`GetDlPruningParam`

## See also

`GetDlPruningParam`

## Module

Deep Learning Professional
