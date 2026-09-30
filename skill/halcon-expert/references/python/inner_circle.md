# inner_circle (Operator)

## Name

`inner_circle` — Largest inner circle of a region.

## Signature

`def inner_circle(regions: HObject) -> Tuple[Sequence[float], Sequence[float], Sequence[float]]`

`def inner_circle_s(regions: HObject) -> Tuple[float, float, float]`

## Description

The operator `inner_circle` determines the largest inner circle
of a region.
This is the biggest discrete circle region that completely fits into
the region.
For this circle the center (*`row`*, *`column`*) and the
radius (*`radius`*) are calculated.
If the position of the circle is ambiguous, the "first possible"
position (as far upper left as possible) is returned.

In the documentation of this chapter ([Regions / Features](toc_regions_features.md)), you can
find an image illustrating regions with varying inner circles.

The output of the operator is chosen in such a way that it can be
used as an input for the operators [`disp_circle`](disp_circle.md),
[`gen_circle`](gen_circle.md), and [`gen_ellipse_contour_xld`](gen_ellipse_contour_xld.md).

If several regions are passed in *`regions`* corresponding tuples
are returned as output parameters.
In case of an empty input region all parameters have the value
*0.0* if no other behavior was set with [`set_system`](set_system.md).

## Attention

If several inner circles are present at a region
only the most upper left solution is returned.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`regions`** (input_object)  region(-array) `→` HObject

Regions to be examined.

**`row`** (output_control)  circle.center.y(-array) `→` Sequence[float]

Line index of the center.

**`column`** (output_control)  circle.center.x(-array) `→` Sequence[float]

Column index of the center.

**`radius`** (output_control)  circle.radius(-array) `→` Sequence[float]

Radius of the inner circle.

Assertion:
`Radius >= 0`

## Complexity

If F is the area of the region and R is the radius of the
inner circle the runtime complexity is O(sqrt(F) * R).

## Result

The operator `inner_circle` returns the value 2 (
H_MSG_TRUE)
if the input is not empty.
The behavior in case of empty input (no input regions available) is
set via the operator `set_system('no_object_result',<Result>)`,
the behavior in case of empty region is set via
`set_system('empty_region_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`threshold`,
`regiongrowing`,
`connection`,
`runlength_features`

## Possible Successors

`gen_circle`,
`disp_circle`

## Alternatives

`erosion_circle`,
`inner_rectangle1`

## See also

`set_shape`,
`select_shape`,
`smallest_circle`

## Module

Foundation
