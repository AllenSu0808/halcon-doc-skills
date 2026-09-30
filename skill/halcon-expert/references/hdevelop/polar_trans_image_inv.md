# polar_trans_image_inv (Operator)

## Name

`polar_trans_image_inv` — Transform an image in polar coordinates back to Cartesian coordinates

## Signature

`polar_trans_image_inv(PolarImage : XYTransImage : Row, Column, AngleStart, AngleEnd, RadiusStart, RadiusEnd, Width, Height, Interpolation : )`

## Description

`polar_trans_image_inv` transforms the polar coordinate
representation of an image, stored in *`PolarImage`*, back onto
an annular arc in Cartesian coordinates, described by the radii
*`RadiusStart`* and *`RadiusEnd`* and the angles
*`AngleStart`* and *`AngleEnd`* with the center point
located at (*`Row`*, *`Column`*). All of these values can
be chosen as real numbers. The overall size of the target image
will be *`Width`* x *`Height`* pixels.

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

The angles and radii are inclusive, which means that the first row
of the input image will be mapped onto a circle with a distance of
*`RadiusStart`* pixels from the specified center and the last
row will be mapped onto a circle of radius *`RadiusEnd`*.

`polar_trans_image_inv` is the inverse function of
[`polar_trans_image_ext`](polar_trans_image_ext.md).

The call sequence:

|  |
| --- |
| `polar_trans_image_ext(Image, PolarImage, Row, Column, rad(360), 0, 0, Radius, Width, Height, Interpolation)` |
| `polar_trans_image_inv(PolarImage, XYTransImage, Row, Column, rad(360), 0, 0, Radius, Width, Height, Interpolation)` |

returns the image `Image`, restricted to the
circle around (*`Row`*, *`Column`*) with radius
`Radius`, as its output image
*`XYTransImage`*.

`polar_trans_image_inv` can be executed on an OpenCL device. There can
be slight differences in the output compared to the execution on the CPU.

Additionally, for images of type byte, int2 or
uint2 the system parameter *'int_zooming'* selects between
fast calculation in fixed point arithmetics
(*'int_zooming'* = *'true'*)
and highly accurate calculation in floating point arithmetics
(*'int_zooming'* = *'false'*). Fixed point calculation
can lead to minor gray value deviations. In this case, the
domain of resulting images can differ as well.

### Further Information

For an explanation of the different 2D coordinate systems
used in HALCON, see the introduction of chapter
[Transformations / 2D Transformations](toc_transformations_2dtransformations.md).

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on internal data level.

## Parameters

**`PolarImage`** (input_object)  (multichannel-)image(-array) `→` object (byte* / int2* / uint2* / real*) **allowed for compute devices*

Input image.

**`XYTransImage`** (output_object)  (multichannel-)image(-array) `→` object (byte / int2 / uint2 / real)

Output image.

**`Row`** (input_control)  number `→`  (real / integer)

Row coordinate of the center of the arc.

Default:
256

Suggested values:
0, 16, 32, 64, 128, 240, 256, 480, 512

Value range:
`0
≤
Row
≤
32767`

**`Column`** (input_control)  number `→`  (real / integer)

Column coordinate of the center of the arc.

Default:
256

Suggested values:
0, 16, 32, 64, 128, 256, 320, 512, 640

Value range:
`0
≤
Column
≤
32767`

**`AngleStart`** (input_control)  angle.rad `→`  (real)

Angle of the ray to map the first column of the
input image to.

Default:
0.0

Suggested values:
0.0, 0.78539816, 1.57079632, 3.141592654, 6.2831853

**`AngleEnd`** (input_control)  angle.rad `→`  (real)

Angle of the ray to map the last column of the
input image to.

Default:
6.2831853

Suggested values:
0.0, 0.78539816, 1.57079632, 3.141592654, 6.2831853

**`RadiusStart`** (input_control)  number `→`  (real / integer)

Radius of the circle to map the first row of
the input image to.

Default:
0

Suggested values:
0, 16, 32, 64, 100, 128, 256, 512

Value range:
`0
≤
RadiusStart`

**`RadiusEnd`** (input_control)  number `→`  (real / integer)

Radius of the circle to map the last row of the
input image to.

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

`polar_trans_image_ext`,
`polar_trans_region`,
`polar_trans_region_inv`,
`polar_trans_contour_xld`,
`polar_trans_contour_xld_inv`

## Module

Foundation
