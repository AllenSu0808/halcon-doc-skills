# contlength (Operator)

## Name

`contlength` — Contour length of a region.

## Signature

`def contlength(regions: HObject) -> Sequence[float]`

`def contlength_s(regions: HObject) -> float`

## Description

The operator `contlength` calculates the total length of the contour
(sum of all connection components of the region) for each region of
*`regions`*. The distance between two neighboring contour
points parallel to the coordinate axes is rated 1, the distance in the diagonal
is rated $\sqrt{2}$ ![figure](../assets/102cc74656473d95.svg).

In the documentation of this chapter ([Regions / Features](toc_regions_features.md)), you can
find an image illustrating regions which vary in the length of their
contours.

If more than one region is passed the numerical values of the
contour length are stored in a tuple, the position of a value in the tuple
corresponding to the position of the region in the input tuple. In case of an
empty region the operator `contlength` returns the value 0.

## Attention

The contour of holes is not calculated.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`regions`** (input_object)  region(-array) `→` HObject

Region(s) to be examined.

**`cont_length`** (output_control)  real(-array) `→` Sequence[float]

Contour length of the input region(s).

Assertion:
`ContLength >= 0`

## Result

The operator `contlength` returns the value 2 (
H_MSG_TRUE)
if the input is not empty.
The behavior in case of empty input (no input regions available) is
set via the operator `set_system('no_object_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`threshold`,
`regiongrowing`,
`connection`

## Possible Successors

`get_region_contour`

## Alternatives

`compactness`

## See also

`area_center`,
`get_region_contour`

## Module

Foundation
