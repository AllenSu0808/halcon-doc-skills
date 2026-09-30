# obj_diff (Operator)

## Name

`obj_diff` — Calculate the difference of two object tuples.

## Signature

`obj_diff(Objects, ObjectsSub : ObjectsDiff : : )`

## Description

`obj_diff` calculates the set-theoretic difference of
two object tuples:
(objects in Objects) - (objects in ObjectsSub)
The resulting object tuple *`ObjectsDiff`*
is defined as the input tuple
*`Objects`* with all objects from *`ObjectsSub`* removed.

For a short description of the iconic objects that are available in HALCON
see the introduction of chapter [Object](toc_object.md).

## Attention

Image matrices and XLDs are not compared regarding their contents. Thus,
two images or XLDs, respectively, are “equal” if they are located
at the same place in the storage.
By contrast, regions that are not located at the same place in the
storage are compared regarding their actual contents.

## Execution Information

- Supports objects on compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Objects`** (input_object)  object(-array) `→` object

Object tuple 1.

**`ObjectsSub`** (input_object)  object(-array) `→` object

Object tuple 2.

**`ObjectsDiff`** (output_object)  object(-array) `→` object

Objects from *`Objects`* that are not part of
*`ObjectsSub`*.

## Result

`obj_diff` always returns 2 (
H_MSG_TRUE)
.

## See also

`test_equal_obj`,
`count_obj`,
`copy_obj`,
`select_obj`

## Module

Foundation
