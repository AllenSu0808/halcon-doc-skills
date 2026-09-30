# fft_image_inv (Operator)

## Name

`fft_image_inv` — Compute the inverse fast Fourier transform of an image.

## Signature

`fft_image_inv(Image : ImageFFTInv : : )`

## Description

`fft_image_inv` calculates the inverse Fourier transform of
the input image (*`Image`*), i.e., it transforms the image
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

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (complex)

Input image.

**`ImageFFTInv`** (output_object)  image(-array) `→` object (byte)

Inverse-Fourier-transformed image.

## Result

`fft_image_inv` returns 2 (
H_MSG_TRUE)
if the input image is of correct
type. If the input is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`. If necessary,
an exception is raised.

## Possible Predecessors

`convol_fft`,
`convol_gabor`,
`fft_image`,
`optimize_fft_speed`,
`read_fft_optimization_data`

## Possible Successors

`convert_image_type`,
`energy_gabor`

## Alternatives

`fft_generic`,
`rft_generic`

## See also

`fft_image`,
`fft_generic`,
`energy_gabor`

## Module

Foundation
