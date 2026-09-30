# clear_class_train_data (Operator)

## Name

`clear_class_train_data` — Clears training data for classifiers.

## Signature

`def clear_class_train_data(class_train_data_handle: HHandle) -> None`

## Description

`clear_class_train_data` clears the training data given in
*`class_train_data_handle`*.
After calling `clear_class_train_data`, *`class_train_data_handle`*
becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- class_train_data_handle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`class_train_data_handle`** (input_control, state is modified)  class_train_data `→` HHandle

Handle of training data for a classifier.

## Result

If the parameters are valid, the operator `clear_class_train_data`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_class_train_data`

## See also

`create_class_train_data`

## Module

Foundation
