# DrawNurbsInterp (Operator)

## Name

`DrawNurbsInterp` — Interactive drawing of a NURBS curve using interpolation.

## Warning

**This operator does not work in an HDevelop graphics window opened with
`dev_open_window`.**

## Signature

`static void HOperatorSet.DrawNurbsInterp(out HObject contOut, HTuple windowHandle, HTuple rotate, HTuple move, HTuple scale, HTuple keepRatio, HTuple degree, out HTuple controlRows, out HTuple controlCols, out HTuple knots, out HTuple rows, out HTuple cols, out HTuple tangents)`

`void HXLDCont.DrawNurbsInterp(HWindow windowHandle, string rotate, string move, string scale, string keepRatio, int degree, out HTuple controlRows, out HTuple controlCols, out HTuple knots, out HTuple rows, out HTuple cols, out HTuple tangents)`

`HXLDCont HWindow.DrawNurbsInterp(string rotate, string move, string scale, string keepRatio, int degree, out HTuple controlRows, out HTuple controlCols, out HTuple knots, out HTuple rows, out HTuple cols, out HTuple tangents)`

## Description

`DrawNurbsInterp` returns the contour *`contOut`* of a
NURBS curve of degree *`degree`*, which has been created
interactively by the user in the window *`windowHandle`* using
interpolation. That means, that the user specifies a set of points and
the operator computes the parameters of a NURBS curve that includes
this points. By contrast, using the Operator [`DrawNurbs`](draw_nurbs.md) it is
possible to create a NURBS curve by drawing its control polygon.

In addition to *`contOut`*, the control information of the curve
(*`controlRows`*, *`controlCols`*, and *`knots`*), the
interpolation points (*`rows`*, *`cols`*) specified by the user
and the tangents at the first and the last point (*`tangents`*) are
returned. *`tangents`* consists of four values. The first two
values correspond to the y (row) and the x (column) value of the tangent at
the start of the curve and the second two values to the tangent at the end of
the curve, respectively.

The weight vector is not returned because it consists of
equal entries. As a consequence, one can use *"auto"* as weight vector
if the control information is used in a subsequent call to the operator
[`GenContourNurbsXld`](gen_contour_nurbs_xld.md). For more information on NURBS see the
documentation of [`GenContourNurbsXld`](gen_contour_nurbs_xld.md).

Directly after calling `DrawNurbsInterp`, you can add interpolation
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
  parameter *`keepRatio`* has to be set to *"true"*.

By pressing the Shift key again you can switch back to the edit mode.
Pressing the right mouse button terminates the procedure.

The appearance of the curve while drawing is determined by the line width,
size, and color set via the operators [`SetColor`](set_color.md), [`SetColored`](set_colored.md),
[`SetLineWidth`](set_line_width.md), and [`SetLineStyle`](set_line_style.md). The tangents and all
handles are displayed in the second color set by [`SetColor`](set_color.md) or
[`SetColored`](set_colored.md). Their line width is fixed to 1 and their line style is
fixed to a drawn-through line.

## Attention

In contrast to [`DrawNurbs`](draw_nurbs.md), each point specified by the user
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

**`contOut`** (output_object)  xld_cont `→` [HXLDCont](HXLDCont.md)

Contour of the curve.

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`rotate`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Enable rotation?

Default:
"true"

List of values:
"false", "true"

**`move`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Enable moving?

Default:
"true"

List of values:
"false", "true"

**`scale`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Enable scaling?

Default:
"true"

List of values:
"false", "true"

**`keepRatio`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Keep ratio while scaling?

Default:
"true"

List of values:
"false", "true"

**`degree`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

The degree p of the NURBS curve.
Reasonable values are 3 to 5.

Default:
3

Suggested values:
2, 3, 4, 5

Restriction:
`Degree >= 2 && Degree <= 9`

**`controlRows`** (output_control)  coordinates.y-array `→` [HTuple](HTuple.md) (*double*)

Row coordinates of the control polygon.

**`controlCols`** (output_control)  coordinates.x-array `→` [HTuple](HTuple.md) (*double*)

Column coordinates of the control polygon.

**`knots`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Knot vector.

**`rows`** (output_control)  coordinates.y-array `→` [HTuple](HTuple.md) (*double*)

Row coordinates of the points specified by the user.

**`cols`** (output_control)  coordinates.x-array `→` [HTuple](HTuple.md) (*double*)

Column coordinates of the points specified by the user.

**`tangents`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Tangents specified by the user.

## Result

`DrawNurbsInterp` returns 2 (
H_MSG_TRUE)
if the window is valid.
If necessary, an exception is raised.

## Possible Predecessors

`OpenWindow`

## Possible Successors

`SetColored`,
`SetLineWidth`,
`SetDraw`

## Alternatives

`DrawXld`,
`DrawNurbs`

## See also

`DrawNurbsInterpMod`,
`DrawNurbs`,
`GenContourNurbsXld`

## Module

Foundation
