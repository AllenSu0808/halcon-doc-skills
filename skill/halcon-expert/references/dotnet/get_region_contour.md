# GetRegionContour (Operator)

## Name

`GetRegionContour` — Access the contour of an object.

## Signature

`static void HOperatorSet.GetRegionContour(HObject region, out HTuple rows, out HTuple columns)`

`void HRegion.GetRegionContour(out HTuple rows, out HTuple columns)`

## Description

The operator `GetRegionContour` returns the contour of a region.
A contour is a result
of line (*`rows`*) and column coordinates (*`columns`*),
describing the boundary
of the region. The contour lies on the region.
It starts at the smallest line number. In that line at the
pixel with the largest column index.
The rotation direction is clockwise. The first pixel of the contour
is identical with the last. Holes of the region are ignored.
The operator `GetRegionContour` returns the coordinates in the form of
tuples. An empty region is passed as empty tuple.

## Attention

Holes of the region are ignored.
Only one region may be passed, and this region must have exactly
one connection component.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region`** (input_object)  region `→` [HRegion](HRegion.md)

Output region.

**`rows`** (output_control)  contour.y-array `→` [HTuple](HTuple.md) (*int* / long)

Line numbers of the contour pixels.

**`columns`** (output_control)  contour.x-array `→` [HTuple](HTuple.md) (*int* / long)

Column numbers of the contour pixels.

Number of elements:
Columns == Rows

## Result

The operator `GetRegionContour` normally returns the value 2 (
H_MSG_TRUE)
.
If more than one connection component is passed an exception is raised.
The behavior in case of empty input (no input regions available) is set via
the operator `set_system('no_object_result',<Result>)`.

## Possible Predecessors

`SobelAmp`,
`Threshold`,
`Skeleton`,
`EdgesImage`,
`GenRectangle1`,
`GenCircle`

## See also

`CopyObj`,
`GetRegionPolygon`

## Module

Foundation
