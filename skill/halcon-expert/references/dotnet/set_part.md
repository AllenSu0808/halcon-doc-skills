# SetPart (Operator)

## Name

`SetPart` — Modify the displayed image part.

## Signature

`static void HOperatorSet.SetPart(HTuple windowHandle, HTuple row1, HTuple column1, HTuple row2, HTuple column2)`

`void HWindow.SetPart(HTuple row1, HTuple column1, HTuple row2, HTuple column2)`

`void HWindow.SetPart(int row1, int column1, int row2, int column2)`

## Description

`SetPart` modifies the image part that is displayed in
the window. (*`row1`*,*`column1`*) denotes the
upper left corner and (*`row2`*,*`column2`*) the lower
right corner of the image part to display. The changed values are
used by gray value output operators ([`DispImage`](disp_image.md),
[`DispColor`](disp_color.md)) as well as region output operators
([`DispRegion`](disp_region.md)).

If only part of an image is displayed, it will be zoomed to full
window size. The zooming interpolation method can be set with
[`SetPartStyle`](set_part_style.md). [`GetPart`](get_part.md) returns the
values of the image part to display.
Adapting the size of the window to the size of the image part to be
displayed will prevent slowing down the display due to necessary
interpolations.
Thus, the window preferably has the same size as the image part to be
displayed, or otherwise half its size, quarter its size, etc.

Beside setting the image part directly, the following special modes are
supported:

- ***`row1`* = *`column1`* =
  *`row2`* = *`column2`* = *-1*:** —

  The window size is chosen as the image part, i.e. no
  zooming of the image will be performed.
- ***`row1`*, *`column1`* > *-1* and
  *`row2`* = *`column2`* = *-1*:** —

  The size of the last displayed image (in this window) is chosen
  as the image part, i.e. the image can completely be displayed in
  the image. For this the image will be zoomed if necessary.
- ***`row1`* = *`column1`* = *0* and
  *`row2`* = *`column2`* = *-2*:** —

  The size of the last displayed image (in this window) is used
  to adapt the image part such that the image fits completely into the
  window, preserving the aspect ratio of the image. For this the image
  will be zoomed if necessary.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`row1`** (input_control)  rectangle.origin.y `→` [HTuple](HTuple.md) (*int* / long / double)

Row of the upper left corner of the
chosen image part.

Default:
0

**`column1`** (input_control)  rectangle.origin.x `→` [HTuple](HTuple.md) (*int* / long / double)

Column of the upper left corner of the
chosen image part.

Default:
0

**`row2`** (input_control)  rectangle.corner.y `→` [HTuple](HTuple.md) (*int* / long / double)

Row of the lower right corner of the
chosen image part.

Default:
-1

Restriction:
`Row2 >= Row1 || Row2 == -1 || Row1 == 0 && Row2 == -2`

**`column2`** (input_control)  rectangle.corner.x `→` [HTuple](HTuple.md) (*int* / long / double)

Column of the lower right corner of the
chosen image part.

Default:
-1

Restriction:
`Column2 >= Column1 || Column2 == -1 || Column1 == 0 && Column2 == -2`

## Example (HDevelop)

```
get_system('width',Width)
get_system('height',Height)
set_part(WindowHandle,0,0,Height-1,Width-1)
disp_image(Image,WindowHandle)
draw_rectangle1(WindowHandle,Row1,Column1,Row2,Column2)
set_part(WindowHandle,Row1,Column1,Row2,Column2)
disp_image(Image,WindowHandle)
```

## Result

`SetPart` returns 2 (
H_MSG_TRUE)
if the window is valid.
Otherwise an exception is raised.

## Possible Predecessors

`GetPart`

## Possible Successors

`SetPartStyle`,
`DispImage`,
`DispRegion`

## Alternatives

`AffineTransImage`

## See also

`GetPart`,
`SetPartStyle`,
`DispRegion`,
`DispImage`,
`DispColor`

## Module

Foundation
