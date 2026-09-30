# gen_region_points (Operator)

## Name

`gen_region_points` — Store individual pixels as image region.

## Signature

`def gen_region_points(rows: MaybeSequence[Union[int, float]], columns: MaybeSequence[Union[int, float]]) -> HObject`

## Description

The operator `gen_region_points` creates a region described by a number
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

**`region`** (output_object)  region `→` HObject

Created region.

**`rows`** (input_control)  coordinates.y(-array) `→` MaybeSequence[Union[int, float]]

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

**`columns`** (input_control)  coordinates.x(-array) `→` MaybeSequence[Union[int, float]]

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

The operator `gen_region_points` returns the value 2 (
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

`get_region_points`

## Possible Successors

`paint_region`,
`reduce_domain`

## Alternatives

`gen_region_polygon`,
`gen_region_runs`,
`gen_region_line`

## See also

`reduce_domain`

## Module

Foundation
