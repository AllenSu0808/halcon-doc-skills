# GenEmptyRegion (Operator)

## Name

`GenEmptyRegion` — Create an empty region.

## Signature

`static void HOperatorSet.GenEmptyRegion(out HObject emptyRegion)`

`void HRegion.GenEmptyRegion()`

## Description

The operator `GenEmptyRegion` creates an empty region.
This means that the output parameter contains an object.
Thus, [`CountObj`](count_obj.md) returns 1.
The area of the region is 0. Most of the
shape features are undefined (0).
It should be noted that an empty region must not
be confused with the empty tuple.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`emptyRegion`** (output_object)  region `→` [HRegion](HRegion.md)

Empty region (no pixels).

## Module

Foundation
