# get_sample_num_class_knn (Operator)

## Name

`get_sample_num_class_knn` — Return the number of training samples stored in the training data of
a k-nearest neighbors (k-NN) classifier.

## Signature

`def get_sample_num_class_knn(knnhandle: HHandle) -> int`

## Description

`get_sample_num_class_knn` returns in *`num_samples`* the
number of training samples that are stored in the k-nearest neighbors
(k-NN) classifier given by *`knnhandle`*.
`get_sample_num_class_knn` should be called before the
individual training samples are accessed with
[`get_sample_class_knn`](get_sample_class_knn.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`knnhandle`** (input_control)  class_knn `→` HHandle

Handle of the k-NN classifier.

**`num_samples`** (output_control)  integer `→` int

Number of stored training samples.

## Result

If *`knnhandle`* is valid, the operator
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
