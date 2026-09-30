# access_channel (Operator)

## Name

`access_channel` — Access a channel of a multi-channel image.

## Signature

`access_channel(MultiChannelImage : Image : Channel : )`

## Description

The operator `access_channel` accesses one or more channels of the
(multi-channel) input image *`MultiChannelImage`*.
The result *`Image`* contains as many channels as specified in
*`Channel`*.
The definition domain of the input is adopted.

Note that the channels are numbered from 1 to n.
The number of channels can be determined via the operator
[`count_channels`](count_channels.md).

If an empty tuple is passed in *`Channel`*, an object that
consists only of the domain of the input is returned.

## Execution Information

- Supports objects on compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MultiChannelImage`** (input_object)  (multichannel-)image(-array) `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Multi-channel image.

**`Image`** (output_object)  (multichannel-)image(-array) `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Selected channels of MultiChannelImage.

**`Channel`** (input_control)  channel(-array) `→`  (integer)

Indices of the channels to be accessed.

Default:
1

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12

Value range:
`1
≤
Channel`

## Example (C)

```
read_image(&Color,"patras");   /* read color image */
access_channel(Color,&Red,1);  /* extract red channel */
disp_image(Red,WindowHandle);
```

## Possible Predecessors

`count_channels`

## Possible Successors

`disp_image`

## Alternatives

`decompose2`,
`decompose3`,
`decompose4`,
`decompose5`

## See also

`count_channels`

## Module

Foundation
