# orientation_region (Operator)

## Name

`orientation_region` — Orientation of a region.

## Signature

`def orientation_region(regions: HObject) -> Sequence[float]`

`def orientation_region_s(regions: HObject) -> float`

## Description

The operator `orientation_region` calculates the
orientation of the region. The operator is based on [`elliptic_axis`](elliptic_axis.md).
In addition the point on the contour with maximal distance to the
center of gravity is calculated. If, in the rotated coordinate system,
the column coordinate of this point is less than the column coordinate
of the center of gravity, the value of $\pi$ is added to the angle.

In the documentation of this chapter ([Regions / Features](toc_regions_features.md)), you can
find an image illustrating regions which vary in their orientation.

If more than one region is passed the results are stored in tuples, the index
of a value in the tuple corresponding to the index of a region in the
input.

In case of empty region all parameters have the value 0.0 if no other
behavior was set
(see `set_system('no_object_result',<Result>)`).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`regions`** (input_object)  region(-array) `→` HObject

Region(s) to be examined.

**`phi`** (output_control)  angle.rad(-array) `→` Sequence[float]

Orientation of region (arc measure).

Assertion:
`- pi <= Phi && Phi < pi`

## Complexity

If F is the area of a region the mean runtime
complexity is O(sqrt(F)).

## Result

The operator `orientation_region` returns the value 2 (
H_MSG_TRUE)
if the input
is not empty. The behavior in case of empty input (no input regions available)
is set via the operator
`set_system('no_object_result',<Result>)`.
The behavior in case of empty region (the region is the empty set) is set via
`set_system('empty_region_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`threshold`,
`regiongrowing`,
`connection`

## Possible Successors

`disp_arrow`

## Alternatives

`elliptic_axis`,
`smallest_rectangle2`

## See also

`moments_region_2nd`,
`line_orientation`

## Module

Foundation
