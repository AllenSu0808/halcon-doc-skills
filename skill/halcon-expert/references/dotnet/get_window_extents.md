# GetWindowExtents (Operator)

## Name

`GetWindowExtents` — Information about a window's size and position.

## Signature

`static void HOperatorSet.GetWindowExtents(HTuple windowHandle, out HTuple row, out HTuple column, out HTuple width, out HTuple height)`

`void HWindow.GetWindowExtents(out int row, out int column, out int width, out int height)`

## Description

`GetWindowExtents` returns the position of the upper left
corner, as well as width and height of the output window.

## Attention

Size and position of a window may be modified by the window manager, without
explicit instruction in the program. Therefore the values which are returned by
`GetWindowExtents` may change cause of side effects.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`row`** (output_control)  rectangle.origin.y `→` [HTuple](HTuple.md) (*int* / long)

Row index of upper left corner of the window.

**`column`** (output_control)  rectangle.origin.x `→` [HTuple](HTuple.md) (*int* / long)

Column index of upper left corner of the window.

**`width`** (output_control)  rectangle.extent.x `→` [HTuple](HTuple.md) (*int* / long)

Window width.

**`height`** (output_control)  rectangle.extent.y `→` [HTuple](HTuple.md) (*int* / long)

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

If the window is valid `GetWindowExtents` returns 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

## Possible Predecessors

`OpenWindow`,
`SetDraw`,
`SetColor`,
`SetColored`,
`SetLineWidth`

## See also

`SetWindowExtents`,
`OpenWindow`

## Module

Foundation
