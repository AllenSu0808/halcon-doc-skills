# DispColor (Operator)

## Name

`DispColor` — Displays a color (RGB) image

## Signature

`static void HOperatorSet.DispColor(HObject colorImage, HTuple windowHandle)`

`void HImage.DispColor(HWindow windowHandle)`

`void HWindow.DispColor(HImage colorImage)`

## Description

`DispColor` displays the three channels of a color image in the
output window. The channels are ordered in the sequence (red,green,blue).
`DispColor` can be simulated by [`DispChannel`](disp_channel.md).

## Attention

Due to the restricted number of available colors the color appearance is
usually different from the original.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`colorImage`** (input_object)  multichannel-image `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Color image to display.

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

## Example (C)

```
/* disp_color(ColorImage) is identical to: */
Herror my_disp_color(Hobject ColorImage, Htuple *WindowHandle) {
  Htuple  Tupel;
  create_tuple(&Tupel,3);
  set_i(Tupel,1,0);
  set_i(Tupel,2,1);
  set_i(Tupel,3,2);
  T_disp_channel(ColorImage,*WindowHandle,Tupel);
  destroy_tuple(Tupel);
}
```

## Result

If the used image contains valid values and a correct
output mode is set, `DispColor` returns 2 (
H_MSG_TRUE)
. Otherwise an
exception is raised.

## Possible Predecessors

`OpenWindow`,
`SetRgb`,
`SetLut`,
`SetHsi`

## Alternatives

`DispChannel`,
`DispObj`

## See also

`DispImage`,
`OpenWindow`,
`ResetObjDb`,
`SetLut`,
`DumpWindow`

## Module

Foundation
