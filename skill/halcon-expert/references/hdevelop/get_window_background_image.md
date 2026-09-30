# get_window_background_image (Operator)

## Name

`get_window_background_image` — Gets a copy of the background image of the HALCON window.

## Signature

`get_window_background_image( : BackgroundImage : WindowHandle : )`

## Description

`get_window_background_image` returns a copy of the background image
*`BackgroundImage`* set in the window *`WindowHandle`*.
This operator is specially useful in cases where
the user would like to perform some operations in one of the callback
functions of a drawing object attached to the window. See
[`set_drawing_object_callback`](set_drawing_object_callback.md) for more details.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`BackgroundImage`** (output_object)  (multichannel-)image `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Copy of the background image.

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

## Result

If the window exists and the specified parameters are correct
`get_window_background_image` returns 2 (
H_MSG_TRUE)
. If necessary an
exception is raised.

## Possible Predecessors

`attach_background_to_window`

## Possible Successors

`close_window`,
`detach_background_from_window`,
`attach_drawing_object_to_window`

## See also

`attach_background_to_window`,
`detach_drawing_object_from_window`

## Module

Foundation
