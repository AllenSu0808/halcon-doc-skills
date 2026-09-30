# get_class_train_data_svm (Operator)

## Name

`get_class_train_data_svm` — Get the training data of a support vector machine (SVM).

## Signature

`get_class_train_data_svm( : : SVMHandle : ClassTrainDataHandle)`

## Description

`get_class_train_data_svm` gets the training data of a
support vector machine (SVM) and returns it in
*`ClassTrainDataHandle`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`SVMHandle`** (input_control)  class_svm `→`  (handle)

Handle of a SVM that contains training data.

**`ClassTrainDataHandle`** (output_control)  class_train_data `→`  (handle)

Handle of the training data of the classifier.

## Result

If the parameters are valid, the operator
`get_class_train_data_svm`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`add_sample_class_svm`,
`read_samples_class_svm`

## Possible Successors

`add_class_train_data_mlp`,
`add_class_train_data_gmm`,
`add_class_train_data_knn`

## See also

`create_class_train_data`

## Module

Foundation
