# GenRegionPoints (Operator)

## Name

`GenRegionPoints` — Store individual pixels as image region.

## Signature

`static void HOperatorSet.GenRegionPoints(out HObject region, HTuple rows, HTuple columns)`

`void HRegion.GenRegionPoints(HTuple rows, HTuple columns)`

`void HRegion.GenRegionPoints(int rows, int columns)`

## Description

The operator `GenRegionPoints` creates a region described by a number
of pixels. The pixels do not have to be stored in a fixed
order, but the best runtime behavior is obtained when the pixels are
stored in ascending order. The order is as follows:

$$(l_{1},c_{1})\le(l_{2},c_{2}):=(l_{1}<l_{2})\vee(l_{1}=l_{2})\wedge(c_{1}\le c_{2})$$
The indicated coordinates stand for two consecutive pixels in the tuple.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`region`** (output_object)  region `→` [HRegion](HRegion.md)

Created region.

**`rows`** (input_control)  coordinates.y(-array) `→` [HTuple](HTuple.md) (*int* / long / double)

Lines of the pixels in the region.

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

**`columns`** (input_control)  coordinates.x(-array) `→` [HTuple](HTuple.md) (*int* / long / double)

Columns of the pixels in the region.

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

## Complexity

F shall be the number of pixels.
If the pixels are sorted in ascending order the runtime complexity
is: O(F), otherwise O(log(F)*F).

## Result

The operator `GenRegionPoints` returns the value 2 (
H_MSG_TRUE)
if the pixels
are located within the image format.
Otherwise an exception is raised.
The clipping according to the current image format is set via the
operator `set_system('clip_region',<'true'/'false'>)`.
If an empty region is created (by the clipping or by an empty input)
the operator
`set_system('store_empty_region',<'true'/'false'>)` determines
whether the region is returned or an empty object tuple.

## Possible Predecessors

`GetRegionPoints`

## Possible Successors

`PaintRegion`,
`ReduceDomain`

## Alternatives

`GenRegionPolygon`,
`GenRegionRuns`,
`GenRegionLine`

## See also

`ReduceDomain`

## Module

Foundation
