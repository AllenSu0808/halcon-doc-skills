# CountChannels (Operator)

## Name

`CountChannels` — Count channels of image.

## Signature

`static void HOperatorSet.CountChannels(HObject multiChannelImage, out HTuple channels)`

`HTuple HImage.CountChannels()`

## Description

The operator `CountChannels` counts the number of
channels of all input images.

## Execution Information

- Supports objects on compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`multiChannelImage`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

One- or multi-channel image.

**`channels`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Number of channels.

## Example (C)

```
read_image(&Color,"patras");
count_channels(Color,&num_channels);
for (i=1; i<=num_channels; i++)
{
  access_channel(Color,&Channel,i);
  disp_image(Channel,WindowHandle);
  clear_obj(Channel);
}
```

## Possible Successors

`AccessChannel`,
`AppendChannel`,
`DispImage`

## See also

`AppendChannel`,
`AccessChannel`

## Module

Foundation
