# ConvolChannels (Operator)

## Name

`ConvolChannels` — Perform a convolution along the channel dimension.

## Signature

`static void HOperatorSet.ConvolChannels(HObject multichannelImage, out HObject imageSmoothed, HTuple filter, HTuple border)`

`HImage HImage.ConvolChannels(HTuple filter, string border)`

## Description

`ConvolChannels` applies the linear filter *`filter`* along the
channel dimension of the multichannel image *`multichannelImage`* and
stores the result in *`imageSmoothed`*.
Each pixel is processed independently.
Border handling along the channel dimension is specified by *`border`*
and either continues the current value (*"constant"*) or mirrors
the values (*"mirror"*).

This operator can be used, for example, to smooth hyperspectral
images across spectra.
Filter parameters can be generated, for instance, with
[`GenSavitzkyGolayFilter`](gen_savitzky_golay_filter.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on domain level.

## Parameters

**`multichannelImage`** (input_object)  multichannel-image(-array) `→` [HImage](HImage.md) (byte / uint2 / real)

Multichannel image to be smoothed.

**`imageSmoothed`** (output_object)  image(-array) `→` [HImage](HImage.md) (real)

Smoothed multichannel image.

**`filter`** (input_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Filter coefficients.

**`border`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Type of boundary treatment.

Default:
"constant"

List of values:
"constant", "mirror"

## Possible Predecessors

`GenSavitzkyGolayFilter`

## Module

Foundation
