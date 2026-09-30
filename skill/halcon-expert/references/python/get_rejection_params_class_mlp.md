# get_rejection_params_class_mlp (Operator)

## Name

`get_rejection_params_class_mlp` — Get the parameters of a rejection class.

## Signature

`def get_rejection_params_class_mlp(mlphandle: HHandle, gen_param_name: MaybeSequence[str]) -> Sequence[Union[str, float, int]]`

`def get_rejection_params_class_mlp_s(mlphandle: HHandle, gen_param_name: MaybeSequence[str]) -> Union[str, float, int]`

## Description

`get_rejection_params_class_mlp` returns the rejection class
parameters of a multilayer perceptron (MLP) that were specified with
[`set_rejection_params_class_mlp`](set_rejection_params_class_mlp.md). For a description of the
parameters, see [`set_rejection_params_class_mlp`](set_rejection_params_class_mlp.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`mlphandle`** (input_control)  class_mlp `→` HHandle

MLP handle.

**`gen_param_name`** (input_control)  string(-array) `→` MaybeSequence[str]

Names of the generic parameters to return.

Default:
"sampling_strategy"

List of values:
"hyperbox_tolerance", "random_seed", "rejection_class_index", "rejection_sample_factor", "sampling_strategy"

**`gen_param_value`** (output_control)  string(-array) `→` Sequence[Union[str, float, int]]

Values of the generic parameters.

## Result

If the parameters are valid, the operator
`get_rejection_params_class_mlp` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`create_class_mlp`

## Possible Successors

`train_class_mlp`

## Module

Foundation
