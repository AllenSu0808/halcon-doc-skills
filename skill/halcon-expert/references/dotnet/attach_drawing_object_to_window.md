# AttachDrawingObjectToWindow (Operator)

## Name

`AttachDrawingObjectToWindow` — Attach an existing drawing object to a HALCON window.

## Signature

`static void HOperatorSet.AttachDrawingObjectToWindow(HTuple windowHandle, HTuple drawHandle)`

`void HWindow.AttachDrawingObjectToWindow(HDrawingObject drawHandle)`

## Description

`AttachDrawingObjectToWindow` attaches the drawing object *`drawHandle`*
to the HALCON window specified in *`windowHandle`*.
When attached to a window the drawing object is displayed in the specified
window. The drawing object can be modified interactively in the HALCON window.
The window is automatically updated when the objects properties are modified
using the operator [`SetDrawingObjectParams`](set_drawing_object_params.md).

When two or more drawing objects overlap, a double-click on the currently
selected drawing object will shift the focus to the next drawing object.

Furthermore it is possible to react to modifications of the drawing object
caused by user interaction when using any of the language interface.
Please see the documentation of [`SetDrawingObjectCallback`](set_drawing_object_callback.md) for
more details.

The drawing object can be removed from the current window with the operator
[`DetachDrawingObjectFromWindow`](detach_drawing_object_from_window.md).

As soon as a drawing object is attached to the window, each HALCON object
which is displayed by any of the graphical operators, namely
[`DispObj`](disp_obj.md), [`DispRegion`](disp_region.md), [`DispImage`](disp_image.md) and
[`DispXld`](disp_xld.md), is stored internally in a graphical stack associated with
the *`windowHandle`*, so that they can be displayed together with the
attached drawing object. These remain in the stack until the user calls
[`ClearWindow`](clear_window.md) or the window is closed.

The size of this graphical stack can be queried and modified
with [`GetSystem`](get_system.md) and [`SetSystem`](set_system.md), respectively. See the
corresponding documentation reference for further details.

## Attention

Note that using any synchronous operator which actively probe the event
queue, e.g., [`GetMbutton`](get_mbutton.md) or [`ReadChar`](read_char.md), will conflict with the
interaction with the drawing objects. In case you need to read the state of the
cursor, please refer to the documentation of your framework of choice for an
appropriate, non-invasive alternative.

Furthermore, the event based functionality should not be used together with
the former blocking operators [`DrawRectangle1`](draw_rectangle1.md),
[`DrawRectangle2`](draw_rectangle2.md), [`DrawRegion`](draw_region.md), [`DrawXld`](draw_xld.md) or
[`DrawCircle`](draw_circle.md). They conflict with the event based functionality, since
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

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`drawHandle`** (input_control)  drawing_object `→` [HDrawingObject](HDrawingObject.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the drawing object.

## Result

`AttachDrawingObjectToWindow` returns 2 (
H_MSG_TRUE)
, if the *`drawHandle`*
and *`windowHandle`* are valid. Otherwise an exception is raised.

## Possible Predecessors

`CreateDrawingObjectRectangle1`,
`CreateDrawingObjectXld`,
`CreateDrawingObjectCircleSector`,
`CreateDrawingObjectEllipseSector`,
`CreateDrawingObjectEllipse`,
`CreateDrawingObjectLine`,
`CreateDrawingObjectRectangle2`,
`CreateDrawingObjectCircle`,
`CreateDrawingObjectText`

## Possible Successors

`DetachDrawingObjectFromWindow`,
`GetDrawingObjectParams`,
`GetDrawingObjectIconic`

## See also

`SetDrawingObjectCallback`,
`GetDrawingObjectIconic`,
`GetDrawingObjectParams`

## Module

Foundation
