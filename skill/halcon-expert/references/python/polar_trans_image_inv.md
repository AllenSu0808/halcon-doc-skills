# polar_trans_image_inv (Operator)

## Name

`polar_trans_image_inv` — Transform an image in polar coordinates back to Cartesian coordinates

## Signature

`def polar_trans_image_inv(polar_image: HObject, row: Union[int, float], column: Union[int, float], angle_start: float, angle_end: float, radius_start: Union[int, float], radius_end: Union[int, float], width: int, height: int, interpolation: str) -> HObject`

## Description

`polar_trans_image_inv` transforms the polar coordinate
representation of an image, stored in *`polar_image`*, back onto
an annular arc in Cartesian coordinates, described by the radii
*`radius_start`* and *`radius_end`* and the angles
*`angle_start`* and *`angle_end`* with the center point
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
*`radius_start`* pixels from the specified center and the last
row will be mapped onto a circle of radius *`radius_end`*.

`polar_trans_image_inv` is the inverse function of
[`polar_trans_image_ext`](polar_trans_image_ext.md).

The call sequence:

|  |
| --- |
| `polar_trans_image_ext(Image, PolarImage, Row, Column, rad(360), 0, 0, Radius, Width, Height, Interpolation)` |
| `polar_trans_image_inv(PolarImage, XYTransImage, Row, Column, rad(360), 0, 0, Radius, Width, Height, Interpolation)` |

returns the image `image`, restricted to the
circle around (*`row`*, *`column`*) with radius
`Radius`, as its output image
*`xytrans_image`*.

`polar_trans_image_inv` can be executed on an OpenCL device. There can
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

**`polar_image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte* / int2* / uint2* / real*) **allowed for compute devices*

Input image.

**`xytrans_image`** (output_object)  (multichannel-)image(-array) `→` HObject (byte / int2 / uint2 / real)

Output image.

**`row`** (input_control)  number `→` Union[int, float]

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

**`column`** (input_control)  number `→` Union[int, float]

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

**`angle_start`** (input_control)  angle.rad `→` float

Angle of the ray to map the first column of the
input image to.

Default:
0.0

Suggested values:
0.0, 0.78539816, 1.57079632, 3.141592654, 6.2831853

**`angle_end`** (input_control)  angle.rad `→` float

Angle of the ray to map the last column of the
input image to.

Default:
6.2831853

Suggested values:
0.0, 0.78539816, 1.57079632, 3.141592654, 6.2831853

**`radius_start`** (input_control)  number `→` Union[int, float]

Radius of the circle to map the first row of
the input image to.

Default:
0

Suggested values:
0, 16, 32, 64, 100, 128, 256, 512

Value range:
`0
≤
radius_start`

**`radius_end`** (input_control)  number `→` Union[int, float]

Radius of the circle to map the last row of the
input image to.

Default:
100

Suggested values:
0, 16, 32, 64, 100, 128, 256, 512

Value range:
`0
≤
radius_end`

**`width`** (input_control)  extent.x `→` int

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

**`height`** (input_control)  extent.y `→` int

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

**`interpolation`** (input_control)  string `→` str

Interpolation method for the transformation.

Default:
"nearest_neighbor"

List of values:
"bilinear", "nearest_neighbor"

## See also

`polar_trans_image_ext`,
`polar_trans_region`,
`polar_trans_region_inv`,
`polar_trans_contour_xld`,
`polar_trans_contour_xld_inv`

## Module

Foundation
