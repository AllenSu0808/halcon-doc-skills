# convexity_xld (Operator)

## Name

`convexity_xld` — Shape factor for the convexity of contours or polygons.

## Signature

`convexity_xld(XLD : : : Convexity)`

## Description

The operator `convexity_xld` calculates the convexity for each input
contour or polygon. The input contour or polygon must not
intersect itself, otherwise the resulting parameter is not meaningful
(Whether the input contour or polygon intersects itself or not can be
determined with [`test_self_intersection_xld`](test_self_intersection_xld.md)). If
the input contour or polygon is not closed it will be closed automatically.

**Calculation:**
If $F_{c}$ is the area of the convex hull and
$F_{o}$ the area enclosed by the original contour or
polygon the shape factor *`Convexity`* is defined
as:
$$\text{Convexity} = \frac{F_{\mathrm{o}}}{F_{\mathrm{c}}}$$ ![figure](../assets/1252ab78200a0166.svg)
The shape factor *`Convexity`* is 1 if the contour or polygon is convex
(e.g., a rectangle, circle, etc.). If there are indentations
*`Convexity`* is smaller than 1.

If more than one contour or polygon is passed, the numerical results of the
shape factor are stored in a tuple in the same order as the respective
contours or polygons in *`XLD`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`XLD`** (input_object)  xld(-array) `→` object

Contours or polygons to be examined.

**`Convexity`** (output_control)  real(-array) `→`  (real)

Convexity of the input contours or polygons.

Assertion:
`Convexity <= 1`

## Result

The operator `convexity_xld` returns the value 2 (
H_MSG_TRUE)
if the input is not empty.
The behavior in case of empty input (no input contour available) is
set via the operator `set_system('no_object_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`gen_contours_skeleton_xld`,
`edges_sub_pix`,
`threshold_sub_pix`,
`gen_contour_polygon_xld`,
`test_self_intersection_xld`

## See also

`area_center_xld`,
`select_shape_xld`,
`shape_trans_xld`

## Module

Foundation
