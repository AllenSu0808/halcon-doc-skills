# gen_sin_bandpass (Operator)

## Name

`gen_sin_bandpass` — Generate a bandpass filter with sinusoidal shape.

## Signature

`def gen_sin_bandpass(frequency: float, norm: str, mode: str, width: int, height: int) -> HObject`

## Description

`gen_sin_bandpass` generates a rotationally invariant bandpass
filter with the response being a sinusoidal function in the
frequency domain. The maximum of the sine is determined by
*`frequency`*, which is given as a fraction of the maximum
(horizontal and vertical) frequency that can be represented in an
image of size *`width`* x *`height`*, i.e.,
*`frequency`* should lie between 0 and 1. To achieve a maximum
overall efficiency of the filtering operation, the parameter
*`norm`* can be used to specify the normalization factor of the
filter. If [`fft_generic`](fft_generic.md) and *`norm`* = *"n"*
is used the normalization in the FFT can be avoided. *`mode`*
can be used to determine where the DC term of the filter lies or
whether the filter should be used in the real-valued FFT. If
[`fft_generic`](fft_generic.md) is used, *"dc_edge"* can be used to gain
efficiency. If [`fft_image`](fft_image.md) and [`fft_image_inv`](fft_image_inv.md) are used
for filtering, *`norm`* = *"none"* and *`mode`*
= *"dc_center"* must be used. If [`rft_generic`](rft_generic.md) is
used, *`mode`* = *"rft"* must be used. The filter is
always zero for the DC term, rises with the sine function up to
*`frequency`*, and drops for higher frequencies accordingly.
The range of the sine used is from 0 to $\pi$. All other
points are set to zero.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image_filter`** (output_object)  image `→` HObject (real)

Bandpass filter as image in the frequency domain.

**`frequency`** (input_control)  real `→` float

Distance of the filter's maximum from the DC term.

Default:
0.1

Suggested values:
0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Restriction:
`Frequency >= 0`

**`norm`** (input_control)  string `→` str

Normalizing factor of the filter.

Default:
"none"

List of values:
"n", "none"

**`mode`** (input_control)  string `→` str

Location of the DC term in the frequency domain.

Default:
"dc_center"

List of values:
"dc_center", "dc_edge", "rft"

**`width`** (input_control)  integer `→` int

Width of the image (filter).

Default:
512

Suggested values:
128, 160, 192, 256, 320, 384, 512, 640, 768, 1024, 2048, 4096, 8192

**`height`** (input_control)  integer `→` int

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
