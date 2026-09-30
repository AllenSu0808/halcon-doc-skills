# ScaleImageMax (Operator)

## Name

`ScaleImageMax` — Maximum gray value spreading in the value range
*0* to *255*.

## Signature

`static void HOperatorSet.ScaleImageMax(HObject image, out HObject imageScaleMax)`

`HImage HImage.ScaleImageMax()`

## Description

The operator `ScaleImageMax` calculates the minimum and
maximum and scales the image to the maximum value range of a byte image.
This way the dynamics (value range) is fully exploited.
The number of different gray scales does not change,
but in general the visual impression is enhanced.
The gray values of images of the *"real"*, *"int2"*,
*"uint2"*, *"int4"*, and *"int8"* type
are scaled to the range *0* to *255*
and returned as *"byte"* images.

## Attention

The output always is an image of the type *"byte"*.

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / int2 / uint2 / int4 / int8 / real)

Image to be scaled.

**`imageScaleMax`** (output_object)  image(-array) `→` [HImage](HImage.md) (byte)

contrast enhanced image.

## Possible Successors

`DispImage`

## Alternatives

`EquHistoImage`,
`EquHistoImageRect`,
`ScaleImage`,
`Illuminate`,
`ConvertImageType`

## See also

`MinMaxGray`,
`GrayHisto`

## Module

Foundation
