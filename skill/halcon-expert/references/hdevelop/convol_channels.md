# convol_channels (Operator)

## Name

`convol_channels` — Perform a convolution along the channel dimension.

## Signature

`convol_channels(MultichannelImage : ImageSmoothed : Filter, Border : )`

## Description

`convol_channels` applies the linear filter *`Filter`* along the
channel dimension of the multichannel image *`MultichannelImage`* and
stores the result in *`ImageSmoothed`*.
Each pixel is processed independently.
Border handling along the channel dimension is specified by *`Border`*
and either continues the current value (*'constant'*) or mirrors
the values (*'mirror'*).

This operator can be used, for example, to smooth hyperspectral
images across spectra.
Filter parameters can be generated, for instance, with
[`gen_savitzky_golay_filter`](gen_savitzky_golay_filter.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on domain level.

## Parameters

**`MultichannelImage`** (input_object)  multichannel-image(-array) `→` object (byte / uint2 / real)

Multichannel image to be smoothed.

**`ImageSmoothed`** (output_object)  image(-array) `→` object (real)

Smoothed multichannel image.

**`Filter`** (input_control)  real-array `→`  (real)

Filter coefficients.

**`Border`** (input_control)  string `→`  (string)

Type of boundary treatment.

Default:
'constant'

List of values:
'constant', 'mirror'

## Possible Predecessors

`gen_savitzky_golay_filter`

## Module

Foundation
