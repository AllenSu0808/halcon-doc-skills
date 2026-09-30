# CropRectangle2 (Operator)

## Name

`CropRectangle2` — Cut out one or more arbitrarily oriented rectangular image areas.

## Signature

`static void HOperatorSet.CropRectangle2(HObject image, out HObject imagePart, HTuple row, HTuple column, HTuple phi, HTuple length1, HTuple length2, HTuple alignToAxis, HTuple interpolation)`

`HImage HImage.CropRectangle2(HTuple row, HTuple column, HTuple phi, HTuple length1, HTuple length2, string alignToAxis, string interpolation)`

`HImage HImage.CropRectangle2(double row, double column, double phi, double length1, double length2, string alignToAxis, string interpolation)`

## Description

`CropRectangle2` cuts one or more rectangular areas from each of the
input images. The areas are indicated by rectangles, which are defined by the
center (*`row`*, *`column`*), the orientation *`phi`* and the
half edge lengths *`length1`* and *`length2`*. *`phi`* is given
in arc measure in mathematically positive direction and indicates the angle
between the horizontal axis and the first edge (with length *`length1`*).
The rectangle parameters use pixel centered, subpixel accurate coordinates,
see [Transformations / 2D Transformations](toc_transformations_2dtransformations.md).

The parameter *`alignToAxis`* determines the alignment of the output
image.
Possible values:

- *"true"*: The cropped image part is rotated such that it is
  aligned with the coordinate axes. For this, a suitable interpolation must be
  performed. A detailed description of the interpolation modes can be found in
  the description of [`AffineTransImage`](affine_trans_image.md).
  The rectangle may protrude the input image. Gray values of pixels lying
  outside the input image are set to 0.
- *"false"*: The smallest surrounding rectangle of the input
  rectangle is cut out and the domain is set accordingly. The rectangle may
  exceed the input image boundaries. However, the size of the resulting cropped
  image part is determined by the portion of the rectangle which lies within the
  input image boundaries.
  For this method no interpolation is required. Therefore, the parameter
  *`interpolation`* has no effect.

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / int2 / uint2 / real)

Input image(s).

**`imagePart`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / int2 / uint2 / real)

Cropped image part(s).

**`row`** (input_control)  rectangle2.center.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row index of the image crop center.

Default:
300.0

Suggested values:
10.0, 20.0, 50.0, 100.0, 200.0, 300.0, 400.0, 500.0

Value range:
`row` (lin)

Recommended increment:
10.0

**`column`** (input_control)  rectangle2.center.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column index of the image crop center.

Default:
200.0

Suggested values:
10.0, 20.0, 50.0, 100.0, 200.0, 300.0, 400.0, 500.0

Value range:
`column` (lin)

Recommended increment:
10.0

**`phi`** (input_control)  rectangle2.angle.rad(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Orientation of the rectangle (arc measure).

Default:
0.0

Suggested values:
-1.178097, -0.785398, -0.392699, 0.0, 0.392699, 0.785398, 1.178097

Value range:
`-1.178097
≤
phi
≤
1.178097` (lin)

**`length1`** (input_control)  rectangle2.hwidth(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

First half edge length of the rectangle.

Default:
100.0

Suggested values:
3.0, 5.0, 10.0, 15.0, 20.0, 50.0, 100.0, 200.0, 300.0, 500.0

Value range:
`length1` (lin)

Recommended increment:
10.0

**`length2`** (input_control)  rectangle2.hheight(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Second half edge length of the rectangle.

Default:
20.0

Suggested values:
1.0, 2.0, 3.0, 5.0, 10.0, 15.0, 20.0, 50.0, 100.0, 200.0

Value range:
`length2` (lin)

Recommended increment:
10.0

**`alignToAxis`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Determines whether the cropped image part is aligned with
the coordinate axes.

Default:
"true"

List of values:
"false", "true"

**`interpolation`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Interpolation method.

Default:
"constant"

List of values:
"bicubic", "bilinear", "constant", "nearest_neighbor", "weighted"

## Possible Successors

`DispImage`

## Alternatives

`CropDomain`,
`CropRectangle1`,
`CropPart`,
`ChangeFormat`,
`ReduceDomain`

## See also

`ZoomImageSize`,
`ZoomImageFactor`

## Module

Foundation
