# clip_region_rel (Operator)

## Name

`clip_region_rel` — Clip a region relative to its smallest surrounding rectangle.

## Signature

`clip_region_rel(Region : RegionClipped : Top, Bottom, Left, Right : )`

## Description

`clip_region_rel` reduces the *`Region`* by eliminating
parts close to the smallest surrounding rectangle of the
*`Region`*. Specifically this means that the *`Region`* is
clipped to a rectangle that is smaller than or equal to the smallest
surrounding rectangle. The resulting clipped region is returned in
*`RegionClipped`*.

The rectangle to which the *`Region`* is clipped is determined by
reducing the smallest surrounding axis-parallel rectangle at the top,
bottom, left, and right side by the values given in *`Top`*,
*`Bottom`*, *`Left`*, and *`Right`*, respectively.

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

**`Region`** (input_object)  region(-array) `→` object

Regions to be clipped.

**`RegionClipped`** (output_object)  region(-array) `→` object

Clipped regions.

**`Top`** (input_control)  integer `→`  (integer)

Number of rows clipped at the top.

Default:
1

Suggested values:
0, 1, 2, 3, 4, 5, 7, 10, 20, 30, 50

Value range:
`0
≤
Top` (lin)

Minimum increment:
1

Recommended increment:
1

**`Bottom`** (input_control)  integer `→`  (integer)

Number of rows clipped at the bottom.

Default:
1

Suggested values:
0, 1, 2, 3, 4, 5, 7, 10, 20, 30, 50

Value range:
`0
≤
Bottom` (lin)

Minimum increment:
1

Recommended increment:
1

**`Left`** (input_control)  integer `→`  (integer)

Number of columns clipped at the left.

Default:
1

Suggested values:
0, 1, 2, 3, 4, 5, 7, 10, 20, 30, 50

Value range:
`0
≤
Left` (lin)

Minimum increment:
1

Recommended increment:
1

**`Right`** (input_control)  integer `→`  (integer)

Number of columns clipped at the right.

Default:
1

Suggested values:
0, 1, 2, 3, 4, 5, 7, 10, 20, 30, 50

Value range:
`0
≤
Right` (lin)

Minimum increment:
1

Recommended increment:
1

## Result

`clip_region_rel` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. The behavior in case of empty input (no regions given) can
be set via `set_system('no_object_result',<Result>)`
and the behavior in case of an empty input region via
`set_system('empty_region_result',<Result>)`.
If necessary, an exception is raised.

## Possible Predecessors

`threshold`,
`connection`,
`regiongrowing`,
`pouring`

## Possible Successors

`select_shape`,
`disp_region`

## Alternatives

`smallest_rectangle1`,
`intersection`,
`gen_rectangle1`,
`clip_region`

## Module

Foundation
