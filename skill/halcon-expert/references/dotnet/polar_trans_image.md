# PolarTransImage (Operator)

## Name

`PolarTransImage` — Transform an image to polar coordinates

## Warning

**`PolarTransImage` is obsolete and is only provided for
reasons of backward compatibility. New applications should use
the operator [`PolarTransImageExt`](polar_trans_image_ext.md) instead.**

## Signature

`static void HOperatorSet.PolarTransImage(HObject imageXY, out HObject imagePolar, HTuple row, HTuple column, HTuple width, HTuple height)`

`HImage HImage.PolarTransImage(int row, int column, int width, int height)`

## Description

`PolarTransImage` transforms an image in Cartesian coordinates
to an image in polar coordinates. The size of the resulting image
is selected with *`width`* and *`height`*.
*`width`* determines the angular resolution, while
*`height`* determines the resolution of the radius.
*`row`* and *`column`* determine the center of the
polar coordinate system in the original image *`imageXY`*.
This point is mapped to the upper row of *`imagePolar`*.

A point (x',y') in the result image corresponds to the point (x,y)
in the original image in the following manner:
$$x = y' * cos(2π(x'/result_width)) + Column\ny = y' * sin(2π(x'/result_width)) + Row.$$ ![figure](../assets/79b1e64d46de286d.svg)

`PolarTransImage` can be executed on an OpenCL device if the input
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

**`imageXY`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte* / int2* / uint2* / real*) **allowed for compute devices*

Input image in Cartesian coordinates.

**`imagePolar`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / int2 / uint2 / real)

Result image in polar coordinates.

**`row`** (input_control)  point.y `→` [HTuple](HTuple.md) (*int* / long)

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

**`column`** (input_control)  point.x `→` [HTuple](HTuple.md) (*int* / long)

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

**`width`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

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

**`height`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long)

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

## Example (HDevelop)

```
read_image(Image,'monkey')
dev_display (Image)
polar_trans_image(Image,PolarImage,100,100,314,200)
dev_display (PolarImage)
```

## Module

Foundation
