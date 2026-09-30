# open_textwindow (Operator)

## Name

`open_textwindow` — Open a textual window.

## Warning

**`open_textwindow` is obsolete and is only provided for
reasons of backward compatibility. New applications should use the
operator [`open_window`](open_window.md) instead.**

## Signature

`open_textwindow( : : Row, Column, Width, Height, BorderWidth, BorderColor, BackgroundColor, FatherWindow, Mode, Machine : WindowHandle)`

## Description

`open_textwindow` opens a new textual window, which can be
used to perform textual input and output, as well as to perform
output of images. All output ([`write_string`](write_string.md), [`read_string`](read_string.md),
[`disp_region`](disp_region.md), etc.) is redirected to this window, if the same
logical window number *`WindowHandle`* is used.

Besides the mouse cursor textual windows possess also a textual cursor which
indicates the current writing position (more exactly: the lower left corner
of the output string without consideration of descenders). Its position
is indicated through an underscore or another type (the indication of
this position may also be disabled (= default setting);
cf. [`set_tshape`](set_tshape.md)).
You may set or query the position by calling the operators
[`set_tposition`](set_tposition.md) or [`get_tposition`](get_tposition.md).

After you opened a textual window the position of the cursor is set to
(H,0). Whereby H signifies the height of the default font less the
descenders. But the cursor is not shown. Hence the output starts for
writing in the upper left corner of the window.

You may query the colors of the background and the image edges by
calling [`query_color`](query_color.md). In the same way you may use
[`query_color`](query_color.md) in a window of type 'invisible'.
During output ([`write_string`](write_string.md)) you may set the clipping
of text out of the window edges by calling
`set_check(::'~text':)`.
This disables the creation of error messages, if text passes over
the edge of the window.

The origin of the coordinate system of the window resides in the
upper left corner (coordinates: (0,0)). The row index grows
downward (maximal: *`Height`*-1), the column index grows
to the right (maximal: *`Width`*-1).

The parameter *`Machine`* indicates the name of the computer,
which has to open the window. In case of a X-window, TCP-IP only sets
the name, DEC-Net sets in addition a colon behind the name. The
“server” or the “screen”, respectively, are not specified.
If the empty string is passed the environment variable
DISPLAY is used. It indicates the target computer. At this the name
is indicated in common syntax <Host>:0.0.

For windows of type *'WIN32-Window'* and *'X-Window'*
the parameter *`FatherWindow`* can be used to determine the father
window for the window to be opened. In case the control 'father' is set via
[`set_check`](set_check.md), *`FatherWindow`* must be the ID of a HALCON window,
otherwise (`set_check(::'~father':)`
)
it can also be the ID of an operating system window. If *`FatherWindow`*
is passed the value 0 or 'root', then under Windows and Unix-like systems the
desktop and the root window become the father window, respectively. In this
case, the value of the control 'father' (set via [`set_check`](set_check.md)) is
irrelevant. The caller must ensure that *`FatherWindow`* is a valid
handle and not destroyed as long as the embedded HALCON window is used.

Position and size of a window may change during runtime of a program.
This may be achieved by calling [`set_window_extents`](set_window_extents.md), but
also through external interferences (window manager). In the latter
case the operator [`set_window_extents`](set_window_extents.md) is provided.

Opening a window causes the assignment of a called default font.
It is used in connection with operators like [`write_string`](write_string.md)
and you may overwrite it by performing [`set_font`](set_font.md) after
calling `open_textwindow`. On the other hand you have the
possibility to specify a default font by calling
`set_system(::'default_font',<Fontname>:)` before opening
a window (and all following windows; see also [`query_font`](query_font.md)).

You may set the color of the font ([`write_string`](write_string.md),
[`read_string`](read_string.md)) by calling [`set_color`](set_color.md),
[`set_rgb`](set_rgb.md), [`set_hsi`](set_hsi.md) or [`set_gray`](set_gray.md).

Normally every output (e.g., [`write_string`](write_string.md), [`disp_region`](disp_region.md),
[`disp_circle`](disp_circle.md), etc.) in a window is terminated by a
“flush”. This causes the data to be fully visible on the display after
termination of the output operator. But this is not necessary in all
cases, in particular if there are permanently output tasks or there
is a mouse procedure active. Therefore it is more favorable (i.e., more
rapid) to store the data until sufficient data is available. You may
stop this behavior by calling `set_system(::'flush_graphic','false':)`.

The content of windows is saved (in case it is supported by special driver
software); i.e., it is preserved, also if the window is hidden by other
windows. But this is not necessary in all cases:
If you use a textual window, e.g., as a parent window for other windows, you
may suppress the security mechanism for it and save the necessary memory at
the same moment. You achieve this before opening the window by calling
`set_system(::'backing_store','false':)`.

Difference: graphical window - textual window

- In contrast to graphical windows ([`open_window`](open_window.md)) you may
  specify more parameters (color, edge) for a textual window while
  opening it.
- You may use textual windows only for input of user data
  ([`read_string`](read_string.md)).
- Using textual windows, the output of images, regions and graphics
  is “clipped” at the edges. Whereas during the use of graphical
  windows the edges are “zoomed”.
- The coordinate system (e.g., with [`get_mbutton`](get_mbutton.md) or
  [`get_mposition`](get_mposition.md)) consists of display coordinates independently
  of image size. The maximum coordinates are equal to the size of the
  window minus 1. In contrast to this, graphical windows ([`open_window`](open_window.md))
  use always a coordinate system, which corresponds to the image format.

The parameter *`Mode`* specifies the mode of the window.
It can have following values:

- **'visible':** —

  Normal mode for textual windows: The window is created according to
  the parameters and all inputs and outputs are possible.
- **'invisible':** —

  Invisible windows are not displayed in the display. Parameters like
  *`Row`*, *`Column`*, *`BorderWidth`*,
  *`BorderColor`*, *`BackgroundColor`* and
  *`FatherWindow`* do not have any meaning. Output to these
  windows has no effect. Input ([`read_string`](read_string.md), mouse, etc.)
  is not possible.
  You may use these windows to query representation parameter for an
  output device without opening a (visible) window.
  General queries are, e.g., [`query_color`](query_color.md) and
  [`get_string_extents`](get_string_extents.md).
- **'transparent':** —

  These windows are transparent: the window itself is not visible
  (edge and background), but all the other operations are possible
  and all output is displayed.
  Parameters like *`BorderColor`* and *`BackgroundColor`*
  do not have any meaning.
  A common use for this mode is the creation of mouse sensitive regions.
- **'buffer':** —

  These are also not visible windows. The output of images, regions and
  graphics is not visible on the display, but is stored in memory.
  Parameters like *`Row`*, *`Column`*, *`BorderWidth`*,
  *`BorderColor`*, *`BackgroundColor`* and *`FatherWindow`*
  do not have any meaning.
  You may use buffer windows, if you prepare output (in the background)
  and copy it finally with [`copy_rectangle`](copy_rectangle.md) in a visible
  window.
  Another usage might be the rapid processing of image regions during
  interactive manipulations.
  Textual input and mouse interaction are not possible in this mode.

## Attention

You have to keep in mind that parameters like *`Row`*, *`Column`*,
*`Width`* and *`Height`* are restricted by the
output device. Is a father window (*`FatherWindow`* <> 'root')
specified, then the coordinates are relative to this window.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`Row`** (input_control)  rectangle.origin.y `→`  (integer)

Row index of upper left corner.

Default:
0

Value range:
`Row` (lin)

Minimum increment:
1

Recommended increment:
1

**`Column`** (input_control)  rectangle.origin.x `→`  (integer)

Column index of upper left corner.

Default:
0

Value range:
`Column` (lin)

Minimum increment:
1

Recommended increment:
1

**`Width`** (input_control)  rectangle.extent.x `→`  (integer)

Window's width.

Default:
256

Value range:
`0
≤
Width` (lin)

Minimum increment:
1

Recommended increment:
1

**`Height`** (input_control)  rectangle.extent.y `→`  (integer)

Window's height.

Default:
256

Value range:
`0
≤
Height` (lin)

Minimum increment:
1

Recommended increment:
1

**`BorderWidth`** (input_control)  integer `→`  (integer)

Window border's width.

Default:
2

Value range:
`0
≤
BorderWidth` (lin)

Minimum increment:
1

Recommended increment:
1

**`BorderColor`** (input_control)  string `→`  (string)

Window border's color.

Default:
'white'

**`BackgroundColor`** (input_control)  string `→`  (string)

Background color.

Default:
'black'

**`FatherWindow`** (input_control)  pointer `→`  (integer / string)

Logical number of the father window. For the display
as father you may specify 'root' or 0.

Default:
0

Restriction:
`FatherWindow >= 0`

**`Mode`** (input_control)  string `→`  (string)

Window mode.

Default:
'visible'

List of values:
'buffer', 'invisible', 'transparent', 'visible'

**`Machine`** (input_control)  string `→`  (string)

Computer name, where the window has to be opened or
empty string.

Default:
''

**`WindowHandle`** (output_control)  window `→`  (handle)

Window handle.

## Example (HDevelop)

```
open_textwindow(0,0,900,600,1,'black','slate blue','root','visible', \
              '',WindowHandle1)
open_textwindow(10,10,300,580,3,'red','blue',WindowHandle1,'visible', \
              '',WindowHandle2)
open_window(10,320,570,580,WindowHandle1,'visible','',WindowHandle)
set_color(WindowHandle,'red')
read_image(Image,'monkey')
disp_image(Image,WindowHandle)
Button := 0
repeat
  try
      get_mposition(WindowHandle,Row,Column,Button)
      get_grayval(Image,Row,Column,Gray)
      write_string(WindowHandle2,['  Position (',Row,',',Column,')  '])
      write_string(WindowHandle2,['Gray value (',Gray,')  '])
      new_line(WindowHandle2)
  catch (Exception)
  endtry
until(Button == 4)
close_window(WindowHandle1)
```

## Result

If the values of the specified parameters are correct
`open_textwindow` returns 2 (
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

## Alternatives

`open_window`

## See also

`write_string`,
`read_string`,
`new_line`,
`get_string_extents`,
`get_tposition`,
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

## Module

Foundation
