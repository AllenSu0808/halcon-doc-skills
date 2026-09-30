# GetWindowBackgroundImage (Operator)

## Name

`GetWindowBackgroundImage` — Gets a copy of the background image of the HALCON window.

## Signature

`static void HOperatorSet.GetWindowBackgroundImage(out HObject backgroundImage, HTuple windowHandle)`

`HImage HWindow.GetWindowBackgroundImage()`

## Description

`GetWindowBackgroundImage` returns a copy of the background image
*`backgroundImage`* set in the window *`windowHandle`*.
This operator is specially useful in cases where
the user would like to perform some operations in one of the callback
functions of a drawing object attached to the window. See
[`SetDrawingObjectCallback`](set_drawing_object_callback.md) for more details.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`backgroundImage`** (output_object)  (multichannel-)image `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Copy of the background image.

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

## Result

If the window exists and the specified parameters are correct
`GetWindowBackgroundImage` returns 2 (
H_MSG_TRUE)
. If necessary an
exception is raised.

## Possible Predecessors

`AttachBackgroundToWindow`

## Possible Successors

`CloseWindow`,
`DetachBackgroundFromWindow`,
`AttachDrawingObjectToWindow`

## See also

`AttachBackgroundToWindow`,
`DetachDrawingObjectFromWindow`

## Module

Foundation
