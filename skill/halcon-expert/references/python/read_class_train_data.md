# read_class_train_data (Operator)

## Name

`read_class_train_data` — Read the training data for classifiers from a file.

## Signature

`def read_class_train_data(file_name: str) -> HHandle`

## Description

`read_class_train_data` reads the saved training data for classifiers
from the file *`file_name`* (see [`write_class_train_data`](write_class_train_data.md)).
The default HALCON file extension for training data for a
classifier is 'ctd'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`file_name`** (input_control)  filename.read `→` str

File name of the training data.

File extension:
.`ctd`

**`class_train_data_handle`** (output_control)  class_train_data `→` HHandle

Handle of the training data.

## Result

`read_class_train_data` returns 2 (
H_MSG_TRUE)
.
An exception is raised if it was not possible to open the file
*`file_name`* or the file has the wrong format.

## See also

`create_class_train_data`,
`write_class_train_data`

## Module

Foundation
