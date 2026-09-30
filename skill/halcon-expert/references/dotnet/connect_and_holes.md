# ConnectAndHoles (Operator)

## Name

`ConnectAndHoles` — Number of connection components and holes

## Signature

`static void HOperatorSet.ConnectAndHoles(HObject regions, out HTuple numConnected, out HTuple numHoles)`

`HTuple HRegion.ConnectAndHoles(out HTuple numHoles)`

`int HRegion.ConnectAndHoles(out int numHoles)`

## Description

The operator `ConnectAndHoles` calculates the number of
connection components and the number of holes of
each region of *`regions`*.

In the documentation of this chapter ([Regions / Features](toc_regions_features.md)), you can
find an image illustrating regions which vary in the number of their
connection components and the number of their holes.

If more than one region is passed the numerical values of the
output control parameters *`numConnected`* and *`numHoles`*
are each stored in a tuple, the position of a value in the tuple
corresponding to the position of the region in the input tuple.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`regions`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Region(s) to be examined.

**`numConnected`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Number of connection components of a region.

**`numHoles`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Number of holes of a region.

## Result

The operator `ConnectAndHoles` returns the value 2 (
H_MSG_TRUE)
if the input is not empty.
The behavior in case of empty input (no input regions available) is
set via the operator `set_system('no_object_result',<Result>)`.
The behavior in case of empty region (the region is the empty set) is set via
`set_system('empty_region_result',<Result>)`.

## Possible Predecessors

`Threshold`,
`Regiongrowing`,
`Connection`

## Alternatives

`EulerNumber`

## See also

`Connection`,
`FillUp`,
`FillUpShape`,
`Union1`

## Module

Foundation
