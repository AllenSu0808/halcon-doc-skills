# set_rgba (Operator)

## Name

`set_rgba` — Set the color definition via RGBA values.

## Signature

`set_rgba( : : WindowHandle, Red, Green, Blue, Alpha : )`

## Description

`set_rgba` sets the output color(s) or the gray values, respectively,
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
colors are used until [`set_color`](set_color.md), `set_rgba`, or
[`set_rgb`](set_rgb.md) is called again. The
values are used by operators like [`disp_region`](disp_region.md),
[`disp_line`](disp_line.md),
[`disp_rectangle1`](disp_rectangle1.md), [`disp_rectangle2`](disp_rectangle2.md),
[`disp_arrow`](disp_arrow.md), etc.

## Attention

`set_rgba` depends on the library libcanvas, which might not be
available on embedded systems.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`Red`** (input_control)  integer(-array) `→`  (integer)

Red component of the color.

Default:
255

Value range:
`0
≤
Red
≤
255`

Restriction:
`0 <= Red && Red <= 255`

**`Green`** (input_control)  integer(-array) `→`  (integer)

Green component of the color.

Default:
0

Value range:
`0
≤
Green
≤
255`

Restriction:
`0 <= Green && Green <= 255`

**`Blue`** (input_control)  integer(-array) `→`  (integer)

Blue component of the color.

Default:
0

Value range:
`0
≤
Blue
≤
255`

Restriction:
`0 <= Blue && Blue <= 255`

**`Alpha`** (input_control)  integer(-array) `→`  (integer)

Alpha component of the color.

Default:
255

Value range:
`0
≤
Alpha
≤
255`

Restriction:
`0 <= Alpha && Alpha <= 255`

## Result

`set_rgba` returns 2 (
H_MSG_TRUE)
if the window is valid and all
passed colors are available and displayable. Otherwise an exception
is raised.

## Possible Successors

`disp_obj`

## Alternatives

`set_rgb`,
`set_color`

## Module

Foundation
