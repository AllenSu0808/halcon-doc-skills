# DispChannel (Operator)

## Name

`DispChannel` — Displays images with several channels.

## Signature

`static void HOperatorSet.DispChannel(HObject multichannelImage, HTuple windowHandle, HTuple channel)`

`void HImage.DispChannel(HWindow windowHandle, HTuple channel)`

`void HImage.DispChannel(HWindow windowHandle, int channel)`

`void HWindow.DispChannel(HImage multichannelImage, HTuple channel)`

`void HWindow.DispChannel(HImage multichannelImage, int channel)`

## Description

`DispChannel` displays an image in the output window.
It is possible to display several images with one call. In this case the
images are displayed one after another. If the definition domains of the
images overlap only the last image is visible. The parameter
*`channel`* defines the number of the channel that is displayed.
For RGB-images the three color channels have to be used within a tuple
parameter. For more information see [`DispImage`](disp_image.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`multichannelImage`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Multichannel images to be displayed.

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`channel`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

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
output mode is set, `DispChannel` returns 2 (
H_MSG_TRUE)
. Otherwise an
exception is raised.

## Possible Predecessors

`OpenWindow`,
`SetRgb`,
`SetLut`,
`SetHsi`

## Alternatives

`DispImage`,
`DispColor`

## See also

`OpenWindow`,
`ResetObjDb`,
`SetLut`,
`DumpWindow`

## Module

Foundation
