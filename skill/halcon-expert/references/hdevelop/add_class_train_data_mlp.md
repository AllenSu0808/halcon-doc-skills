# add_class_train_data_mlp (Operator)

## Name

`add_class_train_data_mlp` — Add training data to a multilayer perceptron (MLP).

## Signature

`add_class_train_data_mlp( : : MLPHandle, ClassTrainDataHandle : )`

## Description

`add_class_train_data_mlp` adds the training data specified by
*`ClassTrainDataHandle`* to a multilayer perceptron (MLP) specified by
*`MLPHandle`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- MLPHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`MLPHandle`** (input_control, state is modified)  class_mlp `→`  (handle)

MLP handle which receives the training data.

**`ClassTrainDataHandle`** (input_control)  class_train_data `→`  (handle)

Training data for a classifier.

## Result

If the parameters are valid, the operator
`add_class_train_data_mlp`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_class_mlp`,
`create_class_train_data`

## Possible Successors

`get_sample_class_mlp`

## Alternatives

`add_sample_class_mlp`

## See also

`create_class_mlp`

## Module

Foundation
