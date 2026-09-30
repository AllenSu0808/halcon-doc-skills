# integer_to_obj (Operator)

## Name

`integer_to_obj` — Convert an “integer number” into an iconic object.

## Signature

`def integer_to_obj(surrogate_tuple: MaybeSequence[int]) -> HObject`

## Description

`integer_to_obj` is the inverse operator to
[`obj_to_integer`](obj_to_integer.md). All surrogates of objects passed in
*`surrogate_tuple`* are stored as objects. In contrast to
[`obj_to_integer`](obj_to_integer.md), the objects are duplicated.
`integer_to_obj` is intended especially for use in
HALCON/C, because iconic objects and control parameters are treated
differently in C. Please note that if you pass the value *0* in
*`surrogate_tuple`*, the program will crash because *0* is no
valid pointer.

For a short description of the iconic objects that are available in HALCON
see the introduction of chapter [Object](toc_object.md).

## Attention

The objects are duplicated in the database.

## Execution Information

- Supports objects on compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`objects`** (output_object)  object(-array) `→` HObject

Created objects.

**`surrogate_tuple`** (input_control)  pointer(-array) `→` MaybeSequence[int]

Tuple of object surrogates.

## Result

`integer_to_obj` returns 2 (
H_MSG_TRUE)
if all parameters are
correct, i.e., if they are valid object keys. If the input is empty
the behavior can be set via
`set_system(::'no_object_result',<Result>:)`.
If necessary, an exception is raised.

## See also

`obj_to_integer`

## Module

Foundation
