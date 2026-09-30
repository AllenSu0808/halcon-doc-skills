# AddSampleClassMlp (Operator)

## Name

`AddSampleClassMlp` — Add a training sample to the training data of a multilayer
perceptron.

## Signature

`static void HOperatorSet.AddSampleClassMlp(HTuple MLPHandle, HTuple features, HTuple target)`

`void HClassMlp.AddSampleClassMlp(HTuple features, HTuple target)`

`void HClassMlp.AddSampleClassMlp(HTuple features, int target)`

## Description

`AddSampleClassMlp` adds a training sample to the
multilayer perceptron (MLP) given by *`MLPHandle`*. The
training sample is given by *`features`* and *`target`*.
*`features`* is the feature vector of the sample, and
consequently must be a real vector of length `numInput`, as
specified in [`CreateClassMlp`](create_class_mlp.md). *`target`* is the
target vector of the sample, which must have the length
`numOutput` (see [`CreateClassMlp`](create_class_mlp.md)) for all three
types of activation functions of the MLP (exception: see below). If
the MLP is used for regression (function approximation), i.e., if
`outputFunction` = *"linear"*, *`target`* is
the value of the function at the coordinate *`features`*. In
this case, *`target`* can contain arbitrary real numbers. For
`outputFunction` = *"logistic"*, *`target`* can
only contain the values *0.0* and *1.0*. A value of
*1.0* specifies that the attribute in question is present,
while a value of *0.0* specifies that the attribute is
absent. Because in this case the attributes are independent,
arbitrary combinations of *0.0* and *1.0* can be
passed. For `outputFunction` = *"softmax"*,
*`target`* also can only contain the values *0.0* and
*1.0*. In contrast to `outputFunction` =
*"logistic"*, the value *1.0* must be present for
exactly one element of the tuple *`target`*. The location in
the tuple designates the class of the sample. For ease of use, a
single integer value may be passed if `outputFunction` =
*"softmax"*. This value directly designates the class of the
sample, which is counted from 0, i.e., the class must be an integer
between 0 and `numOutput` - 1. The class is converted to a
target vector of length `numOutput` internally.

Before the MLP can be trained with [`TrainClassMlp`](train_class_mlp.md),
*all* training samples must be added to the MLP with
`AddSampleClassMlp`.

The number of currently stored training samples can be queried with
[`GetSampleNumClassMlp`](get_sample_num_class_mlp.md). Stored training samples can be
read out again with [`GetSampleClassMlp`](get_sample_class_mlp.md).

Normally, it is useful to save the training samples in a file with
[`WriteSamplesClassMlp`](write_samples_class_mlp.md) to facilitate reusing the samples,
and to facilitate that, if necessary, new training samples can be
added to the data set, and hence to facilitate that a *newly
created* MLP can be trained *anew* with the extended data
set.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- MLPHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`MLPHandle`** (input_control, state is modified)  class_mlp `→` [HClassMlp](HClassMlp.md), [HTuple](HTuple.md) (*IntPtr*)

MLP handle.

**`features`** (input_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Feature vector of the training sample to be
stored.

**`target`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*int* / long / double)

Class or target vector of the training sample
to be stored.

## Result

If the parameters are valid, the operator
`AddSampleClassMlp` returns the value 2 (
H_MSG_TRUE)
. If necessary,
an exception is raised.

## Possible Predecessors

`CreateClassMlp`

## Possible Successors

`TrainClassMlp`,
`WriteSamplesClassMlp`

## Alternatives

`ReadSamplesClassMlp`

## See also

`ClearSamplesClassMlp`,
`GetSampleNumClassMlp`,
`GetSampleClassMlp`

## Module

Foundation
