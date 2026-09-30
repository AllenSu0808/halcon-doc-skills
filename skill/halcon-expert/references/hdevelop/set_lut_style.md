# set_lut_style (Operator)

## Name

`set_lut_style` — Changing the look-up-table (lut).

## Warning

**`set_lut_style` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`set_lut_style( : : WindowHandle, Hue, Saturation, Intensity : )`

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

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`Hue`** (input_control)  real `→`  (real)

Modification of color value.

Default:
0.0

Value range:
`0.0
≤
Hue
≤
1.0`

**`Saturation`** (input_control)  real `→`  (real)

Modification of saturation.

Default:
1.5

Value range:
`0.0
≤
Saturation`

**`Intensity`** (input_control)  real `→`  (real)

Modification of intensity.

Default:
1.5

Value range:
`0.0
≤
Intensity`

## Example (HDevelop)

```
read_image(Image,'monkey')
dev_set_lut('color1')
repeat
  get_mbutton(WindowHandle,Row,Column,Button)
  Saturation := Row/300.0
  Hue := Column/512.0
  set_lut_style(WindowHandle,Hue,Saturation,1.0)
  dev_display(Image)
until(Button == 4)
```

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
