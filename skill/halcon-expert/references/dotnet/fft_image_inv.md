# FftImageInv (Operator)

## Name

`FftImageInv` — Compute the inverse fast Fourier transform of an image.

## Signature

`static void HOperatorSet.FftImageInv(HObject image, out HObject imageFFTInv)`

`HImage HImage.FftImageInv()`

## Description

`FftImageInv` calculates the inverse Fourier transform of
the input image (*`image`*), i.e., it transforms the image
back into the spatial domain. This corresponds to the call
`fft_generic(Image, ImageFFT, 'from_freq', 1, 'sqrt', 'dc_center', 'byte')`.

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

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (complex)

Input image.

**`imageFFTInv`** (output_object)  image(-array) `→` [HImage](HImage.md) (byte)

Inverse-Fourier-transformed image.

## Result

`FftImageInv` returns 2 (
H_MSG_TRUE)
if the input image is of correct
type. If the input is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`. If necessary,
an exception is raised.

## Possible Predecessors

`ConvolFft`,
`ConvolGabor`,
`FftImage`,
`OptimizeFftSpeed`,
`ReadFftOptimizationData`

## Possible Successors

`ConvertImageType`,
`EnergyGabor`

## Alternatives

`FftGeneric`,
`RftGeneric`

## See also

`FftImage`,
`FftGeneric`,
`EnergyGabor`

## Module

Foundation
