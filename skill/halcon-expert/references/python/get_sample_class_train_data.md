# get_sample_class_train_data (Operator)

## Name

`get_sample_class_train_data` — Return a training sample from training data.

## Signature

`def get_sample_class_train_data(class_train_data_handle: HHandle, index_sample: int) -> Tuple[Sequence[float], int]`

## Description

`get_sample_class_train_data` reads a training sample from the
training data given by *`class_train_data_handle`* that was
added, e.g., with [`add_sample_class_train_data`](add_sample_class_train_data.md).
The index of the sample is
specified with *`index_sample`*. The index is counted from 0.
That means that *`index_sample`* must be a number between 0 and
`num_samples` - 1, where `num_samples` can be
determined with [`get_sample_num_class_train_data`](get_sample_num_class_train_data.md). The training
sample is returned in *`features`* and *`class_id`*.
*`features`* is a feature vector of length `num_dim`
(see [`create_class_train_data`](create_class_train_data.md)) and *`class_id`* is
the class of the feature vector.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`class_train_data_handle`** (input_control)  class_train_data `→` HHandle

Handle of training data for a classifier.

**`index_sample`** (input_control)  integer `→` int

Number of stored training sample.

**`features`** (output_control)  real-array `→` Sequence[float]

Feature vector of the training sample.

**`class_id`** (output_control)  integer `→` int

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
