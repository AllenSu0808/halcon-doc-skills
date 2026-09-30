# fill_up (Operator)

## Name

`fill_up` — Fill up holes in regions.

## Signature

`def fill_up(region: HObject) -> HObject`

## Description

`fill_up` fills up holes in regions. The number of
regions remains unchanged. The neighborhood type is set via
`set_system('neighborhood',<4/8>)` (default:
8-neighborhood).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region`** (input_object)  region(-array) `→` HObject

Input regions containing holes.

**`region_fill_up`** (output_object)  region(-array) `→` HObject

Regions without holes.

## Result

`fill_up` returns 2 (
H_MSG_TRUE)
if all parameters are correct. The
behavior in case of empty input (no regions given) can be set via
`set_system('no_object_result',<Result>)`
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

`fill_up_shape`

## See also

`boundary`

## Module

Foundation
