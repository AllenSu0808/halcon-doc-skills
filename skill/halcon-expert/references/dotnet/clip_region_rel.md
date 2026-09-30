# ClipRegionRel (Operator)

## Name

`ClipRegionRel` — Clip a region relative to its smallest surrounding rectangle.

## Signature

`static void HOperatorSet.ClipRegionRel(HObject region, out HObject regionClipped, HTuple top, HTuple bottom, HTuple left, HTuple right)`

`HRegion HRegion.ClipRegionRel(int top, int bottom, int left, int right)`

## Description

`ClipRegionRel` reduces the *`region`* by eliminating
parts close to the smallest surrounding rectangle of the
*`region`*. Specifically this means that the *`region`* is
clipped to a rectangle that is smaller than or equal to the smallest
surrounding rectangle. The resulting clipped region is returned in
*`regionClipped`*.

The rectangle to which the *`region`* is clipped is determined by
reducing the smallest surrounding axis-parallel rectangle at the top,
bottom, left, and right side by the values given in *`top`*,
*`bottom`*, *`left`*, and *`right`*, respectively.

|  |  |
| --- | --- |
| ![figure](../assets/2b2726634b88691b.svg) | ![figure](../assets/04e4596e94b03a55.svg) |
| ( 1) | ( 2) |

Region with smallest surrounding rectangle (1) and clipped region (2).

These four parameters must contain numbers larger or equal to zero. If
all parameters are set to zero, the region remains unchanged.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Regions to be clipped.

**`regionClipped`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Clipped regions.

**`top`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of rows clipped at the top.

Default:
1

Suggested values:
0, 1, 2, 3, 4, 5, 7, 10, 20, 30, 50

Value range:
`0
≤
top` (lin)

Minimum increment:
1

Recommended increment:
1

**`bottom`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of rows clipped at the bottom.

Default:
1

Suggested values:
0, 1, 2, 3, 4, 5, 7, 10, 20, 30, 50

Value range:
`0
≤
bottom` (lin)

Minimum increment:
1

Recommended increment:
1

**`left`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of columns clipped at the left.

Default:
1

Suggested values:
0, 1, 2, 3, 4, 5, 7, 10, 20, 30, 50

Value range:
`0
≤
left` (lin)

Minimum increment:
1

Recommended increment:
1

**`right`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of columns clipped at the right.

Default:
1

Suggested values:
0, 1, 2, 3, 4, 5, 7, 10, 20, 30, 50

Value range:
`0
≤
right` (lin)

Minimum increment:
1

Recommended increment:
1

## Result

`ClipRegionRel` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. The behavior in case of empty input (no regions given) can
be set via `set_system('no_object_result',<Result>)`
and the behavior in case of an empty input region via
`set_system('empty_region_result',<Result>)`.
If necessary, an exception is raised.

## Possible Predecessors

`Threshold`,
`Connection`,
`Regiongrowing`,
`Pouring`

## Possible Successors

`SelectShape`,
`DispRegion`

## Alternatives

`SmallestRectangle1`,
`Intersection`,
`GenRectangle1`,
`ClipRegion`

## Module

Foundation
