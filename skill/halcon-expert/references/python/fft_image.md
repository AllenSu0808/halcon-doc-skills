# fft_image (Operator)

## Name

`fft_image` — Compute the fast Fourier transform of an image.

## Signature

`def fft_image(image: HObject) -> HObject`

## Description

`fft_image` calculates the Fourier transform of the input
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

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte / real)

Input image.

**`image_fft`** (output_object)  image(-array) `→` HObject (complex)

Fourier-transformed image.

## Result

`fft_image` returns 2 (
H_MSG_TRUE)
if the input image is of correct
type. If the input is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`. If necessary,
an exception is raised.

## Possible Predecessors

`optimize_fft_speed`,
`read_fft_optimization_data`

## Possible Successors

`convol_fft`,
`convol_gabor`,
`convert_image_type`,
`power_byte`,
`power_real`,
`power_ln`,
`phase_deg`,
`phase_rad`

## Alternatives

`fft_generic`,
`rft_generic`

## See also

`fft_image_inv`

## Module

Foundation
