# get_sample_class_train_data (Operator)

## Name

`get_sample_class_train_data` — Return a training sample from training data.

## Signature

`get_sample_class_train_data( : : ClassTrainDataHandle, IndexSample : Features, ClassID)`

## Description

`get_sample_class_train_data` reads a training sample from the
training data given by *`ClassTrainDataHandle`* that was
added, e.g., with [`add_sample_class_train_data`](add_sample_class_train_data.md).
The index of the sample is
specified with *`IndexSample`*. The index is counted from 0.
That means that *`IndexSample`* must be a number between 0 and
`NumSamples` - 1, where `NumSamples` can be
determined with [`get_sample_num_class_train_data`](get_sample_num_class_train_data.md). The training
sample is returned in *`Features`* and *`ClassID`*.
*`Features`* is a feature vector of length `NumDim`
(see [`create_class_train_data`](create_class_train_data.md)) and *`ClassID`* is
the class of the feature vector.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ClassTrainDataHandle`** (input_control)  class_train_data `→`  (handle)

Handle of training data for a classifier.

**`IndexSample`** (input_control)  integer `→`  (integer)

Number of stored training sample.

**`Features`** (output_control)  real-array `→`  (real)

Feature vector of the training sample.

**`ClassID`** (output_control)  integer `→`  (integer)

Class of the training sample.

## Result

If the parameters are valid, the operator
[`get_sample_class_mlp`](get_sample_class_mlp.md) returns the value 2 (
H_MSG_TRUE)
. If necessary,
an exception is raised.

## Possible Predecessors

`add_sample_class_train_data`

## See also

`create_class_train_data`

## Module

Foundation
