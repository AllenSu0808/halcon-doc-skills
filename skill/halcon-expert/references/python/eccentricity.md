# eccentricity (Operator)

## Name

`eccentricity` — Shape features derived from the ellipse parameters.

## Signature

`def eccentricity(regions: HObject) -> Tuple[Sequence[float], Sequence[float], Sequence[float]]`

`def eccentricity_s(regions: HObject) -> Tuple[float, float, float]`

## Description

The operator `eccentricity` calculates the three shape features
*`anisometry`*, *`bulkiness`*, and *`structure_factor`*
for the given *`regions`*:
$$Anisometry = \frac{Ra}{Rb} \\ Bulkiness = \frac{\pi \cdot Ra \cdot Rb}{A} \\ StructureFactor = Anisometry\cdotBulkiness - 1$$ ![figure](../assets/079d25fa3daeb637.svg)
where Ra and Rb denote the ellipse radii (see [`elliptic_axis`](elliptic_axis.md))
and A denotes the area of the region (see [`area_center`](area_center.md)).

In the documentation of this chapter ([Regions / Features](toc_regions_features.md)), you can
find an image illustrating regions which vary in their anisometry, bulkiness
and structure factor.

If more than one region is passed the results are stored in tuples, the index
of a value in the tuple corresponding to the index of a region in the input.

In case of empty region all parameters have the value 0.0 if no other
behavior was set (see [`set_system`](set_system.md)).

## Attention

It should be noted that, like for all region-moments-based
operators, the region's pixels are regarded as mathematical,
infinitely small points that are represented by the center of the
pixels (see the documentation of [`elliptic_axis`](elliptic_axis.md)). This can
lead to non-empty regions that have `rb` = *0*. In
these cases, the output features that require a division by
`rb` are set to *0*. In particular, regions that
contain a single point or regions whose points lie exactly on a
straight line (e.g., one pixel high horizontal regions or one pixel
wide vertical regions) have an anisometry of *0*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`regions`** (input_object)  region(-array) `→` HObject

Region(s) to be examined.

**`anisometry`** (output_control)  real(-array) `→` Sequence[float]

Shape feature (in case of a circle = 1.0).

Assertion:
`Anisometry >= 1.0`

**`bulkiness`** (output_control)  real(-array) `→` Sequence[float]

Calculated shape feature.

**`structure_factor`** (output_control)  real(-array) `→` Sequence[float]

Calculated shape feature.

## Complexity

If F is the area of the region the mean runtime
complexity is O(sqrt(F)).

## Result

The operator `eccentricity` returns the value 2 (
H_MSG_TRUE)
if the input is not empty. The behavior in case of empty input (no input
regions available) is set via the operator
`set_system('no_object_result',<Result>)`.
The behavior in case of empty region (the region is the empty set) is set via
`set_system('empty_region_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`threshold`,
`regiongrowing`,
`connection`

## See also

`elliptic_axis`,
`moments_region_2nd`,
`select_shape`,
`area_center`

## Module

Foundation
