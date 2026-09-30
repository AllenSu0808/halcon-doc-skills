# write_class_train_data (Operator)

## Name

`write_class_train_data` — Save the training data for classifiers in a file.

## Signature

`write_class_train_data( : : ClassTrainDataHandle, FileName : )`

## Description

`write_class_train_data` writes the training data for classifiers
*`ClassTrainDataHandle`*
to the file given by *`FileName`*. The classifier can be read again
with [`read_class_train_data`](read_class_train_data.md).
The default HALCON file extension for the training data is 'ctd'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ClassTrainDataHandle`** (input_control)  class_train_data `→`  (handle)

Handle of the training data.

**`FileName`** (input_control)  filename.write `→`  (string)

Name of the file in which the training data will be
written.

File extension:
.`ctd`

## Result

`write_class_train_data` returns 2 (
H_MSG_TRUE)
.
An exception is raised if it was not possible to open file
*`FileName`*.

## See also

`create_class_train_data`,
`read_class_train_data`

## Module

Foundation
