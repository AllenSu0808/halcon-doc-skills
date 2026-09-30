# add_class_train_data_knn (Operator)

## Name

`add_class_train_data_knn` — Add training data to a k-nearest neighbors (k-NN) classifier.

## Signature

`add_class_train_data_knn( : : KNNHandle, ClassTrainDataHandle : )`

## Description

`add_class_train_data_knn` adds the training data specified by
*`ClassTrainDataHandle`* to a k-nearest neighbors (k-NN) classifier
specified by *`KNNHandle`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- KNNHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`KNNHandle`** (input_control, state is modified)  class_knn `→`  (handle)

Handle of a k-NN which receives the
training data.

**`ClassTrainDataHandle`** (input_control)  class_train_data `→`  (handle)

Training data for a classifier.

## Result

If the parameters are valid, the operator
`add_class_train_data_knn`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_class_knn`,
`create_class_train_data`

## Possible Successors

`get_sample_class_knn`

## Alternatives

`add_sample_class_knn`

## See also

`create_class_knn`

## Module

Foundation
