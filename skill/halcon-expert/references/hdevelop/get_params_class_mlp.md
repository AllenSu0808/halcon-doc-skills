# get_params_class_mlp (Operator)

## Name

`get_params_class_mlp` — Return the parameters of a multilayer perceptron.

## Signature

`get_params_class_mlp( : : MLPHandle : NumInput, NumHidden, NumOutput, OutputFunction, Preprocessing, NumComponents)`

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

**`MLPHandle`** (input_control)  class_mlp `→`  (handle)

MLP handle.

**`NumInput`** (output_control)  integer `→`  (integer)

Number of input variables (features) of the MLP.

**`NumHidden`** (output_control)  integer `→`  (integer)

Number of hidden units of the MLP.

**`NumOutput`** (output_control)  integer `→`  (integer)

Number of output variables (classes) of the MLP.

**`OutputFunction`** (output_control)  string `→`  (string)

Type of the activation function in the output
layer of the MLP.

**`Preprocessing`** (output_control)  string `→`  (string)

Type of preprocessing used to transform the
feature vectors.

**`NumComponents`** (output_control)  integer `→`  (integer)

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
