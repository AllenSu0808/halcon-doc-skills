# clear_handle (Operator)

## Name

`clear_handle` — Clear the content of a handle.

## Signature

`clear_handle( : : Handle : )`

## Description

`clear_handle` clears the content of the handle contained in
*`Handle`*.
The handle is left in a cleared state afterwards. Attempts to use it
in any other operator will raise an error.

Usually, handles are automatically cleared once all references in
all tuples are overwritten.
`clear_handle` can be used to clear a handle at a specific
time, even if there are still references to it.

This operator can be used to clear handles of any type instead of the more
specialized operators, such as
[`clear_matrix`](clear_matrix.md) or [`clear_shape_model`](clear_shape_model.md).

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- Handle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`Handle`** (input_control, state is modified)  tuple(-array) `→`  (handle)

Handle to clear.

## Result

If the parameters are valid, the operator `clear_handle`
returns the value 2 (
H_MSG_TRUE)
. Otherwise, an exception is raised.

## See also

`tuple_is_valid_handle`

## Module

Foundation
