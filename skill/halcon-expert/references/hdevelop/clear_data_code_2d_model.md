# clear_data_code_2d_model (Operator)

## Name

`clear_data_code_2d_model` — Delete a 2D code model and free the allocated memory.

## Signature

`clear_data_code_2d_model( : : DataCodeHandle : )`

## Description

The operator `clear_data_code_2d_model` deletes a 2D code
model that was created by [`create_data_code_2d_model`](create_data_code_2d_model.md) or
[`read_data_code_2d_model`](read_data_code_2d_model.md).
All memory used by the model is freed.
The handle of the model is passed in *`DataCodeHandle`*.
After the operator call it is invalid.

For an explanation of the concept of the 2D code reader
see the introduction of chapter [Identification / 2D Code](toc_identification_datacode.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- DataCodeHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`DataCodeHandle`** (input_control, state is modified)  datacode_2d `→`  (handle)

Handle of the 2D code model.

## Result

The operator `clear_data_code_2d_model` returns the value 2 (
H_MSG_TRUE)
if a valid handle was passed and the referred 2D code model can
be freed correctly.
Otherwise, an exception is raised.

## See also

`create_data_code_2d_model`,
`read_data_code_2d_model`

## Module

Data Code
