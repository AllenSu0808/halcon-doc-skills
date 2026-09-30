# set_hsi (Operator)

## Name

`set_hsi` — Define output colors (HSI-coded).

## Signature

`def set_hsi(window_handle: HHandle, hue: MaybeSequence[int], saturation: MaybeSequence[int], intensity: MaybeSequence[int]) -> None`

## Description

`set_hsi` sets the region output color(s)/gray value(s) for
the valid window. Colors are passed as *`hue`*,
*`saturation`*, and *`intensity`*. Transformation from
HSI to RGB is done with:
$$H = (Hue/255.0) * 2\pi S = (Saturation/255.0) * 2.0/\sqrt{6} I = Intensity M1 = S cos(H)/\sqrt{6} * 255.0 M2 = S sin(H)/\sqrt{2} * 255.0 Red = 2M1 + I Green = -M1 + M2 + I Blue = -M1 - M2 + I$$ ![figure](../assets/a4356662a25004b5.svg)

The value range is clipped to 0 to 255.

If only one combination is passed, all output will take place in
that color. If a tuple of colors is passed, the output color of
regions and geometric objects is modulo to the number of colors.
HALCON always begins output with
the first color passed. Note, that the number of output colors
depends on the number of objects that are displayed in one operator
call. If only single objects are displayed, they always appear in
the first color, even if the consist of more than one connected
components.

Selected colors are used until the next call of
[`set_color`](set_color.md),[`set_rgb`](set_rgb.md) or
[`set_gray`](set_gray.md). Colors are relevant to windows, i.e., only the
colors of the valid window can be set. Region output colors are
used by operators like [`disp_region`](disp_region.md), [`disp_line`](disp_line.md),
[`disp_rectangle1`](disp_rectangle1.md), [`disp_rectangle2`](disp_rectangle2.md),
[`disp_arrow`](disp_arrow.md), etc.
It is also used by operators with gray value output in certain output modes
(e.g., *"3d_plot"*, see [`set_paint`](set_paint.md)).

## Attention

The colors are internally stored as RGB triples. Some HSI triples
can not be represented by a valid RGB triple (i.e. in the range 0..255). In
this case the nearest color which can be represented is used instead.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`hue`** (input_control)  integer(-array) `→` MaybeSequence[int]

Hue for region output.

Default:
30

Value range:
`0
≤
hue
≤
255`

**`saturation`** (input_control)  integer(-array) `→` MaybeSequence[int]

Saturation for region output.

Default:
255

Value range:
`0
≤
saturation
≤
255`

**`intensity`** (input_control)  integer(-array) `→` MaybeSequence[int]

Intensity for region output.

Default:
84

Value range:
`0
≤
intensity
≤
255`

## Result

`set_hsi` returns 2 (
H_MSG_TRUE)
if the window is valid and the
output colors are displayable. Otherwise an exception is raised.

## Possible Predecessors

`get_hsi`

## Possible Successors

`disp_region`

## See also

`get_hsi`,
`trans_from_rgb`,
`trans_to_rgb`,
`disp_region`

## Module

Foundation
