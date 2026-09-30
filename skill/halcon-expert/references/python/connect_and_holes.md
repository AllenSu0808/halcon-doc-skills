# connect_and_holes (Operator)

## Name

`connect_and_holes` — Number of connection components and holes

## Signature

`def connect_and_holes(regions: HObject) -> Tuple[Sequence[int], Sequence[int]]`

`def connect_and_holes_s(regions: HObject) -> Tuple[int, int]`

## Description

The operator `connect_and_holes` calculates the number of
connection components and the number of holes of
each region of *`regions`*.

In the documentation of this chapter ([Regions / Features](toc_regions_features.md)), you can
find an image illustrating regions which vary in the number of their
connection components and the number of their holes.

If more than one region is passed the numerical values of the
output control parameters *`num_connected`* and *`num_holes`*
are each stored in a tuple, the position of a value in the tuple
corresponding to the position of the region in the input tuple.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`regions`** (input_object)  region(-array) `→` HObject

Region(s) to be examined.

**`num_connected`** (output_control)  integer(-array) `→` Sequence[int]

Number of connection components of a region.

**`num_holes`** (output_control)  integer(-array) `→` Sequence[int]

Number of holes of a region.

## Result

The operator `connect_and_holes` returns the value 2 (
H_MSG_TRUE)
if the input is not empty.
The behavior in case of empty input (no input regions available) is
set via the operator `set_system('no_object_result',<Result>)`.
The behavior in case of empty region (the region is the empty set) is set via
`set_system('empty_region_result',<Result>)`.

## Possible Predecessors

`threshold`,
`regiongrowing`,
`connection`

## Alternatives

`euler_number`

## See also

`connection`,
`fill_up`,
`fill_up_shape`,
`union1`

## Module

Foundation
