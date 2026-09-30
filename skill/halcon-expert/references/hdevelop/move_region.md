# move_region (Operator)

## Name

`move_region` — Translate a region.

## Signature

`move_region(Region : RegionMoved : Row, Column : )`

## Description

`move_region` translates the input regions by the vector given by
(*`Row`*, *`Column`*). If necessary, the resulting
regions are clipped with the current image format.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Region`** (input_object)  region(-array) `→` object

Region(s) to be moved.

**`RegionMoved`** (output_object)  region(-array) `→` object

Translated region(s).

Number of elements:
RegionMoved == Region

**`Row`** (input_control)  point.y `→`  (integer)

Row coordinate of the vector by which the
region is to be moved.

Default:
30

Suggested values:
-128, -64, -32, -16, -10, -8, -4, -2, -1, 0, 1, 2, 4, 5, 8, 10, 16, 32, 64, 128

Value range:
`-512
≤
Row
≤
512` (lin)

Minimum increment:
1

Recommended increment:
10

**`Column`** (input_control)  point.x `→`  (integer)

Row coordinate of the vector by which the
region is to be moved.

Default:
30

Suggested values:
-128, -64, -32, -16, -10, -8, -4, -2, -1, 0, 1, 2, 4, 5, 8, 10, 16, 32, 64, 128

Value range:
`-512
≤
Column
≤
512` (lin)

Minimum increment:
1

Recommended increment:
10

## Complexity

Let F be the area of the input region. Then the runtime
complexity is O(F).

## Result

`move_region` always returns the value 2 (
H_MSG_TRUE)
. The behavior in
case of empty input (no regions given) can be set via
`set_system('no_object_result',<Result>)`,
the behavior in case of an empty input region via
`set_system('empty_region_result',<Result>)`,
and the behavior in case of an empty result region via
`set_system('store_empty_region',<'true'/'false'>)`.
If necessary, an exception is raised.

## Possible Predecessors

`threshold`,
`connection`,
`regiongrowing`,
`pouring`

## Possible Successors

`select_shape`,
`disp_region`

## See also

`affine_trans_image`,
`mirror_region`,
`zoom_region`

## Module

Foundation
