# elliptic_axis (Operator)

## Name

`elliptic_axis` — Calculate the parameters of the equivalent ellipse.

## Signature

`def elliptic_axis(regions: HObject) -> Tuple[Sequence[float], Sequence[float], Sequence[float]]`

`def elliptic_axis_s(regions: HObject) -> Tuple[float, float, float]`

## Description

The operator `elliptic_axis` calculates the radii *`ra`* and
*`rb`* and the orientation *`phi`* of the ellipse having the
same orientation and the same aspect ratio as the input region in *`regions`*.
Several input regions can be passed as tuples.
*`ra`* represents the main radius of the ellipse whereas the radius
*`rb`* represents the secondary radius of the ellipse.
The orientation of the main axis with regard to the x-axis is returned in
*`phi`* which is represented in radians.
The principle axis of the ellipse is equivalent to the principle axis of the
inertia moment of the input region.

In the documentation of this chapter ([Regions / Features](toc_regions_features.md)), you can
find an image illustrating regions which vary in their Phi, Ra and Rb.

Calculation:

If the moments $M_{20}$, $M_{02}$ and $M_{11}$ are
normalized and passed to the area (see [`moments_region_2nd`](moments_region_2nd.md)),
the radii *`ra`* and *`rb`* are calculated as:

$$Ra = \frac{\sqrt{8(M_{20} + M_{02} + \sqrt{(M_{20} - M_{02})^2 + 4M_{11}^2})}}{2}$$ ![figure](../assets/608f467e3a91284e.svg)
$$R_b = \frac{\sqrt{8(M_{20} + M_{02}) - \sqrt{(M_{20} - M_{02})^2 + 4M_{11}^2}}}{2}$$ ![figure](../assets/04c76bff4850eb88.svg)
The orientation *`phi`* is defined by:
$$\texttt{Phi}=-0.5atan2(2M_{11},M_{02}-M_{20})$$

If more than one region is passed, the results are stored in tuples. The index
of an resulting tuple element corresponds to the index of the respective input
region.

If an empty region is passed, all parameters have the value 0.0 if no other
behavior was set
(see `set_system('no_object_result',<Result>)`).

## Attention

It should be noted that, like for all region-moments-based
operators, the region's pixels are regarded as mathematical,
infinitely small points that are represented by the center of the
pixels. This means that *`ra`* and *`rb`* can assume the
value *0*. In particular, for an empty region and a region
containing a single point *`ra`* = *`rb`* = *0*
is returned. Furthermore, for regions whose points lie exactly on a
straight line (e.g., one pixel high horizontal regions or one pixel
wide vertical regions), *`rb`* = *0* is returned.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`regions`** (input_object)  region(-array) `→` HObject

Input regions.

**`ra`** (output_control)  real(-array) `→` Sequence[float]

Main radius (normalized to the area).

Assertion:
`Ra >= 0.0`

**`rb`** (output_control)  real(-array) `→` Sequence[float]

Secondary radius (normalized to the area).

Assertion:
`Rb >= 0.0 && Rb <= Ra`

**`phi`** (output_control)  angle.rad(-array) `→` Sequence[float]

Angle between main radius and x-axis in radians.

Assertion:
`- pi / 2 < Phi && Phi <= pi / 2`

## Complexity

If F is the area of a region the mean runtime
complexity is O(sqrt(F)).

## Result

The operator `elliptic_axis` returns the value 2 (
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

`gen_ellipse`

## Alternatives

`smallest_rectangle2`,
`orientation_region`

## See also

`moments_region_2nd`,
`select_shape`,
`set_shape`

## References

R. Haralick, L. Shapiro
“Computer and Robot Vision”
Addison-Wesley, 1992, pp. 73-75

## Module

Foundation
