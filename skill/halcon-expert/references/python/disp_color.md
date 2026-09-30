# disp_color (Operator)

## Name

`disp_color` — Displays a color (RGB) image

## Signature

`def disp_color(color_image: HObject, window_handle: HHandle) -> None`

## Description

`disp_color` displays the three channels of a color image in the
output window. The channels are ordered in the sequence (red,green,blue).
`disp_color` can be simulated by [`disp_channel`](disp_channel.md).

## Attention

Due to the restricted number of available colors the color appearance is
usually different from the original.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`color_image`** (input_object)  multichannel-image `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Color image to display.

**`window_handle`** (input_control)  window `→` HHandle

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
output mode is set, `disp_color` returns 2 (
H_MSG_TRUE)
. Otherwise an
exception is raised.

## Possible Predecessors

`open_window`,
`set_rgb`,
`set_lut`,
`set_hsi`

## Alternatives

`disp_channel`,
`disp_obj`

## See also

`disp_image`,
`open_window`,
`reset_obj_db`,
`set_lut`,
`dump_window`

## Module

Foundation
