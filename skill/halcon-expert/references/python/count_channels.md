# count_channels (Operator)

## Name

`count_channels` — Count channels of image.

## Signature

`def count_channels(multi_channel_image: HObject) -> Sequence[int]`

`def count_channels_s(multi_channel_image: HObject) -> int`

## Description

The operator `count_channels` counts the number of
channels of all input images.

## Execution Information

- Supports objects on compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`multi_channel_image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

One- or multi-channel image.

**`channels`** (output_control)  integer(-array) `→` Sequence[int]

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

`access_channel`,
`append_channel`,
`disp_image`

## See also

`append_channel`,
`access_channel`

## Module

Foundation
