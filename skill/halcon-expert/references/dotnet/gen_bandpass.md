# GenBandpass (Operator)

## Name

`GenBandpass` — Generate an ideal bandpass filter.

## Signature

`static void HOperatorSet.GenBandpass(out HObject imageBandpass, HTuple minFrequency, HTuple maxFrequency, HTuple norm, HTuple mode, HTuple width, HTuple height)`

`void HImage.GenBandpass(double minFrequency, double maxFrequency, string norm, string mode, int width, int height)`

## Description

`GenBandpass` generates an ideal bandpass filter in the
frequency domain. The parameters *`minFrequency`* and
*`maxFrequency`* determine the cutoff frequencies of the filter
as a fraction of the maximum (horizontal and vertical) frequency
that can be represented in an image of size *`width`*
x *`height`*, i.e., *`minFrequency`* and
*`maxFrequency`* should lie between 0 and 1. To achieve a
maximum overall efficiency of the filtering operation, the parameter
*`norm`* can be used to specify the normalization factor of the
filter. If [`FftGeneric`](fft_generic.md) and *`norm`* = *"n"*
is used the normalization in the FFT can be avoided. *`mode`*
can be used to determine where the DC term of the filter lies or
whether the filter should be used in the real-valued FFT. If
[`FftGeneric`](fft_generic.md) is used, *"dc_edge"* can be used to gain
efficiency. If [`FftImage`](fft_image.md) and [`FftImageInv`](fft_image_inv.md) are used
for filtering, *`norm`* = *"none"* and *`mode`*
= *"dc_center"* must be used. If [`RftGeneric`](rft_generic.md) is
used, *`mode`* = *"rft"* must be used. The resulting
image contains an annulus with the value 255, and the value 0
outside of this annulus.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`imageBandpass`** (output_object)  image `→` [HImage](HImage.md) (real)

Bandpass filter in the frequency domain.

**`minFrequency`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Minimum frequency.

Default:
0.1

Suggested values:
0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Restriction:
`MinFrequency >= 0`

**`maxFrequency`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Maximum frequency.

Default:
0.2

Suggested values:
0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Restriction:
`MaxFrequency >= 0 && MaxFrequency >= MinFrequency`

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

## Example (HDevelop)

```
* Filtering with maximum efficiency with fft_generic.
gen_bandpass(Bandpass,0.2,0.4,'n','dc_edge',Width,Height)
fft_generic(Image,ImageFFT,'to_freq',-1,'none','dc_edge','complex')
convol_fft(ImageFFT,Bandpass,ImageConvol)
fft_generic(ImageConvol,ImageResult,'from_freq',1,'none','dc_edge','byte')
```

## Result

`GenBandpass` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If necessary, an exception is raised.

## Possible Successors

`ConvolFft`

## See also

`GenHighpass`,
`GenLowpass`,
`GenBandfilter`,
`GenGaussFilter`,
`GenMeanFilter`,
`GenDerivativeFilter`

## Module

Foundation
