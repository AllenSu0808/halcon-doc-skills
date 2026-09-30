# set_fix (Operator)

## Name

`set_fix` — Set fixing of “look-up-table” (lut)

## Warning

**`set_fix` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`set_fix( : : WindowHandle, Mode : )`

## Description

Behavior for *`Mode`* = *'true'*:
`set_fix` fixes that pixel lastly ascertained by one of the
operators [`set_gray`](set_gray.md), [`set_color`](set_color.md), [`set_hsi`](set_hsi.md) or
[`set_rgb`](set_rgb.md)
(Remark: Here a pixel is the index within the current look-up-table).
To assign a new color to a fixed pixel set a color or gray value by using
[`set_color`](set_color.md), [`set_rgb`](set_rgb.md), [`set_hsi`](set_hsi.md) or [`set_gray`](set_gray.md).
This makes it possible to define any color ([`set_color`](set_color.md)), any
gray value ([`set_gray`](set_gray.md)) and any color combination ([`set_rgb`](set_rgb.md),
[`set_hsi`](set_hsi.md)) at any position of the look-up-table.

*`Mode`* set to 'false' reset the fixing. To modify or create a look-up-table
process [`set_pixel`](set_pixel.md),
`set_fix(::WindowHandle,'true':)`,
[`set_rgb`](set_rgb.md) and `set_fix(::WindowHandle,'false':)` one after another.

## Attention

As a side effect `set_fix` can change colors of
“non-HALCON windows”.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`Mode`** (input_control)  string `→`  (string)

Mode of fixing.

Default:
'true'

List of values:
'false', 'true'

## Result

`set_fix` returns 2 (
H_MSG_TRUE)
if the window is valid, the hardware
supports a look-up-table and all parameters are correct. Otherwise an
exception is raised.

## Possible Predecessors

`get_fix`

## Possible Successors

`set_pixel`,
`set_rgb`

## See also

`get_fix`,
`set_pixel`,
`set_rgb`,
`set_color`,
`set_hsi`,
`set_gray`

## Module

Foundation
