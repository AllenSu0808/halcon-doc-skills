# ClearHandle (Operator)

## Name

`ClearHandle` — Clear the content of a handle.

## Signature

`static void HOperatorSet.ClearHandle(HTuple handle)`

`void HTuple.ClearHandle()`

`void HHandle.ClearHandle()`

## Description

`ClearHandle` clears the content of the handle contained in
*`handle`*.
The handle is left in a cleared state afterwards. Attempts to use it
in any other operator will raise an error.

Usually, handles are automatically cleared once all references in
all tuples are overwritten.
`ClearHandle` can be used to clear a handle at a specific
time, even if there are still references to it.

This operator can be used to clear handles of any type instead of the more
specialized operators, such as
[`ClearMatrix`](clear_matrix.md) or [`ClearShapeModel`](clear_shape_model.md).

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- handle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`handle`** (input_control, state is modified)  tuple(-array) `→` [HTuple](HTuple.md) (*HHandle*)

Handle to clear.

## Result

If the parameters are valid, the operator `ClearHandle`
returns the value 2 (
H_MSG_TRUE)
. Otherwise, an exception is raised.

## See also

`TupleIsValidHandle`

## Module

Foundation
