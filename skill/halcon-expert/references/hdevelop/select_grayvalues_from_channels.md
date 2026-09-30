# select_grayvalues_from_channels (Operator)

## Name

`select_grayvalues_from_channels` — Selection of gray values of a multi-channel image using an index image.

## Signature

`select_grayvalues_from_channels(MultichannelImage, IndexImage : Selected : : )`

## Description

The operator `select_grayvalues_from_channels` selects gray
values from the different channels of *`MultichannelImage`*.
The channel number for each pixel is determined from the corresponding
pixel value in *`IndexImage`*.
Note, *`IndexImage`* is allowed to have an arbitrary number of channels
for reasons of backward compatibility, but only the first channel
is considered.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on domain level.

## Parameters

**`MultichannelImage`** (input_object)  (multichannel-)image(-array) `→` object (byte)

Multi-channel gray value image.

**`IndexImage`** (input_object)  singlechannelimage(-array) `→` object (byte)

Image, where pixel values are interpreted as
channel index.

Number of elements:
IndexImage == MultichannelImage || IndexImage == 1

**`Selected`** (output_object)  singlechannelimage(-array) `→` object (byte)

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
