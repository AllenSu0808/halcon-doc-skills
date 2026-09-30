# SelectGrayvaluesFromChannels (Operator)

## Name

`SelectGrayvaluesFromChannels` — Selection of gray values of a multi-channel image using an index image.

## Signature

`static void HOperatorSet.SelectGrayvaluesFromChannels(HObject multichannelImage, HObject indexImage, out HObject selected)`

`HImage HImage.SelectGrayvaluesFromChannels(HImage indexImage)`

## Description

The operator `SelectGrayvaluesFromChannels` selects gray
values from the different channels of *`multichannelImage`*.
The channel number for each pixel is determined from the corresponding
pixel value in *`indexImage`*.
Note, *`indexImage`* is allowed to have an arbitrary number of channels
for reasons of backward compatibility, but only the first channel
is considered.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on domain level.

## Parameters

**`multichannelImage`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte)

Multi-channel gray value image.

**`indexImage`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte)

Image, where pixel values are interpreted as
channel index.

Number of elements:
IndexImage == MultichannelImage || IndexImage == 1

**`selected`** (output_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte)

Resulting image.

## Example (C++)

```
compose3(Focus0,Focus1,Focus2,&MultiFocus);
depth_from_focus(MultiFocus,&Depth,&Confidence,'highpass','next_maximum');
mean_image(Depth,&Smooth,15,15);
select_grayvalues_from_channels(MultiChannel,Smooth,SharpImage);
```

## Possible Predecessors

`DepthFromFocus`,
`MeanImage`

## Possible Successors

`DispImage`

## See also

`CountChannels`

## Module

Foundation
