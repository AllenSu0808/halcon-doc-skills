# CountObj (Operator)

## Name

`CountObj` — Number of objects in a tuple.

## Signature

`static void HOperatorSet.CountObj(HObject objects, out HTuple number)`

`int HObject.CountObj()`

## Description

The operator `CountObj` determines for the object parameter
*`objects`* the number of objects it contains.
In this connection it should be noted that object is not the same
as connection component (see [`Connection`](connection.md)).
For example, the number of objects of one region consisting of
three parts that are not connected is 1.

For a short description of the iconic objects that are available in HALCON
see the introduction of chapter [Object](toc_object.md).

## Execution Information

- Supports objects on compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`objects`** (input_object)  object-array `→` [HObject](HObject.md)

Objects to be examined.

**`number`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of objects in the tuple *`objects`*.

## Complexity

Runtime complexity: O(|*`objects`*|).

## Result

`CountObj` returns the value 2 (
H_MSG_TRUE)
.

## See also

`CopyObj`,
`ObjToInteger`,
`Connection`,
`SetSystem`

## Module

Foundation
