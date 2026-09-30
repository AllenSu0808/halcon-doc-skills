# FftImage (Operator)

## Name

`FftImage` — Compute the fast Fourier transform of an image.

## Signature

`static void HOperatorSet.FftImage(HObject image, out HObject imageFFT)`

`HImage HImage.FftImage()`

## Description

`FftImage` calculates the Fourier transform of the input
image (*`image`*), i.e., it transforms the image into the
frequency domain. The algorithm used is the fast Fourier transform.
This corresponds to the call
`fft_generic(Image,ImageFFT,'to_freq',-1,'sqrt','dc_center','complex')`.

## Attention

The transformation is always performed for the entire image, i.e., the
domain of the image is ignored.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on internal data level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / real)

Input image.

**`imageFFT`** (output_object)  image(-array) `→` [HImage](HImage.md) (complex)

Fourier-transformed image.

## Result

`FftImage` returns 2 (
H_MSG_TRUE)
if the input image is of correct
type. If the input is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`. If necessary,
an exception is raised.

## Possible Predecessors

`OptimizeFftSpeed`,
`ReadFftOptimizationData`

## Possible Successors

`ConvolFft`,
`ConvolGabor`,
`ConvertImageType`,
`PowerByte`,
`PowerReal`,
`PowerLn`,
`PhaseDeg`,
`PhaseRad`

## Alternatives

`FftGeneric`,
`RftGeneric`

## See also

`FftImageInv`

## Module

Foundation
