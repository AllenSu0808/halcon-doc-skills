# unproject_coordinates (Operator)

## Name

`unproject_coordinates` — Calculates image coordinates for a point in a 3D plot window.

## Signature

`def unproject_coordinates(image: HObject, window_handle: HHandle, row: Union[float, int], column: Union[float, int]) -> Tuple[int, int, Union[int, float]]`

## Description

If *`image`* is displayed in *`window_handle`* using a 3D plot
(i.e., *"3d_plot"* was set using [`set_paint`](set_paint.md)),
`unproject_coordinates` calculates the image coordinates
*`image_row`*, *`image_column`*, and the *`height`* for a given
point *`row`*,*`column`* in window coordinates.
The window coordinates *`row`*, *`column`* must be provided in
respect to the current image part. As a consequence, this coordinates are
subpixel coordinates. Given the current image part (row1,column1,row2,
column2), the upper left corner corresponds to the coordinates
(row1 - 0.5, col1 - 0.5). Accordingly, the bottom right corner
corresponds to the coordinates (row2 - 0.5, col2 - 0.5). Use
[`get_mposition_sub_pix`](get_mposition_sub_pix.md) or [`get_mbutton_sub_pix`](get_mbutton_sub_pix.md) to obtain these
coordinates directly.

One of the window parameters *"save_depth_buffer"* or
*"interactive_plot"* must be set to *"true"* using
[`set_window_param`](set_window_param.md). Otherwise, `unproject_coordinates` cannot
be used.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (input_object)  singlechannelimage `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real / complex / vector_field)

Displayed image.

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`row`** (input_control)  integer `→` Union[float, int]

Row coordinate in the window.

**`column`** (input_control)  integer `→` Union[float, int]

Column coordinate in the window.

**`image_row`** (output_control)  integer `→` int

Row coordinate in the image.

**`image_column`** (output_control)  integer `→` int

Column coordinate in the image.

**`height`** (output_control)  real `→` Union[int, float]

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
