# AccessChannel (Operator)

## Name

`AccessChannel` — Access a channel of a multi-channel image.

## Signature

`static void HOperatorSet.AccessChannel(HObject multiChannelImage, out HObject image, HTuple channel)`

`HImage HImage.AccessChannel(HTuple channel)`

`HImage HImage.AccessChannel(int channel)`

## Description

The operator `AccessChannel` accesses one or more channels of the
(multi-channel) input image *`multiChannelImage`*.
The result *`image`* contains as many channels as specified in
*`channel`*.
The definition domain of the input is adopted.

Note that the channels are numbered from 1 to n.
The number of channels can be determined via the operator
[`CountChannels`](count_channels.md).

If an empty tuple is passed in *`channel`*, an object that
consists only of the domain of the input is returned.

## Execution Information

- Supports objects on compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`multiChannelImage`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Multi-channel image.

**`image`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Selected channels of MultiChannelImage.

**`channel`** (input_control)  channel(-array) `→` [HTuple](HTuple.md) (*int* / long)

Indices of the channels to be accessed.

Default:
1

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12

Value range:
`1
≤
channel`

## Example (C)

```
read_image(&Color,"patras");   /* read color image */
access_channel(Color,&Red,1);  /* extract red channel */
disp_image(Red,WindowHandle);
```

## Possible Predecessors

`CountChannels`

## Possible Successors

`DispImage`

## Alternatives

`Decompose2`,
`Decompose3`,
`Decompose4`,
`Decompose5`

## See also

`CountChannels`

## Module

Foundation
