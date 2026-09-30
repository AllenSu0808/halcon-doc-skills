# euler_number (Operator)

## Name

`euler_number` — Calculate the Euler number.

## Signature

`def euler_number(regions: HObject) -> Sequence[int]`

`def euler_number_s(regions: HObject) -> int`

## Description

The operator `euler_number` calculates the Euler number, i.e., the
difference between the number of connection components and the number of
holes.

In the documentation of this chapter ([Regions / Features](toc_regions_features.md)), you can
find an image illustrating regions which vary in their Euler number.

If more than one region is passed the results are stored in tuples, the index
of a value in the tuple corresponding to the index of a region in the input.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`regions`** (input_object)  region(-array) `→` HObject

Region(s) to be examined.

**`euler_number`** (output_control)  integer(-array) `→` Sequence[int]

Calculated Euler number.

## Result

The operator `euler_number` returns the value 2 (
H_MSG_TRUE)
if the input is not empty.
The behavior in case of empty input (no input regions available) is
set via the operator `set_system('no_object_result',<Result>)`.
The behavior in case of empty region (the region is the empty set) is set via
`set_system('empty_region_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`threshold`,
`regiongrowing`,
`connection`

## Alternatives

`connect_and_holes`

## Module

Foundation
