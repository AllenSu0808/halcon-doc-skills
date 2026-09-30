# ReadTrainingComponents (Operator)

## Name

`ReadTrainingComponents` — Read a component training result from a file.

## Warning

**`ReadTrainingComponents` is obsolete and is only provided for
reasons of backward compatibility.
The operator will be removed with HALCON 26.11.**

## Signature

`static void HOperatorSet.ReadTrainingComponents(HTuple fileName, out HTuple componentTrainingID)`

`void HComponentTraining.ReadTrainingComponents(string fileName)`

## Description

The operator `ReadTrainingComponents` reads a component
training result, which has been written with
[`WriteTrainingComponents`](write_training_components.md), from the file *`fileName`*
and returns it in *`componentTrainingID`*.
The default HALCON file extension for the component training result
is 'ct'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`fileName`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

File name.

File extension:
.`ct`

**`componentTrainingID`** (output_control)  component_training `→` [HComponentTraining](HComponentTraining.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the training result.

## Result

If the file name is valid, the operator `ReadTrainingComponents`
returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Module

Matching
