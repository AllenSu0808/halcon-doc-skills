# FillUp (Operator)

## Name

`FillUp` — Fill up holes in regions.

## Signature

`static void HOperatorSet.FillUp(HObject region, out HObject regionFillUp)`

`HRegion HRegion.FillUp()`

## Description

`FillUp` fills up holes in regions. The number of
regions remains unchanged. The neighborhood type is set via
`set_system('neighborhood',<4/8>)` (default:
8-neighborhood).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Input regions containing holes.

**`regionFillUp`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Regions without holes.

## Result

`FillUp` returns 2 (
H_MSG_TRUE)
if all parameters are correct. The
behavior in case of empty input (no regions given) can be set via
`set_system('no_object_result',<Result>)`
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

`FillUpShape`

## See also

`Boundary`

## Module

Foundation
