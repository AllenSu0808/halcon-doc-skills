# set_rgb (Operator)

## Name

`set_rgb` — Set the color definition via RGB values.

## Signature

`def set_rgb(window_handle: HHandle, red: MaybeSequence[int], green: MaybeSequence[int], blue: MaybeSequence[int]) -> None`

## Description

`set_rgb` sets the output color(s) or the gray values, respectively,
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
colors are used until [`set_color`](set_color.md),
`set_rgb` or [`set_gray`](set_gray.md) is called again. The
values are used by operators like [`disp_region`](disp_region.md),
[`disp_line`](disp_line.md),
[`disp_rectangle1`](disp_rectangle1.md), [`disp_rectangle2`](disp_rectangle2.md),
[`disp_arrow`](disp_arrow.md), etc.

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

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`red`** (input_control)  integer(-array) `→` MaybeSequence[int]

Red component of the color.

Default:
255

Value range:
`0
≤
red
≤
255`

**`green`** (input_control)  integer(-array) `→` MaybeSequence[int]

Green component of the color.

Default:
0

Value range:
`0
≤
green
≤
255`

**`blue`** (input_control)  integer(-array) `→` MaybeSequence[int]

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

`set_rgb` returns 2 (
H_MSG_TRUE)
if the window is valid and all
passed colors are available and displayable. Otherwise an exception
is raised.

## Possible Successors

`disp_image`,
`disp_region`

## Alternatives

`set_hsi`,
`set_color`,
`set_gray`

## See also

`disp_region`

## Module

Foundation
