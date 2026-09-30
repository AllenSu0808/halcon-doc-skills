# get_sample_class_knn (Operator)

## Name

`get_sample_class_knn` — Return a training sample from the training data of a k-nearest neighbors
(k-NN) classifier.

## Signature

`get_sample_class_knn( : : KNNHandle, IndexSample : Features, ClassID)`

## Description

`get_sample_class_knn` reads a training sample from the
k-nearest neighbors (k-NN) classifier given by *`KNNHandle`* that was
added with [`add_sample_class_knn`](add_sample_class_knn.md) or
[`read_class_knn`](read_class_knn.md). The index of the sample is
specified with *`IndexSample`*. The index is counted from 0,
i.e., *`IndexSample`* must be a number between 0 and
`NumSamples` - 1, where `NumSamples` can be
determined with [`get_sample_num_class_knn`](get_sample_num_class_knn.md). The training
sample is returned in *`Features`* and *`ClassID`*.
*`Features`* is a feature vector of length
`NumDim` (see [`create_class_knn`](create_class_knn.md)), while *`ClassID`*
is the class label, which is a number between 0 and the
number of classes.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`KNNHandle`** (input_control)  class_knn `→`  (handle)

Handle of the k-NN classifier.

**`IndexSample`** (input_control)  integer `→`  (integer)

Index of the training sample.

**`Features`** (output_control)  real-array `→`  (real)

Feature vector of the training sample.

**`ClassID`** (output_control)  integer-array `→`  (integer)

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
