# set_part (Operator)

## Name

`set_part` — Modify the displayed image part.

## Signature

`def set_part(window_handle: HHandle, row_1: Union[int, float], column_1: Union[int, float], row_2: Union[int, float], column_2: Union[int, float]) -> None`

## Description

`set_part` modifies the image part that is displayed in
the window. (*`row_1`*,*`column_1`*) denotes the
upper left corner and (*`row_2`*,*`column_2`*) the lower
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

- ***`row_1`* = *`column_1`* =
  *`row_2`* = *`column_2`* = *-1*:** —

  The window size is chosen as the image part, i.e. no
  zooming of the image will be performed.
- ***`row_1`*, *`column_1`* > *-1* and
  *`row_2`* = *`column_2`* = *-1*:** —

  The size of the last displayed image (in this window) is chosen
  as the image part, i.e. the image can completely be displayed in
  the image. For this the image will be zoomed if necessary.
- ***`row_1`* = *`column_1`* = *0* and
  *`row_2`* = *`column_2`* = *-2*:** —

  The size of the last displayed image (in this window) is used
  to adapt the image part such that the image fits completely into the
  window, preserving the aspect ratio of the image. For this the image
  will be zoomed if necessary.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`row_1`** (input_control)  rectangle.origin.y `→` Union[int, float]

Row of the upper left corner of the
chosen image part.

Default:
0

**`column_1`** (input_control)  rectangle.origin.x `→` Union[int, float]

Column of the upper left corner of the
chosen image part.

Default:
0

**`row_2`** (input_control)  rectangle.corner.y `→` Union[int, float]

Row of the lower right corner of the
chosen image part.

Default:
-1

Restriction:
`Row2 >= Row1 || Row2 == -1 || Row1 == 0 && Row2 == -2`

**`column_2`** (input_control)  rectangle.corner.x `→` Union[int, float]

Column of the lower right corner of the
chosen image part.

Default:
-1

Restriction:
`Column2 >= Column1 || Column2 == -1 || Column1 == 0 && Column2 == -2`

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
