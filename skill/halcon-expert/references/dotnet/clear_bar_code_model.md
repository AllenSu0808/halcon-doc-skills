# ClearBarCodeModel (Operator)

## Name

`ClearBarCodeModel` — Delete a bar code model and free the allocated memory

## Signature

`static void HOperatorSet.ClearBarCodeModel(HTuple barCodeHandle)`

`static void HBarCode.ClearBarCodeModel(HBarCode[] barCodeHandle)`

`void HBarCode.ClearBarCodeModel()`

## Description

The operator `ClearBarCodeModel` deletes a bar code model
that was created by [`CreateBarCodeModel`](create_bar_code_model.md). All memory used
by the model is freed. The handle of the model is passed in
*`barCodeHandle`*, which is invalid after the operator call.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- barCodeHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`barCodeHandle`** (input_control, state is modified)  barcode(-array) `→` [HBarCode](HBarCode.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the bar code model.

## Result

The operator `ClearBarCodeModel` returns the value 2 (
H_MSG_TRUE)
if a valid handle was passed and the referred bar code model can
be freed correctly.
Otherwise, an exception will be raised.

## See also

`FindBarCode`

## Module

Bar Code
