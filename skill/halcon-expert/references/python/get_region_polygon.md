# get_region_polygon (Operator)

## Name

`get_region_polygon` — Polygon approximation of a region.

## Signature

`def get_region_polygon(region: HObject, tolerance: Union[int, float]) -> Tuple[Sequence[int], Sequence[int]]`

## Description

The operator `get_region_polygon` calculates a polygon to approximate the
edge of a region. A polygon is a sequence of line (*`rows`*) and
column coordinates (*`columns`*). It describes the contour of the region.
Only the base points of the polygon are returned.
The parameter *`tolerance`* indicates how large the maximum distance
between the polygon and the edge of the region may be.
Holes of the region are ignored.
The operator `get_region_polygon` returns the coordinates in the form of tuples.

## Attention

Holes of the region are ignored.
Only one region may be passed, and this region must have exactly
one connection component.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region`** (input_object)  region `→` HObject

Region to be approximated.

**`tolerance`** (input_control)  number `→` Union[int, float]

Maximum distance between the polygon and the
edge of the region.

Default:
5.0

Suggested values:
0.0, 2.0, 5.0, 10.0

Value range:
`0.0
≤
tolerance` (lin)

Minimum increment:
0.01

Recommended increment:
1.0

**`rows`** (output_control)  polygon.y-array `→` Sequence[int]

Line numbers of the base points of the contour.

**`columns`** (output_control)  polygon.x-array `→` Sequence[int]

Column numbers of the base points of the contour.

Number of elements:
Columns == Rows

## Result

The operator `get_region_polygon` normally returns the value 2 (
H_MSG_TRUE)
.
If more than one connection component is passed an exception is raised.
The behavior in case of empty input (no input regions available) is set via
the operator `set_system('no_object_result',<Result>)`.

## Possible Predecessors

`sobel_amp`,
`threshold`,
`skeleton`,
`edges_image`

## See also

`copy_obj`,
`gen_region_polygon`,
`disp_polygon`,
`get_region_contour`,
`set_line_approx`

## Module

Foundation
