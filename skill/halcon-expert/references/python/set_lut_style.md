# set_lut_style (Operator)

## Name

`set_lut_style` — Changing the look-up-table (lut).

## Warning

**`set_lut_style` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`def set_lut_style(window_handle: HHandle, hue: float, saturation: float, intensity: float) -> None`

## Description

`set_lut_style` changes the look-up-table (lut) of the device
displaying the valid output window. It has got three parameters:

- **Hue:** —

  Rotation of color space,
  Hue = 1.9 conforms to a one-time rotation of the
  color space.
  No changes: Hue = 0.0
  Complement colors: Hue = 0.5
- **Saturation:** —

  Changes of saturation,
  No changes: Saturation = 1.0
  Gray value image: Saturation = 0.0
- **Intensity:** —

  Changes of intensity,
  No changes: Intensity = 1.0
  Black image: Intensity = 0.0

Changes affect only the part of an look-up-table that is used for
displaying images. The parameter of modification remain until the next
call of `set_lut_style`. Calling [`set_lut`](set_lut.md) has got no
effect on these parameters.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`hue`** (input_control)  real `→` float

Modification of color value.

Default:
0.0

Value range:
`0.0
≤
hue
≤
1.0`

**`saturation`** (input_control)  real `→` float

Modification of saturation.

Default:
1.5

Value range:
`0.0
≤
saturation`

**`intensity`** (input_control)  real `→` float

Modification of intensity.

Default:
1.5

Value range:
`0.0
≤
intensity`

## Result

`set_lut_style` returns 2 (
H_MSG_TRUE)
if the window is valid and the parameter
is correct. Otherwise an exception is raised.

## Possible Predecessors

`get_lut_style`

## Possible Successors

`set_lut`

## Alternatives

`set_lut`,
`scale_image`

## See also

`get_lut_style`

## Module

Foundation
