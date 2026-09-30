# DrawNurbsMod (Operator)

## Name

`DrawNurbsMod` — Interactive modification of a NURBS curve.

## Warning

**This operator does not work in an HDevelop graphics window opened with
`dev_open_window`.**

## Signature

`static void HOperatorSet.DrawNurbsMod(out HObject contOut, HTuple windowHandle, HTuple rotate, HTuple move, HTuple scale, HTuple keepRatio, HTuple edit, HTuple degree, HTuple rowsIn, HTuple colsIn, HTuple weightsIn, out HTuple rows, out HTuple cols, out HTuple weights)`

`void HXLDCont.DrawNurbsMod(HWindow windowHandle, string rotate, string move, string scale, string keepRatio, string edit, int degree, HTuple rowsIn, HTuple colsIn, HTuple weightsIn, out HTuple rows, out HTuple cols, out HTuple weights)`

`HXLDCont HWindow.DrawNurbsMod(string rotate, string move, string scale, string keepRatio, string edit, int degree, HTuple rowsIn, HTuple colsIn, HTuple weightsIn, out HTuple rows, out HTuple cols, out HTuple weights)`

## Description

`DrawNurbsMod` returns the contour *`contOut`* and control
information (*`rows`*, *`cols`*, and *`weights`*) of a NURBS
curve of degree *`degree`*, which has been interactively
modified by the user in the window *`windowHandle`*. For additional
information concerning NURBS curves, see the documentation of
[`GenContourNurbsXld`](gen_contour_nurbs_xld.md). To use the control information
*`rows`*, *`cols`*, and *`weights`* in a subsequent call to
the operator [`GenContourNurbsXld`](gen_contour_nurbs_xld.md), the knot vector `knots`
should be set to *"auto"*.

The input NURBS curve is specified by its control polygon
(*`rowsIn`*, *`colsIn`*), its weight vector *`weightsIn`* and
its degree *`degree`*. The knot vector is assumed to be uniform (i.e.
*"auto"* in [`GenContourNurbsXld`](gen_contour_nurbs_xld.md)).

You can modify the curve in two ways: by editing the control polygon,
e.g., by inserting or moving control points, or by transforming the contour
as a whole, e.g., by rotating moving or scaling it. Note that you can only
edit the control polygon if *`edit`* is set to *"true"*.
Similarly, you can only rotate, move or scale it if *`rotate`*,
*`move`*, and *`scale`*, respectively, are set to *"true"*.

`DrawNurbsMod` starts in the transformation mode. In this mode, the
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
  ratio, the parameter *`keepRatio`* has to be set to
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
size and color set via the operators [`SetColor`](set_color.md), [`SetColored`](set_colored.md),
[`SetLineWidth`](set_line_width.md), and [`SetLineStyle`](set_line_style.md). The control polygon and
all handles are displayed in the second color set by [`SetColor`](set_color.md) or
[`SetColored`](set_colored.md). Their line width is fixed to 1 and their line style is
fixed to a drawn-through line.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contOut`** (output_object)  xld_cont `→` [HXLDCont](HXLDCont.md)

Contour of the modified curve.

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

**`edit`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Enable editing?

Default:
"true"

List of values:
"false", "true"

**`degree`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

The degree p of the NURBS curve.
Reasonable values are 3 to 25.

Default:
3

Suggested values:
2, 3, 4, 5

Restriction:
`Degree >= 2`

**`rowsIn`** (input_control)  coordinates.y-array `→` [HTuple](HTuple.md) (*double*)

Row coordinates of the input control polygon.

**`colsIn`** (input_control)  coordinates.x-array `→` [HTuple](HTuple.md) (*double*)

Column coordinates of the input control polygon.

**`weightsIn`** (input_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Input weight vector.

**`rows`** (output_control)  coordinates.y-array `→` [HTuple](HTuple.md) (*double*)

Row coordinates of the control polygon.

**`cols`** (output_control)  coordinates.x-array `→` [HTuple](HTuple.md) (*double*)

Columns coordinates of the control polygon.

**`weights`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Weight vector.

## Result

`DrawNurbsMod` returns 2 (
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

`DrawNurbsInterpMod`,
`DrawXldMod`

## See also

`DrawNurbs`,
`DrawNurbsInterp`,
`GenContourNurbsXld`

## Module

Foundation
