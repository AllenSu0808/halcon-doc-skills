# TupleIsValidHandle (Operator)

## Name

`TupleIsValidHandle` — Check if a handle is valid.

## Signature

`static void HOperatorSet.TupleIsValidHandle(HTuple handle, out HTuple isValid)`

`HTuple HTuple.TupleIsValidHandle()`

`HTuple HHandle.TupleIsValidHandle()`

## Description

`TupleIsValidHandle` returns *1* in *`isValid`* if
*`handle`* is a valid handle that has not been cleared, and *0*
otherwise.

If multiple handles are passed in *`handle`*, a
validity value will be returned for each of them in *`isValid`*.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleIsValidHandle`,
which can be used in an expression in the following syntax:

[`IsValid := is_valid_handle(Handle)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_type_0000.html)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`handle`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*HHandle*)

The handle to check for validity.

**`isValid`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

The validity of the handle, *1* or *0*.

## Result

If the parameters are valid, the operator `TupleIsValidHandle`
returns the value 2 (
H_MSG_TRUE)
. Otherwise, an exception is raised.

## Module

Foundation
