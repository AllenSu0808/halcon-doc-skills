# compactness (Operator)

## Name

`compactness` — Shape factor for the compactness of a region.

## Signature

`def compactness(regions: HObject) -> Sequence[float]`

`def compactness_s(regions: HObject) -> float`

## Description

The operator `compactness` calculates the compactness of the input regions.

- **Calculation:** —

  If L is the length of the contour (see
  [`contlength`](contlength.md)) and F the area of the region the shape
  factor C is defined as:

  $$C' = \frac{L^2}{4F\pi}$$ ![figure](../assets/315e3a3a5b215549.svg)

  C = max(1,C')

In the documentation of this chapter ([Regions / Features](toc_regions_features.md)), you can
find an image illustrating regions which vary in their compactness.

The shape factor C of a circle is 1. If the region
is long or has holes C is larger than 1.
The operator `compactness` responds to the course of the contour
(roughness) and to holes. The value of C is clipped to 1.0,
because the pixel area of a region can only be an approximation of a
real circle's area. This approximation error is bigger for small
regions than for large regions.

In case of an empty region the operator `compactness` returns the
value 0 if no other behavior was set (see [`set_system`](set_system.md)).
If more than one region is passed the numerical values of the shape
factor are stored in a tuple, the position of a value in the tuple corresponding
to the position of the region in the input tuple.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`regions`** (input_object)  region(-array) `→` HObject

Region(s) to be examined.

**`compactness`** (output_control)  real(-array) `→` Sequence[float]

Compactness of the input region(s).

Assertion:
`Compactness >= 1.0 || Compactness == 0`

## Result

The operator `compactness` returns the value 2 (
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

`convexity`,
`eccentricity`

## See also

`contlength`,
`area_center`,
`select_shape`

## Module

Foundation
