# get_params_class_mlp (Operator)

## Name

`get_params_class_mlp` — Return the parameters of a multilayer perceptron.

## Signature

`def get_params_class_mlp(mlphandle: HHandle) -> Tuple[int, int, int, str, str, int]`

## Description

`get_params_class_mlp` returns the parameters of a multilayer
perceptron (MLP) that were specified when the MLP was created with
[`create_class_mlp`](create_class_mlp.md). This is particularly useful if the MLP
was read from a file with [`read_class_mlp`](read_class_mlp.md). The output of
`get_params_class_mlp` can, for example, be used to check
whether the feature vectors and, if necessary, the target data to be
used with the MLP have the correct lengths. For a description of
the parameters, see [`create_class_mlp`](create_class_mlp.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`mlphandle`** (input_control)  class_mlp `→` HHandle

MLP handle.

**`num_input`** (output_control)  integer `→` int

Number of input variables (features) of the MLP.

**`num_hidden`** (output_control)  integer `→` int

Number of hidden units of the MLP.

**`num_output`** (output_control)  integer `→` int

Number of output variables (classes) of the MLP.

**`output_function`** (output_control)  string `→` str

Type of the activation function in the output
layer of the MLP.

**`preprocessing`** (output_control)  string `→` str

Type of preprocessing used to transform the
feature vectors.

**`num_components`** (output_control)  integer `→` int

Preprocessing parameter: Number of transformed
features.

## Result

If the parameters are valid, the operator
`get_params_class_mlp` returns the value 2 (
H_MSG_TRUE)
. If necessary,
an exception is raised.

## Possible Predecessors

`create_class_mlp`,
`read_class_mlp`

## Possible Successors

`add_sample_class_mlp`,
`train_class_mlp`

## See also

`evaluate_class_mlp`,
`classify_class_mlp`

## Module

Foundation
