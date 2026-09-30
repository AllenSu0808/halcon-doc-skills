# UnprojectCoordinates (Operator)

## Name

`UnprojectCoordinates` — Calculates image coordinates for a point in a 3D plot window.

## Signature

`static void HOperatorSet.UnprojectCoordinates(HObject image, HTuple windowHandle, HTuple row, HTuple column, out HTuple imageRow, out HTuple imageColumn, out HTuple height)`

`void HImage.UnprojectCoordinates(HWindow windowHandle, HTuple row, HTuple column, out int imageRow, out int imageColumn, out HTuple height)`

`void HImage.UnprojectCoordinates(HWindow windowHandle, double row, double column, out int imageRow, out int imageColumn, out int height)`

`void HWindow.UnprojectCoordinates(HImage image, HTuple row, HTuple column, out int imageRow, out int imageColumn, out HTuple height)`

`void HWindow.UnprojectCoordinates(HImage image, double row, double column, out int imageRow, out int imageColumn, out int height)`

## Description

If *`image`* is displayed in *`windowHandle`* using a 3D plot
(i.e., *"3d_plot"* was set using [`SetPaint`](set_paint.md)),
`UnprojectCoordinates` calculates the image coordinates
*`imageRow`*, *`imageColumn`*, and the *`height`* for a given
point *`row`*,*`column`* in window coordinates.
The window coordinates *`row`*, *`column`* must be provided in
respect to the current image part. As a consequence, this coordinates are
subpixel coordinates. Given the current image part (row1,column1,row2,
column2), the upper left corner corresponds to the coordinates
(row1 - 0.5, col1 - 0.5). Accordingly, the bottom right corner
corresponds to the coordinates (row2 - 0.5, col2 - 0.5). Use
[`GetMpositionSubPix`](get_mposition_sub_pix.md) or [`GetMbuttonSubPix`](get_mbutton_sub_pix.md) to obtain these
coordinates directly.

One of the window parameters *"save_depth_buffer"* or
*"interactive_plot"* must be set to *"true"* using
[`SetWindowParam`](set_window_param.md). Otherwise, `UnprojectCoordinates` cannot
be used.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real / complex / vector_field)

Displayed image.

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`row`** (input_control)  integer `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate in the window.

**`column`** (input_control)  integer `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate in the window.

**`imageRow`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Row coordinate in the image.

**`imageColumn`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Column coordinate in the image.

**`height`** (output_control)  real `→` [HTuple](HTuple.md) (*int* / long / double)

Height value.

## Possible Predecessors

`GetMbuttonSubPix`,
`GetMpositionSubPix`,
`DispImage`

## See also

`DispObj`,
`UpdateWindowPose`,
`SetPaint`

## Module

Foundation
