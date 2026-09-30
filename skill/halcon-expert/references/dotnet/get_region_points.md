# GetRegionPoints (Operator)

## Name

`GetRegionPoints` — Access the pixels of a region.

## Signature

`static void HOperatorSet.GetRegionPoints(HObject region, out HTuple rows, out HTuple columns)`

`void HRegion.GetRegionPoints(out HTuple rows, out HTuple columns)`

## Description

The operator `GetRegionPoints` returns the region data in the form
of coordinate lists. The coordinates are sorted in the following
order:

$$(r_{1},c_{1})\le(r_{2},c_{2}):=(r_{1}<r_{2})\vee(r_{1}=r_{2})\wedge(c1\le c2)$$
`GetRegionPoints` returns the coordinates in the form of tuples.
An empty region is passed as empty tuple.

## Attention

Only one region may be passed.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region`** (input_object)  region `→` [HRegion](HRegion.md)

This region is accessed.

**`rows`** (output_control)  coordinates.y-array `→` [HTuple](HTuple.md) (*int* / long)

Line numbers of the pixels in the region

**`columns`** (output_control)  coordinates.x-array `→` [HTuple](HTuple.md) (*int* / long)

Column numbers of the pixels in the region.

Number of elements:
Columns == Rows

## Result

The operator `GetRegionPoints` normally returns the value 2 (
H_MSG_TRUE)
.
If more than one connection component is passed an exception is raised.
The behavior in case of empty input (no input regions available) is set via
the operator `set_system('no_object_result',<Result>)`.

## Possible Predecessors

`SobelAmp`,
`Threshold`,
`Connection`

## Alternatives

`GetRegionRuns`

## See also

`CopyObj`,
`GenRegionPoints`

## Module

Foundation
