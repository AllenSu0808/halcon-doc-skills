# convexity (Operator)

## Name

`convexity` — Shape factor for the convexity of a region.

## Signature

`convexity(Regions : : : Convexity)`

## Description

The operator `convexity` calculates the convexity of each input
region of *`Regions`*.

- **Calculation:** —

  If $F_{c}$ is the area of the convex hull and
  $F_{o}$ the
  original area of the region the shape factor
  C is defined as:

  $$C = \frac{F_{o}}{F_{c}}$$ ![figure](../assets/9fb5b39f6a1c41ca.svg)

The shape factor C is 1 if the region is convex (e.g., rectangle,
circle etc.). If there are indentations or holes C is smaller than 1.

In the documentation of this chapter ([Regions / Features](toc_regions_features.md)), you can
find an image illustrating regions which vary in their convexity.

In case of an empty region the operator `convexity` returns
the value 0 (if no other behavior was set (see [`set_system`](set_system.md))).
If more than one region is passed the numerical values of the
contour length are stored in a tuple, the position of a value in the tuple
corresponding to the position of the region in the input tuple.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Regions`** (input_object)  region(-array) `→` object

Region(s) to be examined.

**`Convexity`** (output_control)  real(-array) `→`  (real)

Convexity of the input region(s).

Assertion:
`Convexity <= 1`

## Result

The operator `convexity` returns the value 2 (
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

## See also

`select_shape`,
`area_center`,
`shape_trans`

## Module

Foundation
