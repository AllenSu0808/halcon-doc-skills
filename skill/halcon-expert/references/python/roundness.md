# roundness (Operator)

## Name

`roundness` — Shape factors from contour.

## Signature

`def roundness(regions: HObject) -> Tuple[Sequence[float], Sequence[float], Sequence[float], Sequence[float]]`

`def roundness_s(regions: HObject) -> Tuple[float, float, float, float]`

## Description

The operator `roundness` examines the distance between the
contour and the center of the area. In particular the mean
distance (*`distance`*), the deviation from the mean distance
(*`sigma`*) and two shape features derived therefrom are determined.
*`roundness`* is the relation between mean value and standard
deviation, and *`sides`* indicates the number of polygon pieces
if a regular polygon is concerned.

In the documentation of this chapter ([Regions / Features](toc_regions_features.md)), you can
find an image illustrating regions which vary in their mean distance,
distance deviation, roundness and number of polygon pieces.

The contour for calculating the features is determined depending on the
global neighborhood (see [`set_system`](set_system.md)).

Calculation:

If p is the center of the area, $p_{i}$ the pixels
and F the area of the contour.
$$\text{Distance} = \frac{1}{F} \sum_i \| p - p_i \|$$ ![figure](../assets/d9247b5e34aec370.svg)
$$\Sigma^2 = \frac{1}{F} \sum_i \left( \lVert p - p_i \rVert - Distance \right)^2$$ ![figure](../assets/8abf791520da46e9.svg)
$$\text{Roundness} = 1 - \frac{\mathrm{Sigma}}{\mathrm{Distance}}$$ ![figure](../assets/1e7281e72f2f82e4.svg)
$$Sides = 1.4111\left(\frac{Distance}{Sigma}\right)^{0.4724}$$ ![figure](../assets/05d82c12f9dd6ad9.svg)

If more than one region is passed the results are stored in tuples, the index
of a value in the tuple corresponding to the index of a region in the input.

In case of empty region all parameters have the value 0.0 if no other
behavior was set (see [`set_system`](set_system.md)).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`regions`** (input_object)  region(-array) `→` HObject

Region(s) to be examined.

**`distance`** (output_control)  real(-array) `→` Sequence[float]

Mean distance from the center.

Assertion:
`Distance >= 0.0`

**`sigma`** (output_control)  real(-array) `→` Sequence[float]

Standard deviation of *`distance`*.

Assertion:
`Sigma >= 0.0`

**`roundness`** (output_control)  real(-array) `→` Sequence[float]

Shape factor for roundness.

Assertion:
`Roundness <= 1.0`

**`sides`** (output_control)  real(-array) `→` Sequence[float]

Number of polygon sides.

Assertion:
`Sides >= 0`

## Complexity

If F is the area of a region the mean runtime
complexity is O(sqrt(F)).

## Result

The operator `roundness` returns the value 2 (
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
`connection`

## Alternatives

`compactness`

## See also

`contlength`

## References

R. Haralick, L. Shapiro
“Computer and Robot Vision”
Addison-Wesley, 1992, pp. 61

## Module

Foundation
