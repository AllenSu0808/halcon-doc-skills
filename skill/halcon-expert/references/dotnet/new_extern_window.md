# NewExternWindow (Operator)

## Name

`NewExternWindow` — Create a virtual graphics window under Windows.

## Signature

`static void HOperatorSet.NewExternWindow(HTuple WINHWnd, HTuple row, HTuple column, HTuple width, HTuple height, out HTuple windowHandle)`

`void HWindow.NewExternWindow(IntPtr WINHWnd, int row, int column, int width, int height)`

## Description

`NewExternWindow` opens a new virtual window.
Note that this only works on Windows systems and drawing objects are not
supported.

Virtual means that a new window will not be created, but the window
whose window handle is given in the parameter *`WINHWnd`* is used
to perform output of gray value data, regions, graphics as well as
to perform textual output.

All operators that allow the user to define graphical primitives
through mouse interactions, like for example [`DrawRectangle1`](draw_rectangle1.md), do not
work on external windows. The following operators can be used:

- Output of gray values:
  [`SetPaint`](set_paint.md), [`SetLut`](set_lut.md)
- Regions:
  [`SetColor`](set_color.md), [`SetRgb`](set_rgb.md), [`SetHsi`](set_hsi.md),
  [`SetGray`](set_gray.md), [`SetShape`](set_shape.md),
  [`SetLineWidth`](set_line_width.md),
  [`SetLineStyle`](set_line_style.md), [`SetDraw`](set_draw.md)
- Image part:
  [`SetPart`](set_part.md)
- Text:
  [`SetFont`](set_font.md)

You may query current set values by calling operators like
[`GetShape`](get_shape.md). As some parameters are specified through the
hardware (Resolution/Colors), you may query current available
resources by calling operators like [`QueryColor`](query_color.md).

The parameter *`WINHWnd`* is used to pass the window handle of
the window in which output should be done.

The origin of the coordinate system of the window resides in the
upper left corner (coordinates: (0,0)). The row index grows downward
(maximum: *`height`*-1), the column index grows to the right
(maximal: *`width`*-1).

You may use the value *-1* for parameters *`width`* and
*`height`*. This means, that the corresponding value is chosen
automatically. In particular, this is important if the aspect ratio
of the pixels is not 1.0 (see [`SetSystem`](set_system.md)). If one of the
two parameters is set to *-1*, it will be chosen through the
size which results out of the aspect ratio of the pixels. If both
parameters are set to *-1*, they will be set to the current
image format.

The position and size of a window may change during runtime of a
program, e.g., through external influences (window manager). With
the operator [`SetWindowExtents`](set_window_extents.md), you can change the size of
the (external) widow via the program. Note that
[`SetWindowExtents`](set_window_extents.md) offers to change the position as well,
but you cannot change the position of an external window under
Windows.

Opening a window causes the assignment of a default font. It is
used in connection with operators like [`WriteString`](write_string.md) and you
may change it by performing [`SetFont`](set_font.md) after calling
[`OpenWindow`](open_window.md). On the other hand, you have the possibility to
specify a default font by calling
`set_system(::'default_font',<Fontname>:)` before opening a
window (and all following windows; see also [`QueryFont`](query_font.md)).

You may set the color of graphics and font, which is used for output
operators like [`DispRegion`](disp_region.md) or [`DispCircle`](disp_circle.md), by
calling [`SetRgb`](set_rgb.md), [`SetHsi`](set_hsi.md) or [`SetGray`](set_gray.md).

The content of the window is not saved, if other windows overlap the
window. This must be done in the program code that handles the
window in the calling program.

For graphical output ([`DispImage`](disp_image.md),[`DispRegion`](disp_region.md), etc.)
you may adjust the window by calling the operator [`SetPart`](set_part.md) in
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
example [`DrawRectangle1`](draw_rectangle1.md), do not work on external windows.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`WINHWnd`** (input_control)  pointer `→` [HTuple](HTuple.md) (*IntPtr*)

Windows window handle of a previously created window.

Restriction:
`WINHWnd != 0`

**`row`** (input_control)  rectangle.origin.y `→` [HTuple](HTuple.md) (*int* / long)

Row coordinate of upper left corner.

Default:
0

Restriction:
`Row >= 0`

**`column`** (input_control)  rectangle.origin.x `→` [HTuple](HTuple.md) (*int* / long)

Column coordinate of upper left corner.

Default:
0

Restriction:
`Column >= 0`

**`width`** (input_control)  rectangle.extent.x `→` [HTuple](HTuple.md) (*int* / long)

Width of the window.

Default:
512

Restriction:
`Width > 0 || Width == -1`

**`height`** (input_control)  rectangle.extent.y `→` [HTuple](HTuple.md) (*int* / long)

Height of the window.

Default:
512

Restriction:
`Height > 0 || Height == -1`

**`windowHandle`** (output_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

## Example (C++)

```
// Needs to be embedded into an application framework,
// see examples/cpp/mfc/MatchingExtWin.
```

## Result

If the values of the specified parameters are correct
`NewExternWindow` returns 2 (
H_MSG_TRUE)
. If necessary, an exception
is raised.

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

`OpenWindow`,
`DispRegion`,
`DispImage`,
`DispColor`,
`SetLut`,
`QueryColor`,
`SetColor`,
`SetRgb`,
`SetHsi`,
`SetPixel`,
`SetGray`,
`SetPart`,
`SetPartStyle`,
`QueryWindowType`,
`GetWindowType`,
`SetWindowType`,
`GetMposition`,
`SetTposition`,
`SetWindowExtents`,
`GetWindowExtents`,
`SetWindowAttr`,
`SetCheck`,
`SetSystem`

## Module

Foundation
