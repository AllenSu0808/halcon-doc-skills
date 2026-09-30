# draw_nurbs_interp (Operator)

## Name

`draw_nurbs_interp` — Interactive drawing of a NURBS curve using interpolation.

## Warning

**This operator does not work in an HDevelop graphics window opened with
`dev_open_window`.**

## Signature

`def draw_nurbs_interp(window_handle: HHandle, rotate: str, move: str, scale: str, keep_ratio: str, degree: int) -> Tuple[HObject, Sequence[float], Sequence[float], Sequence[float], Sequence[float], Sequence[float], Sequence[float]]`

## Description

`draw_nurbs_interp` returns the contour *`cont_out`* of a
NURBS curve of degree *`degree`*, which has been created
interactively by the user in the window *`window_handle`* using
interpolation. That means, that the user specifies a set of points and
the operator computes the parameters of a NURBS curve that includes
this points. By contrast, using the Operator [`draw_nurbs`](draw_nurbs.md) it is
possible to create a NURBS curve by drawing its control polygon.

In addition to *`cont_out`*, the control information of the curve
(*`control_rows`*, *`control_cols`*, and *`knots`*), the
interpolation points (*`rows`*, *`cols`*) specified by the user
and the tangents at the first and the last point (*`tangents`*) are
returned. *`tangents`* consists of four values. The first two
values correspond to the y (row) and the x (column) value of the tangent at
the start of the curve and the second two values to the tangent at the end of
the curve, respectively.

The weight vector is not returned because it consists of
equal entries. As a consequence, one can use *"auto"* as weight vector
if the control information is used in a subsequent call to the operator
[`gen_contour_nurbs_xld`](gen_contour_nurbs_xld.md). For more information on NURBS see the
documentation of [`gen_contour_nurbs_xld`](gen_contour_nurbs_xld.md).

Directly after calling `draw_nurbs_interp`, you can add interpolation
points by clicking with the left mouse button in the window at the desired
positions. If enough points are specified (at least *`degree`*-1),
a NURBS curve that goes through all specified points (in the
order of their generation) is computed and displayed.

When there are three points or more, the first and the last point will be
marked with an additional square. By clicking on them
you can close the curve or open it again. You delete the point appended last
by pressing the Ctrl key.

The tangents (i.e. the first derivative of the curve) of the first
and the last point are displayed as lines. They can be modified by dragging
their ends using the mouse.

Existing points can be moved by dragging them with the mouse. Further
new points on the curve can be inserted by a left click on the desired
position on the curve.

By pressing the Shift key, you can switch into the transformation mode.
In this mode you can rotate, move, and scale the curve as a whole, but only
if you set the parameters *`rotate`*, *`move`*, and
*`scale`*, respectively, to *"true"*. Instead of the pick points
and the two tangents, 3 symbols are displayed with the curve: a cross in the
middle and an arrow to the right if *`rotate`* is set to *"true"*,
and a double-headed arrow to the upper right if *`scale`* is set to
*"true"*.

You can

- move the curve by clicking the left mouse button on the cross in
  the center and then dragging it to the new position,
- rotate it by clicking with the left mouse button on the arrow and
  then dragging it, till the curve has the right direction, and
- scale it by dragging the double arrow. To keep the ratio, the
  parameter *`keep_ratio`* has to be set to *"true"*.

By pressing the Shift key again you can switch back to the edit mode.
Pressing the right mouse button terminates the procedure.

The appearance of the curve while drawing is determined by the line width,
size, and color set via the operators [`set_color`](set_color.md), [`set_colored`](set_colored.md),
[`set_line_width`](set_line_width.md), and [`set_line_style`](set_line_style.md). The tangents and all
handles are displayed in the second color set by [`set_color`](set_color.md) or
[`set_colored`](set_colored.md). Their line width is fixed to 1 and their line style is
fixed to a drawn-through line.

## Attention

In contrast to [`draw_nurbs`](draw_nurbs.md), each point specified by the user
influences the whole curve. Thus, if one point is moved, the whole curve can
and will change. To minimize this effects, it is recommended to use a small
degree (3-5) and to place the points such that they are approximately equally
spaced. In general, uneven degrees will perform slightly better than even
degrees.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`cont_out`** (output_object)  xld_cont `→` HObject

Contour of the curve.

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`rotate`** (input_control)  string `→` str

Enable rotation?

Default:
"true"

List of values:
"false", "true"

**`move`** (input_control)  string `→` str

Enable moving?

Default:
"true"

List of values:
"false", "true"

**`scale`** (input_control)  string `→` str

Enable scaling?

Default:
"true"

List of values:
"false", "true"

**`keep_ratio`** (input_control)  string `→` str

Keep ratio while scaling?

Default:
"true"

List of values:
"false", "true"

**`degree`** (input_control)  integer `→` int

The degree p of the NURBS curve.
Reasonable values are 3 to 5.

Default:
3

Suggested values:
2, 3, 4, 5

Restriction:
`Degree >= 2 && Degree <= 9`

**`control_rows`** (output_control)  coordinates.y-array `→` Sequence[float]

Row coordinates of the control polygon.

**`control_cols`** (output_control)  coordinates.x-array `→` Sequence[float]

Column coordinates of the control polygon.

**`knots`** (output_control)  real-array `→` Sequence[float]

Knot vector.

**`rows`** (output_control)  coordinates.y-array `→` Sequence[float]

Row coordinates of the points specified by the user.

**`cols`** (output_control)  coordinates.x-array `→` Sequence[float]

Column coordinates of the points specified by the user.

**`tangents`** (output_control)  real-array `→` Sequence[float]

Tangents specified by the user.

## Result

`draw_nurbs_interp` returns 2 (
H_MSG_TRUE)
if the window is valid.
If necessary, an exception is raised.

## Possible Predecessors

`open_window`

## Possible Successors

`set_colored`,
`set_line_width`,
`set_draw`

## Alternatives

`draw_xld`,
`draw_nurbs`

## See also

`draw_nurbs_interp_mod`,
`draw_nurbs`,
`gen_contour_nurbs_xld`

## Module

Foundation
