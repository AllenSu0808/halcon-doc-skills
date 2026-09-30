# gen_bandfilter (Operator)

## Name

`gen_bandfilter` — Generate an ideal band filter.

## Signature

`def gen_bandfilter(min_frequency: float, max_frequency: float, norm: str, mode: str, width: int, height: int) -> HObject`

## Description

`gen_bandfilter` generates an ideal band filter in the
frequency domain. The parameters *`min_frequency`* and
*`max_frequency`* determine the cutoff frequencies of the filter
as a fraction of the maximum (horizontal and vertical) frequency
that can be represented in an image of size *`width`*
x *`height`*, i.e., *`min_frequency`* and
*`max_frequency`* should lie between 0 and 1. To achieve a
maximum overall efficiency of the filtering operation, the parameter
*`norm`* can be used to specify the normalization factor of the
filter. If [`fft_generic`](fft_generic.md) and *`norm`* = *"n"*
is used the normalization in the FFT can be avoided. *`mode`*
can be used to determine where the DC term of the filter lies or
whether the filter should be used in the real-valued FFT. If
[`fft_generic`](fft_generic.md) is used, *"dc_edge"* can be used to gain
efficiency. If [`fft_image`](fft_image.md) and [`fft_image_inv`](fft_image_inv.md) are used
for filtering, *`norm`* = *"none"* and *`mode`*
= *"dc_center"* must be used. If [`rft_generic`](rft_generic.md) is
used, *`mode`* = *"rft"* must be used. The resulting
image contains an annulus with the value 0, and a value determined
by the normalization outside of this annulus.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image_filter`** (output_object)  image `→` HObject (real)

Band filter in the frequency domain.

**`min_frequency`** (input_control)  real `→` float

Minimum frequency.

Default:
0.1

Suggested values:
0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Restriction:
`MinFrequency >= 0`

**`max_frequency`** (input_control)  real `→` float

Maximum frequency.

Default:
0.2

Suggested values:
0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Restriction:
`MaxFrequency >= 0 && MaxFrequency >= MinFrequency`

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

## Example (HDevelop)

```
* Filtering with maximum efficiency with fft_generic.
gen_bandpass(Bandfilter,0.2,0.4,'n','dc_edge',Width,Height)
fft_generic(Image,ImageFFT,'to_freq',-1,'none','dc_edge','complex')
convol_fft(ImageFFT,Bandfilter,ImageConvol)
fft_generic(ImageConvol,ImageResult,'from_freq',1,'none','dc_edge','byte')
```

## Result

`gen_bandfilter` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Successors

`convol_fft`

## Alternatives

`gen_circle`,
`paint_region`

## See also

`gen_highpass`,
`gen_lowpass`,
`gen_bandpass`,
`gen_gauss_filter`,
`gen_mean_filter`,
`gen_derivative_filter`

## Module

Foundation
