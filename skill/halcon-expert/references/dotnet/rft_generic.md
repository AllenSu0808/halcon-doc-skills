# RftGeneric (Operator)

## Name

`RftGeneric` — Compute the real-valued fast Fourier transform of an image.

## Signature

`static void HOperatorSet.RftGeneric(HObject image, out HObject imageFFT, HTuple direction, HTuple norm, HTuple resultType, HTuple width)`

`HImage HImage.RftGeneric(string direction, string norm, string resultType, int width)`

## Description

`RftGeneric` computes the fast Fourier transform of the input
image *`image`*. In contrast to [`FftGeneric`](fft_generic.md),
[`FftImage`](fft_image.md), and [`FftImageInv`](fft_image_inv.md), the fact that the
input image in the forward transform is a real-valued image (i.e.,
not a complex image) is used. In this case, the complex output
image has a redundancy. The values in the right half of the image
are the complex conjugates of the corresponding values in the left
half of the image. Consequently, runtime and memory can be saved by
only computing and storing the left half of the complex image.

The parameter *`resultType`* can be used to specify the result
image type of the reverse transform (*`direction`* =
*"from_freq"*). In the forward transform (*`direction`*
= *"to_freq"*), *`resultType`* must be set to
*"complex"*.

The parameter direction determines whether the transform should be
performed to the frequency domain or back into the spatial domain.
For *`direction`* = *"to_freq"* the input image must
have a real-valued type, i.e., a complex image may not be used as
input. All image types that can be converted into an image of type
real are supported. In this case, the output is a complex image of
dimension (w/2+1)*h, where w and h are
the width and height of the input image. In this mode, the exponent
-1 is used in the transform (see [`FftGeneric`](fft_generic.md)). For
*`direction`* = *"from_freq"*, the input image must be
complex. In this case, the size of the input image is insufficient
to determine the size of the output image. This must be done by
setting *`width`* to a valid value, i.e., to 2*w-2
or 2*w-1, where w is the width of the complex image.
In this mode, the exponent 1 is used in the transform.

The normalizing factor can be set with *`norm`*, and can take
on the values *"none"*, *"sqrt"* and *"n"*.
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

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real / complex)

Input image.

**`imageFFT`** (output_object)  image(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real / complex)

Fourier-transformed image.

**`direction`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Calculate forward or reverse transform.

Default:
"to_freq"

List of values:
"from_freq", "to_freq"

**`norm`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Normalizing factor of the transform.

Default:
"sqrt"

List of values:
"n", "none", "sqrt"

**`resultType`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Image type of the output image.

Default:
"complex"

List of values:
"byte", "complex", "cyclic", "direction", "int1", "int2", "int4", "real", "uint2"

**`width`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Width of the image for which the runtime should be
optimized.

Default:
512

Suggested values:
128, 160, 192, 256, 320, 384, 512, 640, 768, 1024, 2048

## Result

`RftGeneric` returns 2 (
H_MSG_TRUE)
if all parameters are correct. If
the input is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`. If necessary,
an exception is raised.

## Possible Predecessors

`OptimizeRftSpeed`,
`ReadFftOptimizationData`

## Possible Successors

`ConvolFft`,
`CorrelationFft`,
`PhaseCorrelationFft`,
`ConvertImageType`,
`PowerByte`,
`PowerReal`,
`PowerLn`,
`PhaseDeg`,
`PhaseRad`

## Alternatives

`FftGeneric`,
`FftImage`,
`FftImageInv`

## Module

Foundation
