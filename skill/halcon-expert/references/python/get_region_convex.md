# get_region_convex (Operator)

## Name

`get_region_convex` — Access convex hull as contour.

## Signature

`def get_region_convex(region: HObject) -> Tuple[Sequence[int], Sequence[int]]`

## Description

The operator `get_region_convex` returns the convex hull of a region
as polygon. The polygon is the minimum result
of line (*`rows`*) and column coordinates (*`columns`*)
describing the hull of the region. The polygon pixels lie
on the region.
The polygon starts at the smallest line number; in this line at the
pixel with the largest column index.
The rotation direction is clockwise. The first pixel of the polygon
is identical with the last.
The operator `get_region_convex` returns the coordinates in the form
of tuples. An empty region is passed as empty tuple.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region`** (input_object)  region `→` HObject

Output region.

**`rows`** (output_control)  contour.y-array `→` Sequence[int]

Line numbers of contour pixels.

**`columns`** (output_control)  contour.x-array `→` Sequence[int]

Column numbers of the contour pixels.

Number of elements:
Columns == Rows

## Result

The operator `get_region_convex` returns the value 2 (
H_MSG_TRUE)
.

## Possible Predecessors

`threshold`,
`skeleton`,
`dyn_threshold`

## Possible Successors

`disp_polygon`

## Alternatives

`shape_trans`

## See also

`select_obj`,
`get_region_contour`

## Module

Foundation
