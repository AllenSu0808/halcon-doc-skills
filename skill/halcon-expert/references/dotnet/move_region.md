# MoveRegion (Operator)

## Name

`MoveRegion` — Translate a region.

## Signature

`static void HOperatorSet.MoveRegion(HObject region, out HObject regionMoved, HTuple row, HTuple column)`

`HRegion HRegion.MoveRegion(int row, int column)`

## Description

`MoveRegion` translates the input regions by the vector given by
(*`row`*, *`column`*). If necessary, the resulting
regions are clipped with the current image format.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Region(s) to be moved.

**`regionMoved`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Translated region(s).

Number of elements:
RegionMoved == Region

**`row`** (input_control)  point.y `→` [HTuple](HTuple.md) (*int* / long)

Row coordinate of the vector by which the
region is to be moved.

Default:
30

Suggested values:
-128, -64, -32, -16, -10, -8, -4, -2, -1, 0, 1, 2, 4, 5, 8, 10, 16, 32, 64, 128

Value range:
`-512
≤
row
≤
512` (lin)

Minimum increment:
1

Recommended increment:
10

**`column`** (input_control)  point.x `→` [HTuple](HTuple.md) (*int* / long)

Row coordinate of the vector by which the
region is to be moved.

Default:
30

Suggested values:
-128, -64, -32, -16, -10, -8, -4, -2, -1, 0, 1, 2, 4, 5, 8, 10, 16, 32, 64, 128

Value range:
`-512
≤
column
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

`MoveRegion` always returns the value 2 (
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

`Threshold`,
`Connection`,
`Regiongrowing`,
`Pouring`

## Possible Successors

`SelectShape`,
`DispRegion`

## See also

`AffineTransImage`,
`MirrorRegion`,
`ZoomRegion`

## Module

Foundation
