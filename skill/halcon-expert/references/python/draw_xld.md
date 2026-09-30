# draw_xld (Operator)

## Name

`draw_xld` — Interactive drawing of a contour.

## Signature

`def draw_xld(window_handle: HHandle, rotate: str, move: str, scale: str, keep_ratio: str) -> HObject`

## Description

`draw_xld` returns a contour, which has been created interactively
by the user in the window.

Directly after calling `draw_xld` you can add contour points by
clicking with the left mouse button in the window at the desired positions.
You delete the point appended last by pressing the Ctrl key. As soon as you
add three contour points, 5 so-called pick points are displayed, one in the
middle and 4 at the corners of the surrounding rectangle. By clicking on a
pick point you can close the contour or open it again. If the contour is
closed, the pick points are displayed in form of squares, otherwise they
are shaped like a 'u'.

If the contour is closed you can

- move contour points by clicking with the
  left mouse button on a point marked by a rectangle and keep the mouse
  button pressed while moving the mouse,
- insert contour points by clicking with the left mouse button in the
  vicinity of a line and then move the mouse to the position where you want
  the new point to be placed, and
- delete contour points by selecting the point which should be deleted
  with the left mouse button and then press the Ctrl key.

By pressing the Shift key, you can switch into the transformation mode.
In this mode you can rotate, move, and scale the contour as a whole, but only
if you set the parameters *`rotate`*, *`move`*, and
*`scale`*, respectively, to *"true"*. Instead of the pick points,
3 symbols are displayed with the contour: a cross in the middle and an arrow
to the right if *`rotate`* is set to *"true"*, and a double-headed
arrow to the upper right if *`scale`* is set to *"true"*.

You can

- move the contour by clicking the left mouse button on the cross in
  the center and then dragging it to the new position,
- rotate it by clicking with the left mouse button on the arrow and
  then dragging it, till the contour has the right direction, and
- scale it by dragging the double arrow. To keep the ratio the
  parameter *`keep_ratio`* has to be set to *"true"*.

Pressing the right mouse button terminates the procedure.

## Attention

If used in a buffer window, mouse events have to be supplied by the
application, while the draw operator must be run in another thread.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

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

## Result

`draw_xld` returns 2 (
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
