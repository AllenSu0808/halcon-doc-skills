# handle_to_integer (Operator)

## Name

`handle_to_integer` — Convert a handle into an integer.

## Warning

**It is not recommended to use this operator in HDevelop.
This operator is only provided for reasons of backward compatibility.**

## Signature

`handle_to_integer( : : Handle : CastedHandle)`

## Description

`handle_to_integer` converts the handle *`Handle`* into an
integer representation and returns it in *`CastedHandle`*.

The ownership of the handle is not transferred. Once all instances of the
handle, such as in the tuple *`Handle`*, were overwritten, the handle
and its content will be destroyed and *`CastedHandle`* will become
invalid.

## Attention

It is not recommended to use this operator in HDevelop.
It is solely provided to enable backward compatibility with legacy code.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Handle`** (input_control)  handle(-array) `→`  (handle)

The handle to be cast.

**`CastedHandle`** (output_control)  pointer(-array) `→`  (integer)

The handle cast to an integer value.

## Result

If the parameters are valid, the operator `handle_to_integer`
returns the value 2 (
H_MSG_TRUE)
. Otherwise, an exception is raised.

## See also

`integer_to_handle`

## Module

Foundation
