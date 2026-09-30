# WriteTrainingComponents (Operator)

## Name

`WriteTrainingComponents` — Write a component training result to a file.

## Warning

**`WriteTrainingComponents` is obsolete and is only provided for
reasons of backward compatibility.
The operator will be removed with HALCON 26.11.**

## Signature

`static void HOperatorSet.WriteTrainingComponents(HTuple componentTrainingID, HTuple fileName)`

`void HComponentTraining.WriteTrainingComponents(string fileName)`

## Description

The operator `WriteTrainingComponents` writes the component
training result *`componentTrainingID`* to the file
*`fileName`*. The training result can be read again with
[`ReadTrainingComponents`](read_training_components.md).
The default HALCON file extension for the component training result
is 'ct'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`componentTrainingID`** (input_control)  component_training `→` [HComponentTraining](HComponentTraining.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the training result.

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

File name.

File extension:
.`ct`

## Result

If the file name is valid (write permission), the operator
`WriteTrainingComponents` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Module

Matching
