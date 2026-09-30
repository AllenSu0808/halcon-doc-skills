# ClearDataCode2dModel (Operator)

## Name

`ClearDataCode2dModel` — Delete a 2D code model and free the allocated memory.

## Signature

`static void HOperatorSet.ClearDataCode2dModel(HTuple dataCodeHandle)`

`void HDataCode2D.ClearDataCode2dModel()`

## Description

The operator `ClearDataCode2dModel` deletes a 2D code
model that was created by [`CreateDataCode2dModel`](create_data_code_2d_model.md) or
[`ReadDataCode2dModel`](read_data_code_2d_model.md).
All memory used by the model is freed.
The handle of the model is passed in *`dataCodeHandle`*.
After the operator call it is invalid.

For an explanation of the concept of the 2D code reader
see the introduction of chapter [Identification / 2D Code](toc_identification_datacode.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- dataCodeHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`dataCodeHandle`** (input_control, state is modified)  datacode_2d `→` [HDataCode2D](HDataCode2D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 2D code model.

## Result

The operator `ClearDataCode2dModel` returns the value 2 (
H_MSG_TRUE)
if a valid handle was passed and the referred 2D code model can
be freed correctly.
Otherwise, an exception is raised.

## See also

`CreateDataCode2dModel`,
`ReadDataCode2dModel`

## Module

Data Code
