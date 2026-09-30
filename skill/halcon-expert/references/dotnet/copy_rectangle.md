# CopyRectangle (Operator)

## Name

`CopyRectangle` — Copy all pixels within rectangles between output windows.

## Signature

`static void HOperatorSet.CopyRectangle(HTuple windowHandleSource, HTuple windowHandleDestination, HTuple row1, HTuple column1, HTuple row2, HTuple column2, HTuple destRow, HTuple destColumn)`

`void HWindow.CopyRectangle(HWindow windowHandleDestination, HTuple row1, HTuple column1, HTuple row2, HTuple column2, HTuple destRow, HTuple destColumn)`

`void HWindow.CopyRectangle(HWindow windowHandleDestination, int row1, int column1, int row2, int column2, int destRow, int destColumn)`

## Description

`CopyRectangle` copies all pixels from the window
*`windowHandleSource`* in the
window
*`windowHandleDestination`*. It copies pixels which reside
inside a rectangle which is specified by parameters *`row1`*,
*`column1`*, *`row2`* and *`column2`*. The target
position is specified through the upper left corner of the rectangle
(*`destRow`*, *`destColumn`*).

If you want to move more than one rectangle, you may pass them at
once (in form of the tuple mode).

You may use `CopyRectangle` to copy edited graphics from an
“invisible” window in a visible window. Therefore a window with
the option 'buffer' is opened. The graphics is then displayed in
this window and is copied in a visible window afterwards. The
advantage of this strategy is, that `CopyRectangle` is much
more rapid than output operators as, e.g., [`DispChannel`](disp_channel.md). This
means a particular advantage while using demo programs. You could
even realize short “clips”: you have to create for every image of
a sequence a window of a 'buffer' type and pass the data into
it. Output is the image sequence whereat all buffers are copied one
after another in a visible window.

## Attention

Both windows have to reside on the same display.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandleSource`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Source window handle.

**`windowHandleDestination`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Destination window handle.

**`row1`** (input_control)  rectangle.origin.y(-array) `→` [HTuple](HTuple.md) (*int* / long)

Row index of upper left corner in the source window.

Default:
0

Value range:
`0
≤
row1
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

**`column1`** (input_control)  rectangle.origin.x(-array) `→` [HTuple](HTuple.md) (*int* / long)

Column index of upper left corner in the source window.

Default:
0

Value range:
`0
≤
column1
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

**`row2`** (input_control)  rectangle.corner.y(-array) `→` [HTuple](HTuple.md) (*int* / long)

Row index of lower right corner in the source window.

Default:
128

Value range:
`0
≤
row2
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

Restriction:
`Row2 >= Row1`

**`column2`** (input_control)  rectangle.corner.x(-array) `→` [HTuple](HTuple.md) (*int* / long)

Column index of lower right corner in the source window.

Default:
128

Value range:
`0
≤
column2
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

Restriction:
`Column2 >= Column1`

**`destRow`** (input_control)  point.y(-array) `→` [HTuple](HTuple.md) (*int* / long)

Row index of upper left corner in the target window.

Default:
0

Value range:
`0
≤
destRow
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

**`destColumn`** (input_control)  point.x(-array) `→` [HTuple](HTuple.md) (*int* / long)

Column index of upper left corner in the target window.

Default:
0

Value range:
`0
≤
destColumn
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

## Example (HDevelop)

```
read_image(Image,'monkey')
open_window(0,0,-1,-1,'root','buffer','',WindowHandleBuffer)
disp_obj(Image,WindowHandleBuffer)
dev_open_window (0, 0, 512, 512, 'black', WindowHandle)
draw_rectangle1 (WindowHandle, Row1, Column1, Row2, Column2)
copy_rectangle(WindowHandleBuffer,WindowHandle,\
               Row1, Column1, Row2, Column2,Row1,Column1)
close_window(WindowHandleBuffer)
```

## Result

If the output window is valid and if the specified parameters are correct
[`CloseWindow`](close_window.md) returns 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

## Possible Predecessors

`OpenWindow`

## Possible Successors

`CloseWindow`

## Alternatives

`MoveRectangle`,
`SlideImage`

## See also

`OpenWindow`

## Module

Foundation
