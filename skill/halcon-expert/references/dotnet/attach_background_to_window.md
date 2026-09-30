# AttachBackgroundToWindow (Operator)

## Name

`AttachBackgroundToWindow` — Attach a background image to a HALCON window.

## Signature

`static void HOperatorSet.AttachBackgroundToWindow(HObject image, HTuple windowHandle)`

`void HWindow.AttachBackgroundToWindow(HImage image)`

`static void HDrawingObject.AttachBackgroundToWindow(HImage image, HWindow windowHandle)`

## Description

This operator attaches the background image passed in *`image`*
to a HALCON window defined in *`windowHandle`*. The input image is
copied. Thus it can be freed safely.

The background image is instantly displayed in the HALCON window
when calling `AttachBackgroundToWindow`. All HALCON objects
that were previously displayed in the window will still be displayed
when calling this operator. Thus the previous window content will
not be overwritten.

The window contents are displayed in the following order: first the
background image, then HALCON objects, and finally the drawing objects.
Thus, the drawing object is displayed always on top.
Note that the window will be redrawn for each user interaction within
the window and each call of [`SetPart`](set_part.md). HALCON objects can be
deleted from the window with [`ClearWindow`](clear_window.md).

The background image can be removed from the window with the
operator [`DetachBackgroundFromWindow`](detach_background_from_window.md).

## Attention

Note that using any synchronous operator which actively probe the event
queue, e.g., [`GetMbutton`](get_mbutton.md) or [`ReadChar`](read_char.md), will conflict with the
interaction with the drawing objects. In case the state of the cursor has to
be read, please refer to the documentation of your framework of choice for an
appropriate, non-invasive alternative.

Furthermore, the event based functionality should not be used together with
the former blocking operators [`DrawRectangle1`](draw_rectangle1.md),
[`DrawRectangle2`](draw_rectangle2.md), [`DrawRegion`](draw_region.md), [`DrawXld`](draw_xld.md) or
[`DrawCircle`](draw_circle.md). They conflict with the event based functionality, since
they actively fetch all events sent to the HALCON window.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Background image.

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

## Result

If the window exists and the specified parameters are correct
`AttachBackgroundToWindow` returns 2 (
H_MSG_TRUE)
. If necessary an exception
is raised.

## Possible Predecessors

`OpenWindow`

## Possible Successors

`DetachBackgroundFromWindow`

## Module

Foundation
