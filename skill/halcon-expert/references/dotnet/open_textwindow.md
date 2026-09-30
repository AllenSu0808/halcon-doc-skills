# OpenTextwindow (Operator)

## Name

`OpenTextwindow` — Open a textual window.

## Warning

**`OpenTextwindow` is obsolete and is only provided for
reasons of backward compatibility. New applications should use the
operator [`OpenWindow`](open_window.md) instead.**

## Signature

`static void HOperatorSet.OpenTextwindow(HTuple row, HTuple column, HTuple width, HTuple height, HTuple borderWidth, HTuple borderColor, HTuple backgroundColor, HTuple fatherWindow, HTuple mode, HTuple machine, out HTuple windowHandle)`

`void HWindow.OpenTextwindow(int row, int column, int width, int height, int borderWidth, string borderColor, string backgroundColor, HTuple fatherWindow, string mode, string machine)`

`void HWindow.OpenTextwindow(int row, int column, int width, int height, int borderWidth, string borderColor, string backgroundColor, IntPtr fatherWindow, string mode, string machine)`

## Description

`OpenTextwindow` opens a new textual window, which can be
used to perform textual input and output, as well as to perform
output of images. All output ([`WriteString`](write_string.md), [`ReadString`](read_string.md),
[`DispRegion`](disp_region.md), etc.) is redirected to this window, if the same
logical window number *`windowHandle`* is used.

Besides the mouse cursor textual windows possess also a textual cursor which
indicates the current writing position (more exactly: the lower left corner
of the output string without consideration of descenders). Its position
is indicated through an underscore or another type (the indication of
this position may also be disabled (= default setting);
cf. [`SetTshape`](set_tshape.md)).
You may set or query the position by calling the operators
[`SetTposition`](set_tposition.md) or [`GetTposition`](get_tposition.md).

After you opened a textual window the position of the cursor is set to
(H,0). Whereby H signifies the height of the default font less the
descenders. But the cursor is not shown. Hence the output starts for
writing in the upper left corner of the window.

You may query the colors of the background and the image edges by
calling [`QueryColor`](query_color.md). In the same way you may use
[`QueryColor`](query_color.md) in a window of type 'invisible'.
During output ([`WriteString`](write_string.md)) you may set the clipping
of text out of the window edges by calling
`set_check(::'~text':)`.
This disables the creation of error messages, if text passes over
the edge of the window.

The origin of the coordinate system of the window resides in the
upper left corner (coordinates: (0,0)). The row index grows
downward (maximal: *`height`*-1), the column index grows
to the right (maximal: *`width`*-1).

The parameter *`machine`* indicates the name of the computer,
which has to open the window. In case of a X-window, TCP-IP only sets
the name, DEC-Net sets in addition a colon behind the name. The
“server” or the “screen”, respectively, are not specified.
If the empty string is passed the environment variable
DISPLAY is used. It indicates the target computer. At this the name
is indicated in common syntax <Host>:0.0.

For windows of type *"WIN32-Window"* and *"X-Window"*
the parameter *`fatherWindow`* can be used to determine the father
window for the window to be opened. In case the control 'father' is set via
[`SetCheck`](set_check.md), *`fatherWindow`* must be the ID of a HALCON window,
otherwise (`set_check(::'~father':)`
)
it can also be the ID of an operating system window. If *`fatherWindow`*
is passed the value 0 or 'root', then under Windows and Unix-like systems the
desktop and the root window become the father window, respectively. In this
case, the value of the control 'father' (set via [`SetCheck`](set_check.md)) is
irrelevant. The caller must ensure that *`fatherWindow`* is a valid
handle and not destroyed as long as the embedded HALCON window is used.

Position and size of a window may change during runtime of a program.
This may be achieved by calling [`SetWindowExtents`](set_window_extents.md), but
also through external interferences (window manager). In the latter
case the operator [`SetWindowExtents`](set_window_extents.md) is provided.

Opening a window causes the assignment of a called default font.
It is used in connection with operators like [`WriteString`](write_string.md)
and you may overwrite it by performing [`SetFont`](set_font.md) after
calling `OpenTextwindow`. On the other hand you have the
possibility to specify a default font by calling
`set_system(::'default_font',<Fontname>:)` before opening
a window (and all following windows; see also [`QueryFont`](query_font.md)).

You may set the color of the font ([`WriteString`](write_string.md),
[`ReadString`](read_string.md)) by calling [`SetColor`](set_color.md),
[`SetRgb`](set_rgb.md), [`SetHsi`](set_hsi.md) or [`SetGray`](set_gray.md).

Normally every output (e.g., [`WriteString`](write_string.md), [`DispRegion`](disp_region.md),
[`DispCircle`](disp_circle.md), etc.) in a window is terminated by a
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

- In contrast to graphical windows ([`OpenWindow`](open_window.md)) you may
  specify more parameters (color, edge) for a textual window while
  opening it.
- You may use textual windows only for input of user data
  ([`ReadString`](read_string.md)).
- Using textual windows, the output of images, regions and graphics
  is “clipped” at the edges. Whereas during the use of graphical
  windows the edges are “zoomed”.
- The coordinate system (e.g., with [`GetMbutton`](get_mbutton.md) or
  [`GetMposition`](get_mposition.md)) consists of display coordinates independently
  of image size. The maximum coordinates are equal to the size of the
  window minus 1. In contrast to this, graphical windows ([`OpenWindow`](open_window.md))
  use always a coordinate system, which corresponds to the image format.

The parameter *`mode`* specifies the mode of the window.
It can have following values:

- **'visible':** —

  Normal mode for textual windows: The window is created according to
  the parameters and all inputs and outputs are possible.
- **'invisible':** —

  Invisible windows are not displayed in the display. Parameters like
  *`row`*, *`column`*, *`borderWidth`*,
  *`borderColor`*, *`backgroundColor`* and
  *`fatherWindow`* do not have any meaning. Output to these
  windows has no effect. Input ([`ReadString`](read_string.md), mouse, etc.)
  is not possible.
  You may use these windows to query representation parameter for an
  output device without opening a (visible) window.
  General queries are, e.g., [`QueryColor`](query_color.md) and
  [`GetStringExtents`](get_string_extents.md).
- **'transparent':** —

  These windows are transparent: the window itself is not visible
  (edge and background), but all the other operations are possible
  and all output is displayed.
  Parameters like *`borderColor`* and *`backgroundColor`*
  do not have any meaning.
  A common use for this mode is the creation of mouse sensitive regions.
- **'buffer':** —

  These are also not visible windows. The output of images, regions and
  graphics is not visible on the display, but is stored in memory.
  Parameters like *`row`*, *`column`*, *`borderWidth`*,
  *`borderColor`*, *`backgroundColor`* and *`fatherWindow`*
  do not have any meaning.
  You may use buffer windows, if you prepare output (in the background)
  and copy it finally with [`CopyRectangle`](copy_rectangle.md) in a visible
  window.
  Another usage might be the rapid processing of image regions during
  interactive manipulations.
  Textual input and mouse interaction are not possible in this mode.

## Attention

You have to keep in mind that parameters like *`row`*, *`column`*,
*`width`* and *`height`* are restricted by the
output device. Is a father window (*`fatherWindow`* <> 'root')
specified, then the coordinates are relative to this window.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`row`** (input_control)  rectangle.origin.y `→` [HTuple](HTuple.md) (*int* / long)

Row index of upper left corner.

Default:
0

Value range:
`row` (lin)

Minimum increment:
1

Recommended increment:
1

**`column`** (input_control)  rectangle.origin.x `→` [HTuple](HTuple.md) (*int* / long)

Column index of upper left corner.

Default:
0

Value range:
`column` (lin)

Minimum increment:
1

Recommended increment:
1

**`width`** (input_control)  rectangle.extent.x `→` [HTuple](HTuple.md) (*int* / long)

Window's width.

Default:
256

Value range:
`0
≤
width` (lin)

Minimum increment:
1

Recommended increment:
1

**`height`** (input_control)  rectangle.extent.y `→` [HTuple](HTuple.md) (*int* / long)

Window's height.

Default:
256

Value range:
`0
≤
height` (lin)

Minimum increment:
1

Recommended increment:
1

**`borderWidth`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Window border's width.

Default:
2

Value range:
`0
≤
borderWidth` (lin)

Minimum increment:
1

Recommended increment:
1

**`borderColor`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Window border's color.

Default:
"white"

**`backgroundColor`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Background color.

Default:
"black"

**`fatherWindow`** (input_control)  pointer `→` [HTuple](HTuple.md) (*IntPtr* / IntPtr)

Logical number of the father window. For the display
as father you may specify 'root' or 0.

Default:
0

Restriction:
`FatherWindow >= 0`

**`mode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Window mode.

Default:
"visible"

List of values:
"buffer", "invisible", "transparent", "visible"

**`machine`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Computer name, where the window has to be opened or
empty string.

Default:
""

**`windowHandle`** (output_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

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
`OpenTextwindow` returns 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

## Possible Predecessors

`ResetObjDb`

## Possible Successors

`SetColor`,
`QueryWindowType`,
`GetWindowType`,
`SetWindowType`,
`GetMposition`,
`SetTposition`,
`SetTshape`,
`SetWindowExtents`,
`GetWindowExtents`,
`QueryColor`,
`SetCheck`,
`SetSystem`

## Alternatives

`OpenWindow`

## See also

`WriteString`,
`ReadString`,
`NewLine`,
`GetStringExtents`,
`GetTposition`,
`SetColor`,
`QueryWindowType`,
`GetWindowType`,
`SetWindowType`,
`GetMposition`,
`SetTposition`,
`SetTshape`,
`SetWindowExtents`,
`GetWindowExtents`,
`QueryColor`,
`SetCheck`,
`SetSystem`

## Module

Foundation
