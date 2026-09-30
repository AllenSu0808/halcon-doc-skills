# gen_mean_filter (Operator)

## Name

`gen_mean_filter` — Generate a mean filter in the frequency domain.

## Signature

`def gen_mean_filter(mask_shape: str, diameter_1: float, diameter_2: float, phi: float, norm: str, mode: str, width: int, height: int) -> HObject`

## Description

`gen_mean_filter` generates a mean filter in the frequency
domain. The shape of the mean filter is determined by
*`mask_shape`*. For *`mask_shape`* =
*"rectangle"*, a rectangular mean filter is generated. For
*`mask_shape`* = *"ellipse"*, an elliptical mean filter
is generated. The diameters (i.e., the amount of smoothing) of the
mean filter in the spatial domain are determined by
*`diameter_1`* and *`diameter_2`*. *`diameter_1`* is
the diameter in the principal direction of the filter in the spatial
domain determined by the angle *`phi`*. To achieve a maximum
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
used, *`mode`* = *"rft"* must be used.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image_mean`** (output_object)  image `→` HObject (real)

Mean filter as image in the frequency domain.

**`mask_shape`** (input_control)  string `→` str

Shape of the filter mask in the spatial domain.

Default:
"ellipse"

List of values:
"ellipse", "rectangle"

**`diameter_1`** (input_control)  real `→` float

Diameter of the mean filter in the principal
direction of the filter in the spatial domain.

Default:
11.0

Suggested values:
3.0, 5.0, 7.0, 9.0, 11.0, 15.0, 21.0, 31.0, 51.0

Restriction:
`Diameter1 > 0`

**`diameter_2`** (input_control)  real `→` float

Diameter of the mean filter perpendicular to
the principal direction of the filter in the
spatial domain.

Default:
11.0

Suggested values:
3.0, 5.0, 7.0, 9.0, 11.0, 15.0, 21.0, 31.0, 51.0

Restriction:
`Diameter2 > 0`

**`phi`** (input_control)  angle.rad `→` float

Principal direction of the filter in the
spatial domain.

Default:
0.0

Suggested values:
0.0, 0.523599, 0.785398, 1.047198, 1.570796, 2.094395, 2.356194, 2.617994, 3.141593

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
* Generate a circular mean filter.
gen_mean_filter (FilterMean, 'ellipse', 15, 15, 0, 'n', 'dc_edge', 512, 512)
* Filter an image with the circular mean filter.
fft_generic (Image, ImageFFT, 'to_freq', -1, 'none', 'dc_edge', 'complex')
convol_fft (ImageFFT, FilterMean, Filtered)
fft_generic (Filtered, ImageMean, 'from_freq', 1, 'none', 'dc_edge', 'real')
```

## Result

`gen_mean_filter` returns 2 (
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
`gen_gauss_filter`,
`gen_derivative_filter`,
`gen_lowpass`,
`gen_bandpass`,
`gen_bandfilter`,
`gen_highpass`

## Module

Foundation
