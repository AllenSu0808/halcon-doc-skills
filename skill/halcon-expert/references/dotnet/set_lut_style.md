# SetLutStyle (Operator)

## Name

`SetLutStyle` — Changing the look-up-table (lut).

## Warning

**`SetLutStyle` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`static void HOperatorSet.SetLutStyle(HTuple windowHandle, HTuple hue, HTuple saturation, HTuple intensity)`

`void HWindow.SetLutStyle(double hue, double saturation, double intensity)`

## Description

`SetLutStyle` changes the look-up-table (lut) of the device
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
call of `SetLutStyle`. Calling [`SetLut`](set_lut.md) has got no
effect on these parameters.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`hue`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Modification of color value.

Default:
0.0

Value range:
`0.0
≤
hue
≤
1.0`

**`saturation`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Modification of saturation.

Default:
1.5

Value range:
`0.0
≤
saturation`

**`intensity`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Modification of intensity.

Default:
1.5

Value range:
`0.0
≤
intensity`

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

`SetLutStyle` returns 2 (
H_MSG_TRUE)
if the window is valid and the parameter
is correct. Otherwise an exception is raised.

## Possible Predecessors

`GetLutStyle`

## Possible Successors

`SetLut`

## Alternatives

`SetLut`,
`ScaleImage`

## See also

`GetLutStyle`

## Module

Foundation
