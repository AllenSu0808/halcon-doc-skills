# attach_drawing_object_to_window (Operator)

## Name

`attach_drawing_object_to_window` — Attach an existing drawing object to a HALCON window.

## Signature

`attach_drawing_object_to_window( : : WindowHandle, DrawHandle : )`

## Description

`attach_drawing_object_to_window` attaches the drawing object *`DrawHandle`*
to the HALCON window specified in *`WindowHandle`*.
When attached to a window the drawing object is displayed in the specified
window. The drawing object can be modified interactively in the HALCON window.
The window is automatically updated when the objects properties are modified
using the operator [`set_drawing_object_params`](set_drawing_object_params.md).

When two or more drawing objects overlap, a double-click on the currently
selected drawing object will shift the focus to the next drawing object.

Furthermore it is possible to react to modifications of the drawing object
caused by user interaction when using any of the language interface.
Please see the documentation of [`set_drawing_object_callback`](set_drawing_object_callback.md) for
more details.

The drawing object can be removed from the current window with the operator
[`detach_drawing_object_from_window`](detach_drawing_object_from_window.md).

As soon as a drawing object is attached to the window, each HALCON object
which is displayed by any of the graphical operators, namely
[`disp_obj`](disp_obj.md), [`disp_region`](disp_region.md), [`disp_image`](disp_image.md) and
[`disp_xld`](disp_xld.md), is stored internally in a graphical stack associated with
the *`WindowHandle`*, so that they can be displayed together with the
attached drawing object. These remain in the stack until the user calls
[`clear_window`](clear_window.md) or the window is closed.

The size of this graphical stack can be queried and modified
with [`get_system`](get_system.md) and [`set_system`](set_system.md), respectively. See the
corresponding documentation reference for further details.

## Attention

Note that using any synchronous operator which actively probe the event
queue, e.g., [`get_mbutton`](get_mbutton.md) or [`read_char`](read_char.md), will conflict with the
interaction with the drawing objects. In case you need to read the state of the
cursor, please refer to the documentation of your framework of choice for an
appropriate, non-invasive alternative.

Furthermore, the event based functionality should not be used together with
the former blocking operators [`draw_rectangle1`](draw_rectangle1.md),
[`draw_rectangle2`](draw_rectangle2.md), [`draw_region`](draw_region.md), [`draw_xld`](draw_xld.md) or
[`draw_circle`](draw_circle.md). They conflict with the event based functionality, since
they actively fetch all events sent to the HALCON window.

When working under UNIX/Linux it is necessary to turn on the support for
multithreading in the Xlib. This is achieved by calling the function
XInitThreads() before any other function of the Xlib library. This means
that you need to call it before any other function or method of your
graphical development environment of choice. See the documentation of the
function XInitThreads() in the corresponding manual page for further details.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`DrawHandle`** (input_control)  drawing_object `→`  (handle)

Handle of the drawing object.

## Result

`attach_drawing_object_to_window` returns 2 (
H_MSG_TRUE)
, if the *`DrawHandle`*
and *`WindowHandle`* are valid. Otherwise an exception is raised.

## Possible Predecessors

`create_drawing_object_rectangle1`,
`create_drawing_object_xld`,
`create_drawing_object_circle_sector`,
`create_drawing_object_ellipse_sector`,
`create_drawing_object_ellipse`,
`create_drawing_object_line`,
`create_drawing_object_rectangle2`,
`create_drawing_object_circle`,
`create_drawing_object_text`

## Possible Successors

`detach_drawing_object_from_window`,
`get_drawing_object_params`,
`get_drawing_object_iconic`

## See also

`set_drawing_object_callback`,
`get_drawing_object_iconic`,
`get_drawing_object_params`

## Module

Foundation
