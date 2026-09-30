# disp_channel (Operator)

## Name

`disp_channel` — Displays images with several channels.

## Signature

`disp_channel(MultichannelImage : : WindowHandle, Channel : )`

## Description

`disp_channel` displays an image in the output window.
It is possible to display several images with one call. In this case the
images are displayed one after another. If the definition domains of the
images overlap only the last image is visible. The parameter
*`Channel`* defines the number of the channel that is displayed.
For RGB-images the three color channels have to be used within a tuple
parameter. For more information see [`disp_image`](disp_image.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MultichannelImage`** (input_object)  (multichannel-)image(-array) `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Multichannel images to be displayed.

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`Channel`** (input_control)  integer(-array) `→`  (integer)

Number of channel or the numbers of the RGB-channels

Default:
1

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10

## Example (HDevelop)

```
read_image(Image,'patras')
count_channels (Image, Channels)
for I := 1 to Channels by 1
    disp_channel (Image, WindowHandle, I)
endfor
```

## Result

If the used images contain valid values and a correct
output mode is set, `disp_channel` returns 2 (
H_MSG_TRUE)
. Otherwise an
exception is raised.

## Possible Predecessors

`open_window`,
`set_rgb`,
`set_lut`,
`set_hsi`

## Alternatives

`disp_image`,
`disp_color`

## See also

`open_window`,
`reset_obj_db`,
`set_lut`,
`dump_window`

## Module

Foundation
