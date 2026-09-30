# gen_region_polygon (Operator)

## Name

`gen_region_polygon` — Store a polygon as a region.

## Signature

`def gen_region_polygon(rows: Sequence[int], columns: Sequence[int]) -> HObject`

## Description

The operator `gen_region_polygon` creates a region from a polygon
row described by
a series of line and column coordinates. The created
region
consists of the pixels of the routes defined thereby, wherein it is linearly
interpolated between the base points.

## Attention

The region is not automatically closed and not filled.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`region`** (output_object)  region `→` HObject

Created region.

**`rows`** (input_control)  polygon.y-array `→` Sequence[int]

Line indices of the base points of the region contour.

Default:
100

Suggested values:
0, 10, 30, 50, 100, 200, 300, 500

Value range:
`rows` (lin)

Minimum increment:
1

Recommended increment:
1

**`columns`** (input_control)  polygon.x-array `→` Sequence[int]

Column indices of the base points of the region
contour.

Number of elements:
Columns == Rows

Default:
100

Suggested values:
0, 10, 30, 50, 100, 200, 300, 500

Value range:
`columns` (lin)

Minimum increment:
1

Recommended increment:
1

## Result

If the base points are correct the operator `gen_region_polygon`
returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.
The clipping according to the current image format is set via the
operator `set_system('clip_region',<'true'/'false'>)`.
If an empty region is created (by the clipping or by an empty input)
the operator
`set_system('store_empty_region',<'true'/'false'>)` determines
whether the region is returned or an empty object tuple.

## Possible Predecessors

`get_region_polygon`,
`draw_polygon`

## Alternatives

`gen_region_polygon_filled`,
`gen_region_points`,
`gen_region_runs`

## See also

`fill_up`,
`reduce_domain`,
`get_region_polygon`,
`draw_polygon`

## Module

Foundation
