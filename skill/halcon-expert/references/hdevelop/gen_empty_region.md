# gen_empty_region (Operator)

## Name

`gen_empty_region` — Create an empty region.

## Signature

`gen_empty_region( : EmptyRegion : : )`

## Description

The operator `gen_empty_region` creates an empty region.
This means that the output parameter contains an object.
Thus, [`count_obj`](count_obj.md) returns 1.
The area of the region is 0. Most of the
shape features are undefined (0).
It should be noted that an empty region must not
be confused with the empty tuple.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`EmptyRegion`** (output_object)  region `→` object

Empty region (no pixels).

## Module

Foundation
