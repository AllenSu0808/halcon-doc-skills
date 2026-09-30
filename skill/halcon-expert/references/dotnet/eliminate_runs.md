# EliminateRuns (Operator)

## Name

`EliminateRuns` — Eliminate runs of a given length.

## Signature

`static void HOperatorSet.EliminateRuns(HObject region, out HObject regionClipped, HTuple elimShorter, HTuple elimLonger)`

`HRegion HRegion.EliminateRuns(int elimShorter, int elimLonger)`

## Description

`EliminateRuns` eliminates all runs of the
run length encoding of the input regions which are shorter
than *`elimShorter`* or longer as
*`elimLonger`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Region to be clipped.

**`regionClipped`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Clipped regions.

**`elimShorter`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

All runs which are shorter are eliminated.

Default:
3

Suggested values:
2, 3, 4, 5, 6, 8, 10, 12, 15

Value range:
`1
≤
elimShorter
≤
500` (lin)

Minimum increment:
1

Recommended increment:
1

**`elimLonger`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

All runs which are longer are eliminated.

Default:
1000

Suggested values:
50, 100, 200, 500, 1000, 2000

Value range:
`1
≤
elimLonger
≤
10000` (lin)

Minimum increment:
1

Recommended increment:
10

## Result

`EliminateRuns` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
The behavior in case of empty input (no regions given) can be set
via `set_system('no_object_result',<Result>)`
and the behavior in case of an empty input region via
`set_system('empty_region_result',<Result>)`.
If necessary, an exception is raised.

## Possible Predecessors

`Threshold`,
`Connection`,
`Regiongrowing`,
`Pouring`

## Possible Successors

`Erosion1`,
`Dilation1`,
`DispRegion`

## Alternatives

`ShapeTrans`

## Module

Foundation
