# smallest_rectangle1 (Operator)

## Name

`smallest_rectangle1` — Surrounding rectangle parallel to the coordinate axes.

## Signature

`smallest_rectangle1(Regions : : : Row1, Column1, Row2, Column2)`

## Description

The operator `smallest_rectangle1` calculates the surrounding
rectangle of all input regions (parallel to the coordinate axes).
The surrounding rectangle is described by the coordinates of the
corner pixels
(*`Row1`*,*`Column1`*,*`Row2`*,*`Column2`*).
The calculation of the rectangle is based on the center coordinates
of the region pixels.

![figure](../assets/3c3d4ecee09df07a.svg)

The smallest axis aligned surrounding rectangle of a region. Note
that the calculation is based on the center coordinates of the
region pixels.

If more than one region is passed in *`Regions`*, the results
are stored in tuples, the index of a value in the tuple
corresponding to the index of a region in the input. In case of
empty region all parameters have the value 0 if no other behavior
was set (see [`set_system`](set_system.md)).

## Attention

In case of empty region the result of
*`Row1`*,*`Column1`*, *`Row2`* and *`Column2`*
(all are 0) can lead to confusion.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Regions`** (input_object)  region(-array) `→` object

Regions to be examined.

**`Row1`** (output_control)  rectangle.origin.y(-array) `→`  (integer)

Line index of upper left corner point.

**`Column1`** (output_control)  rectangle.origin.x(-array) `→`  (integer)

Column index of upper left corner point.

**`Row2`** (output_control)  rectangle.corner.y(-array) `→`  (integer)

Line index of lower right corner point.

**`Column2`** (output_control)  rectangle.corner.x(-array) `→`  (integer)

Column index of lower right corner point.

## Complexity

If F is the area of the region the mean runtime complexity is
O(sqrt(F)).

## Result

The operator `smallest_rectangle1` returns the value 2 (
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

## Possible Successors

`disp_rectangle1`,
`gen_rectangle1`

## Alternatives

`height_width_ratio`,
`smallest_rectangle2`,
`area_center`

## See also

`select_shape`

## Module

Foundation
