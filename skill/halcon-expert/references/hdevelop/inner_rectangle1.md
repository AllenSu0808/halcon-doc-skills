# inner_rectangle1 (Operator)

## Name

`inner_rectangle1` — Largest inner rectangle of a region.

## Signature

`inner_rectangle1(Regions : : : Row1, Column1, Row2, Column2)`

## Description

The operator `inner_rectangle1` determines the largest
axis-parallel rectangle that fits into a region. The rectangle is
described by the coordinates of the corner pixels (*`Row1`*,
*`Column1`*, *`Row2`*, *`Column2`*).

In the documentation of this chapter ([Regions / Features](toc_regions_features.md)), you can
find an image illustrating regions which vary in the width and height
of their inner rectangle.

If more than one region is passed in *`Regions`* the results
are stored in tuples, the index of a value in the tuple
corresponding to the index of the input region. For empty regions
all parameters have the value 0 if no other behavior was set (see
[`set_system`](set_system.md)).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on internal data level.

## Parameters

**`Regions`** (input_object)  region(-array) `→` object

Region to be examined.

**`Row1`** (output_control)  rectangle.origin.y(-array) `→`  (integer)

Row coordinate of the upper left corner point.

**`Column1`** (output_control)  rectangle.origin.x(-array) `→`  (integer)

Column coordinate of the upper left corner point.

**`Row2`** (output_control)  rectangle.corner.y(-array) `→`  (integer)

Row coordinate of the lower right corner point.

**`Column2`** (output_control)  rectangle.corner.x(-array) `→`  (integer)

Column coordinate of the lower right corner point.

## Result

The operator `inner_rectangle1` returns the value 2 (
H_MSG_TRUE)
if the
input is not empty. The behavior in case of empty input (no input
regions available) is set via the operator
`set_system('no_object_result',<Result>)`. The behavior in
case of empty region (the region is the empty set) is set via
`set_system('no_object_result',<Result>)`. If necessary an
exception is raised.

## Possible Predecessors

`threshold`,
`regiongrowing`,
`connection`

## Possible Successors

`disp_rectangle1`,
`gen_rectangle1`

## Alternatives

`inner_circle`

## See also

`smallest_rectangle1`,
`select_shape`

## Module

Foundation
