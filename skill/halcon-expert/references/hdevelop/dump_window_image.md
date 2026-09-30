# dump_window_image (Operator)

## Name

`dump_window_image` — Write the window content in an image object.

## Signature

`dump_window_image( : Image : WindowHandle : )`

## Description

`dump_window_image` writes the content of the graphics window
(*`WindowHandle`*) in an image (*`Image`*).
To transform gray values the current color table of the window is
used.

## Attention

Under Unix-like systems, the graphics window must be completely visible on the
root window, because otherwise the contents of the window cannot be
read due to limitations in X Windows.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Image`** (output_object)  image `→` object (byte)

Saved image.

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

## Result

If the window is valid `dump_window_image` returns 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

## Possible Predecessors

`open_window`,
`set_draw`,
`set_color`,
`set_colored`,
`set_line_width`,
`disp_region`

## See also

`open_window`,
`set_system`,
`dump_window`

## Module

Foundation
