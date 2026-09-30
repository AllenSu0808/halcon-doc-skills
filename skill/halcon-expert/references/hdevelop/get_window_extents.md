# get_window_extents (Operator)

## Name

`get_window_extents` — Information about a window's size and position.

## Signature

`get_window_extents( : : WindowHandle : Row, Column, Width, Height)`

## Description

`get_window_extents` returns the position of the upper left
corner, as well as width and height of the output window.

## Attention

Size and position of a window may be modified by the window manager, without
explicit instruction in the program. Therefore the values which are returned by
`get_window_extents` may change cause of side effects.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`Row`** (output_control)  rectangle.origin.y `→`  (integer)

Row index of upper left corner of the window.

**`Column`** (output_control)  rectangle.origin.x `→`  (integer)

Column index of upper left corner of the window.

**`Width`** (output_control)  rectangle.extent.x `→`  (integer)

Window width.

**`Height`** (output_control)  rectangle.extent.y `→`  (integer)

Window height.

## Example (HDevelop)

```
open_window(100,100,200,200,'root','visible','',WindowHandle)
fwrite_string(FileHandle, 'Move the window with the mouse!')
fnew_line(FileHandle)
repeat
get_mbutton(WindowHandle,_,_,Button)
get_window_extents(WindowHandle,Row,Column,Width,Height)
fwrite_string(FileHandle, ['(',Row,',',Column,')'])
fnew_line(FileHandle)
until(Button == 4)
```

## Result

If the window is valid `get_window_extents` returns 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

## Possible Predecessors

`open_window`,
`set_draw`,
`set_color`,
`set_colored`,
`set_line_width`

## See also

`set_window_extents`,
`open_window`

## Module

Foundation
