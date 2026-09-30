# get_region_convex (Operator)

## Name

`get_region_convex` — Access convex hull as contour.

## Signature

`get_region_convex(Region : : : Rows, Columns)`

## Description

The operator `get_region_convex` returns the convex hull of a region
as polygon. The polygon is the minimum result
of line (*`Rows`*) and column coordinates (*`Columns`*)
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

**`Region`** (input_object)  region `→` object

Output region.

**`Rows`** (output_control)  contour.y-array `→`  (integer)

Line numbers of contour pixels.

**`Columns`** (output_control)  contour.x-array `→`  (integer)

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
