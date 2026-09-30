# gen_gauss_filter (Operator)

## Name

`gen_gauss_filter` — Generate a Gaussian filter in the frequency domain.

## Signature

`gen_gauss_filter( : ImageGauss : Sigma1, Sigma2, Phi, Norm, Mode, Width, Height : )`

## Description

`gen_gauss_filter` generates a (possibly anisotropic) Gaussian
filter in the frequency domain. The standard deviations (i.e., the
amount of smoothing) of the Gaussian in the spatial domain are
determined by *`Sigma1`* and *`Sigma2`*. *`Sigma1`*
is the standard deviation in the principal direction of the filter
in the spatial domain determined by the angle *`Phi`*. To
achieve a maximum overall efficiency of the filtering operation, the
parameter *`Norm`* can be used to specify the normalization
factor of the filter. If [`fft_generic`](fft_generic.md) and *`Norm`* =
*'n'* is used the normalization in the FFT can be avoided.
*`Mode`* can be used to determine where the DC term of the
filter lies or whether the filter should be used in the real-valued
FFT. If [`fft_generic`](fft_generic.md) is used, *'dc_edge'* can be used
to gain efficiency. If [`fft_image`](fft_image.md) and [`fft_image_inv`](fft_image_inv.md)
are used for filtering, *`Norm`* = *'none'* and
*`Mode`* = *'dc_center'* must be used. If
[`rft_generic`](rft_generic.md) is used, *`Mode`* = *'rft'* must
be used.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ImageGauss`** (output_object)  image `→` object (real)

Gaussian filter as image in the frequency domain.

**`Sigma1`** (input_control)  real `→`  (real)

Standard deviation of the Gaussian in the
principal direction of the filter in the
spatial domain.

Default:
1.0

Suggested values:
0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0

Restriction:
`Sigma1 >= 0`

**`Sigma2`** (input_control)  real `→`  (real)

Standard deviation of the Gaussian perpendicular
to the principal direction of the filter in the
spatial domain.

Default:
1.0

Suggested values:
0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0

Restriction:
`Sigma2 >= 0`

**`Phi`** (input_control)  angle.rad `→`  (real)

Principal direction of the filter in the
spatial domain.

Default:
0.0

Suggested values:
0.0, 0.523599, 0.785398, 1.047198, 1.570796, 2.094395, 2.356194, 2.617994, 3.141593

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

`gen_gauss_filter` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If necessary, an exception is raised.

## Possible Predecessors

`fft_image`,
`fft_generic`,
`rft_generic`

## Possible Successors

`convol_fft`

## See also

`fft_image_inv`,
`gen_mean_filter`,
`gen_derivative_filter`,
`gen_lowpass`,
`gen_bandpass`,
`gen_bandfilter`,
`gen_highpass`

## Module

Foundation
