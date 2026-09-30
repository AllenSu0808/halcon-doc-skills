# polar_trans_image_ext (Operator)

## Name

`polar_trans_image_ext` — Transform an annular arc in an image to polar coordinates.

## Signature

`polar_trans_image_ext(Image : PolarTransImage : Row, Column, AngleStart, AngleEnd, RadiusStart, RadiusEnd, Width, Height, Interpolation : )`

## Description

`polar_trans_image_ext` transforms the annular arc specified
by the center point (*`Row`*, *`Column`*), the radii
*`RadiusStart`* and *`RadiusEnd`* and the angles
*`AngleStart`* and *`AngleEnd`* in the image
*`Image`* to its polar coordinate version in the image
*`PolarTransImage`* of the dimensions *`Width`*
x *`Height`*.

The upper left pixel in the output image always corresponds to the
point in the input image that is specified by *`RadiusStart`*
and *`AngleStart`*. Analogously, the lower right pixel in the
output image always corresponds to the point in the input image that
is specified by *`RadiusEnd`* and *`AngleEnd`*. In the
usual mode (*`AngleStart`* < *`AngleEnd`* and
*`RadiusStart`* < *`RadiusEnd`*), the polar
transformation is performed in the mathematically positive
orientation (counterclockwise). Furthermore, points with smaller
radii lie in the upper part of the output image. By suitably
exchanging the values of these parameters (e.g., *`AngleStart`*
> *`AngleEnd`* or *`RadiusStart`* >
*`RadiusEnd`*), any desired orientation of the output image can
be achieved.

The parameter *`Interpolation`* is used to select the
interpolation method *'bilinear'* or
*'nearest_neighbor'*. With *'nearest_neighbor'*, the
gray value of a pixel in the output image is determined by the gray
value of the closest pixel in the input image. With
*'bilinear'*, the gray value of a pixel in the output image
is determined by bilinear interpolation of the gray values of the
four closest pixels in the input image. The mode
*'bilinear'* results in images of better quality, but is
slower than the mode *'nearest_neighbor'*.

The angles can be chosen from all real numbers. Center point and
radii can be real as well. However, if they are both integers and
the difference of *`RadiusEnd`* and *`RadiusStart`* equals
the height *`Height`* of the destination image, calculation
will be sped up through an optimized routine.

The radii and angles are inclusive, which means that the first row
of the target image contains the circle with radius
*`RadiusStart`* and the last row contains the circle with
radius *`RadiusEnd`*. For complete circles, where the
difference between *`AngleStart`* and *`AngleEnd`* equals
$2\pi$ (360 degrees), this also means that the first
column of the target image will be the same as the last.

To avoid this, do not make this difference $2\pi$, but
$2\pi\bigl(1 - \frac{1}{\mathrm{widt}h}\bigr)$ ![figure](../assets/7a628e5fd266ca23.svg) degrees instead.

The call
`polar_trans_image(Image, PolarTransImage, Row, Column, Width, Height)`
produces the same result as the call
`polar_trans_image_ext(Image, PolarTransImage, Row-0.5, Column-0.5, 6.2831853, 6.2831853/Width, 0, Height-1, Width, Height, 'nearest_neighbor')`.

The offset of 0.5 is necessary since [`polar_trans_image`](polar_trans_image.md) does
not do exact nearest neighbor interpolation and the radii and angles
can be calculated using the information in the above paragraph and
knowing that [`polar_trans_image`](polar_trans_image.md) does not handle its arguments
inclusively. The start angle is bigger than the end angle to make
`polar_trans_image_ext` go clockwise, just like
[`polar_trans_image`](polar_trans_image.md) does.

`polar_trans_image_ext` can be executed on an OpenCL device if the
input image does not exceed the maximum size of image objects of the selected
device. Due to numerical reasons, there can be slight differences in
the output compared to the execution on the CPU.

Additionally, for images of type byte, int2 or
uint2 the system parameter *'int_zooming'* selects between
fast calculation in fixed point arithmetics
(*'int_zooming'* = *'true'*)
and highly accurate calculation in floating point arithmetics
(*'int_zooming'* = *'false'*). Fixed point calculation
can lead to minor gray value deviations and pixels with undefined gray
values.

### Further Information

For an explanation of the different 2D coordinate systems
used in HALCON, see the introduction of chapter
[Transformations / 2D Transformations](toc_transformations_2dtransformations.md).

## Attention

For speed reasons, the domain of the input image is ignored. The
output image always has a complete rectangle as its domain.

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on internal data level.

## Parameters

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte* / int2* / uint2* / real*) **allowed for compute devices*

Input image.

**`PolarTransImage`** (output_object)  (multichannel-)image(-array) `→` object (byte / int2 / uint2 / real)

Output image.

**`Row`** (input_control)  number `→`  (real / integer)

Row coordinate of the center of the arc.

Default:
256

Suggested values:
0, 16, 32, 64, 128, 240, 256, 480, 512

**`Column`** (input_control)  number `→`  (real / integer)

Column coordinate of the center of the arc.

Default:
256

Suggested values:
0, 16, 32, 64, 128, 256, 320, 512, 640

**`AngleStart`** (input_control)  angle.rad `→`  (real)

Angle of the ray to be mapped to the first
column of the output image.

Default:
0.0

Suggested values:
0.0, 0.78539816, 1.57079632, 3.141592654, 6.2831853, 12.566370616

**`AngleEnd`** (input_control)  angle.rad `→`  (real)

Angle of the ray to be mapped to the last
column of the output image.

Default:
6.2831853

Suggested values:
0.0, 0.78539816, 1.57079632, 3.141592654, 6.2831853, 12.566370616

**`RadiusStart`** (input_control)  number `→`  (real / integer)

Radius of the circle to be mapped to the first
row of the output image.

Default:
0

Suggested values:
0, 16, 32, 64, 100, 128, 256, 512

Value range:
`0
≤
RadiusStart`

**`RadiusEnd`** (input_control)  number `→`  (real / integer)

Radius of the circle to be mapped to the last
row of the output image.

Default:
100

Suggested values:
0, 16, 32, 64, 100, 128, 256, 512

Value range:
`0
≤
RadiusEnd`

**`Width`** (input_control)  extent.x `→`  (integer)

Width of the output image.

Default:
512

Suggested values:
256, 320, 512, 640, 800, 1024

Value range:
`0
≤
Width
≤
32767`

**`Height`** (input_control)  extent.y `→`  (integer)

Height of the output image.

Default:
512

Suggested values:
240, 256, 480, 512, 600, 1024

Value range:
`0
≤
Height
≤
32767`

**`Interpolation`** (input_control)  string `→`  (string)

Interpolation method for the transformation.

Default:
'nearest_neighbor'

List of values:
'bilinear', 'nearest_neighbor'

## See also

`polar_trans_image_inv`,
`polar_trans_region`,
`polar_trans_region_inv`,
`polar_trans_contour_xld`,
`polar_trans_contour_xld_inv`

## Module

Foundation
