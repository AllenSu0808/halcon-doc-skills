# draw_nurbs_interp_mod (Operator)

## Name

`draw_nurbs_interp_mod` — Interactive modification of a NURBS curve using interpolation.

## Warning

**This operator does not work in an HDevelop graphics window opened with
`dev_open_window`.**

## Signature

`draw_nurbs_interp_mod( : ContOut : WindowHandle, Rotate, Move, Scale, KeepRatio, Edit, Degree, RowsIn, ColsIn, TangentsIn : ControlRows, ControlCols, Knots, Rows, Cols, Tangents)`

## Description

`draw_nurbs_interp_mod` returns the contour *`ContOut`* of a
NURBS curve of degree *`Degree`*, which has been modified
interactively by the user in the window *`WindowHandle`*.

In addition to *`ContOut`* the control information of
the curve (*`ControlRows`*, *`ControlCols`*, and *`Knots`*),
the interpolation points (*`Rows`*, *`Cols`*) specified by the
user and the tangents at the first and the last point (*`Tangents`*)
are returned. *`Tangents`* consists of four values. The first two
values correspond to the y (row) and the x (column) value of the tangent at
the start of the curve and the second two values to the tangent at the end
of the curve, respectively.

The weight vector is not returned because it consists of
equal entries. As a consequence one can use *'auto'* as weight vector,
if the control information is used in a subsequent call to the operator
[`gen_contour_nurbs_xld`](gen_contour_nurbs_xld.md). For more information on NURBS see the
documentation of [`gen_contour_nurbs_xld`](gen_contour_nurbs_xld.md).

The input curve is specified by the interpolation points (*`RowsIn`*,
*`ColsIn`*), its degree *`Degree`* and the tangents
*`TangentsIn`*, such that `draw_nurbs_interp_mod` can be applied
to the output data of [`draw_nurbs_interp`](draw_nurbs_interp.md).

You can modify the curve in two ways: by editing the interpolation points,
e.g., by inserting or moving points, or by transforming the curve
as a whole, e.g., by rotating moving or scaling it. Note that you can only
edit the curve if *`Edit`* is set to *'true'*.
Similarly, you can only rotate, move or scale it if *`Rotate`*,
*`Move`*, and *`Scale`*, respectively, are set to *'true'*.

`draw_nurbs_interp_mod` starts in the transformation mode. In this
mode, the curve is displayed together with 3 symbols: a cross in the middle
and an arrow to the right if *`Rotate`* is set to *'true'*, and a
double-headed arrow to the upper right if *`Scale`* is set to
*'true'*.
To switch into the edit mode, press the Shift key; by pressing it again,
you can switch back into the transformation mode.

### Transformation Mode

In this mode a NURBS curve can be rotated, moved and scaled, as long as the
respective parameter *`Rotate`*, *`Move`* and *`Scale`*
are set to *'true'*. The NURBS curve is displayed along with a cross in
its center, an arrow pointing to the right (if *`Rotate`* is set to
*'true'*), and a double arrow (if *`Scale`* is set to
*'true'*).

- To move the curve, click with the left mouse button on the cross
  in the center and then drag it to the new position, i.e., keep the
  mouse button pressed while moving the mouse.
- To rotate it, click with the left mouse button on the arrow and
  then drag it, till the curve has the right direction.
- Scaling is achieved by dragging the double arrow. To keep the
  ratio, the parameter *`KeepRatio`* has to be set to
  *'true'*.

### Edit Mode

In this mode, the curve is displayed together with its interpolation
points and the start and end tangent.
Start and end point are marked by an additional square. You can
perform the following modifications:

- To append new points, click with the left mouse button in the window
  and a new point is added at this position.
- You can delete the point appended last by pressing the Ctrl key.
- To move a point, drag it with the mouse.
- To insert a point on the curve, click on the desired
  position on the curve.
- To close respectively open the curve, click on the first or on
  the last point.

Pressing the right mouse button terminates the procedure.

The appearance of the curve while drawing is determined by the line width,
size and color set via the operators [`set_color`](set_color.md), [`set_colored`](set_colored.md),
[`set_line_width`](set_line_width.md), and [`set_line_style`](set_line_style.md). The tangents and
all handles are displayed in the second color set by [`set_color`](set_color.md) or
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

**`ContOut`** (output_object)  xld_cont `→` object

Contour of the modified curve.

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

**`Edit`** (input_control)  string `→`  (string)

Enable editing?

Default:
'true'

List of values:
'false', 'true'

**`Degree`** (input_control)  integer `→`  (integer)

The degree p of the NURBS curve.
Reasonable values are 3 to 5.

Default:
3

Suggested values:
2, 3, 4, 5

Restriction:
`Degree >= 2 && Degree <= 9`

**`RowsIn`** (input_control)  coordinates.y-array `→`  (real)

Row coordinates of the input interpolation points.

**`ColsIn`** (input_control)  coordinates.x-array `→`  (real)

Column coordinates of the input interpolation points.

**`TangentsIn`** (input_control)  real-array `→`  (real)

Input tangents.

**`ControlRows`** (output_control)  coordinates.y-array `→`  (real)

Row coordinates of the control polygon.

**`ControlCols`** (output_control)  coordinates.x-array `→`  (real)

Column coordinates of the control polygon.

**`Knots`** (output_control)  real-array `→`  (real)

Knot vector.

**`Rows`** (output_control)  coordinates.y-array `→`  (real)

Row coordinates of the points specified by the user.

**`Cols`** (output_control)  coordinates.x-array `→`  (real)

Column coordinates of the points specified by the user.

**`Tangents`** (output_control)  real-array `→`  (real)

Tangents specified by the user.

## Result

`draw_nurbs_interp_mod` returns 2 (
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

`draw_xld_mod`,
`draw_nurbs_mod`

## See also

`draw_nurbs_interp`,
`gen_contour_nurbs_xld`

## Module

Foundation
