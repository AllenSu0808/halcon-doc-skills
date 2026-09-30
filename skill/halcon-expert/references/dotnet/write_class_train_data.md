# WriteClassTrainData (Operator)

## Name

`WriteClassTrainData` — Save the training data for classifiers in a file.

## Signature

`static void HOperatorSet.WriteClassTrainData(HTuple classTrainDataHandle, HTuple fileName)`

`void HClassTrainData.WriteClassTrainData(string fileName)`

## Description

`WriteClassTrainData` writes the training data for classifiers
*`classTrainDataHandle`*
to the file given by *`fileName`*. The classifier can be read again
with [`ReadClassTrainData`](read_class_train_data.md).
The default HALCON file extension for the training data is 'ctd'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`classTrainDataHandle`** (input_control)  class_train_data `→` [HClassTrainData](HClassTrainData.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the training data.

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

Name of the file in which the training data will be
written.

File extension:
.`ctd`

## Result

`WriteClassTrainData` returns 2 (
H_MSG_TRUE)
.
An exception is raised if it was not possible to open file
*`fileName`*.

## See also

`CreateClassTrainData`,
`ReadClassTrainData`

## Module

Foundation
