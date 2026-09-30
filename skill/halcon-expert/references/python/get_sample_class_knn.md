# get_sample_class_knn (Operator)

## Name

`get_sample_class_knn` — Return a training sample from the training data of a k-nearest neighbors
(k-NN) classifier.

## Signature

`def get_sample_class_knn(knnhandle: HHandle, index_sample: int) -> Tuple[Sequence[float], Sequence[int]]`

## Description

`get_sample_class_knn` reads a training sample from the
k-nearest neighbors (k-NN) classifier given by *`knnhandle`* that was
added with [`add_sample_class_knn`](add_sample_class_knn.md) or
[`read_class_knn`](read_class_knn.md). The index of the sample is
specified with *`index_sample`*. The index is counted from 0,
i.e., *`index_sample`* must be a number between 0 and
`num_samples` - 1, where `num_samples` can be
determined with [`get_sample_num_class_knn`](get_sample_num_class_knn.md). The training
sample is returned in *`features`* and *`class_id`*.
*`features`* is a feature vector of length
`num_dim` (see [`create_class_knn`](create_class_knn.md)), while *`class_id`*
is the class label, which is a number between 0 and the
number of classes.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`knnhandle`** (input_control)  class_knn `→` HHandle

Handle of the k-NN classifier.

**`index_sample`** (input_control)  integer `→` int

Index of the training sample.

**`features`** (output_control)  real-array `→` Sequence[float]

Feature vector of the training sample.

**`class_id`** (output_control)  integer-array `→` Sequence[int]

Class of the training sample.

## Result

If the parameters are valid the operator
`get_sample_class_knn` returns the value 2 (
H_MSG_TRUE)
. If necessary,
an exception is raised.

## Possible Predecessors

`add_sample_class_train_data`

## See also

`create_class_knn`

## Module

Foundation
