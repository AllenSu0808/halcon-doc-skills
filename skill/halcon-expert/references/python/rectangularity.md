# rectangularity (Operator)

## Name

`rectangularity` — Shape factor for the rectangularity of a region.

## Signature

`def rectangularity(regions: HObject) -> Sequence[float]`

`def rectangularity_s(regions: HObject) -> float`

## Description

The operator `rectangularity` calculates the rectangularity of the
input regions.

To determine the rectangularity, first a rectangle is computed that has
the same first and second order moments as the input region. The
computation of the rectangularity measure is finally based on the
area of the difference between the computed rectangle and the
input region normalized with respect to the area of the rectangle.

In the documentation of this chapter ([Regions / Features](toc_regions_features.md)), you can
find an image illustrating regions which vary in their rectangularity.

For rectangles `rectangularity` returns the value 1. The more the
input region deviates from a perfect rectangle, the less the returned
value for *`rectangularity`* will be.

In case of an empty region the operator `rectangularity` returns
the value 0 (if no other behavior was set (see [`set_system`](set_system.md))).
If more than one region is passed the numerical values of the
rectangularity are stored in a tuple, the position of a value in the tuple
corresponding to the position of the region in the input tuple.

## Attention

For input regions which orientation cannot be computed by using second
order moments (as it is the case for square regions, for example),
the returned *`rectangularity`* is underestimated by up to 10%
depending on the orientation of the input region.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`regions`** (input_object)  region(-array) `→` HObject

Region(s) to be examined.

**`rectangularity`** (output_control)  real(-array) `→` Sequence[float]

Rectangularity of the input region(s).

Assertion:
`0 <= Rectangularity && Rectangularity <= 1.0`

## Result

The operator `rectangularity` returns the value 2 (
H_MSG_TRUE)
if the input is not empty.
The behavior in case of empty input (no input regions available) is
set via the operator `set_system('no_object_result',<Result>)`.
The behavior in case of empty region (the region is the empty set) is set via
`set_system('empty_region_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`threshold`,
`regiongrowing`,
`connection`

## Alternatives

`circularity`,
`compactness`,
`convexity`,
`eccentricity`

## See also

`contlength`,
`area_center`,
`select_shape`

## References

P. L. Rosin: “Measuring rectangularity”;
Machine Vision and Applications; vol. 11;
pp. 191-196; Springer-Verlag, 1999.

## Module

Foundation
