# obj_diff (Operator)

## Name

`obj_diff` — Calculate the difference of two object tuples.

## Signature

`def obj_diff(objects: HObject, objects_sub: HObject) -> HObject`

## Description

`obj_diff` calculates the set-theoretic difference of
two object tuples:
(objects in Objects) - (objects in ObjectsSub)
The resulting object tuple *`objects_diff`*
is defined as the input tuple
*`objects`* with all objects from *`objects_sub`* removed.

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

**`objects`** (input_object)  object(-array) `→` HObject

Object tuple 1.

**`objects_sub`** (input_object)  object(-array) `→` HObject

Object tuple 2.

**`objects_diff`** (output_object)  object(-array) `→` HObject

Objects from *`objects`* that are not part of
*`objects_sub`*.

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
