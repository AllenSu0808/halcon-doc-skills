# rft_generic (Operator)

## Name

`rft_generic` — Compute the real-valued fast Fourier transform of an image.

## Signature

`rft_generic(Image : ImageFFT : Direction, Norm, ResultType, Width : )`

## Description

`rft_generic` computes the fast Fourier transform of the input
image *`Image`*. In contrast to [`fft_generic`](fft_generic.md),
[`fft_image`](fft_image.md), and [`fft_image_inv`](fft_image_inv.md), the fact that the
input image in the forward transform is a real-valued image (i.e.,
not a complex image) is used. In this case, the complex output
image has a redundancy. The values in the right half of the image
are the complex conjugates of the corresponding values in the left
half of the image. Consequently, runtime and memory can be saved by
only computing and storing the left half of the complex image.

The parameter *`ResultType`* can be used to specify the result
image type of the reverse transform (*`Direction`* =
*'from_freq'*). In the forward transform (*`Direction`*
= *'to_freq'*), *`ResultType`* must be set to
*'complex'*.

The parameter direction determines whether the transform should be
performed to the frequency domain or back into the spatial domain.
For *`Direction`* = *'to_freq'* the input image must
have a real-valued type, i.e., a complex image may not be used as
input. All image types that can be converted into an image of type
real are supported. In this case, the output is a complex image of
dimension (w/2+1)*h, where w and h are
the width and height of the input image. In this mode, the exponent
-1 is used in the transform (see [`fft_generic`](fft_generic.md)). For
*`Direction`* = *'from_freq'*, the input image must be
complex. In this case, the size of the input image is insufficient
to determine the size of the output image. This must be done by
setting *`Width`* to a valid value, i.e., to 2*w-2
or 2*w-1, where w is the width of the complex image.
In this mode, the exponent 1 is used in the transform.

The normalizing factor can be set with *`Norm`*, and can take
on the values *'none'*, *'sqrt'* and *'n'*.
The user must ensure the consistent use of the parameters. This
means that the normalizing factors used for the forward and backward
transform must yield w*h when multiplied.

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

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real / complex)

Input image.

**`ImageFFT`** (output_object)  image(-array) `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real / complex)

Fourier-transformed image.

**`Direction`** (input_control)  string `→`  (string)

Calculate forward or reverse transform.

Default:
'to_freq'

List of values:
'from_freq', 'to_freq'

**`Norm`** (input_control)  string `→`  (string)

Normalizing factor of the transform.

Default:
'sqrt'

List of values:
'n', 'none', 'sqrt'

**`ResultType`** (input_control)  string `→`  (string)

Image type of the output image.

Default:
'complex'

List of values:
'byte', 'complex', 'cyclic', 'direction', 'int1', 'int2', 'int4', 'real', 'uint2'

**`Width`** (input_control)  integer `→`  (integer)

Width of the image for which the runtime should be
optimized.

Default:
512

Suggested values:
128, 160, 192, 256, 320, 384, 512, 640, 768, 1024, 2048

## Result

`rft_generic` returns 2 (
H_MSG_TRUE)
if all parameters are correct. If
the input is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`. If necessary,
an exception is raised.

## Possible Predecessors

`optimize_rft_speed`,
`read_fft_optimization_data`

## Possible Successors

`convol_fft`,
`correlation_fft`,
`phase_correlation_fft`,
`convert_image_type`,
`power_byte`,
`power_real`,
`power_ln`,
`phase_deg`,
`phase_rad`

## Alternatives

`fft_generic`,
`fft_image`,
`fft_image_inv`

## Module

Foundation
