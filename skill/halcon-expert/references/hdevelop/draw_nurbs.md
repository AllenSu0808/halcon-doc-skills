# draw_nurbs (Operator)

## Name

`draw_nurbs` — Interactive drawing of a NURBS curve.

## Warning

**This operator does not work in an HDevelop graphics window opened with
`dev_open_window`.**

## Signature

`draw_nurbs( : ContOut : WindowHandle, Rotate, Move, Scale, KeepRatio, Degree : Rows, Cols, Weights)`

## Description

`draw_nurbs` returns the contour *`ContOut`* and control
information
(*`Rows`*, *`Cols`*, and *`Weights`*) of a NURBS curve of
degree *`Degree`*, which
has been created interactively by the user in the window
*`WindowHandle`*. For additional
information concerning NURBS curves, see the documentation of
[`gen_contour_nurbs_xld`](gen_contour_nurbs_xld.md). To use the control information
*`Rows`*, *`Cols`*, and *`Weights`* in a subsequent call to
the operator [`gen_contour_nurbs_xld`](gen_contour_nurbs_xld.md), the knot vector
`Knots` should be set to *'auto'*.

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

As soon as the number of control points exceeds *`Degree`*, the NURBS
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
but only if you set the parameters *`Rotate`*, *`Move`*, and
*`Scale`*, respectively, to *'true'*. Instead of the pick points
and the control polygon,
3 symbols are displayed with the contour: a cross in the middle and an arrow
to the right if *`Rotate`* is set to *'true'*, and a double-headed
arrow to the upper right if *`Scale`* is set to *'true'*.

You can

- move the curve by clicking the left mouse button on the cross in
  the center and then dragging it to the new position,
- rotate it by clicking with the left mouse button on the arrow and
  then dragging it, till the curve has the right direction, and
- scale it by dragging the double arrow. To keep the ratio the
  parameter *`KeepRatio`* has to be set to *'true'*.

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

**`ContOut`** (output_object)  xld_cont `→` object

Contour approximating the NURBS curve.

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`Rotate`** (input_control)  string `→`  (string)

Enable rotation?

Default:
'true'

List of values:
'false', 'true'

**`Move`** (input_control)  string `→`  (string)

Enable moving?

Default:
'true'

List of values:
'false', 'true'

**`Scale`** (input_control)  string `→`  (string)

Enable scaling?

Default:
'true'

List of values:
'false', 'true'

**`KeepRatio`** (input_control)  string `→`  (string)

Keep ratio while scaling?

Default:
'true'

List of values:
'false', 'true'

**`Degree`** (input_control)  integer `→`  (integer)

The degree p of the NURBS curve. Reasonable values are
3 to 25.

Default:
3

Suggested values:
2, 3, 4, 5

Restriction:
`Degree >= 2`

**`Rows`** (output_control)  coordinates.y-array `→`  (real)

Row coordinates of the control polygon.

**`Cols`** (output_control)  coordinates.x-array `→`  (real)

Columns coordinates of the control polygon.

**`Weights`** (output_control)  real-array `→`  (real)

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
