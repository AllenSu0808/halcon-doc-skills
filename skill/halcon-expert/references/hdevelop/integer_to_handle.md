# integer_to_handle (Operator)

## Name

`integer_to_handle` — Convert an integer into a handle.

## Warning

**It is not recommended to use this operator in HDevelop.
This operator is only provided for reasons of backward compatibility.**

## Signature

`integer_to_handle( : : IntegerHandle : Handle)`

## Description

`integer_to_handle` converts the integer *`IntegerHandle`*, that
represents a handle, to a handle of type HANDLE_PAR and returns it in
*`Handle`*.

The ownership of the handle is transferred onto the handle. The handle will
automatically be cleared once all references to that handle, such as in the
tuple *`Handle`*, are overwritten. If the original *`IntegerHandle`*
should continue to be used, a reference to the returned *`Handle`* must
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

**`IntegerHandle`** (input_control)  pointer(-array) `→`  (integer)

The handle as integer.

**`Handle`** (output_control)  handle(-array) `→`  (handle)

The handle as handle.

## Result

If the parameters are valid, the operator `integer_to_handle`
returns the value 2 (
H_MSG_TRUE)
. Otherwise, an exception is raised.

## See also

`handle_to_integer`

## Module

Foundation
