# IntegerToObj (Operator)

## Name

`IntegerToObj` — Convert an “integer number” into an iconic object.

## Signature

`static void HOperatorSet.IntegerToObj(out HObject objects, HTuple surrogateTuple)`

`void HObject.IntegerToObj(HTuple surrogateTuple)`

`void HObject.IntegerToObj(IntPtr surrogateTuple)`

## Description

`IntegerToObj` is the inverse operator to
[`ObjToInteger`](obj_to_integer.md). All surrogates of objects passed in
*`surrogateTuple`* are stored as objects. In contrast to
[`ObjToInteger`](obj_to_integer.md), the objects are duplicated.
`IntegerToObj` is intended especially for use in
HALCON/C, because iconic objects and control parameters are treated
differently in C. Please note that if you pass the value *0* in
*`surrogateTuple`*, the program will crash because *0* is no
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

**`objects`** (output_object)  object(-array) `→` [HObject](HObject.md)

Created objects.

**`surrogateTuple`** (input_control)  pointer(-array) `→` [HTuple](HTuple.md) (*IntPtr*)

Tuple of object surrogates.

## Result

`IntegerToObj` returns 2 (
H_MSG_TRUE)
if all parameters are
correct, i.e., if they are valid object keys. If the input is empty
the behavior can be set via
`set_system(::'no_object_result',<Result>:)`.
If necessary, an exception is raised.

## See also

`ObjToInteger`

## Module

Foundation
