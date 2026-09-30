# unproject_coordinates (Operator)

## Name

`unproject_coordinates` — Calculates image coordinates for a point in a 3D plot window.

## Signature

`unproject_coordinates(Image : : WindowHandle, Row, Column : ImageRow, ImageColumn, Height)`

## Description

If *`Image`* is displayed in *`WindowHandle`* using a 3D plot
(i.e., *'3d_plot'* was set using [`set_paint`](set_paint.md)),
`unproject_coordinates` calculates the image coordinates
*`ImageRow`*, *`ImageColumn`*, and the *`Height`* for a given
point *`Row`*,*`Column`* in window coordinates.
The window coordinates *`Row`*, *`Column`* must be provided in
respect to the current image part. As a consequence, this coordinates are
subpixel coordinates. Given the current image part (row1,column1,row2,
column2), the upper left corner corresponds to the coordinates
(row1 - 0.5, col1 - 0.5). Accordingly, the bottom right corner
corresponds to the coordinates (row2 - 0.5, col2 - 0.5). Use
[`get_mposition_sub_pix`](get_mposition_sub_pix.md) or [`get_mbutton_sub_pix`](get_mbutton_sub_pix.md) to obtain these
coordinates directly.

One of the window parameters *'save_depth_buffer'* or
*'interactive_plot'* must be set to *'true'* using
[`set_window_param`](set_window_param.md). Otherwise, `unproject_coordinates` cannot
be used.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Image`** (input_object)  singlechannelimage `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real / complex / vector_field)

Displayed image.

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`Row`** (input_control)  integer `→`  (real / integer)

Row coordinate in the window.

**`Column`** (input_control)  integer `→`  (real / integer)

Column coordinate in the window.

**`ImageRow`** (output_control)  integer `→`  (integer)

Row coordinate in the image.

**`ImageColumn`** (output_control)  integer `→`  (integer)

Column coordinate in the image.

**`Height`** (output_control)  real `→`  (integer / real)

Height value.

## Possible Predecessors

`get_mbutton_sub_pix`,
`get_mposition_sub_pix`,
`disp_image`

## See also

`disp_obj`,
`update_window_pose`,
`set_paint`

## Module

Foundation
