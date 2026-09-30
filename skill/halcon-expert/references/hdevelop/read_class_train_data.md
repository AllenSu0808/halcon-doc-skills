# read_class_train_data (Operator)

## Name

`read_class_train_data` — Read the training data for classifiers from a file.

## Signature

`read_class_train_data( : : FileName : ClassTrainDataHandle)`

## Description

`read_class_train_data` reads the saved training data for classifiers
from the file *`FileName`* (see [`write_class_train_data`](write_class_train_data.md)).
The default HALCON file extension for training data for a
classifier is 'ctd'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`FileName`** (input_control)  filename.read `→`  (string)

File name of the training data.

File extension:
.`ctd`

**`ClassTrainDataHandle`** (output_control)  class_train_data `→`  (handle)

Handle of the training data.

## Result

`read_class_train_data` returns 2 (
H_MSG_TRUE)
.
An exception is raised if it was not possible to open the file
*`FileName`* or the file has the wrong format.

## See also

`create_class_train_data`,
`write_class_train_data`

## Module

Foundation
