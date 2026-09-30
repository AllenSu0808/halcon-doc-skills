# GenGaussFilter (Operator)

## Name

`GenGaussFilter` — Generate a Gaussian filter in the frequency domain.

## Signature

`static void HOperatorSet.GenGaussFilter(out HObject imageGauss, HTuple sigma1, HTuple sigma2, HTuple phi, HTuple norm, HTuple mode, HTuple width, HTuple height)`

`void HImage.GenGaussFilter(double sigma1, double sigma2, double phi, string norm, string mode, int width, int height)`

## Description

`GenGaussFilter` generates a (possibly anisotropic) Gaussian
filter in the frequency domain. The standard deviations (i.e., the
amount of smoothing) of the Gaussian in the spatial domain are
determined by *`sigma1`* and *`sigma2`*. *`sigma1`*
is the standard deviation in the principal direction of the filter
in the spatial domain determined by the angle *`phi`*. To
achieve a maximum overall efficiency of the filtering operation, the
parameter *`norm`* can be used to specify the normalization
factor of the filter. If [`FftGeneric`](fft_generic.md) and *`norm`* =
*"n"* is used the normalization in the FFT can be avoided.
*`mode`* can be used to determine where the DC term of the
filter lies or whether the filter should be used in the real-valued
FFT. If [`FftGeneric`](fft_generic.md) is used, *"dc_edge"* can be used
to gain efficiency. If [`FftImage`](fft_image.md) and [`FftImageInv`](fft_image_inv.md)
are used for filtering, *`norm`* = *"none"* and
*`mode`* = *"dc_center"* must be used. If
[`RftGeneric`](rft_generic.md) is used, *`mode`* = *"rft"* must
be used.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`imageGauss`** (output_object)  image `→` [HImage](HImage.md) (real)

Gaussian filter as image in the frequency domain.

**`sigma1`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Standard deviation of the Gaussian in the
principal direction of the filter in the
spatial domain.

Default:
1.0

Suggested values:
0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0

Restriction:
`Sigma1 >= 0`

**`sigma2`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Standard deviation of the Gaussian perpendicular
to the principal direction of the filter in the
spatial domain.

Default:
1.0

Suggested values:
0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0

Restriction:
`Sigma2 >= 0`

**`phi`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double*)

Principal direction of the filter in the
spatial domain.

Default:
0.0

Suggested values:
0.0, 0.523599, 0.785398, 1.047198, 1.570796, 2.094395, 2.356194, 2.617994, 3.141593

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
* Generate a smoothed derivative filter.
gen_gauss_filter (ImageGauss, Sigma, Sigma, 0, 'n', 'dc_edge', 512, 512)
convert_image_type (ImageGauss, ImageGaussComplex, 'complex')
gen_derivative_filter (ImageDerivX, 'x', 1, 'none', 'dc_edge', 512, 512)
mult_image (ImageGaussComplex, ImageDerivX, ImageDerivXGauss, 1, 0)
* Filter an image with the smoothed derivative filter.
fft_generic (Image, ImageFFT, 'to_freq', -1, 'none', 'dc_edge', 'complex')
convol_fft (ImageFFT, ImageDerivXGauss, Filtered)
fft_generic (Filtered, ImageX, 'from_freq', 1, 'none', 'dc_edge', 'real')
```

## Result

`GenGaussFilter` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If necessary, an exception is raised.

## Possible Predecessors

`FftImage`,
`FftGeneric`,
`RftGeneric`

## Possible Successors

`ConvolFft`

## See also

`FftImageInv`,
`GenMeanFilter`,
`GenDerivativeFilter`,
`GenLowpass`,
`GenBandpass`,
`GenBandfilter`,
`GenHighpass`

## Module

Foundation
