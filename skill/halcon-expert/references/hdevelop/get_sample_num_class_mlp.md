# get_sample_num_class_mlp (Operator)

## Name

`get_sample_num_class_mlp` — Return the number of training samples stored in the training data of
a multilayer perceptron.

## Signature

`get_sample_num_class_mlp( : : MLPHandle : NumSamples)`

## Description

`get_sample_num_class_mlp` returns in *`NumSamples`* the
number of training samples that are stored in the multilayer
perceptron (MLP) given by *`MLPHandle`*.
`get_sample_num_class_mlp` should be called before the
individual training samples are accessed with
[`get_sample_class_mlp`](get_sample_class_mlp.md), e.g., for the purpose of reclassifying
the training data (see [`get_sample_class_mlp`](get_sample_class_mlp.md)).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MLPHandle`** (input_control)  class_mlp `→`  (handle)

MLP handle.

**`NumSamples`** (output_control)  integer `→`  (integer)

Number of stored training samples.

## Result

If *`MLPHandle`* is valid, the operator
`get_sample_num_class_mlp` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`add_sample_class_mlp`,
`read_samples_class_mlp`

## Possible Successors

`get_sample_class_mlp`

## See also

`create_class_mlp`

## Module

Foundation
