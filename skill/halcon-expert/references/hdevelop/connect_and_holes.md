# connect_and_holes (Operator)

## Name

`connect_and_holes` — Number of connection components and holes

## Signature

`connect_and_holes(Regions : : : NumConnected, NumHoles)`

## Description

The operator `connect_and_holes` calculates the number of
connection components and the number of holes of
each region of *`Regions`*.

In the documentation of this chapter ([Regions / Features](toc_regions_features.md)), you can
find an image illustrating regions which vary in the number of their
connection components and the number of their holes.

If more than one region is passed the numerical values of the
output control parameters *`NumConnected`* and *`NumHoles`*
are each stored in a tuple, the position of a value in the tuple
corresponding to the position of the region in the input tuple.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Regions`** (input_object)  region(-array) `→` object

Region(s) to be examined.

**`NumConnected`** (output_control)  integer(-array) `→`  (integer)

Number of connection components of a region.

**`NumHoles`** (output_control)  integer(-array) `→`  (integer)

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
