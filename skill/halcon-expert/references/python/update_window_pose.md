# update_window_pose (Operator)

## Name

`update_window_pose` — Modify the pose of a 3D plot.

## Signature

`def update_window_pose(window_handle: HHandle, last_row: Union[float, int], last_col: Union[float, int], current_row: Union[float, int], current_col: Union[float, int], mode: str) -> None`

## Description

The operator `update_window_pose` provides an easy way to modify the
pose of the height field displayed by [`disp_obj`](disp_obj.md) if the paint mode is
set to *"3d_plot"* using [`set_paint`](set_paint.md).

Two window coordinates (*`last_row`*,*`last_col`*) and
(*`current_row`*, *`current_col`*) are transformed into rotation,
scaling, or movement depending on *`mode`*.
This window coordinates must be provided with respect to the current image
part. As a consequence, this coordinates are subpixel coordinates. Given the
current image part (row1,column1,row2,column2), the upper left
corner corresponds to the coordinate (row1 - 0.5, col1 - 0.5). Accordingly,
the bottom right corner corresponds to the coordinate
(row2 - 0.5, col2 - 0.5). Use [`get_mposition_sub_pix`](get_mposition_sub_pix.md) or
[`get_mbutton_sub_pix`](get_mbutton_sub_pix.md) to obtain this coordinates directly.

If *`mode`* is set to *"rotate"*, the height field is rotated
using a virtual trackball model. Both points are projected on a sphere
centered in the center of the window *`window_handle`*. The circular
arc between this two projections corresponds to the rotation applied
to the height field.

If *`mode`* is set to *"scale"*, zooming is reduced if
*`current_row`* is greater than *`last_row`* and increased if
*`current_row`* is smaller than *`last_row`*.

If *`mode`* is set to *"move"*, the input points are projected
onto the plane through the center of the height field parallel to the viewing
plane. The center of the height field is moved in this plane by the distance
between both projections.

If *`mode`* is set to *"move_plane"*, the input points are
projected on the plane given by height zero. The height field is moved in
this plane by the distance between both projections.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`last_row`** (input_control)  point.y `→` Union[float, int]

Row coordinate of the first point.

**`last_col`** (input_control)  point.x `→` Union[float, int]

Column coordinate of the first point.

**`current_row`** (input_control)  point.y `→` Union[float, int]

Row coordinate of the second point.

**`current_col`** (input_control)  point.x `→` Union[float, int]

Column coordinate of the second point.

**`mode`** (input_control)  string `→` str

Navigation mode.

Default:
"rotate"

List of values:
"move", "move_plane", "rotate", "scale"

## Example (HDevelop)

```
* Interactive display of a height field
dev_set_paint ('3d_plot')
while (1)
  dev_set_check ('~give_error')
  get_mposition_sub_pix (WindowHandle, Row, Column, Button)
  dev_set_check ('give_error')
  if (ButtonDown and (Button == 0))
    ButtonDown := false
  endif
  if (not(Button == 0))
    if (ButtonDown)
      if (Button == 1)
        mode := 'rotate'
      endif
      if (Button == 4)
        mode := 'scale'
      endif
      if (Button == 5)
        mode := 'move'
      endif
      update_window_pose (WindowHandle, lastRow, lastCol, Row, Column, mode)
    else
      if (Button == 2)
        break
      endif
      ButtonDown := true
    endif
    lastCol := Column
    lastRow := Row
  endif
  dev_display (Image)
endwhile
```

## Possible Predecessors

`set_paint`,
`open_window`,
`get_mposition_sub_pix`,
`get_mbutton_sub_pix`

## Possible Successors

`disp_image`

## See also

`unproject_coordinates`

## Module

Foundation
