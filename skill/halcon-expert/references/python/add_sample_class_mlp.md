# add_sample_class_mlp (Operator)

## Name

`add_sample_class_mlp` — Add a training sample to the training data of a multilayer
perceptron.

## Signature

`def add_sample_class_mlp(mlphandle: HHandle, features: Sequence[float], target: MaybeSequence[Union[int, float]]) -> None`

## Description

`add_sample_class_mlp` adds a training sample to the
multilayer perceptron (MLP) given by *`mlphandle`*. The
training sample is given by *`features`* and *`target`*.
*`features`* is the feature vector of the sample, and
consequently must be a real vector of length `num_input`, as
specified in [`create_class_mlp`](create_class_mlp.md). *`target`* is the
target vector of the sample, which must have the length
`num_output` (see [`create_class_mlp`](create_class_mlp.md)) for all three
types of activation functions of the MLP (exception: see below). If
the MLP is used for regression (function approximation), i.e., if
`output_function` = *"linear"*, *`target`* is
the value of the function at the coordinate *`features`*. In
this case, *`target`* can contain arbitrary real numbers. For
`output_function` = *"logistic"*, *`target`* can
only contain the values *0.0* and *1.0*. A value of
*1.0* specifies that the attribute in question is present,
while a value of *0.0* specifies that the attribute is
absent. Because in this case the attributes are independent,
arbitrary combinations of *0.0* and *1.0* can be
passed. For `output_function` = *"softmax"*,
*`target`* also can only contain the values *0.0* and
*1.0*. In contrast to `output_function` =
*"logistic"*, the value *1.0* must be present for
exactly one element of the tuple *`target`*. The location in
the tuple designates the class of the sample. For ease of use, a
single integer value may be passed if `output_function` =
*"softmax"*. This value directly designates the class of the
sample, which is counted from 0, i.e., the class must be an integer
between 0 and `num_output` - 1. The class is converted to a
target vector of length `num_output` internally.

Before the MLP can be trained with [`train_class_mlp`](train_class_mlp.md),
*all* training samples must be added to the MLP with
`add_sample_class_mlp`.

The number of currently stored training samples can be queried with
[`get_sample_num_class_mlp`](get_sample_num_class_mlp.md). Stored training samples can be
read out again with [`get_sample_class_mlp`](get_sample_class_mlp.md).

Normally, it is useful to save the training samples in a file with
[`write_samples_class_mlp`](write_samples_class_mlp.md) to facilitate reusing the samples,
and to facilitate that, if necessary, new training samples can be
added to the data set, and hence to facilitate that a *newly
created* MLP can be trained *anew* with the extended data
set.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- mlphandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`mlphandle`** (input_control, state is modified)  class_mlp `→` HHandle

MLP handle.

**`features`** (input_control)  real-array `→` Sequence[float]

Feature vector of the training sample to be
stored.

**`target`** (input_control)  number(-array) `→` MaybeSequence[Union[int, float]]

Class or target vector of the training sample
to be stored.

## Result

If the parameters are valid, the operator
`add_sample_class_mlp` returns the value 2 (
H_MSG_TRUE)
. If necessary,
an exception is raised.

## Possible Predecessors

`create_class_mlp`

## Possible Successors

`train_class_mlp`,
`write_samples_class_mlp`

## Alternatives

`read_samples_class_mlp`

## See also

`clear_samples_class_mlp`,
`get_sample_num_class_mlp`,
`get_sample_class_mlp`

## Module

Foundation
