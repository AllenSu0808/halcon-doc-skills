# ReadClassTrainData (Operator)

## Name

`ReadClassTrainData` — Read the training data for classifiers from a file.

## Signature

`static void HOperatorSet.ReadClassTrainData(HTuple fileName, out HTuple classTrainDataHandle)`

`public HClassTrainData(string fileName)`

`void HClassTrainData.ReadClassTrainData(string fileName)`

## Description

`ReadClassTrainData` reads the saved training data for classifiers
from the file *`fileName`* (see [`WriteClassTrainData`](write_class_train_data.md)).
The default HALCON file extension for training data for a
classifier is 'ctd'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`fileName`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

File name of the training data.

File extension:
.`ctd`

**`classTrainDataHandle`** (output_control)  class_train_data `→` [HClassTrainData](HClassTrainData.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the training data.

## Result

`ReadClassTrainData` returns 2 (
H_MSG_TRUE)
.
An exception is raised if it was not possible to open the file
*`fileName`* or the file has the wrong format.

## See also

`CreateClassTrainData`,
`WriteClassTrainData`

## Module

Foundation
