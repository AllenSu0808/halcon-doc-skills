# draw_nurbs (Operator)

## Name

`draw_nurbs` — Interactive drawing of a NURBS curve.

## Warning

**This operator does not work in an HDevelop graphics window opened with
`dev_open_window`.**

## Signature

`def draw_nurbs(window_handle: HHandle, rotate: str, move: str, scale: str, keep_ratio: str, degree: int) -> Tuple[HObject, Sequence[float], Sequence[float], Sequence[float]]`

## Description

`draw_nurbs` returns the contour *`cont_out`* and control
information
(*`rows`*, *`cols`*, and *`weights`*) of a NURBS curve of
degree *`degree`*, which
has been created interactively by the user in the window
*`window_handle`*. For additional
information concerning NURBS curves, see the documentation of
[`gen_contour_nurbs_xld`](gen_contour_nurbs_xld.md). To use the control information
*`rows`*, *`cols`*, and *`weights`* in a subsequent call to
the operator [`gen_contour_nurbs_xld`](gen_contour_nurbs_xld.md), the knot vector
`knots` should be set to *"auto"*.

The NURBS curve is created and manipulated by the means of its control
polygon. By contrast, using the operator [`draw_nurbs_interp`](draw_nurbs_interp.md), it is
possible to create a NURBS curve that interpolates points specified by the
user.
Directly after calling `draw_nurbs`, you can add control points
by clicking with the left mouse button in the window at the desired
positions.

When there are three control points or more, the first and the last point
will be marked with an additional square. By clicking on them you can close
the curve or open it again. You delete the point appended last by pressing
the Ctrl key.

As soon as the number of control points exceeds *`degree`*, the NURBS
curve given by the specified control polygon and weight vector is
displayed in addition to the control polygon.

The control point which was handled last is surrounded by a circle
representing its weight. By simply dragging the circle you can increase or
decrease the weight of this control point.

Existing control points can be moved by dragging them with the mouse. Further
new points on the control polygon (to refine the control polygon) can be
inserted by a left click on the desired position on the control polygon.

By pressing the Shift key, you can switch into the transformation mode.
In this mode you can rotate, move, and scale the contour as a whole,
but only if you set the parameters *`rotate`*, *`move`*, and
*`scale`*, respectively, to *"true"*. Instead of the pick points
and the control polygon,
3 symbols are displayed with the contour: a cross in the middle and an arrow
to the right if *`rotate`* is set to *"true"*, and a double-headed
arrow to the upper right if *`scale`* is set to *"true"*.

You can

- move the curve by clicking the left mouse button on the cross in
  the center and then dragging it to the new position,
- rotate it by clicking with the left mouse button on the arrow and
  then dragging it, till the curve has the right direction, and
- scale it by dragging the double arrow. To keep the ratio the
  parameter *`keep_ratio`* has to be set to *"true"*.

By pressing the Shift key again you can switch back to the edit mode.
Pressing the right mouse button terminates the procedure.

The appearance of the curve while drawing is determined by the line width,
size, and color set via the operators [`set_color`](set_color.md), [`set_colored`](set_colored.md),
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

Contour approximating the NURBS curve.

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

The degree p of the NURBS curve. Reasonable values are
3 to 25.

Default:
3

Suggested values:
2, 3, 4, 5

Restriction:
`Degree >= 2`

**`rows`** (output_control)  coordinates.y-array `→` Sequence[float]

Row coordinates of the control polygon.

**`cols`** (output_control)  coordinates.x-array `→` Sequence[float]

Columns coordinates of the control polygon.

**`weights`** (output_control)  real-array `→` Sequence[float]

Weight vector.

## Result

`draw_nurbs` returns 2 (
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
`draw_nurbs_interp`

## See also

`draw_nurbs_mod`,
`draw_nurbs_interp`,
`gen_contour_nurbs_xld`

## Module

Foundation
