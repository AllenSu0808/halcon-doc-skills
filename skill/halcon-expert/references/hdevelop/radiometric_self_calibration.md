# radiometric_self_calibration (Operator)

## Name

`radiometric_self_calibration` — Perform a radiometric self-calibration of a camera.

## Signature

`radiometric_self_calibration(Images : : ExposureRatios, Features, FunctionType, Smoothness, PolynomialDegree : InverseResponse)`

## Description

`radiometric_self_calibration` performs a radiometric
self-calibration of a camera. For this, at least two images that
show the same image contents (scene) must be passed in
*`Images`*. All images passed in *`Images`* must be
acquired with different exposures. Typically, the different
exposures are obtained by changing the shutter times at the camera.
It is not recommended to change the exposure by changing the aperture
of the lens since in this case the exposures cannot be determined
accurately enough. The ratio of the exposures of consecutive images
is passed in *`ExposureRatios`*. For example, a value of
*0.5* specifies that the second image of an image pair has
been acquired with half the exposure of the first image of the pair.
The exposure ratio can easily be determined from the shutter times
since the exposure is proportional to the shutter time. The
exposure ratio must be greater than 0 and smaller than 1. This
means that the images must be sorted according to descending
exposure. *`ExposureRatios`* must contain one element less
than the number of images passed in *`Images`*. If all
exposure ratios are identical, as a simplification a single value
can be passed in *`ExposureRatios`*.

As described above, the images passed in *`Images`* must show
identical image contents. Hence, it is typically necessary that
neither the camera nor the objects in the scene move. If the camera
has rotated around the optical center, the images should be aligned
to a reference image (one of the images) using
[`proj_match_points_ransac`](proj_match_points_ransac.md) and [`projective_trans_image`](projective_trans_image.md).
If the features used for the radiometric calibration are determined
from the 2D gray value histogram of consecutive image pairs
(*`Features`* = *'2d_histogram'*), it is essential
that the images are aligned and that the objects in the scene do not
move. For *`Features`* = *'1d_histograms'*, the
features used for the radiometric calibration are determined from
the 1D gray value histograms of the image pairs. In this mode, the
calibration can theoretically be performed if the 1D histograms of
the images do not change by the movement of the objects in the
images. This can, for example, be the case if an object moves in
front of a uniformly textured background. However, it is preferable
to use *`Features`* = *'2d_histogram'* because this
mode is more accurate. The mode *`Features`* =
*'1d_histograms'* should only be used if it is impossible to
construct the camera set-up such that neither the camera nor the
objects in the scene move.

Furthermore, care should be taken to cover the range of gray values
without gaps by choosing appropriate image contents. Whether there
are gaps in the range of gray values can easily be checked based on
the 1D gray value histograms of the images or the 2D gray value
histograms of consecutive images. In the 1D gray value histograms
(see [`gray_histo_abs`](gray_histo_abs.md)), there should be no areas between the
minimum and maximum gray value that have a frequency of 0 or a very
small frequency. In the 2D gray value histograms (see
[`histo_2dim`](histo_2dim.md)), a single connected region having the shape of a
“strip” should result from a threshold operation with a lower
threshold of 1. If more than one connected component results, a
more suitable image content should be chosen. If the image content
can be chosen such that the gray value range of the image (e.g.,
0-255 for byte images) can be covered with two images with different
exposures, and if there are no gaps in the histograms, the two
images suffice for the calibration. This, however, is typically not
the case, and hence multiple images must be used to cover the entire
gray value range. As described above, for this multiple images with
different exposures must be taken to cover the entire gray value
range as well as possible. For this, normally the first image
should be exposed such that the maximum gray value is slightly below
the saturation limit of the camera, or such that the image is
significantly overexposed. If the first image is overexposed, a
significant overexposure is necessary to enable
`radiometric_self_calibration` to detect the overexposed areas
reliably. If the camera exhibits an unusual saturation behavior
(e.g., a saturation limit that lies significantly below the maximum
gray value) the overexposed areas should be masked out by hand with
[`reduce_domain`](reduce_domain.md) in the overexposed image.

`radiometric_self_calibration` returns the inverse gray value
response function of the camera in *`InverseResponse`*. The
inverse response function can be used to create an image with a
linear response by using *`InverseResponse`* as the LUT in
[`lut_trans`](lut_trans.md). The parameter *`FunctionType`* determines
which function model is used to model the response function. For
*`FunctionType`* = *'discrete'*, the response function
is described by a discrete function with the relevant number of gray
values (256 for byte images). For *`FunctionType`* =
*'polynomial'*, the response is described by a polynomial of
degree *`PolynomialDegree`*. The computation of the response
function is slower for *`FunctionType`* =
*'discrete'*. However, since a polynomial tends to
oscillate in the areas in which no gray value information can be
derived, even if smoothness constraints are imposed as described
below, the discrete model should usually be preferred over the
polynomial model.

The inverse response function is returned as a tuple of integer
values for *`FunctionType`* = *'discrete'* and
*`FunctionType`* = *'polynomial'*. In some
applications, it might be desirable to return the inverse response
function as floating point values to avoid the numerical error that
is introduced by rounding. For example, if the inverse response
function must be inverted to obtain the response function of the
camera, there is some loss of information if the values are returned
as integers. For these applications, *`FunctionType`* can be
set to *'discrete_real'* or *'polynomial_real'*, in
which case the inverse response function will be returned as a tuple
of floating point numbers.

The parameter *`Smoothness`* defines (in addition to the
constraints on the response function that can be derived from the
images) constraints on the smoothness of the response function. If,
as described above, the gray value range can be covered completely
and without gaps, the default value of *1* should not be
changed. Otherwise, values > *1* can be used to obtain a
stronger smoothing of the response function, while values <
*1* lead to a weaker smoothing. The smoothing is
particularly important in areas for which no gray value information
can be derived from the images, i.e., in gaps in the histograms and
for gray values smaller than the minimum gray value of all images or
larger than the maximum gray value of all images. In these areas,
the smoothness constraints lead to an interpolation or extrapolation
of the response function. Because of the nature of the internally
derived constraints, *`FunctionType`* = *'discrete'*
favors an exponential function in the undefined areas, whereas
*`FunctionType`* = *'polynomial'* favors a straight
line. Please note that the interpolation and extrapolation is
always less reliable than to cover the gray value range completely
and without gaps. Therefore, in any case it should be attempted
first to acquire the images optimally, before the smoothness
constraints are used to fill in the remaining gaps. In all cases,
the response function should be checked for plausibility after the
call to `radiometric_self_calibration`. In particular, it
should be checked whether *`InverseResponse`* is monotonic. If
this is not the case, a more suitable scene should be used to avoid
interpolation, or *`Smoothness`* should be set to a larger
value. For *`FunctionType`* = *'polynomial'*, it may
also be necessary to change *`PolynomialDegree`*. If, despite
these changes, an implausible response is returned, the saturation
behavior of the camera should be checked, e.g., based on the 2D gray
value histogram, and the saturated areas should be masked out by
hand, as described above.

When the inverse gray value response function of the camera is
determined, the absolute energy falling on the camera cannot be
determined. This means that *`InverseResponse`* can only be
determined up to a scale factor. Therefore, an additional
constraint is used to fix the unknown scale factor: the maximum gray
value that can occur should occur for the maximum input gray value,
e.g., *`InverseResponse`*[255] = 255 for byte images. This
constraint usually leads to the most intuitive results. If,
however, a multichannel image (typically an RGB image) should be
radiometrically calibrated (for this, each channel must be
calibrated separately), the above constraint may lead to the result
that a different scaling factor is determined for each channel.
This may lead to the result that gray tones no longer appear gray
after the correction. In this case, a manual white balancing step
must be carried out by identifying a homogeneous gray area in the
original image, and by deriving appropriate scaling factors from the
corrected gray values for two of the three response curves (or, in
general, for n-1 of the n channels). Here, the response curve
that remains invariant should be chosen such that all scaling
factors are < 1. With the scaling factors thus determined, new
response functions should be calculated by multiplying each value of
a response function with the scaling factor corresponding to that
response function.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Images`** (input_object)  singlechannelimage-array `→` object (byte / uint2)

Input images.

**`ExposureRatios`** (input_control)  real(-array) `→`  (real)

Ratio of the exposure energies of successive
image pairs.

Default:
0.5

Suggested values:
0.25, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8

Restriction:
`ExposureRatios > 0 && ExposureRatios < 1`

**`Features`** (input_control)  string `→`  (string)

Features that are used to compute the inverse
response function of the camera.

Default:
'2d_histogram'

List of values:
'1d_histograms', '2d_histogram'

**`FunctionType`** (input_control)  string `→`  (string)

Type of the inverse response function of the
camera.

Default:
'discrete'

List of values:
'discrete', 'discrete_real', 'polynomial', 'polynomial_real'

**`Smoothness`** (input_control)  real `→`  (real)

Smoothness of the inverse response function of
the camera.

Default:
1.0

Suggested values:
0.3, 0.5, 0.7, 0.8, 1.0, 1.2, 1.5, 2.0, 3.0

Restriction:
`Smoothness > 0`

**`PolynomialDegree`** (input_control)  integer `→`  (integer)

Degree of the polynomial if
*`FunctionType`* = *'polynomial'*.

Default:
5

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10

Restriction:
`PolynomialDegree >= 1 && PolynomialDegree <= 20`

**`InverseResponse`** (output_control)  number-array `→`  (integer / real)

Inverse response function of the camera.

## Example (HDevelop)

```
open_framegrabber ('1394IIDC', 1, 1, 0, 0, 0, 0, 'default', -1, \
                   'default', -1, 'default', 'default', 'default', \
                   -1, -1, AcqHandle)
* Define appropriate shutter times.
Shutters := [1000,750,500,250,125]
Num := |Shutters|
* Grab and accumulate images with the different exposures.  In this
* loop, it must be ensured that the scene remains static.
gen_empty_obj (Images)
for I := 0 to Num-1 by 1
    set_framegrabber_param (AcqHandle, 'shutter', Shutters[I])
    grab_image (Image, AcqHandle)
    concat_obj (Images, Image, Images)
endfor
* Compute the exposure ratios from the shutter times.
ExposureRatios := real(Shutters[1:Num-1])/real(Shutters[0:Num-2])
radiometric_self_calibration (Images, ExposureRatios, '2d_histogram', \
                              'discrete', 1, 5, InverseResponse)
* Note that if the frame grabber supports hardware LUTs, we could
* also call set_framegrabber_lut here instead of lut_trans below.
* This would be more efficient.
while (1)
    grab_image_async (Image, AcqHandle, -1)
    lut_trans (Image, ImageLinear, InverseResponse)
    * Process radiometrically correct image.
    * [...]
endwhile
close_framegrabber (AcqHandle)
```

## Result

If the parameters are valid, the operator
`radiometric_self_calibration` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`read_image`,
`grab_image`,
`grab_image_async`,
`set_framegrabber_param`,
`concat_obj`,
`proj_match_points_ransac`,
`proj_match_points_ransac_guided`,
`projective_trans_image`

## Possible Successors

`lut_trans`

## See also

`histo_2dim`,
`gray_histo`,
`gray_histo_abs`,
`reduce_domain`

## Module

Calibration
