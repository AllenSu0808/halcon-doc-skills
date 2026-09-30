# OrientationRegion (Operator)

## Name

`OrientationRegion` — Orientation of a region.

## Signature

`static void HOperatorSet.OrientationRegion(HObject regions, out HTuple phi)`

`HTuple HRegion.OrientationRegion()`

## Description

The operator `OrientationRegion` calculates the
orientation of the region. The operator is based on [`EllipticAxis`](elliptic_axis.md).
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

**`regions`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Region(s) to be examined.

**`phi`** (output_control)  angle.rad(-array) `→` [HTuple](HTuple.md) (*double*)

Orientation of region (arc measure).

Assertion:
`- pi <= Phi && Phi < pi`

## Complexity

If F is the area of a region the mean runtime
complexity is O(sqrt(F)).

## Result

The operator `OrientationRegion` returns the value 2 (
H_MSG_TRUE)
if the input
is not empty. The behavior in case of empty input (no input regions available)
is set via the operator
`set_system('no_object_result',<Result>)`.
The behavior in case of empty region (the region is the empty set) is set via
`set_system('empty_region_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`Threshold`,
`Regiongrowing`,
`Connection`

## Possible Successors

`DispArrow`

## Alternatives

`EllipticAxis`,
`SmallestRectangle2`

## See also

`MomentsRegion2nd`,
`LineOrientation`

## Module

Foundation
