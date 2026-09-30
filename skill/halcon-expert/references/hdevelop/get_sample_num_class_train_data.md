# get_sample_num_class_train_data (Operator)

## Name

`get_sample_num_class_train_data` — Return the number of training samples stored in the training data.

## Signature

`get_sample_num_class_train_data( : : ClassTrainDataHandle : NumSamples)`

## Description

`get_sample_num_class_train_data` returns in *`NumSamples`* the
number of training samples which are stored in the training data specified
by *`ClassTrainDataHandle`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ClassTrainDataHandle`** (input_control)  class_train_data `→`  (handle)

Handle of training data.

**`NumSamples`** (output_control)  integer `→`  (integer)

Number of stored training samples.

## Result

If *`ClassTrainDataHandle`* is valid, the operator
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
