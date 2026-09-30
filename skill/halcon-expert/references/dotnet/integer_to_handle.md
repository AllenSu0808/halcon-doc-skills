# IntegerToHandle (Operator)

## Name

`IntegerToHandle` — Convert an integer into a handle.

## Warning

**It is not recommended to use this operator in HDevelop.
This operator is only provided for reasons of backward compatibility.**

## Signature

`static void HOperatorSet.IntegerToHandle(HTuple integerHandle, out HTuple handle)`

## Description

`IntegerToHandle` converts the integer *`integerHandle`*, that
represents a handle, to a handle of type HANDLE_PAR and returns it in
*`handle`*.

The ownership of the handle is transferred onto the handle. The handle will
automatically be cleared once all references to that handle, such as in the
tuple *`handle`*, are overwritten. If the original *`integerHandle`*
should continue to be used, a reference to the returned *`handle`* must
be kept in order to avoid clearing the handle.

## Attention

It is not recommended to use this operator in HDevelop.
This operator is solely provided to enable backward compatibility with
legacy code.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`integerHandle`** (input_control)  pointer(-array) `→` [HTuple](HTuple.md) (*IntPtr*)

The handle as integer.

**`handle`** (output_control)  handle(-array) `→` [HHandle](HHandle.md), [HTuple](HTuple.md) (*IntPtr*)

The handle as handle.

## Result

If the parameters are valid, the operator `IntegerToHandle`
returns the value 2 (
H_MSG_TRUE)
. Otherwise, an exception is raised.

## See also

`HandleToInteger`

## Module

Foundation
