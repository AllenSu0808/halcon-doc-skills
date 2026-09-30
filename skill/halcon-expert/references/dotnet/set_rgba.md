# SetRgba (Operator)

## Name

`SetRgba` — Set the color definition via RGBA values.

## Signature

`static void HOperatorSet.SetRgba(HTuple windowHandle, HTuple red, HTuple green, HTuple blue, HTuple alpha)`

`void HWindow.SetRgba(HTuple red, HTuple green, HTuple blue, HTuple alpha)`

`void HWindow.SetRgba(int red, int green, int blue, int alpha)`

## Description

`SetRgba` sets the output color(s) or the gray values, respectively,
for region output for the window. The colors are defined with
the red, green, blue, and alpha components. If only one combination is
passed, all output takes place in that color. If a tuple is passed,
region output and output of geometric objects takes place modulo the
passed colors.

For every call of an output operator, output is started with the
first color. If only one object is displayed per call, it will
always be displayed in the first color. This is even true for
objects with multiple connection components. If multiple objects are
displayed per operator call, multiple colors are used. The defined
colors are used until [`SetColor`](set_color.md), `SetRgba`, or
[`SetRgb`](set_rgb.md) is called again. The
values are used by operators like [`DispRegion`](disp_region.md),
[`DispLine`](disp_line.md),
[`DispRectangle1`](disp_rectangle1.md), [`DispRectangle2`](disp_rectangle2.md),
[`DispArrow`](disp_arrow.md), etc.

## Attention

`SetRgba` depends on the library libcanvas, which might not be
available on embedded systems.

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

Restriction:
`0 <= Red && Red <= 255`

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

Restriction:
`0 <= Green && Green <= 255`

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

Restriction:
`0 <= Blue && Blue <= 255`

**`alpha`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Alpha component of the color.

Default:
255

Value range:
`0
≤
alpha
≤
255`

Restriction:
`0 <= Alpha && Alpha <= 255`

## Result

`SetRgba` returns 2 (
H_MSG_TRUE)
if the window is valid and all
passed colors are available and displayable. Otherwise an exception
is raised.

## Possible Successors

`DispObj`

## Alternatives

`SetRgb`,
`SetColor`

## Module

Foundation
