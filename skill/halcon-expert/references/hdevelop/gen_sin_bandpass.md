# gen_sin_bandpass (Operator)

## Name

`gen_sin_bandpass` — Generate a bandpass filter with sinusoidal shape.

## Signature

`gen_sin_bandpass( : ImageFilter : Frequency, Norm, Mode, Width, Height : )`

## Description

`gen_sin_bandpass` generates a rotationally invariant bandpass
filter with the response being a sinusoidal function in the
frequency domain. The maximum of the sine is determined by
*`Frequency`*, which is given as a fraction of the maximum
(horizontal and vertical) frequency that can be represented in an
image of size *`Width`* x *`Height`*, i.e.,
*`Frequency`* should lie between 0 and 1. To achieve a maximum
overall efficiency of the filtering operation, the parameter
*`Norm`* can be used to specify the normalization factor of the
filter. If [`fft_generic`](fft_generic.md) and *`Norm`* = *'n'*
is used the normalization in the FFT can be avoided. *`Mode`*
can be used to determine where the DC term of the filter lies or
whether the filter should be used in the real-valued FFT. If
[`fft_generic`](fft_generic.md) is used, *'dc_edge'* can be used to gain
efficiency. If [`fft_image`](fft_image.md) and [`fft_image_inv`](fft_image_inv.md) are used
for filtering, *`Norm`* = *'none'* and *`Mode`*
= *'dc_center'* must be used. If [`rft_generic`](rft_generic.md) is
used, *`Mode`* = *'rft'* must be used. The filter is
always zero for the DC term, rises with the sine function up to
*`Frequency`*, and drops for higher frequencies accordingly.
The range of the sine used is from 0 to $\pi$. All other
points are set to zero.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ImageFilter`** (output_object)  image `→` object (real)

Bandpass filter as image in the frequency domain.

**`Frequency`** (input_control)  real `→`  (real)

Distance of the filter's maximum from the DC term.

Default:
0.1

Suggested values:
0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Restriction:
`Frequency >= 0`

**`Norm`** (input_control)  string `→`  (string)

Normalizing factor of the filter.

Default:
'none'

List of values:
'n', 'none'

**`Mode`** (input_control)  string `→`  (string)

Location of the DC term in the frequency domain.

Default:
'dc_center'

List of values:
'dc_center', 'dc_edge', 'rft'

**`Width`** (input_control)  integer `→`  (integer)

Width of the image (filter).

Default:
512

Suggested values:
128, 160, 192, 256, 320, 384, 512, 640, 768, 1024, 2048, 4096, 8192

**`Height`** (input_control)  integer `→`  (integer)

Height of the image (filter).

Default:
512

Suggested values:
120, 128, 144, 240, 256, 288, 480, 512, 576, 1024, 2048, 4096, 8192

## Result

`gen_sin_bandpass` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If necessary, an exception is raised.

## Possible Predecessors

`fft_image`,
`fft_generic`,
`rft_generic`

## Possible Successors

`convol_fft`

## Alternatives

`gen_std_bandpass`

## See also

`fft_image_inv`,
`gen_gauss_filter`,
`gen_mean_filter`,
`gen_derivative_filter`,
`gen_bandpass`,
`gen_bandfilter`,
`gen_highpass`,
`gen_lowpass`

## Module

Foundation
