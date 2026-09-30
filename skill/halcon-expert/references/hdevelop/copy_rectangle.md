# copy_rectangle (Operator)

## Name

`copy_rectangle` — Copy all pixels within rectangles between output windows.

## Signature

`copy_rectangle( : : WindowHandleSource, WindowHandleDestination, Row1, Column1, Row2, Column2, DestRow, DestColumn : )`

## Description

`copy_rectangle` copies all pixels from the window
*`WindowHandleSource`* in the
window
*`WindowHandleDestination`*. It copies pixels which reside
inside a rectangle which is specified by parameters *`Row1`*,
*`Column1`*, *`Row2`* and *`Column2`*. The target
position is specified through the upper left corner of the rectangle
(*`DestRow`*, *`DestColumn`*).

If you want to move more than one rectangle, you may pass them at
once (in form of the tuple mode).

You may use `copy_rectangle` to copy edited graphics from an
“invisible” window in a visible window. Therefore a window with
the option 'buffer' is opened. The graphics is then displayed in
this window and is copied in a visible window afterwards. The
advantage of this strategy is, that `copy_rectangle` is much
more rapid than output operators as, e.g., [`disp_channel`](disp_channel.md). This
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

**`WindowHandleSource`** (input_control)  window `→`  (handle)

Source window handle.

**`WindowHandleDestination`** (input_control)  window `→`  (handle)

Destination window handle.

**`Row1`** (input_control)  rectangle.origin.y(-array) `→`  (integer)

Row index of upper left corner in the source window.

Default:
0

Value range:
`0
≤
Row1
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

**`Column1`** (input_control)  rectangle.origin.x(-array) `→`  (integer)

Column index of upper left corner in the source window.

Default:
0

Value range:
`0
≤
Column1
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

**`Row2`** (input_control)  rectangle.corner.y(-array) `→`  (integer)

Row index of lower right corner in the source window.

Default:
128

Value range:
`0
≤
Row2
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

Restriction:
`Row2 >= Row1`

**`Column2`** (input_control)  rectangle.corner.x(-array) `→`  (integer)

Column index of lower right corner in the source window.

Default:
128

Value range:
`0
≤
Column2
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

Restriction:
`Column2 >= Column1`

**`DestRow`** (input_control)  point.y(-array) `→`  (integer)

Row index of upper left corner in the target window.

Default:
0

Value range:
`0
≤
DestRow
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

**`DestColumn`** (input_control)  point.x(-array) `→`  (integer)

Column index of upper left corner in the target window.

Default:
0

Value range:
`0
≤
DestColumn
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
[`close_window`](close_window.md) returns 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

## Possible Predecessors

`open_window`

## Possible Successors

`close_window`

## Alternatives

`move_rectangle`,
`slide_image`

## See also

`open_window`

## Module

Foundation
