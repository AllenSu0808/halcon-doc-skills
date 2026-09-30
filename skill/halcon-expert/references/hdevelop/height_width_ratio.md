# height_width_ratio (Operator)

## Name

`height_width_ratio` — Compute the width, height, and aspect ratio of the surrounding
rectangle parallel to the coordinate axes.

## Signature

`height_width_ratio(Regions : : : Height, Width, Ratio)`

## Description

The operator `height_width_ratio` calculates the surrounding
rectangle of all input regions (parallel to the coordinate axes).
The surrounding rectangle is described by the coordinates of the
corner pixels
(`Row1`,`Column1`,`Row2`,`Column2`)
(see [`smallest_rectangle1`](smallest_rectangle1.md)). Based on these values,
`height_width_ratio` computes the width, height, and aspect
ratio of the smallest surrounding rectangle as follows:
$$Width = Column2-Column1+1 Height = Row2-Row1+1 Ratio = Height/Width$$ ![figure](../assets/05e73c057c084698.svg)

If more than one region is passed in *`Regions`*, the results
are stored in tuples in the same order as the respective regions in
the *`Regions`*. In case of empty regions, all parameters have
the value 0 if no other behavior was set (see [`set_system`](set_system.md)).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Regions`** (input_object)  region(-array) `→` object

Regions to be examined.

**`Height`** (output_control)  extent.y(-array) `→`  (integer)

Height of the surrounding rectangle of the region.

**`Width`** (output_control)  extent.x(-array) `→`  (integer)

Width of the surrounding rectangle of the region.

**`Ratio`** (output_control)  real(-array) `→`  (real)

Aspect ratio of the surrounding rectangle of the region.

## Complexity

If F is the area of the region the mean runtime complexity is
O(sqrt(F)).

## Result

The operator `height_width_ratio` returns the value 2 (
H_MSG_TRUE)
if
the input is not empty. The behavior in case of empty input (no
input regions available) is set via the operator
`set_system('no_object_result',<Result>)`. The behavior in
case of empty region (the region is the empty set) is set via
`set_system('empty_region_result',<Result>)`. If necessary an
exception is raised.

## Possible Predecessors

`threshold`,
`regiongrowing`,
`connection`,
`runlength_features`

## Alternatives

`smallest_rectangle1`,
`smallest_rectangle2`,
`region_features`

## See also

`select_shape`,
`smallest_circle`,
`elliptic_axis`,
`area_center`

## Module

Foundation
