# get_regularization_params_class_mlp (Operator)

## Name

`get_regularization_params_class_mlp` — Return the regularization parameters of a multilayer perceptron.

## Signature

`def get_regularization_params_class_mlp(mlphandle: HHandle, gen_param_name: str) -> Sequence[Union[float, int]]`

`def get_regularization_params_class_mlp_s(mlphandle: HHandle, gen_param_name: str) -> Union[float, int]`

## Description

`get_regularization_params_class_mlp` returns the
regularization parameters of a multilayer perceptron (MLP) that were
specified with [`set_regularization_params_class_mlp`](set_regularization_params_class_mlp.md).
Furthermore, `get_regularization_params_class_mlp` returns the
parameters that were determined by an automatic determination of the
regularization parameters. For a description of the parameters, see
[`set_regularization_params_class_mlp`](set_regularization_params_class_mlp.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`mlphandle`** (input_control)  class_mlp `→` HHandle

MLP handle.

**`gen_param_name`** (input_control)  string `→` str

Name of the regularization parameter to return.

Default:
"weight_prior"

List of values:
"fraction_well_determined_params", "noise_prior", "num_inner_iterations", "num_outer_iterations", "num_well_determined_params", "weight_prior"

**`gen_param_value`** (output_control)  number(-array) `→` Sequence[Union[float, int]]

Value of the regularization parameter.

## Result

If the parameters are valid, the operator
`get_regularization_params_class_mlp` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Possible Predecessors

`set_regularization_params_class_mlp`,
`read_class_mlp`

## Possible Successors

`train_class_mlp`

## Module

Foundation
