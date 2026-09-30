# add_class_train_data_svm (Operator)

## Name

`add_class_train_data_svm` — Add training data to a support vector machine (SVM).

## Signature

`def add_class_train_data_svm(svmhandle: HHandle, class_train_data_handle: HHandle) -> None`

## Description

`add_class_train_data_svm` adds the training data specified by
*`class_train_data_handle`* to a support vector machine (SVM) specified by
*`svmhandle`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- svmhandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`svmhandle`** (input_control, state is modified)  class_svm `→` HHandle

Handle of a SVM which receives the training data.

**`class_train_data_handle`** (input_control)  class_train_data `→` HHandle

Training data for a classifier.

## Result

If the parameters are valid, the operator
`add_class_train_data_svm`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_class_svm`,
`create_class_train_data`

## Possible Successors

`get_sample_class_svm`

## Alternatives

`add_sample_class_svm`

## See also

`create_class_svm`

## Module

Foundation
