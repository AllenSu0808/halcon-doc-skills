# tuple_is_valid_handle (Operator)

## Name

`tuple_is_valid_handle` — Check if a handle is valid.

## Signature

`tuple_is_valid_handle( : : Handle : IsValid)`

## Description

`tuple_is_valid_handle` returns *1* in *`IsValid`* if
*`Handle`* is a valid handle that has not been cleared, and *0*
otherwise.

If multiple handles are passed in *`Handle`*, a
validity value will be returned for each of them in *`IsValid`*.

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

**`Handle`** (input_control)  tuple(-array) `→`  (handle)

The handle to check for validity.

**`IsValid`** (output_control)  integer(-array) `→`  (integer)

The validity of the handle, *1* or *0*.

## Result

If the parameters are valid, the operator `tuple_is_valid_handle`
returns the value 2 (
H_MSG_TRUE)
. Otherwise, an exception is raised.

## Module

Foundation
