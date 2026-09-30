# dev_open_window (Operator)

## Name

`dev_open_window` — Open a new graphics window.

## Signature

`dev_open_window( : : Row, Column, Width, Height, Background : WindowHandle)`

## Description

`dev_open_window` opens a new graphics window, which can
be used to display iconic objects like images, regions, and lines
as well as to perform textual output. This window automatically
becomes active, which means that all output ([`dev_display`](dev_display.md)
and automatic display of operator results) is redirected to this
window. This is shown by the lucent lamp on the `Active`
button.

Each graphics window is identified by its *`WindowHandle`*.
This logical number is displayed in the title bar of the graphics
window and is required as input parameter for some operators
like [`disp_image`](disp_image.md), [`disp_region`](disp_region.md),
[`draw_circle`](draw_circle.md), [`get_mbutton`](get_mbutton.md), [`write_string`](write_string.md),
and [`set_rgb`](set_rgb.md).

The graphics window is closed by pressing the `Close`
button of the window frame, via the `Visualization` menu,
or by calling [`dev_close_window`](dev_close_window.md).

### Graphics Window Position

By default, the graphics window opens within the canvas
window. If this is not desired,
select `Restore Default Layout use` ->
`Docked Graphics Window` from the `Window` menu
in HDevelop. See also “`Canvas Window`” in the
[`“HDevelop User's Guide”`.](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_gui_0000.html)

The parameters *`Row`* and *`Column`* are used to
pass the position of the window. Its reference point (0, 0)
on the canvas is visualized by a cross.

For floating windows, the reference point is by default the
upper left corner of the HDevelop main window. You can change
this reference point, so that, for example, the graphics
window position aligns with the upper left corner of the
screen. To do so, open the HDevelop preferences and choose
the desired `Origin of coordinates` under
`General options`.

Moreover, you can adapt the window position via the setting
`Window open offset`. These offset values are added to
the row and the column index, respectively. See also “Menu
`Window open offset`” in the `“HDevelop User's
Guide”`.

### Graphics Window Visualization

The background of the created graphics window is set to the color
specified in *`Background`*. This parameter is not
available for the operator [`open_window`](open_window.md). There, the same
behavior can be achieved by calling
`set_window_attr(::'background_color',Background:)` in
advance.

As a default, the visible image part in the graphics window
(viewport) is set in a way that images are displayed without
clipping and fitted completely into the window. The image part
is adapted to the window's size according to this rule for the
first image that is displayed after a program reset or the
loading of a new program or if the current image has a different
image size than the image that was displayed before. The size of
the window is not adapted automatically, hence, if the aspect
ratio of the image differs from that of the window, the image is
distorted to fit into the window. This can be changed via the
`Window Size` menu.

The visible image part can be changed interactively by spinning
the mouse wheel, using the `Move` or `Zoom` mode,
via the `Image Size` menu, with the help of the
`Zoom` tab card on the `Visualization Parameters`
dialog, or with the operator [`dev_set_part`](dev_set_part.md).

The display parameters of the graphics window can be specified
via its context menu, the `Visualization` menu, the
`Visualization Parameters` dialog, or the appropriate
HDevelop operators like [`dev_set_color`](dev_set_color.md),
[`dev_set_line_width`](dev_set_line_width.md), [`dev_set_draw`](dev_set_draw.md). Depending on
the `Apply Immediately` preference, the parameter changes
are applied to the lastly displayed object or apply from now on
for all following objects. In contrast to the standard HALCON
window operators, the new settings are also used for all new
graphics windows.

### Graphics Window History

Each graphics window manages a history that contains the

- objects and
- display parameters

that have been displayed or changed since the most recent
clear action or display of a full image. This history is used if
a redraw of the window is triggered, e.g., after a change of the
window's size, in order to reconstruct the complete window
contents. Other iconic output that was displayed using HALCON
operators like [`disp_image`](disp_image.md) or [`disp_region`](disp_region.md), text
([`write_string`](write_string.md)), or geometric objects ([`disp_line`](disp_line.md),
[`disp_circle`](disp_circle.md), etc.) are **not** part of the history,
and can therefore **not** be redrawn. Only the object
classes image, region, and XLD that are displayed with the
HDevelop operator [`dev_display`](dev_display.md) or by HDevelop actions
like double clicking on an icon are part of the history.

Pressing the `Clear` button clears the graphics
window contents and the history of the window. This can also be
achieved by using the operator [`dev_clear_window`](dev_clear_window.md).
This will not affect the current display parameters.

### Further Information

Additional information about the underlying HALCON window can
be found at [`open_window`](open_window.md). For more information about the
graphics window, please have a look at the
`“HDevelop User's Guide”`.

## Attention

Using the code export feature of HDevelop, the code that is
generated for this operator may have a different behavior than
the related HALCON operator. For a detailed description of the
code export of HDevelop graphics operators into the different
programming languages, in the `“HDevelop User's Guide”`,
see the chapter `Code Export` ->
`General Aspects of Code Generation`
-> `Graphics Windows`.

## Parameters

**`Row`** (input_control)  rectangle.origin.y `→`  (integer)

Row index of upper left corner.

Default:
0

Value range:
`0
≤
Row`

Minimum increment:
1

Recommended increment:
1

**`Column`** (input_control)  rectangle.origin.x `→`  (integer)

Column index of upper left corner.

Default:
0

Value range:
`0
≤
Column`

Minimum increment:
1

Recommended increment:
1

**`Width`** (input_control)  rectangle.extent.x `→`  (integer)

Width of the window.

Default:
512

Minimum increment:
1

Recommended increment:
1

Restriction:
`Width > 0 || Width == -1`

**`Height`** (input_control)  rectangle.extent.y `→`  (integer)

Height of the window.

Default:
512

Minimum increment:
1

Recommended increment:
1

Restriction:
`Height > 0 || Height == -1`

**`Background`** (input_control)  integer `→`  (integer / string)

Color of the background of the new window.

Default:
'black'

**`WindowHandle`** (output_control)  window `→`  (handle)

Window handle.

## Example (HDevelop)

```
dev_close_window ()
read_image (For5, 'for5')
get_image_size (For5, Width, Height)
dev_open_window (0, 0, Width, Height, 'black', WindowHandle)
dev_display (For5)
dev_set_lut ('rainbow')
dev_display (For5)
stop ()
dev_set_lut ('default')
dev_display (For5)
stop ()
dev_set_part (100, 100, 300, 300)
dev_display (For5)
```

## Result

If the values of the specified parameters are correct,
`dev_open_window` returns 2 (
H_MSG_TRUE)
. Otherwise, an
exception is raised and an error code returned.

## Possible Successors

`dev_display`,
`dev_set_lut`,
`dev_set_color`,
`dev_set_draw`,
`dev_set_part`

## Alternatives

`open_window`

## See also

`query_color`

## Module

Foundation
