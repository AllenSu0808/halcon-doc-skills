# draw_xld_mod (Operator)

## Name

`draw_xld_mod` — Interactive modification of a contour.

## Signature

`def draw_xld_mod(cont_in: HObject, window_handle: HHandle, rotate: str, move: str, scale: str, keep_ratio: str, edit: str) -> HObject`

## Description

`draw_xld_mod` returns a contour, which has been interactively
modified by the user in the window.

You can modify the contour in two ways: by editing the contour itself,
e.g., by inserting or moving contour points, or by transforming the contour
as a whole, e.g., by rotating moving or scaling it. Note that you can only
edit a contour if *`edit`* is set to *"true"*.
Similarly, you can only rotate, move or scale it if *`rotate`*,
*`move`*, and *`scale`*, respectively, are set to *"true"*.

`draw_xld_mod` starts in the transformation mode. In this mode, the
contour is displayed together with 3 symbols: a cross in the middle and an
arrow to the right if *`rotate`* is set to *"true"*, and a
double-headed arrow to the upper right if *`scale`* is set to
*"true"*.
To switch into the edit mode, press the Shift key; by pressing it again,
you can switch back into the transformation mode.

### Transformation Mode

In this mode a contour can be rotated, moved and scaled, as long as the
respective parameter *`rotate`*, *`move`* and *`scale`*
are set to *"true"*. The contour is displayed along with a cross in its
center, an arrow pointing to the right (if *`rotate`* is set to
*"true"*), and a double arrow (if *`scale`* is set to
*"true"*).

- To move the contour, click with the left mouse button on the cross in the
  center and then drag it to the new position, i.e., keep the mouse button
  pressed while moving the mouse.
- To rotate it, click with the left mouse button on the arrow and then drag it,
  till the contour has the right direction.
- Scaling is achieved by dragging the double arrow.
  To keep the ratio the parameter *`keep_ratio`* has to be set to *"true"*.

### Edit Mode

In this mode, the contour is display together with 5 pick points, which are
located in the middle and at the corners of the surrounding rectangle. If
the contour is closed, the pick points are displayed as squares, otherwise
shaped like a 'u'. By clicking on a pick point, you can close an open
contour and vice versa. Depending on the state of the contour, you can
perform different modifications.
Open contours (pick points shaped like a 'u')

- To append points, click with the left mouse button in the window and a new
  point is added at this position.
- You can delete the point appended last by pressing the Ctrl key.
- To move or insert points, you must first close the contour by clicking on
  one of the pick points.

Closed contours (square pick points)

- To move a point, click with the left mouse button on a point marked by a
  rectangle and then drag it to the new position.
- To insert a point, click with the left mouse button in the vicinity of a
  line and then move the mouse to the position where you want the new point
  to be placed.
- To delete a point, select the point which should be deleted with the left
  mouse button and then press the Ctrl key.

Pressing the right mouse button terminates the procedure.

## Attention

If used in a buffer window, mouse events have to be supplied by the
application, while the draw operator must be run in another thread.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`cont_in`** (input_object)  xld_cont `→` HObject

Input contour.

**`cont_out`** (output_object)  xld_cont `→` HObject

Modified contour.

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

## Result

`draw_xld_mod` returns 2 (
H_MSG_TRUE)
if the window is valid.
If necessary, an exception is raised.

## Possible Predecessors

`open_window`

## Possible Successors

`reduce_domain`,
`disp_region`,
`set_colored`,
`set_line_width`,
`set_draw`

## Alternatives

`draw_rectangle2`,
`draw_rectangle1`,
`draw_rectangle2`,
`draw_region`

## See also

`gen_rectangle2`,
`draw_circle`,
`draw_ellipse`

## Module

Foundation
