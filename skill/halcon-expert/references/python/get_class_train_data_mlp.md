# get_class_train_data_mlp (Operator)

## Name

`get_class_train_data_mlp` — Get the training data of a multilayer perceptron (MLP).

## Signature

`def get_class_train_data_mlp(mlphandle: HHandle) -> HHandle`

## Description

`get_class_train_data_mlp` gets the training data of a
multilayer perceptron (MLP) and returns it in
*`class_train_data_handle`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`mlphandle`** (input_control)  class_mlp `→` HHandle

Handle of a MLP that contains training data.

**`class_train_data_handle`** (output_control)  class_train_data `→` HHandle

Handle of the training data of the classifier.

## Result

If the parameters are valid, the operator
`get_class_train_data_mlp`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`add_sample_class_mlp`,
`read_samples_class_mlp`

## Possible Successors

`add_class_train_data_svm`,
`add_class_train_data_gmm`,
`add_class_train_data_knn`

## See also

`create_class_train_data`

## Module

Foundation
