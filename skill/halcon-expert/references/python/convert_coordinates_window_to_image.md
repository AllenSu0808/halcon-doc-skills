# convert_coordinates_window_to_image (Operator)

## Name

`convert_coordinates_window_to_image` — Convert window coordinates to image coordinates

## Signature

`def convert_coordinates_window_to_image(window_handle: HHandle, row_window: MaybeSequence[float], column_window: MaybeSequence[float]) -> Tuple[Sequence[float], Sequence[float]]`

`def convert_coordinates_window_to_image_s(window_handle: HHandle, row_window: MaybeSequence[float], column_window: MaybeSequence[float]) -> Tuple[float, float]`

## Description

`convert_coordinates_window_to_image` converts window coordinates
*`row_window`* and *`column_window`* into image coordinates
*`row_image`* and *`column_image`* based on the displayed image part
and the window size of the window defined in *`window_handle`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`row_window`** (input_control)  coordinates.y(-array) `→` MaybeSequence[float]

Row (Y) in window coordinates.

**`column_window`** (input_control)  coordinates.x(-array) `→` MaybeSequence[float]

Column (X) in window coordinates.

**`row_image`** (output_control)  coordinates.y(-array) `→` Sequence[float]

Row in image coordinates.

**`column_image`** (output_control)  coordinates.x(-array) `→` Sequence[float]

Column in image coordinates.

## Example (HDevelop)

```
read_image (Image, 'printer_chip/printer_chip_01')
dev_get_window (WindowHandle)
get_window_extents (WindowHandle, Row, Column, Width, Height)
dev_set_part (450, 300, 750, 600)
dev_display (Image)
*
* Generate rectangle in image coordinates
Row := [474, 746]
Column := [314, 589]
gen_rectangle1 (Rectangle1, Row[0], Column[0], Row[1], Column[1])
* Convert rectangle corner points to window coordinates
convert_coordinates_image_to_window (WindowHandle, Row[[0,1,0,1]], \
    Column[[0,0,1,1]], RowWindow, ColumnWindow)
*
* Window center in window coordinates
WindowCenterRow := Height/2-1
WindowCenterColumn := Width/2-1
* Convert window center to image coordinates
convert_coordinates_window_to_image (WindowHandle, WindowCenterRow, \
    WindowCenterColumn, RowImage, ColumnImage)
*
* Display all points in image coordinates
dev_display (Image)
disp_cross (WindowHandle, Row[[0,1,0,1]], Column[[0,0,1,1]], 6, rad(45))
disp_cross (WindowHandle, RowImage, ColumnImage, 6, 0)
```

## Result

`convert_coordinates_window_to_image` returns 2 (
H_MSG_TRUE)
if the window is valid.
Otherwise an exception is raised.

## Possible Predecessors

`set_window_extents`,
`set_part`

## See also

`convert_coordinates_image_to_window`

## Module

Foundation
