# smallest_rectangle2 (Operator)

## Name

`smallest_rectangle2` — Smallest surrounding rectangle with any orientation.

## Signature

`def smallest_rectangle2(regions: HObject) -> Tuple[Sequence[float], Sequence[float], Sequence[float], Sequence[float], Sequence[float]]`

`def smallest_rectangle2_s(regions: HObject) -> Tuple[float, float, float, float, float]`

## Description

The operator `smallest_rectangle2` determines the smallest
surrounding rectangle of a region, i.e., the rectangle with the smallest
area of all rectangles containing the region.
For this rectangle the center,
the inclination and the two radii are calculated.
The calculation of the rectangle is based on the center coordinates of
the region pixels.

In the documentation of this chapter ([Regions / Features](toc_regions_features.md)), you can
find an image illustrating regions which vary in the length and phi of their
smallest surrounding rectangle.

![figure](../assets/a2a01dc51ffc262b.svg)

The smallest surrounding rectangle of a region. Note that the
calculation is based on the center coordinates of the region pixels.

The operator is applied when, for example, the location of a scenery of
several regions (e.g., printed text on a rectangular paper or
in rectangular print (justified lines)) must be found.
The parameters of `smallest_rectangle2` are chosen in such a way
that they can be used directly as input for the operators
[`disp_rectangle2`](disp_rectangle2.md) and [`gen_rectangle2`](gen_rectangle2.md).

If more than one region is passed in *`regions`* the results are
stored in tuples, the index of a value in the tuple corresponding to the
index of a region in the input. In case of empty region all parameters
have the value 0.0 if no other behavior was set (see [`set_system`](set_system.md)).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`regions`** (input_object)  region(-array) `→` HObject

Regions to be examined.

**`row`** (output_control)  rectangle2.center.y(-array) `→` Sequence[float]

Line index of the center.

**`column`** (output_control)  rectangle2.center.x(-array) `→` Sequence[float]

Column index of the center.

**`phi`** (output_control)  rectangle2.angle.rad(-array) `→` Sequence[float]

Orientation of the surrounding rectangle (arc measure)

Assertion:
`- pi / 2 < Phi && Phi <= pi / 2`

**`length_1`** (output_control)  rectangle2.hwidth(-array) `→` Sequence[float]

First radius (half length) of the surrounding
rectangle.

Assertion:
`Length1 >= 0.0`

**`length_2`** (output_control)  rectangle2.hheight(-array) `→` Sequence[float]

Second radius (half width) of the surrounding
rectangle.

Assertion:
`Length2 >= 0.0 && Length2 <= Length1`

## Complexity

If F is the area of the region and N is the number of supporting points
of the convex hull, the runtime complexity is O(sqrt(F) + N^2).

## Result

The operator `smallest_rectangle2` returns the value 2 (
H_MSG_TRUE)
if the input is not empty. The behavior in case of empty input (no input regions available)
is set via the operator `set_system('no_object_result',<Result>)`.
The behavior in case of empty region (the region is the empty set) is set via
`set_system('empty_region_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`threshold`,
`regiongrowing`,
`connection`,
`runlength_features`

## Possible Successors

`disp_rectangle2`,
`gen_rectangle2`

## Alternatives

`elliptic_axis`,
`smallest_rectangle1`

## See also

`smallest_circle`,
`set_shape`

## Module

Foundation
