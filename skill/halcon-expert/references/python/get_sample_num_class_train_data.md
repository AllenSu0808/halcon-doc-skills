# get_sample_num_class_train_data (Operator)

## Name

`get_sample_num_class_train_data` — Return the number of training samples stored in the training data.

## Signature

`def get_sample_num_class_train_data(class_train_data_handle: HHandle) -> int`

## Description

`get_sample_num_class_train_data` returns in *`num_samples`* the
number of training samples which are stored in the training data specified
by *`class_train_data_handle`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`class_train_data_handle`** (input_control)  class_train_data `→` HHandle

Handle of training data.

**`num_samples`** (output_control)  integer `→` int

Number of stored training samples.

## Result

If *`class_train_data_handle`* is valid, the operator
`get_sample_num_class_train_data` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`add_sample_class_train_data`

## Possible Successors

`get_sample_class_train_data`

## See also

`create_class_train_data`

## Module

Foundation
