# get_rejection_params_class_mlp (Operator)

## Name

`get_rejection_params_class_mlp` — Get the parameters of a rejection class.

## Signature

`get_rejection_params_class_mlp( : : MLPHandle, GenParamName : GenParamValue)`

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

**`MLPHandle`** (input_control)  class_mlp `→`  (handle)

MLP handle.

**`GenParamName`** (input_control)  string(-array) `→`  (string)

Names of the generic parameters to return.

Default:
'sampling_strategy'

List of values:
'hyperbox_tolerance', 'random_seed', 'rejection_class_index', 'rejection_sample_factor', 'sampling_strategy'

**`GenParamValue`** (output_control)  string(-array) `→`  (string / real / integer)

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
