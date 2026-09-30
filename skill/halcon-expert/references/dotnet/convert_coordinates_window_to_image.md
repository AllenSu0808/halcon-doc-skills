# ConvertCoordinatesWindowToImage (Operator)

## Name

`ConvertCoordinatesWindowToImage` — Convert window coordinates to image coordinates

## Signature

`static void HOperatorSet.ConvertCoordinatesWindowToImage(HTuple windowHandle, HTuple rowWindow, HTuple columnWindow, out HTuple rowImage, out HTuple columnImage)`

`void HWindow.ConvertCoordinatesWindowToImage(HTuple rowWindow, HTuple columnWindow, out HTuple rowImage, out HTuple columnImage)`

`void HWindow.ConvertCoordinatesWindowToImage(double rowWindow, double columnWindow, out double rowImage, out double columnImage)`

## Description

`ConvertCoordinatesWindowToImage` converts window coordinates
*`rowWindow`* and *`columnWindow`* into image coordinates
*`rowImage`* and *`columnImage`* based on the displayed image part
and the window size of the window defined in *`windowHandle`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`rowWindow`** (input_control)  coordinates.y(-array) `→` [HTuple](HTuple.md) (*double*)

Row (Y) in window coordinates.

**`columnWindow`** (input_control)  coordinates.x(-array) `→` [HTuple](HTuple.md) (*double*)

Column (X) in window coordinates.

**`rowImage`** (output_control)  coordinates.y(-array) `→` [HTuple](HTuple.md) (*double*)

Row in image coordinates.

**`columnImage`** (output_control)  coordinates.x(-array) `→` [HTuple](HTuple.md) (*double*)

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

`ConvertCoordinatesWindowToImage` returns 2 (
H_MSG_TRUE)
if the window is valid.
Otherwise an exception is raised.

## Possible Predecessors

`SetWindowExtents`,
`SetPart`

## See also

`ConvertCoordinatesImageToWindow`

## Module

Foundation
