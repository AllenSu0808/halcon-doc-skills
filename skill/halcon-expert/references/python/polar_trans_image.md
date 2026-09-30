# polar_trans_image (Operator)

## Name

`polar_trans_image` — Transform an image to polar coordinates

## Warning

**`polar_trans_image` is obsolete and is only provided for
reasons of backward compatibility. New applications should use
the operator [`polar_trans_image_ext`](polar_trans_image_ext.md) instead.**

## Signature

`def polar_trans_image(image_xy: HObject, row: int, column: int, width: int, height: int) -> HObject`

## Description

`polar_trans_image` transforms an image in Cartesian coordinates
to an image in polar coordinates. The size of the resulting image
is selected with *`width`* and *`height`*.
*`width`* determines the angular resolution, while
*`height`* determines the resolution of the radius.
*`row`* and *`column`* determine the center of the
polar coordinate system in the original image *`image_xy`*.
This point is mapped to the upper row of *`image_polar`*.

A point (x',y') in the result image corresponds to the point (x,y)
in the original image in the following manner:
$$x = y' * cos(2π(x'/result_width)) + Column\ny = y' * sin(2π(x'/result_width)) + Row.$$ ![figure](../assets/79b1e64d46de286d.svg)

`polar_trans_image` can be executed on an OpenCL device if the input
image does not exceed the maximum size of image objects of the selected
device. Due to numerical reasons, there can be slight differences in the
output compared to the execution on the CPU.

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

## Parameters

**`image_xy`** (input_object)  (multichannel-)image(-array) `→` HObject (byte* / int2* / uint2* / real*) **allowed for compute devices*

Input image in Cartesian coordinates.

**`image_polar`** (output_object)  (multichannel-)image(-array) `→` HObject (byte / int2 / uint2 / real)

Result image in polar coordinates.

**`row`** (input_control)  point.y `→` int

Row coordinate of the center of the coordinate
system.

Default:
100

Suggested values:
0, 10, 100, 200

Value range:
`0
≤
row
≤
512`

Minimum increment:
1

Recommended increment:
1

**`column`** (input_control)  point.x `→` int

Column coordinate of the center of the
coordinate system.

Default:
100

Suggested values:
0, 10, 100, 200

Value range:
`0
≤
column
≤
512`

Minimum increment:
1

Recommended increment:
1

**`width`** (input_control)  extent.x `→` int

Width of the result image.

Default:
314

Suggested values:
100, 200, 157, 314, 512

Value range:
`2
≤
width
≤
512`

Minimum increment:
1

Recommended increment:
10

**`height`** (input_control)  extent.y `→` int

Height of the result image.

Default:
200

Suggested values:
100, 128, 256, 512

Value range:
`2
≤
height
≤
512`

Minimum increment:
1

Recommended increment:
10

## Module

Foundation
