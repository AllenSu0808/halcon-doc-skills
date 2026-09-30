# new_extern_window (Operator)

## Name

`new_extern_window` — Create a virtual graphics window under Windows.

## Signature

`def new_extern_window(winhwnd: int, row: int, column: int, width: int, height: int) -> HHandle`

## Description

`new_extern_window` opens a new virtual window.
Note that this only works on Windows systems and drawing objects are not
supported.

Virtual means that a new window will not be created, but the window
whose window handle is given in the parameter *`winhwnd`* is used
to perform output of gray value data, regions, graphics as well as
to perform textual output.

All operators that allow the user to define graphical primitives
through mouse interactions, like for example [`draw_rectangle1`](draw_rectangle1.md), do not
work on external windows. The following operators can be used:

- Output of gray values:
  [`set_paint`](set_paint.md), [`set_lut`](set_lut.md)
- Regions:
  [`set_color`](set_color.md), [`set_rgb`](set_rgb.md), [`set_hsi`](set_hsi.md),
  [`set_gray`](set_gray.md), [`set_shape`](set_shape.md),
  [`set_line_width`](set_line_width.md),
  [`set_line_style`](set_line_style.md), [`set_draw`](set_draw.md)
- Image part:
  [`set_part`](set_part.md)
- Text:
  [`set_font`](set_font.md)

You may query current set values by calling operators like
[`get_shape`](get_shape.md). As some parameters are specified through the
hardware (Resolution/Colors), you may query current available
resources by calling operators like [`query_color`](query_color.md).

The parameter *`winhwnd`* is used to pass the window handle of
the window in which output should be done.

The origin of the coordinate system of the window resides in the
upper left corner (coordinates: (0,0)). The row index grows downward
(maximum: *`height`*-1), the column index grows to the right
(maximal: *`width`*-1).

You may use the value *-1* for parameters *`width`* and
*`height`*. This means, that the corresponding value is chosen
automatically. In particular, this is important if the aspect ratio
of the pixels is not 1.0 (see [`set_system`](set_system.md)). If one of the
two parameters is set to *-1*, it will be chosen through the
size which results out of the aspect ratio of the pixels. If both
parameters are set to *-1*, they will be set to the current
image format.

The position and size of a window may change during runtime of a
program, e.g., through external influences (window manager). With
the operator [`set_window_extents`](set_window_extents.md), you can change the size of
the (external) widow via the program. Note that
[`set_window_extents`](set_window_extents.md) offers to change the position as well,
but you cannot change the position of an external window under
Windows.

Opening a window causes the assignment of a default font. It is
used in connection with operators like [`write_string`](write_string.md) and you
may change it by performing [`set_font`](set_font.md) after calling
[`open_window`](open_window.md). On the other hand, you have the possibility to
specify a default font by calling
`set_system(::'default_font',<Fontname>:)` before opening a
window (and all following windows; see also [`query_font`](query_font.md)).

You may set the color of graphics and font, which is used for output
operators like [`disp_region`](disp_region.md) or [`disp_circle`](disp_circle.md), by
calling [`set_rgb`](set_rgb.md), [`set_hsi`](set_hsi.md) or [`set_gray`](set_gray.md).

The content of the window is not saved, if other windows overlap the
window. This must be done in the program code that handles the
window in the calling program.

For graphical output ([`disp_image`](disp_image.md),[`disp_region`](disp_region.md), etc.)
you may adjust the window by calling the operator [`set_part`](set_part.md) in
order to represent a logical clipping of the image format. In
particular this implies that only this part (appropriately scaled)
of images and regions is displayed. Before you close your window,
you have to close the HALCON-window.

## Attention

Note that parameters as *`row`*, *`column`*,
*`width`* and *`height`* are constrained through the
output device, i.e., the size of the Windows NT desktop.
Furthermore, be aware that all operators that allow the user to
define graphical primitives through mouse interactions, like for
example [`draw_rectangle1`](draw_rectangle1.md), do not work on external windows.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`winhwnd`** (input_control)  pointer `→` int

Windows window handle of a previously created window.

Restriction:
`WINHWnd != 0`

**`row`** (input_control)  rectangle.origin.y `→` int

Row coordinate of upper left corner.

Default:
0

Restriction:
`Row >= 0`

**`column`** (input_control)  rectangle.origin.x `→` int

Column coordinate of upper left corner.

Default:
0

Restriction:
`Column >= 0`

**`width`** (input_control)  rectangle.extent.x `→` int

Width of the window.

Default:
512

Restriction:
`Width > 0 || Width == -1`

**`height`** (input_control)  rectangle.extent.y `→` int

Height of the window.

Default:
512

Restriction:
`Height > 0 || Height == -1`

**`window_handle`** (output_control)  window `→` HHandle

Window handle.

## Example (C++)

```
// Needs to be embedded into an application framework,
// see examples/cpp/mfc/MatchingExtWin.
```

## Result

If the values of the specified parameters are correct
`new_extern_window` returns 2 (
H_MSG_TRUE)
. If necessary, an exception
is raised.

## Possible Predecessors

`reset_obj_db`

## Possible Successors

`set_color`,
`query_window_type`,
`get_window_type`,
`set_window_type`,
`get_mposition`,
`set_tposition`,
`set_tshape`,
`set_window_extents`,
`get_window_extents`,
`query_color`,
`set_check`,
`set_system`

## Alternatives

`open_window`

## See also

`open_window`,
`disp_region`,
`disp_image`,
`disp_color`,
`set_lut`,
`query_color`,
`set_color`,
`set_rgb`,
`set_hsi`,
`set_pixel`,
`set_gray`,
`set_part`,
`set_part_style`,
`query_window_type`,
`get_window_type`,
`set_window_type`,
`get_mposition`,
`set_tposition`,
`set_window_extents`,
`get_window_extents`,
`set_window_attr`,
`set_check`,
`set_system`

## Module

Foundation
