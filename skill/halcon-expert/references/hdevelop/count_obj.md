# count_obj (Operator)

## Name

`count_obj` — Number of objects in a tuple.

## Signature

`count_obj(Objects : : : Number)`

## Description

The operator `count_obj` determines for the object parameter
*`Objects`* the number of objects it contains.
In this connection it should be noted that object is not the same
as connection component (see [`connection`](connection.md)).
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

**`Objects`** (input_object)  object-array `→` object

Objects to be examined.

**`Number`** (output_control)  integer `→`  (integer)

Number of objects in the tuple *`Objects`*.

## Complexity

Runtime complexity: O(|*`Objects`*|).

## Result

`count_obj` returns the value 2 (
H_MSG_TRUE)
.

## See also

`copy_obj`,
`obj_to_integer`,
`connection`,
`set_system`

## Module

Foundation
