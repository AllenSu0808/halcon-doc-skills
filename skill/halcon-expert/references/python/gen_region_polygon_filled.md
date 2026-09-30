# gen_region_polygon_filled (Operator)

## Name

`gen_region_polygon_filled` — Store a polygon as a “filled” region.

## Signature

`def gen_region_polygon_filled(rows: Sequence[Union[int, float]], columns: Sequence[Union[int, float]]) -> HObject`

## Description

The operator `gen_region_polygon_filled` creates a region from
a polygon containing the corner points of the region (line and
column coordinates) either clockwise or anti-clockwise.
Contrary to [`gen_region_polygon`](gen_region_polygon.md) a “filled” region is
returned here.
Note that for subpixel coordinates *`rows`* and *`columns`* the
coordinates are rounded before the polygon containing the corner points is
determined. Therefore there might be pixels in the *`region`* which
do not lie on the original (subpixel) polygon. An simple alternative in
the case of polygons without holes would be to use the operators
[`gen_region_polygon`](gen_region_polygon.md) and [`fill_up`](fill_up.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region`** (output_object)  region `→` HObject

Created region.

**`rows`** (input_control)  polygon.y-array `→` Sequence[Union[int, float]]

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

**`columns`** (input_control)  polygon.x-array `→` Sequence[Union[int, float]]

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

## Example (C)

```
/* Polygon approximation */
T_get_region_polygon(Region,7,&Row,&Column);
T_gen_region_polygon_filled(&Pol,Row,Column);
/* fill up with original gray value */
reduce_domain(Image,Pol,&New);
```

## Result

If the base points are correct the operator `gen_region_polygon_filled`
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

`gen_region_polygon`,
`gen_region_points`,
`draw_polygon`

## See also

`gen_region_polygon`,
`reduce_domain`,
`get_region_polygon`,
`gen_region_runs`

## Module

Foundation
