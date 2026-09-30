# clear_bar_code_model (Operator)

## Name

`clear_bar_code_model` — Delete a bar code model and free the allocated memory

## Signature

`clear_bar_code_model( : : BarCodeHandle : )`

## Description

The operator `clear_bar_code_model` deletes a bar code model
that was created by [`create_bar_code_model`](create_bar_code_model.md). All memory used
by the model is freed. The handle of the model is passed in
*`BarCodeHandle`*, which is invalid after the operator call.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- BarCodeHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`BarCodeHandle`** (input_control, state is modified)  barcode(-array) `→`  (handle)

Handle of the bar code model.

## Result

The operator `clear_bar_code_model` returns the value 2 (
H_MSG_TRUE)
if a valid handle was passed and the referred bar code model can
be freed correctly.
Otherwise, an exception will be raised.

## See also

`find_bar_code`

## Module

Bar Code
