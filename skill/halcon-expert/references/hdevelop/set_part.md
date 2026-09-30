# set_part (Operator)

## Name

`set_part` — Modify the displayed image part.

## Signature

`set_part( : : WindowHandle, Row1, Column1, Row2, Column2 : )`

## Description

`set_part` modifies the image part that is displayed in
the window. (*`Row1`*,*`Column1`*) denotes the
upper left corner and (*`Row2`*,*`Column2`*) the lower
right corner of the image part to display. The changed values are
used by gray value output operators ([`disp_image`](disp_image.md),
[`disp_color`](disp_color.md)) as well as region output operators
([`disp_region`](disp_region.md)).

If only part of an image is displayed, it will be zoomed to full
window size. The zooming interpolation method can be set with
[`set_part_style`](set_part_style.md). [`get_part`](get_part.md) returns the
values of the image part to display.
Adapting the size of the window to the size of the image part to be
displayed will prevent slowing down the display due to necessary
interpolations.
Thus, the window preferably has the same size as the image part to be
displayed, or otherwise half its size, quarter its size, etc.

Beside setting the image part directly, the following special modes are
supported:

- ***`Row1`* = *`Column1`* =
  *`Row2`* = *`Column2`* = *-1*:** —

  The window size is chosen as the image part, i.e. no
  zooming of the image will be performed.
- ***`Row1`*, *`Column1`* > *-1* and
  *`Row2`* = *`Column2`* = *-1*:** —

  The size of the last displayed image (in this window) is chosen
  as the image part, i.e. the image can completely be displayed in
  the image. For this the image will be zoomed if necessary.
- ***`Row1`* = *`Column1`* = *0* and
  *`Row2`* = *`Column2`* = *-2*:** —

  The size of the last displayed image (in this window) is used
  to adapt the image part such that the image fits completely into the
  window, preserving the aspect ratio of the image. For this the image
  will be zoomed if necessary.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`Row1`** (input_control)  rectangle.origin.y `→`  (integer / real)

Row of the upper left corner of the
chosen image part.

Default:
0

**`Column1`** (input_control)  rectangle.origin.x `→`  (integer / real)

Column of the upper left corner of the
chosen image part.

Default:
0

**`Row2`** (input_control)  rectangle.corner.y `→`  (integer / real)

Row of the lower right corner of the
chosen image part.

Default:
-1

Restriction:
`Row2 >= Row1 || Row2 == -1 || Row1 == 0 && Row2 == -2`

**`Column2`** (input_control)  rectangle.corner.x `→`  (integer / real)

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

`set_part` returns 2 (
H_MSG_TRUE)
if the window is valid.
Otherwise an exception is raised.

## Possible Predecessors

`get_part`

## Possible Successors

`set_part_style`,
`disp_image`,
`disp_region`

## Alternatives

`affine_trans_image`

## See also

`get_part`,
`set_part_style`,
`disp_region`,
`disp_image`,
`disp_color`

## Module

Foundation
