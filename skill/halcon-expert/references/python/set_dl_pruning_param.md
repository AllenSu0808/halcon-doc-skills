# set_dl_pruning_param (Operator)

## Name

`set_dl_pruning_param` — Set parameter in a pruning data handle.

## Signature

`def set_dl_pruning_param(dlpruning_handle: HHandle, gen_param_name: str, gen_param_value: MaybeSequence[Union[str, float, int]]) -> None`

## Description

`set_dl_pruning_param` sets the parameter *`gen_param_name`* in the
pruning handle *`dlpruning_handle`* to the value *`gen_param_value`*.

An overview as well as a description of the settable parameters is given in
[`get_dl_model_param`](get_dl_model_param.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dlpruning_handle`** (input_control)  dl_pruning `→` HHandle

Pruning data handle.

**`gen_param_name`** (input_control)  attribute.name `→` str

Name of the generic parameter.

Default:
"percentage"

List of values:
"mode", "percentage"

**`gen_param_value`** (input_control)  attribute.value(-array) `→` MaybeSequence[Union[str, float, int]]

Value of the generic parameter.

Default:
10

Suggested values:
"oracle", 10, 20, 30, 40, 50

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
