# SetRgb (Operator)

## Name

`SetRgb` — Set the color definition via RGB values.

## Signature

`static void HOperatorSet.SetRgb(HTuple windowHandle, HTuple red, HTuple green, HTuple blue)`

`void HWindow.SetRgb(HTuple red, HTuple green, HTuple blue)`

`void HWindow.SetRgb(int red, int green, int blue)`

## Description

`SetRgb` sets the output color(s) or the gray values, respectively,
for region output for the window. The colors are defined with
the red, green and blue components. If only one combination is
passed, all output takes place in that color. If a tuple is passed,
region output and output of geometric objects takes place modulo the
passed colors.

For every call of an output operator, output is started with the
first color. If only one object is displayed per call, it will
always be displayed in the first color. This is even true for
objects with multiple connection components. If multiple objects are
displayed per operator call, multiple colors are used. The defined
colors are used until [`SetColor`](set_color.md),
`SetRgb` or [`SetGray`](set_gray.md) is called again. The
values are used by operators like [`DispRegion`](disp_region.md),
[`DispLine`](disp_line.md),
[`DispRectangle1`](disp_rectangle1.md), [`DispRectangle2`](disp_rectangle2.md),
[`DispArrow`](disp_arrow.md), etc.

## Attention

If a passed color is not available, an exception is raised.
If `set_check(::'~color':)`
was called before,
HALCON uses a similar color and suppresses the error.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`red`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Red component of the color.

Default:
255

Value range:
`0
≤
red
≤
255`

**`green`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Green component of the color.

Default:
0

Value range:
`0
≤
green
≤
255`

**`blue`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Blue component of the color.

Default:
0

Value range:
`0
≤
blue
≤
255`

## Result

`SetRgb` returns 2 (
H_MSG_TRUE)
if the window is valid and all
passed colors are available and displayable. Otherwise an exception
is raised.

## Possible Successors

`DispImage`,
`DispRegion`

## Alternatives

`SetHsi`,
`SetColor`,
`SetGray`

## See also

`DispRegion`

## Module

Foundation
