# union1 (Operator)

## Name

`union1` — Return the union of all input regions.

## Signature

`def union1(region: HObject) -> HObject`

## Description

`union1` computes the union of all input regions and
returns the result in *`region_union`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region`** (input_object)  region-array `→` HObject

Regions of which the union is to be computed.

**`region_union`** (output_object)  region `→` HObject

Union of all input regions.

Number of elements:
RegionUnion <= Region

## Complexity

Let F be the sum of all areas of the input regions. Then the
runtime complexity is O(log(sqrt(F)) * sqrt(F)).

## Result

`union1` always returns 2 (
H_MSG_TRUE)
. The behavior in case of
empty input (no regions given) can be set via
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

`union2`

## See also

`intersection`,
`complement`

## Module

Foundation
