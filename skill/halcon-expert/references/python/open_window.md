# open_window (Operator)

## Name

`open_window` — Open a graphics window.

## Signature

`def open_window(row: int, column: int, width: int, height: int, father_window: Union[int, str], mode: str, machine: str) -> HHandle`

## Description

`open_window` opens a new window, which can be
used to perform output of gray value data, regions, graphics as well as to
perform textual output. All output ([`disp_region`](disp_region.md),
[`disp_image`](disp_image.md),
etc.) is redirected to this window, if the same logical window number
*`window_handle`* is used.

The background of the created window is set to black in advance and it
has a white border, which is 2 pixels wide (see also
`set_window_attr(::'border_width',<Width>:)`).

Certain parameters used for the editing of output data are assigned to a window.
These parameters are considered during the output itself (e.g., with
[`disp_image`](disp_image.md) or [`disp_region`](disp_region.md)).
They are not specified by an output operator, but by “configuration
operators”. If you want to set, e.g., the color red for the output of regions,
you have to call `set_color(::WindowHandle,'red':)` before calling
[`disp_region`](disp_region.md). These parameters are always set for the
window with the logical window number *`window_handle`* and remain
assigned to a window as long as they will be overwritten.
You may use the following configuration operators:

- Output of gray values:
  [`set_paint`](set_paint.md), [`set_lut`](set_lut.md)
- Regions:
  [`set_color`](set_color.md), [`set_rgb`](set_rgb.md), [`set_hsi`](set_hsi.md),
  [`set_gray`](set_gray.md),
  [`set_shape`](set_shape.md), [`set_line_width`](set_line_width.md),
  [`set_line_style`](set_line_style.md), [`set_draw`](set_draw.md)
- Image clipping:
  [`set_part`](set_part.md)
- Text:
  [`set_font`](set_font.md)

You may query current set values by calling operators like
[`get_shape`](get_shape.md).
As some parameters are specified through the hardware (Resolution/Colors),
you may query current available resources by calling [`query_color`](query_color.md).

The origin of the coordinate system of the window resides in the
upper left corner (coordinates: (0,0)). The row index grows
downward (maximal: *`height`*-1), the column index grows
to the right (maximal: *`width`*-1).
You have to keep in mind, that the range of the coordinate system
is independent of the window size. It is specified only through
the image format (see [`reset_obj_db`](reset_obj_db.md)).

The parameter *`machine`* indicates the name of the computer,
which has to open the window. In case of a X-window, TCP-IP only sets
the name, DEC-Net sets in addition a colon behind the name. The
“server” resp. the “screen” are not specified.
If the empty string is passed the environment variable
DISPLAY is used. It indicates the target computer. At this the name
is indicated in common syntax <Host>:0.0.

For windows of type *"WIN32-Window"* and *"X-Window"*
the parameter *`father_window`* can be used to determine the father
window for the window to be opened. In case the control 'father' is set via
[`set_check`](set_check.md), *`father_window`* must be the ID of a HALCON window,
otherwise (`set_check(::'~father':)`
)
it can also be the ID of an operating system window. If *`father_window`*
is passed the value 0 or 'root', then under Windows and Unix-like systems the
desktop and the root window become the father window, respectively. In this
case, the value of the control 'father' (set via [`set_check`](set_check.md)) is
irrelevant. The caller must ensure that *`father_window`* is a valid
handle and not destroyed as long as the embedded HALCON window is used.

You may use the value “-1” for parameters *`width`* and
*`height`*. This means, that the according value has to be
specified automatically. In particular this is of importance, if
the proportion of pixels is not 1.0 (see [`set_system`](set_system.md)):
Is one of the two parameters set to “-1”, it will be specified
through the size which results out of the proportion of pixels.
Are both parameters set to “-1”, they will be set to the maximum
image format, which is currently used (further information about the
currently used maximum image format can be found in the description
of [`get_system`](get_system.md) using “width” or “height”).

Position and size of a window may change during runtime of a program.
This may be achieved by calling [`set_window_extents`](set_window_extents.md), but
also through external interferences (window manager). In the latter
case the operator [`set_window_extents`](set_window_extents.md) is provided.

Opening a window causes the assignment of a called default font.
It is used in connection with operators like [`write_string`](write_string.md)
and you may overwrite it by performing [`set_font`](set_font.md) after
calling `open_window`. On the other hand you have the
possibility to specify a default font by calling
`set_system(::'default_font',<Fontname>:)` before opening
a window (and all following windows; see also [`query_font`](query_font.md)).

You may set the color of graphics and font, which is used for output
operators like [`disp_region`](disp_region.md) or [`disp_circle`](disp_circle.md), by
calling [`set_rgb`](set_rgb.md), [`set_hsi`](set_hsi.md) or [`set_gray`](set_gray.md).

Normally every output (e.g., [`disp_image`](disp_image.md), [`disp_region`](disp_region.md),
[`disp_circle`](disp_circle.md), etc.) in a window is terminated by a called
“flush”. This causes the data to be fully visible on the display after
termination of the output operator. But this is not necessary in all
cases, in particular if there are permanently output tasks or if there
is a mouse procedure active. Therefore it is more favorable (i.e., more
rapid) to store the data until sufficient data is available. You may
stop this behavior by calling `set_system(::'flush_graphic','false':)`.

The content of windows is saved (in case it is supported by special driver
software); i.e., it is preserved, also if the window is hidden by other
windows. But this is not necessary in all cases:
If the content of a window is built up permanently new
([`copy_rectangle`](copy_rectangle.md)), you may suppress the security mechanism for
that and hence you can save the necessary memory.
This is done by calling `set_system(::'backing_store','false':)`
before opening a window. In doing so you save not only memory but also
time to compute. This is significant for the output of video clips
(see [`copy_rectangle`](copy_rectangle.md)).

For graphical output ([`disp_image`](disp_image.md),[`disp_region`](disp_region.md), etc.)
you may adjust the window by calling the operator [`set_part`](set_part.md) in order
to represent a logical clipping of the image format.
In particular this implicates that you obtain this clipping (with appropriate
enlargement) of images and regions only.

Difference: graphical window - textual window

- Using graphical windows the layout is not as variable as concerned
  to textual windows.
- You may use textual windows for the input of user data only
  ([`read_string`](read_string.md)).
- During the output of images, regions and graphics a “zooming” is
  performed using graphical windows: Independent on size and side ratio of
  the window images are transformed in that way, that they are displayed
  in the window by filling it completely.
  On the opposite side using textual windows the output does not care
  about the size of the window (only if clipping is necessary).
- Using graphical windows the coordinate system of the window corresponds
  to the coordinate system of the image format. Using textual windows, its
  coordinate system is always equal to the display coordinates independent
  on image size.

The parameter *`mode`* determines the mode of the window.
It may have following values:

- **'visible':** —

  Normal mode for graphical windows:
  The window is created according to the parameters and all input and
  output are possible.
- **'invisible':** —

  Invisible windows are not displayed in the display. Parameters like
  *`row`*, *`column`* and *`father_window`* do not
  have any meaning. Output to these windows has no effect. Input
  ([`read_string`](read_string.md), mouse, etc.) is not possible.
  You may use these windows to query representation parameter for an
  output device without opening a (visible) window.
  Common queries are, e.g., [`query_color`](query_color.md) and
  [`get_string_extents`](get_string_extents.md).
- **'transparent':** —

  These windows are transparent: the window itself is not visible
  (edge and background), but all the other operations are possible and all
  output is displayed.
  A common use for this mode is the creation of mouse sensitive regions.
- **'buffer':** —

  These are also not visible windows. The output of images, regions and
  graphics is not visible on the display, but is stored in memory.
  Parameters like *`row`*, *`column`* and *`father_window`*
  do not have any meaning.
  You may use buffer windows, if you prepare output (in the background)
  and copy it finally with [`copy_rectangle`](copy_rectangle.md) in a visible
  window.
  Another usage might be the rapid processing of image regions during
  interactive manipulations.
  Textual input and mouse interaction are not possible in this mode.

## Attention

You may keep in mind that parameters as *`row`*, *`column`*,
*`width`* and *`height`* are constrained by the output
device. If you specify a father window (*`father_window`* < > 'root') the coordinates are relative to this window.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`row`** (input_control)  rectangle.origin.y `→` int

Row index of upper left corner.

Default:
0

Value range:
`row` (lin)

Minimum increment:
1

Recommended increment:
1

**`column`** (input_control)  rectangle.origin.x `→` int

Column index of upper left corner.

Default:
0

Value range:
`column` (lin)

Minimum increment:
1

Recommended increment:
1

**`width`** (input_control)  rectangle.extent.x `→` int

Width of the window.

Default:
256

Value range:
`width` (lin)

Minimum increment:
1

Recommended increment:
1

Restriction:
`0 <= Width <= 32768 || Width == -1`

**`height`** (input_control)  rectangle.extent.y `→` int

Height of the window.

Default:
256

Value range:
`height` (lin)

Minimum increment:
1

Recommended increment:
1

Restriction:
`0 <= Height <= 32768 || Height == -1`

**`father_window`** (input_control)  pointer `→` Union[int, str]

Logical number of the father window. To specify the
display as father you may enter 'root' or 0.

Default:
0

Restriction:
`FatherWindow >= 0`

**`mode`** (input_control)  string `→` str

Window mode.

Default:
"visible"

List of values:
"buffer", "invisible", "transparent", "visible"

**`machine`** (input_control)  string `→` str

Name of the computer on which you want to open
the window. Otherwise the empty string.

Default:
""

**`window_handle`** (output_control)  window `→` HHandle

Window handle.

## Result

If the values of the specified parameters are correct
`open_window` returns 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

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

## See also

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
