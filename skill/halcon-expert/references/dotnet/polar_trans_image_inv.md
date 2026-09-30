# PolarTransImageInv (Operator)

## Name

`PolarTransImageInv` — Transform an image in polar coordinates back to Cartesian coordinates

## Signature

`static void HOperatorSet.PolarTransImageInv(HObject polarImage, out HObject XYTransImage, HTuple row, HTuple column, HTuple angleStart, HTuple angleEnd, HTuple radiusStart, HTuple radiusEnd, HTuple width, HTuple height, HTuple interpolation)`

`HImage HImage.PolarTransImageInv(HTuple row, HTuple column, double angleStart, double angleEnd, HTuple radiusStart, HTuple radiusEnd, int width, int height, string interpolation)`

`HImage HImage.PolarTransImageInv(double row, double column, double angleStart, double angleEnd, double radiusStart, double radiusEnd, int width, int height, string interpolation)`

## Description

`PolarTransImageInv` transforms the polar coordinate
representation of an image, stored in *`polarImage`*, back onto
an annular arc in Cartesian coordinates, described by the radii
*`radiusStart`* and *`radiusEnd`* and the angles
*`angleStart`* and *`angleEnd`* with the center point
located at (*`row`*, *`column`*). All of these values can
be chosen as real numbers. The overall size of the target image
will be *`width`* x *`height`* pixels.

The parameter *`interpolation`* is used to select the
interpolation method *"bilinear"* or
*"nearest_neighbor"*. With *"nearest_neighbor"*, the
gray value of a pixel in the output image is determined by the gray
value of the closest pixel in the input image. With
*"bilinear"*, the gray value of a pixel in the output image
is determined by bilinear interpolation of the gray values of the
four closest pixels in the input image. The mode
*"bilinear"* results in images of better quality, but is
slower than the mode *"nearest_neighbor"*.

The angles and radii are inclusive, which means that the first row
of the input image will be mapped onto a circle with a distance of
*`radiusStart`* pixels from the specified center and the last
row will be mapped onto a circle of radius *`radiusEnd`*.

`PolarTransImageInv` is the inverse function of
[`PolarTransImageExt`](polar_trans_image_ext.md).

The call sequence:

|  |
| --- |
| `polar_trans_image_ext(Image, PolarImage, Row, Column, rad(360), 0, 0, Radius, Width, Height, Interpolation)` |
| `polar_trans_image_inv(PolarImage, XYTransImage, Row, Column, rad(360), 0, 0, Radius, Width, Height, Interpolation)` |

returns the image `image`, restricted to the
circle around (*`row`*, *`column`*) with radius
`Radius`, as its output image
*`XYTransImage`*.

`PolarTransImageInv` can be executed on an OpenCL device. There can
be slight differences in the output compared to the execution on the CPU.

Additionally, for images of type byte, int2 or
uint2 the system parameter *"int_zooming"* selects between
fast calculation in fixed point arithmetics
(*"int_zooming"* = *"true"*)
and highly accurate calculation in floating point arithmetics
(*"int_zooming"* = *"false"*). Fixed point calculation
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

**`polarImage`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte* / int2* / uint2* / real*) **allowed for compute devices*

Input image.

**`XYTransImage`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / int2 / uint2 / real)

Output image.

**`row`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the center of the arc.

Default:
256

Suggested values:
0, 16, 32, 64, 128, 240, 256, 480, 512

Value range:
`0
≤
row
≤
32767`

**`column`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the center of the arc.

Default:
256

Suggested values:
0, 16, 32, 64, 128, 256, 320, 512, 640

Value range:
`0
≤
column
≤
32767`

**`angleStart`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double*)

Angle of the ray to map the first column of the
input image to.

Default:
0.0

Suggested values:
0.0, 0.78539816, 1.57079632, 3.141592654, 6.2831853

**`angleEnd`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double*)

Angle of the ray to map the last column of the
input image to.

Default:
6.2831853

Suggested values:
0.0, 0.78539816, 1.57079632, 3.141592654, 6.2831853

**`radiusStart`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Radius of the circle to map the first row of
the input image to.

Default:
0

Suggested values:
0, 16, 32, 64, 100, 128, 256, 512

Value range:
`0
≤
radiusStart`

**`radiusEnd`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Radius of the circle to map the last row of the
input image to.

Default:
100

Suggested values:
0, 16, 32, 64, 100, 128, 256, 512

Value range:
`0
≤
radiusEnd`

**`width`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

Width of the output image.

Default:
512

Suggested values:
256, 320, 512, 640, 800, 1024

Value range:
`0
≤
width
≤
32767`

**`height`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long)

Height of the output image.

Default:
512

Suggested values:
240, 256, 480, 512, 600, 1024

Value range:
`0
≤
height
≤
32767`

**`interpolation`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Interpolation method for the transformation.

Default:
"nearest_neighbor"

List of values:
"bilinear", "nearest_neighbor"

## See also

`PolarTransImageExt`,
`PolarTransRegion`,
`PolarTransRegionInv`,
`PolarTransContourXld`,
`PolarTransContourXldInv`

## Module

Foundation
