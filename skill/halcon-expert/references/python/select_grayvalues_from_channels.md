# select_grayvalues_from_channels (Operator)

## Name

`select_grayvalues_from_channels` — Selection of gray values of a multi-channel image using an index image.

## Signature

`def select_grayvalues_from_channels(multichannel_image: HObject, index_image: HObject) -> HObject`

## Description

The operator `select_grayvalues_from_channels` selects gray
values from the different channels of *`multichannel_image`*.
The channel number for each pixel is determined from the corresponding
pixel value in *`index_image`*.
Note, *`index_image`* is allowed to have an arbitrary number of channels
for reasons of backward compatibility, but only the first channel
is considered.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on domain level.

## Parameters

**`multichannel_image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte)

Multi-channel gray value image.

**`index_image`** (input_object)  singlechannelimage(-array) `→` HObject (byte)

Image, where pixel values are interpreted as
channel index.

Number of elements:
IndexImage == MultichannelImage || IndexImage == 1

**`selected`** (output_object)  singlechannelimage(-array) `→` HObject (byte)

Resulting image.

## Example (C++)

```
compose3(Focus0,Focus1,Focus2,&MultiFocus);
depth_from_focus(MultiFocus,&Depth,&Confidence,'highpass','next_maximum');
mean_image(Depth,&Smooth,15,15);
select_grayvalues_from_channels(MultiChannel,Smooth,SharpImage);
```

## Possible Predecessors

`depth_from_focus`,
`mean_image`

## Possible Successors

`disp_image`

## See also

`count_channels`

## Module

Foundation
