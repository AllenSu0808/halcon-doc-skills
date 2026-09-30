# adjust_mosaic_images (Operator)

## Name

`adjust_mosaic_images` — Apply an automatic color correction to panorama images.

## Signature

`adjust_mosaic_images(Images : CorrectedImages : From, To, ReferenceImage, HomMatrices2D, EstimationMethod, EstimateParameters, OECFModel : )`

## Description

`adjust_mosaic_images` performs the radiometric adjustment of images
in panoramas. The images to be corrected have to be passed in
*`Images`*, the corrected images will be returned in
*`CorrectedImages`*.

The parameters *`From`* and *`To`* must contain the source and
destination indices of all image pairs in the panorama. The projective
3x3-matrix of each image pair has to be passed in *`HomMatrices2D`*.
The image, which will be used as the reference for brightness and
white balance, is selected with the parameter *`ReferenceImage`*.

This means, that one image specifies the "ideal" brightness and white
balance settings. All other images will be corrected such that their
brightness and white balance match that of the reference image. In other
words, the reference image will not be changed, but all other images will
be.

*`EstimationMethod`* is used for choosing whether a fast but less
accurate, or a slower but more accurate determination method should be used.
This is done by setting *`EstimationMethod`* either to
*'standard'* or *'gold_standard'*.

The methods based on *'standard'* use only the average gray value
difference of all images in the overlap area between each image pair. With
*'gold_standard'* the gray value difference for each pixel in the
overlap area is taken into account explicitly.

The error function that is minimized in all cases is computed as the summed
square of the difference between the corresponding gray values.

The availability of the individual method is depending on the selected
*`EstimateParameters`*, which determines the model to be used for
estimating the radiometric adjustment terms. It is always possible to
determine the amount of vignetting in the images by selecting
*'vignetting'*. However, if selected, *`EstimationMethod`* must
be set to *'gold_standard'*. For the remainder of the radiometric
adjustment three different options are available:

Estimation of vignetting in images is based on the commonly known $$\cos^{4}Alpha$$
approach. This approach assumes that vignetting does not exist in the
center of the image and increases with the opening angle by the above
equation.

1. Image adjustment with the additive model. This should only be used to
adjust images with very small differences in exposure or white balance. To
choose this method, *`EstimateParameters`* must be set to
*'add_gray'*. This model can be selected either exclusively and only
with *`EstimationMethod`* = *'standard'* or in combination with
*`EstimateParameters`* = *'vignetting'* and only with
*`EstimationMethod`* = *'gold_standard'*.

This model is based on the assumption, that the gray value differences
between the images can be corrected by adding an individual value to each
image accept the reference image. Basically, the modification to every
image can be expressed as a call of [`scale_image`](scale_image.md):

|  |
| --- |
| `scale_image(Image_n,CorrectedImage_n,1.0,Add_n)` |

where `Add_n` is the correction term for this image.

2. Image adjustment with the linear model. In this model, images are
expected to be taken with a camera using a linear transfer function. The
adjustment terms are consequently represented as multiplication factors.
To select this model, *`EstimateParameters`* must be set to
*'mult_gray'*. It can be called with
*`EstimationMethod`* = *'standard'* or
*`EstimationMethod`* = *'gold_standard'*. A combined call with
*`EstimateParameters`* = *'vignetting'* is also possible,
*`EstimationMethod`* must be set to *'gold_standard'* in that
case.

This model is based on the assumption that the gray value differences
between the images can be corrected by multiplying the gray values in each
image by a factor. Basically, the modification to every image can again be
expressed as a call of [`scale_image`](scale_image.md):

|  |
| --- |
| `scale_image(Image_n,CorrectedImage_n,Mult_n,0)` |

where `Mult_n` is the correction term for this image.

3. Image adjustment with the calibrated model. In this model, images are
assumed to be taken with a camera using a nonlinear transfer function.
A function of the OECF class selected with *`OECFModel`* is used to
approximate the actually used OECF in the process of image acquisition. As
with the linear model, the correction terms are represented as
multiplication factors. This model can be selected by choosing
*`EstimateParameters`* = *['mult_gray','response']* and must be
called with *`EstimationMethod`* = *'gold_standard'*. It is
possible to determine the amount of vignetting as well in this case by
choosing *`EstimateParameters`* = *'vignetting'*.

This model is similar to the linear model. However, in this case the camera
may have a nonlinear response. This means that before the gray values of
the images can be multiplied by their respective correction factor, the
gray values must be backprojected to a linear response. To do so, the
camera's response must be determined. Since the response usually does not
change over an image sequence, this parameter is assumed to be constant
throughout the whole image sequence.

Any kind of function could be considered to be used as an OECF. As in the
operator [`radiometric_self_calibration`](radiometric_self_calibration.md), a polynomial fitting might
be used, but for typical images in a mosaicking application this would not
work very well. The reason for this is that polynomial fitting has too many
parameters that need to be determined. Instead, only simpler types of
response functions can be estimated. Currently, only so-called
Laguerre-functions are available.

The response of a Laguerre-type OECF is determined by only one parameter
called Phi. In a first step, the whole gray value spectrum (in case of 8bit
images the values 0 to 255) is converted to floating point numbers in the
interval [0:1]. Then, the OECF backprojection is calculated based on this
and the resulting gray values are once again converted to the original
interval.

The inverse transform of the gray values back to linear values based on a
Laguerre-type OECF is described by the following equation:

$$I_l = I_nl + \frac{2}{\pi} \cdot \arctan\left(\frac{\Phi \cdot \sin(\pi \cdot I_nl)}{1 - P hi \cdot \cos(\pi \cdot I_nl)}\right)$$ ![figure](../assets/3711785007ff0909.svg)

with I_l the linear gray value and I_nl the (nonlinear) gray value.

The parameter *`OECFModel`* is only used if the calibrated model has
been chosen. Otherwise, any input for *`OECFModel`* will be ignored.

The parameter *`EstimateParameters`* can also be used to influence
the performance and memory consumption of the operator. With
*'no_cache'* the internal caching mechanism can be disabled. This
switch only has and influence if *`EstimationMethod`* is set to
*'gold_standard'*. Otherwise this switch will be ignored. When
disabling the internal caching, the operator uses far less memory, but
therefore calculates the corresponding gray value pairs in each iteration
of the minimization algorithm again. Therefore, disabling caching is only
advisable if all physical memory is used up at some point of the calculation
and the operating system starts using swap space.

A second option to influence the performance is using subsampling. When
setting *`EstimateParameters`* to *'subsampling_2'*, images
are internally zoomed down by a factor of 2. Despite the suggested value
list, not only factors of 2 and 4 are available, but any integer number
might be specified by appending it to subsampling_ in
*`EstimateParameters`*. With this, the amount of image data is
tremendously reduced, which leads to a much faster computation of the
internal minimization. In fact, using moderate subsampling might even lead
to better results since it also decreases the influence of slightly
misaligned pixels. Although subsampling also influences the minimization if
*`EstimationMethod`* is set to *'standard'*, it is mostly
useful for *'gold_standard'*.

Some more general remarks on using `adjust_mosaic_images` in
applications:

- Estimation of vignetting will only work well if significant
  vignetting is visible in the images. Otherwise, the operator may lead
  to erratic results.
- Estimation of the response is rather slow because the problem is quite
  complex. Therefore, it is advisable not to determine the response in
  time critical applications. Apart from this, the response can only be
  determined correctly if there are relatively large brightness
  differences between the images.
- It is not possible to correct saturation. If there are saturated
  areas in an image, they will remain saturated.
- `adjust_mosaic_images` can only be used to correct different
  brightness in images, which is caused by different exposure
  (shutter time, aperture) or different light intensity.
  It cannot be used to correct brightness differences based on
  inhomogeneous illumination within each image.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Images`** (input_object)  (multichannel-)image-array `→` object (byte)

Input images.

**`CorrectedImages`** (output_object)  (multichannel-)image-array `→` object (byte)

Output images.

**`From`** (input_control)  integer-array `→`  (integer)

List of source images.

**`To`** (input_control)  integer-array `→`  (integer)

List of destination images.

**`ReferenceImage`** (input_control)  integer `→`  (integer)

Reference image.

**`HomMatrices2D`** (input_control)  real-array `→`  (real)

Projective matrices.

**`EstimationMethod`** (input_control)  string `→`  (string)

Estimation algorithm for the correction.

Default:
'standard'

List of values:
'gold_standard', 'standard'

**`EstimateParameters`** (input_control)  string(-array) `→`  (string)

Parameters to be estimated.

Default:
['mult_gray']

Suggested values:
'add_gray', 'mult_gray', 'response', 'vignetting', 'subsampling_2', 'subsampling_4', 'no_cache'

**`OECFModel`** (input_control)  string `→`  (string)

Model of OECF to be used.

Default:
['laguerre']

List of values:
'laguerre'

## Example (HDevelop)

```
* For the input data to stationary_camera_self_calibration, please
* refer to the example for stationary_camera_self_calibration.
stationary_camera_self_calibration (4, 640, 480, 1, From, To, \
                                    HomMatrices2D, Rows1, Cols1, \
                                    Rows2, Cols2, NumMatches, \
                                    'gold_standard', \
                                    ['focus','principal_point'], \
                                    'true', CameraMatrix, Kappa, \
                                    RotationMatrices, X, Y, Z, Error)
adjust_mosaic_images(Images,CorrectedImages,From,To,1,HomMatrices2D, \
                     'gold_standard',['mult_gray','response'],'laguerre')
```

## Result

If the parameters are valid, the operator
`adjust_mosaic_images` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`stationary_camera_self_calibration`

## Possible Successors

`gen_spherical_mosaic`

## References

David Hasler, Sabine Süsstrunk: Mapping colour in image stitching
applications. Journal of Visual Communication and Image Representation,
15(1):65-90, 2004.

## Module

Foundation
