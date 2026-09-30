# GetRegionChain (Operator)

## Name

`GetRegionChain` — Contour of an object as chain code.

## Warning

**`GetRegionChain` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`static void HOperatorSet.GetRegionChain(HObject region, out HTuple row, out HTuple column, out HTuple chain)`

`void HRegion.GetRegionChain(out int row, out int column, out HTuple chain)`

## Description

The operator `GetRegionChain` returns the contour of a region.
A contour is a series of
pixels describing the outline of the region.
The contour “lies on” the region.
It starts at the smallest line number;
in that line at the pixel with the largest column index.
The rotation occurs clockwise.
Holes of the region are ignored.
The direction code (chain code) is defined as follows:

3 2 1
4 * 0
5 6 7
The operator `GetRegionChain` returns the code in the form of a tuple.
In case of an empty region the parameters *`row`* and
*`column`* are zero and *`chain`* is the empty tuple.

## Attention

Holes of the region are ignored.
Only one region may be passed, and it must have exactly one
connection component.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region`** (input_object)  region `→` [HRegion](HRegion.md)

Region to be transformed.

**`row`** (output_control)  chain.begin.y `→` [HTuple](HTuple.md) (*int* / long)

Line of starting point.

**`column`** (output_control)  chain.begin.x `→` [HTuple](HTuple.md) (*int* / long)

Column of starting point.

**`chain`** (output_control)  chain.code-array `→` [HTuple](HTuple.md) (*int* / long)

Direction code of the contour (from starting point).

Value range:
`0
≤
chain
≤
7`

## Result

The operator `GetRegionChain` normally returns the value 2 (
H_MSG_TRUE)
.
If more than one connection component is passed an exception is raised.
The behavior in case of empty input (no input regions available) is set via
the operator `set_system('no_object_result',<Result>)`.
The behavior in case of empty region (the region is the empty set) is set via
the operator `set_system('empty_region_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`SobelAmp`,
`Threshold`,
`Skeleton`,
`EdgesImage`,
`GenRectangle1`,
`GenCircle`

## Possible Successors

`ApproxChain`,
`ApproxChainSimple`

## See also

`CopyObj`,
`GetRegionContour`,
`GetRegionPolygon`

## Module

Foundation
