# height_width_ratio_xld (Operator)

## Name

`height_width_ratio_xld` — Compute the width, height, and aspect ratio of the enclosing
rectangle parallel to the coordinate axes of contours or polygons.

## Signature

`height_width_ratio_xld(XLD : : : Height, Width, Ratio)`

## Description

The operator `height_width_ratio_xld` calculates the enclosing
rectangle (parallel to the coordinate axes) for each input contour
or polygon. The enclosing rectangle is described by the coordinates
of the corner pixels
(`Row1`,`Column1`,`Row2`,`Column2`)
(see [`smallest_rectangle1_xld`](smallest_rectangle1_xld.md)). Based on these values,
`height_width_ratio_xld` computes the width, height, and
aspect ratio of the smallest surrounding rectangle as follows:
$$Width = Column2 - Column1 \\ Height = Row2 - Row1 \\ Ratio = Height/Width$$ ![figure](../assets/5525136d703e84dc.svg)

If more than one contour or polygon is passed, the results are
stored in tuples in the same order as the respective contours or
polygons in *`XLD`*. In case of an empty contour all parameters
have the value 0 if no other behavior was set (see
[`set_system`](set_system.md)).

## Attention

If $\texttt{Width}=0$, *`Ratio`* is set
to DBL_MAX (1.797e308).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`XLD`** (input_object)  xld(-array) `→` object

Contours or polygons to be examined.

**`Height`** (output_control)  extent.y(-array) `→`  (real)

Height of the enclosing rectangle.

**`Width`** (output_control)  extent.x(-array) `→`  (real)

Width of the enclosing rectangle.

**`Ratio`** (output_control)  real(-array) `→`  (real)

Aspect ratio of the enclosing rectangle.

## Complexity

If N is the number of contour points, the runtime complexity is
O(N).

## Result

`height_width_ratio_xld` returns 2 (
H_MSG_TRUE)
if the input is not
empty. If the input is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`. If necessary,
an exception is raised.

## Possible Predecessors

`gen_contours_skeleton_xld`,
`edges_sub_pix`,
`threshold_sub_pix`,
`gen_contour_polygon_xld`

## Possible Successors

`gen_polygons_xld`

## Alternatives

`smallest_rectangle1_xld`,
`smallest_rectangle2_xld`,
`shape_trans_xld`

## See also

`shape_trans_xld`,
`smallest_circle_xld`,
`elliptic_axis_xld`,
`area_center_xld`

## Module

Foundation
