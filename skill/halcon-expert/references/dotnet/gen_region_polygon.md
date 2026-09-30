# GenRegionPolygon (Operator)

## Name

`GenRegionPolygon` — Store a polygon as a region.

## Signature

`static void HOperatorSet.GenRegionPolygon(out HObject region, HTuple rows, HTuple columns)`

`void HRegion.GenRegionPolygon(HTuple rows, HTuple columns)`

## Description

The operator `GenRegionPolygon` creates a region from a polygon
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

**`region`** (output_object)  region `→` [HRegion](HRegion.md)

Created region.

**`rows`** (input_control)  polygon.y-array `→` [HTuple](HTuple.md) (*int* / long)

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

**`columns`** (input_control)  polygon.x-array `→` [HTuple](HTuple.md) (*int* / long)

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

## Example (HDevelop)

```
* Polygon-approximation
get_region_polygon(Region,7,Row,Column)
* store it as a region
gen_region_polygon(Pol,Row,Column)
* fill up the hole
fill_up(Pol,Filled)
```

## Result

If the base points are correct the operator `GenRegionPolygon`
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

`GenRegionPolygonFilled`,
`GenRegionPoints`,
`GenRegionRuns`

## See also

`FillUp`,
`ReduceDomain`,
`GetRegionPolygon`,
`DrawPolygon`

## Module

Foundation
