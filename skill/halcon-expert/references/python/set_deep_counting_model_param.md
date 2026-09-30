# set_deep_counting_model_param (Operator)

## Name

`set_deep_counting_model_param` — Set selected parameters of the Deep Counting model.

## Signature

`def set_deep_counting_model_param(deep_counting_handle: HHandle, gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[float, int, str]]) -> None`

## Description

The operator `set_deep_counting_model_param` sets the selected parameters
*`gen_param_name`* in the Deep Counting handle *`deep_counting_handle`* to
the values passed in *`gen_param_value`*.

The possible parameters are listed and described in
[`get_deep_counting_model_param`](get_deep_counting_model_param.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- deep_counting_handle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`deep_counting_handle`** (input_control, state is modified)  deep_counting `→` HHandle

Handle of the Deep Counting model.

**`gen_param_name`** (input_control)  attribute.name(-array) `→` MaybeSequence[str]

Parameter names.

Default:
"min_score"

List of values:
"angle_end", "angle_start", "angle_step", "backbone_model", "device", "max_overlap", "min_score", "scale_max", "scale_min", "scale_step"

**`gen_param_value`** (input_control)  attribute.value(-array) `→` MaybeSequence[Union[float, int, str]]

Parameter values.

Default:
0.5

## Result

If the parameters are valid, the operator `set_deep_counting_model_param`
returns the value 2 (
H_MSG_TRUE)
. If necessary an exception is raised.

## Possible Predecessors

`create_deep_counting_model`,
`get_deep_counting_model_param`

## Possible Successors

`prepare_deep_counting_model`,
`apply_deep_counting_model`

## See also

`get_deep_counting_model_param`

## Module

Matching
