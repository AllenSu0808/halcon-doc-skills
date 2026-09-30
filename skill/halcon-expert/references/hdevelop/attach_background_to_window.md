# attach_background_to_window (Operator)

## Name

`attach_background_to_window` — Attach a background image to a HALCON window.

## Signature

`attach_background_to_window(Image : : WindowHandle : )`

## Description

This operator attaches the background image passed in *`Image`*
to a HALCON window defined in *`WindowHandle`*. The input image is
copied. Thus it can be freed safely.

The background image is instantly displayed in the HALCON window
when calling `attach_background_to_window`. All HALCON objects
that were previously displayed in the window will still be displayed
when calling this operator. Thus the previous window content will
not be overwritten.

The window contents are displayed in the following order: first the
background image, then HALCON objects, and finally the drawing objects.
Thus, the drawing object is displayed always on top.
Note that the window will be redrawn for each user interaction within
the window and each call of [`set_part`](set_part.md). HALCON objects can be
deleted from the window with [`clear_window`](clear_window.md).

The background image can be removed from the window with the
operator [`detach_background_from_window`](detach_background_from_window.md).

## Attention

Note that using any synchronous operator which actively probe the event
queue, e.g., [`get_mbutton`](get_mbutton.md) or [`read_char`](read_char.md), will conflict with the
interaction with the drawing objects. In case the state of the cursor has to
be read, please refer to the documentation of your framework of choice for an
appropriate, non-invasive alternative.

Furthermore, the event based functionality should not be used together with
the former blocking operators [`draw_rectangle1`](draw_rectangle1.md),
[`draw_rectangle2`](draw_rectangle2.md), [`draw_region`](draw_region.md), [`draw_xld`](draw_xld.md) or
[`draw_circle`](draw_circle.md). They conflict with the event based functionality, since
they actively fetch all events sent to the HALCON window.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Image`** (input_object)  singlechannelimage `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Background image.

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

## Result

If the window exists and the specified parameters are correct
`attach_background_to_window` returns 2 (
H_MSG_TRUE)
. If necessary an exception
is raised.

## Possible Predecessors

`open_window`

## Possible Successors

`detach_background_from_window`

## Module

Foundation
