# add_class_train_data_gmm (Operator)

## Name

`add_class_train_data_gmm` — Add training data to a Gaussian Mixture Model (GMM).

## Signature

`def add_class_train_data_gmm(gmmhandle: HHandle, class_train_data_handle: HHandle) -> None`

## Description

`add_class_train_data_gmm` adds the training data specified by
*`class_train_data_handle`* to a Gaussian Mixture Model (GMM)
specified by *`gmmhandle`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- gmmhandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`gmmhandle`** (input_control, state is modified)  class_gmm `→` HHandle

Handle of a GMM which receives the training data.

**`class_train_data_handle`** (input_control)  class_train_data `→` HHandle

Handle of training data for a classifier.

## Result

If the parameters are valid, the operator
`add_class_train_data_gmm`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_class_gmm`,
`create_class_train_data`

## Possible Successors

`get_sample_class_gmm`

## Alternatives

`add_sample_class_gmm`

## See also

`create_class_gmm`

## Module

Foundation
