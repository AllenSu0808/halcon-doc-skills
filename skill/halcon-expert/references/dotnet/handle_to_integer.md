# HandleToInteger (Operator)

## Name

`HandleToInteger` — Convert a handle into an integer.

## Warning

**It is not recommended to use this operator in HDevelop.
This operator is only provided for reasons of backward compatibility.**

## Signature

`static void HOperatorSet.HandleToInteger(HTuple handle, out HTuple castedHandle)`

## Description

`HandleToInteger` converts the handle *`handle`* into an
integer representation and returns it in *`castedHandle`*.

The ownership of the handle is not transferred. Once all instances of the
handle, such as in the tuple *`handle`*, were overwritten, the handle
and its content will be destroyed and *`castedHandle`* will become
invalid.

## Attention

It is not recommended to use this operator in HDevelop.
It is solely provided to enable backward compatibility with legacy code.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`handle`** (input_control)  handle(-array) `→` [HHandle](HHandle.md), [HTuple](HTuple.md) (*IntPtr*)

The handle to be cast.

**`castedHandle`** (output_control)  pointer(-array) `→` [HTuple](HTuple.md) (*IntPtr*)

The handle cast to an integer value.

## Result

If the parameters are valid, the operator `HandleToInteger`
returns the value 2 (
H_MSG_TRUE)
. Otherwise, an exception is raised.

## See also

`IntegerToHandle`

## Module

Foundation
