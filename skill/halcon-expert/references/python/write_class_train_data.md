# write_class_train_data (Operator)

## Name

`write_class_train_data` — Save the training data for classifiers in a file.

## Signature

`def write_class_train_data(class_train_data_handle: HHandle, file_name: str) -> None`

## Description

`write_class_train_data` writes the training data for classifiers
*`class_train_data_handle`*
to the file given by *`file_name`*. The classifier can be read again
with [`read_class_train_data`](read_class_train_data.md).
The default HALCON file extension for the training data is 'ctd'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`class_train_data_handle`** (input_control)  class_train_data `→` HHandle

Handle of the training data.

**`file_name`** (input_control)  filename.write `→` str

Name of the file in which the training data will be
written.

File extension:
.`ctd`

## Result

`write_class_train_data` returns 2 (
H_MSG_TRUE)
.
An exception is raised if it was not possible to open file
*`file_name`*.

## See also

`create_class_train_data`,
`read_class_train_data`

## Module

Foundation
