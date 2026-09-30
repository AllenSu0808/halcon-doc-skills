# get_sample_num_class_knn (Operator)

## Name

`get_sample_num_class_knn` — Return the number of training samples stored in the training data of
a k-nearest neighbors (k-NN) classifier.

## Signature

`get_sample_num_class_knn( : : KNNHandle : NumSamples)`

## Description

`get_sample_num_class_knn` returns in *`NumSamples`* the
number of training samples that are stored in the k-nearest neighbors
(k-NN) classifier given by *`KNNHandle`*.
`get_sample_num_class_knn` should be called before the
individual training samples are accessed with
[`get_sample_class_knn`](get_sample_class_knn.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`KNNHandle`** (input_control)  class_knn `→`  (handle)

Handle of the k-NN classifier.

**`NumSamples`** (output_control)  integer `→`  (integer)

Number of stored training samples.

## Result

If *`KNNHandle`* is valid, the operator
`get_sample_num_class_knn` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`add_sample_class_knn`

## Possible Successors

`get_sample_class_knn`

## See also

`create_class_knn`

## Module

Foundation
