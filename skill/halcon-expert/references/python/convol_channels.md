# convol_channels (Operator)

## Name

`convol_channels` — Perform a convolution along the channel dimension.

## Signature

`def convol_channels(multichannel_image: HObject, filter: Sequence[float], border: str) -> HObject`

## Description

`convol_channels` applies the linear filter *`filter`* along the
channel dimension of the multichannel image *`multichannel_image`* and
stores the result in *`image_smoothed`*.
Each pixel is processed independently.
Border handling along the channel dimension is specified by *`border`*
and either continues the current value (*"constant"*) or mirrors
the values (*"mirror"*).

This operator can be used, for example, to smooth hyperspectral
images across spectra.
Filter parameters can be generated, for instance, with
[`gen_savitzky_golay_filter`](gen_savitzky_golay_filter.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on domain level.

## Parameters

**`multichannel_image`** (input_object)  multichannel-image(-array) `→` HObject (byte / uint2 / real)

Multichannel image to be smoothed.

**`image_smoothed`** (output_object)  image(-array) `→` HObject (real)

Smoothed multichannel image.

**`filter`** (input_control)  real-array `→` Sequence[float]

Filter coefficients.

**`border`** (input_control)  string `→` str

Type of boundary treatment.

Default:
"constant"

List of values:
"constant", "mirror"

## Possible Predecessors

`gen_savitzky_golay_filter`

## Module

Foundation
