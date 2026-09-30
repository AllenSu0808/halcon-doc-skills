# GenRegionPolygonFilled (Operator)

## Name

`GenRegionPolygonFilled` — Store a polygon as a “filled” region.

## Signature

`static void HOperatorSet.GenRegionPolygonFilled(out HObject region, HTuple rows, HTuple columns)`

`void HRegion.GenRegionPolygonFilled(HTuple rows, HTuple columns)`

## Description

The operator `GenRegionPolygonFilled` creates a region from
a polygon containing the corner points of the region (line and
column coordinates) either clockwise or anti-clockwise.
Contrary to [`GenRegionPolygon`](gen_region_polygon.md) a “filled” region is
returned here.
Note that for subpixel coordinates *`rows`* and *`columns`* the
coordinates are rounded before the polygon containing the corner points is
determined. Therefore there might be pixels in the *`region`* which
do not lie on the original (subpixel) polygon. An simple alternative in
the case of polygons without holes would be to use the operators
[`GenRegionPolygon`](gen_region_polygon.md) and [`FillUp`](fill_up.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region`** (output_object)  region `→` [HRegion](HRegion.md)

Created region.

**`rows`** (input_control)  polygon.y-array `→` [HTuple](HTuple.md) (*int* / long / double)

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

**`columns`** (input_control)  polygon.x-array `→` [HTuple](HTuple.md) (*int* / long / double)

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

If the base points are correct the operator `GenRegionPolygonFilled`
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

`GetRegionPolygon`,
`DrawPolygon`

## Alternatives

`GenRegionPolygon`,
`GenRegionPoints`,
`DrawPolygon`

## See also

`GenRegionPolygon`,
`ReduceDomain`,
`GetRegionPolygon`,
`GenRegionRuns`

## Module

Foundation
