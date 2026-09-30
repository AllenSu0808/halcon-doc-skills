# draw_nurbs_mod (Operator)

## Name

`draw_nurbs_mod` — Interactive modification of a NURBS curve.

## Warning

**This operator does not work in an HDevelop graphics window opened with
`dev_open_window`.**

## Signature

`def draw_nurbs_mod(window_handle: HHandle, rotate: str, move: str, scale: str, keep_ratio: str, edit: str, degree: int, rows_in: Sequence[float], cols_in: Sequence[float], weights_in: Sequence[float]) -> Tuple[HObject, Sequence[float], Sequence[float], Sequence[float]]`

## Description

`draw_nurbs_mod` returns the contour *`cont_out`* and control
information (*`rows`*, *`cols`*, and *`weights`*) of a NURBS
curve of degree *`degree`*, which has been interactively
modified by the user in the window *`window_handle`*. For additional
information concerning NURBS curves, see the documentation of
[`gen_contour_nurbs_xld`](gen_contour_nurbs_xld.md). To use the control information
*`rows`*, *`cols`*, and *`weights`* in a subsequent call to
the operator [`gen_contour_nurbs_xld`](gen_contour_nurbs_xld.md), the knot vector `knots`
should be set to *"auto"*.

The input NURBS curve is specified by its control polygon
(*`rows_in`*, *`cols_in`*), its weight vector *`weights_in`* and
its degree *`degree`*. The knot vector is assumed to be uniform (i.e.
*"auto"* in [`gen_contour_nurbs_xld`](gen_contour_nurbs_xld.md)).

You can modify the curve in two ways: by editing the control polygon,
e.g., by inserting or moving control points, or by transforming the contour
as a whole, e.g., by rotating moving or scaling it. Note that you can only
edit the control polygon if *`edit`* is set to *"true"*.
Similarly, you can only rotate, move or scale it if *`rotate`*,
*`move`*, and *`scale`*, respectively, are set to *"true"*.

`draw_nurbs_mod` starts in the transformation mode. In this mode, the
curve is displayed together with 3 symbols: a cross in the middle and an
arrow to the right if *`rotate`* is set to *"true"*, and a
double-headed arrow to the upper right if *`scale`* is set to
*"true"*.
To switch into the edit mode, press the Shift key; by pressing it again,
you can switch back into the transformation mode.

### Transformation Mode

In this mode a curve can be rotated, moved and scaled, as long as the
respective parameter *`rotate`*, *`move`* and *`scale`*
are set to *"true"*. The curve is displayed along with a cross in its
center, an arrow pointing to the right (if *`rotate`* is set to
*"true"*), and a double arrow (if *`scale`* is set to
*"true"*).

- To move the curve, click with the left mouse button on the cross
  in the center and then drag it to the new position, i.e., keep
  the mouse button pressed while moving the mouse.
- To rotate it, click with the left mouse button on the arrow and
  then drag it, till the curve has the right direction.
- Scaling is achieved by dragging the double arrow. To keep the
  ratio, the parameter *`keep_ratio`* has to be set to
  *"true"*.

### Edit Mode

In this mode, the curve is displayed together with its control polygon.
Start and end point are marked by an additional square and the point which
was handled last is surrounded by a circle representing its weight. You can
perform the following modifications:

- To append control points, click with the left mouse button in the
  window and a new point is added at this position.
- You can delete the point appended last by pressing the Ctrl key.
- To move a point, drag it with the mouse.
- To insert a point on the control polygon, click on the
  desired position on the polygon.
- To close respectively open the curve, click on the first or on
  the last control point.
- You can modify the weight of a control point by first clicking on the
  point itself (if it is not already the point which was modified or
  created last) and then dragging the circle around the point.

Pressing the right mouse button terminates the procedure.

The appearance of the curve while drawing is determined by the line width,
size and color set via the operators [`set_color`](set_color.md), [`set_colored`](set_colored.md),
[`set_line_width`](set_line_width.md), and [`set_line_style`](set_line_style.md). The control polygon and
all handles are displayed in the second color set by [`set_color`](set_color.md) or
[`set_colored`](set_colored.md). Their line width is fixed to 1 and their line style is
fixed to a drawn-through line.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`cont_out`** (output_object)  xld_cont `→` HObject

Contour of the modified curve.

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

**`edit`** (input_control)  string `→` str

Enable editing?

Default:
"true"

List of values:
"false", "true"

**`degree`** (input_control)  integer `→` int

The degree p of the NURBS curve.
Reasonable values are 3 to 25.

Default:
3

Suggested values:
2, 3, 4, 5

Restriction:
`Degree >= 2`

**`rows_in`** (input_control)  coordinates.y-array `→` Sequence[float]

Row coordinates of the input control polygon.

**`cols_in`** (input_control)  coordinates.x-array `→` Sequence[float]

Column coordinates of the input control polygon.

**`weights_in`** (input_control)  real-array `→` Sequence[float]

Input weight vector.

**`rows`** (output_control)  coordinates.y-array `→` Sequence[float]

Row coordinates of the control polygon.

**`cols`** (output_control)  coordinates.x-array `→` Sequence[float]

Columns coordinates of the control polygon.

**`weights`** (output_control)  real-array `→` Sequence[float]

Weight vector.

## Result

`draw_nurbs_mod` returns 2 (
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

`draw_nurbs_interp_mod`,
`draw_xld_mod`

## See also

`draw_nurbs`,
`draw_nurbs_interp`,
`gen_contour_nurbs_xld`

## Module

Foundation
