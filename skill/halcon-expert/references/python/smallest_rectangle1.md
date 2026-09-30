# smallest_rectangle1 (Operator)

## Name

`smallest_rectangle1` — Surrounding rectangle parallel to the coordinate axes.

## Signature

`def smallest_rectangle1(regions: HObject) -> Tuple[Sequence[int], Sequence[int], Sequence[int], Sequence[int]]`

`def smallest_rectangle1_s(regions: HObject) -> Tuple[int, int, int, int]`

## Description

The operator `smallest_rectangle1` calculates the surrounding
rectangle of all input regions (parallel to the coordinate axes).
The surrounding rectangle is described by the coordinates of the
corner pixels
(*`row_1`*,*`column_1`*,*`row_2`*,*`column_2`*).
The calculation of the rectangle is based on the center coordinates
of the region pixels.

![figure](../assets/3c3d4ecee09df07a.svg)

The smallest axis aligned surrounding rectangle of a region. Note
that the calculation is based on the center coordinates of the
region pixels.

If more than one region is passed in *`regions`*, the results
are stored in tuples, the index of a value in the tuple
corresponding to the index of a region in the input. In case of
empty region all parameters have the value 0 if no other behavior
was set (see [`set_system`](set_system.md)).

## Attention

In case of empty region the result of
*`row_1`*,*`column_1`*, *`row_2`* and *`column_2`*
(all are 0) can lead to confusion.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`regions`** (input_object)  region(-array) `→` HObject

Regions to be examined.

**`row_1`** (output_control)  rectangle.origin.y(-array) `→` Sequence[int]

Line index of upper left corner point.

**`column_1`** (output_control)  rectangle.origin.x(-array) `→` Sequence[int]

Column index of upper left corner point.

**`row_2`** (output_control)  rectangle.corner.y(-array) `→` Sequence[int]

Line index of lower right corner point.

**`column_2`** (output_control)  rectangle.corner.x(-array) `→` Sequence[int]

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
