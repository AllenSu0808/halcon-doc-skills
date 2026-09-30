# set_dl_pruning_param (Operator)

## Name

`set_dl_pruning_param` — Set parameter in a pruning data handle.

## Signature

`set_dl_pruning_param( : : DLPruningHandle, GenParamName, GenParamValue : )`

## Description

`set_dl_pruning_param` sets the parameter *`GenParamName`* in the
pruning handle *`DLPruningHandle`* to the value *`GenParamValue`*.

An overview as well as a description of the settable parameters is given in
[`get_dl_model_param`](get_dl_model_param.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DLPruningHandle`** (input_control)  dl_pruning `→`  (handle)

Pruning data handle.

**`GenParamName`** (input_control)  attribute.name `→`  (string)

Name of the generic parameter.

Default:
'percentage'

List of values:
'mode', 'percentage'

**`GenParamValue`** (input_control)  attribute.value(-array) `→`  (real / string / integer)

Value of the generic parameter.

Default:
10

Suggested values:
'oracle', 10, 20, 30, 40, 50

## Result

If the parameters are valid, the operator
`set_dl_pruning_param` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`create_dl_pruning`,
`get_dl_pruning_param`

## See also

`get_dl_pruning_param`

## Module

Deep Learning Professional
