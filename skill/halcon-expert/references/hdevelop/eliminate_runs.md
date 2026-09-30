# eliminate_runs (Operator)

## Name

`eliminate_runs` — Eliminate runs of a given length.

## Signature

`eliminate_runs(Region : RegionClipped : ElimShorter, ElimLonger : )`

## Description

`eliminate_runs` eliminates all runs of the
run length encoding of the input regions which are shorter
than *`ElimShorter`* or longer as
*`ElimLonger`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Region`** (input_object)  region(-array) `→` object

Region to be clipped.

**`RegionClipped`** (output_object)  region(-array) `→` object

Clipped regions.

**`ElimShorter`** (input_control)  integer `→`  (integer)

All runs which are shorter are eliminated.

Default:
3

Suggested values:
2, 3, 4, 5, 6, 8, 10, 12, 15

Value range:
`1
≤
ElimShorter
≤
500` (lin)

Minimum increment:
1

Recommended increment:
1

**`ElimLonger`** (input_control)  integer `→`  (integer)

All runs which are longer are eliminated.

Default:
1000

Suggested values:
50, 100, 200, 500, 1000, 2000

Value range:
`1
≤
ElimLonger
≤
10000` (lin)

Minimum increment:
1

Recommended increment:
10

## Result

`eliminate_runs` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
The behavior in case of empty input (no regions given) can be set
via `set_system('no_object_result',<Result>)`
and the behavior in case of an empty input region via
`set_system('empty_region_result',<Result>)`.
If necessary, an exception is raised.

## Possible Predecessors

`threshold`,
`connection`,
`regiongrowing`,
`pouring`

## Possible Successors

`erosion1`,
`dilation1`,
`disp_region`

## Alternatives

`shape_trans`

## Module

Foundation
