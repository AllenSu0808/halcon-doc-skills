# SetFix (Operator)

## Name

`SetFix` — Set fixing of “look-up-table” (lut)

## Warning

**`SetFix` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`static void HOperatorSet.SetFix(HTuple windowHandle, HTuple mode)`

`void HWindow.SetFix(string mode)`

## Description

Behavior for *`mode`* = *"true"*:
`SetFix` fixes that pixel lastly ascertained by one of the
operators [`SetGray`](set_gray.md), [`SetColor`](set_color.md), [`SetHsi`](set_hsi.md) or
[`SetRgb`](set_rgb.md)
(Remark: Here a pixel is the index within the current look-up-table).
To assign a new color to a fixed pixel set a color or gray value by using
[`SetColor`](set_color.md), [`SetRgb`](set_rgb.md), [`SetHsi`](set_hsi.md) or [`SetGray`](set_gray.md).
This makes it possible to define any color ([`SetColor`](set_color.md)), any
gray value ([`SetGray`](set_gray.md)) and any color combination ([`SetRgb`](set_rgb.md),
[`SetHsi`](set_hsi.md)) at any position of the look-up-table.

*`mode`* set to 'false' reset the fixing. To modify or create a look-up-table
process [`SetPixel`](set_pixel.md),
`set_fix(::WindowHandle,'true':)`,
[`SetRgb`](set_rgb.md) and `set_fix(::WindowHandle,'false':)` one after another.

## Attention

As a side effect `SetFix` can change colors of
“non-HALCON windows”.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`mode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Mode of fixing.

Default:
"true"

List of values:
"false", "true"

## Result

`SetFix` returns 2 (
H_MSG_TRUE)
if the window is valid, the hardware
supports a look-up-table and all parameters are correct. Otherwise an
exception is raised.

## Possible Predecessors

`GetFix`

## Possible Successors

`SetPixel`,
`SetRgb`

## See also

`GetFix`,
`SetPixel`,
`SetRgb`,
`SetColor`,
`SetHsi`,
`SetGray`

## Module

Foundation
