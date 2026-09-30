# GetRegionConvex (Operator)

## Name

`GetRegionConvex` — Access convex hull as contour.

## Signature

`static void HOperatorSet.GetRegionConvex(HObject region, out HTuple rows, out HTuple columns)`

`void HRegion.GetRegionConvex(out HTuple rows, out HTuple columns)`

## Description

The operator `GetRegionConvex` returns the convex hull of a region
as polygon. The polygon is the minimum result
of line (*`rows`*) and column coordinates (*`columns`*)
describing the hull of the region. The polygon pixels lie
on the region.
The polygon starts at the smallest line number; in this line at the
pixel with the largest column index.
The rotation direction is clockwise. The first pixel of the polygon
is identical with the last.
The operator `GetRegionConvex` returns the coordinates in the form
of tuples. An empty region is passed as empty tuple.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region`** (input_object)  region `→` [HRegion](HRegion.md)

Output region.

**`rows`** (output_control)  contour.y-array `→` [HTuple](HTuple.md) (*int* / long)

Line numbers of contour pixels.

**`columns`** (output_control)  contour.x-array `→` [HTuple](HTuple.md) (*int* / long)

Column numbers of the contour pixels.

Number of elements:
Columns == Rows

## Result

The operator `GetRegionConvex` returns the value 2 (
H_MSG_TRUE)
.

## Possible Predecessors

`Threshold`,
`Skeleton`,
`DynThreshold`

## Possible Successors

`DispPolygon`

## Alternatives

`ShapeTrans`

## See also

`SelectObj`,
`GetRegionContour`

## Module

Foundation
