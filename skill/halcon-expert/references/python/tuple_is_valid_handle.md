# tuple_is_valid_handle (Operator)

## Name

`tuple_is_valid_handle` — Check if a handle is valid.

## Signature

`def tuple_is_valid_handle(handle: MaybeSequence[HHandle]) -> Sequence[int]`

`def tuple_is_valid_handle_s(handle: MaybeSequence[HHandle]) -> int`

## Description

`tuple_is_valid_handle` returns *1* in *`is_valid`* if
*`handle`* is a valid handle that has not been cleared, and *0*
otherwise.

If multiple handles are passed in *`handle`*, a
validity value will be returned for each of them in *`is_valid`*.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_is_valid_handle`,
which can be used in an expression in the following syntax:

[`IsValid := is_valid_handle(Handle)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_type_0000.html)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`handle`** (input_control)  tuple(-array) `→` MaybeSequence[HHandle]

The handle to check for validity.

**`is_valid`** (output_control)  integer(-array) `→` Sequence[int]

The validity of the handle, *1* or *0*.

## Result

If the parameters are valid, the operator `tuple_is_valid_handle`
returns the value 2 (
H_MSG_TRUE)
. Otherwise, an exception is raised.

## Module

Foundation
