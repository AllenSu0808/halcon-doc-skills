# GenEmptyObj (Operator)

## Name

`GenEmptyObj` — Create an empty object tuple.

## Signature

`static void HOperatorSet.GenEmptyObj(out HObject emptyObject)`

`void HObject.GenEmptyObj()`

## Description

The operator `GenEmptyObj` creates an empty tuple.
This means that the output parameter does not contain any objects.
Thus, the operator [`CountObj`](count_obj.md) returns 0.
However, [`ClearObj`](clear_obj.md) can be called for the output.
It should be noted that no objects must not be confused
with an empty region. In case of an empty region,
i.e. a region with 0 pixels [`CountObj`](count_obj.md) returns
the value 1.

For a short description of the iconic objects that are available in HALCON
see the introduction of chapter [Object](toc_object.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`emptyObject`** (output_object)  object `→` [HObject](HObject.md)

No objects.

## Module

Foundation
