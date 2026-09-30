# SetGray (Operator)

## Name

`SetGray` — Define gray values for region output.

## Signature

`static void HOperatorSet.SetGray(HTuple windowHandle, HTuple grayValues)`

`void HWindow.SetGray(HTuple grayValues)`

`void HWindow.SetGray(int grayValues)`

## Description

`SetGray` defines the gray values for region
output. Gray values are defined as the range of the color lookup
table that is used for gray value output with [`DispImage`](disp_image.md)
in conjunction with `set_paint(::WindowHandle,'gray':)`. These entries
can be modified by [`SetLut`](set_lut.md). So a 'gray value' is the
color in which a pixel with the same value is displayed (not
necessarily really gray). In general, when changing the color lookup
table with [`SetLut`](set_lut.md), the colors of the displayed image
will change too.

If a gray value is needed as a color for image output (i.e. no color
changes with [`SetLut`](set_lut.md) are possible), it can be set with
`set_color(::WindowHandle,'gray':)`.

If only a single gray value is passed, all output will take place in
that gray value. If a tuple of gray values is passed, all output will
take place in gray values modulo the number of tuple elements. In the
example below, the first circle is displayed with gray value 100, the
second with 200 and the third with 100 again. Every output operator
starts with the first gray value. Note, that the number of output
gray values depends on the number of objects that are displayed in
one operator call. If only single objects are displayed, they
always appear in the first gray value, even if the consist of more
than one connected components.

When the operators `SetGray`, [`SetColor`](set_color.md),
[`SetRgb`](set_rgb.md), [`SetHsi`](set_hsi.md) are called, the overwrite
the existing values. If not all gray values are displayable on the
output device, the number range of *`grayValues`* (0..255) is
dithered to the range of displayable gray values. In any case 0 is
displayed as black and 255 as white. The displayable gray values can
be queried with the operator [`QueryGray`](query_gray.md).
With `set_check(::'~color':)`
error messages can be
suppressed if a gray value can't be displayed on the screen. In that
case, a similar gray value is displayed.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`grayValues`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Gray values for region output.

Default:
255

Suggested values:
0, 1, 2, 10, 16, 32, 64, 100, 120, 128, 250, 251, 252, 253, 254, 255

Value range:
`0
≤
grayValues
≤
255`

## Example (HDevelop)

```
set_gray(WindowHandle,[100,200])
disp_circle(WindowHandle,[100,200,300],[200,300,100],[100,100,100])
```

## Result

[`SetHsi`](set_hsi.md) returns 2 (
H_MSG_TRUE)
if the window is valid and the
given gray value is displayable. Otherwise an exception is raised.

## Possible Successors

`DispRegion`

## See also

`SetColor`

## Module

Foundation
