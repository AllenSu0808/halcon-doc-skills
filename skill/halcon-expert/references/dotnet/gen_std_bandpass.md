# GenStdBandpass (Operator)

## Name

`GenStdBandpass` — Generate a bandpass filter with Gaussian or sinusoidal shape.

## Signature

`static void HOperatorSet.GenStdBandpass(out HObject imageFilter, HTuple frequency, HTuple sigma, HTuple type, HTuple norm, HTuple mode, HTuple width, HTuple height)`

`void HImage.GenStdBandpass(double frequency, double sigma, string type, string norm, string mode, int width, int height)`

## Description

`GenStdBandpass` generates a rotationally invariant bandpass
filter with the response being determined by the parameters
*`frequency`* and *`sigma`*: *`frequency`* determines
the location of the maximum response with respect to the DC term,
while *`sigma`* determines the width of the frequency band that
passes the filter. *`frequency`* and *`sigma`* are
specified as a fraction of the maximum (horizontal and vertical)
frequency that can be represented in an image of size *`width`*
x *`height`*. *`frequency`* should lie
between 0 and 1. For *`type`* = *"gauss"*, a Gaussian
response is generated with *`sigma`* being the standard
deviation. For *`type`* = *"sin"*, a sine function is
generated with the maximum at *`frequency`* and the extent
*`sigma`*. To achieve a maximum overall efficiency of the
filtering operation, the parameter *`norm`* can be used to
specify the normalization factor of the filter. If
[`FftGeneric`](fft_generic.md) and *`norm`* = *"n"* is used the
normalization in the FFT can be avoided. *`mode`* can be used
to determine where the DC term of the filter lies or whether the
filter should be used in the real-valued FFT. If
[`FftGeneric`](fft_generic.md) is used, *"dc_edge"* can be used to gain
efficiency. If [`FftImage`](fft_image.md) and [`FftImageInv`](fft_image_inv.md) are used
for filtering, *`norm`* = *"none"* and *`mode`*
= *"dc_center"* must be used. If [`RftGeneric`](rft_generic.md) is
used, *`mode`* = *"rft"* must be used.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`imageFilter`** (output_object)  image `→` [HImage](HImage.md) (real)

Bandpass filter as image in the frequency domain.

**`frequency`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Distance of the filter's maximum from the DC term.

Default:
0.1

Suggested values:
0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Restriction:
`Frequency >= 0`

**`sigma`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Bandwidth of the filter (standard deviation).

Default:
0.01

Suggested values:
0.002, 0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.7, 1.0

Restriction:
`Sigma >= 0`

**`type`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Filter type.

Default:
"sin"

List of values:
"gauss", "sin"

**`norm`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Normalizing factor of the filter.

Default:
"none"

List of values:
"n", "none"

**`mode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Location of the DC term in the frequency domain.

Default:
"dc_center"

List of values:
"dc_center", "dc_edge", "rft"

**`width`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Width of the image (filter).

Default:
512

Suggested values:
128, 160, 192, 256, 320, 384, 512, 640, 768, 1024, 2048, 4096, 8192

**`height`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Height of the image (filter).

Default:
512

Suggested values:
120, 128, 144, 240, 256, 288, 480, 512, 576, 1024, 2048, 4096, 8192

## Result

`GenStdBandpass` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If necessary, an exception is raised.

## Possible Predecessors

`FftImage`,
`FftGeneric`,
`RftGeneric`

## Possible Successors

`ConvolFft`

## Alternatives

`GenSinBandpass`

## See also

`FftImageInv`,
`GenGaussFilter`,
`GenMeanFilter`,
`GenDerivativeFilter`,
`GenBandpass`,
`GenBandfilter`,
`GenHighpass`,
`GenLowpass`

## Module

Foundation
