# crop_rectangle2 (Operator)

## Name

`crop_rectangle2` — Cut out one or more arbitrarily oriented rectangular image areas.

## Signature

`crop_rectangle2(Image : ImagePart : Row, Column, Phi, Length1, Length2, AlignToAxis, Interpolation : )`

## Description

`crop_rectangle2` cuts one or more rectangular areas from each of the
input images. The areas are indicated by rectangles, which are defined by the
center (*`Row`*, *`Column`*), the orientation *`Phi`* and the
half edge lengths *`Length1`* and *`Length2`*. *`Phi`* is given
in arc measure in mathematically positive direction and indicates the angle
between the horizontal axis and the first edge (with length *`Length1`*).
The rectangle parameters use pixel centered, subpixel accurate coordinates,
see [Transformations / 2D Transformations](toc_transformations_2dtransformations.md).

The parameter *`AlignToAxis`* determines the alignment of the output
image.
Possible values:

- *'true'*: The cropped image part is rotated such that it is
  aligned with the coordinate axes. For this, a suitable interpolation must be
  performed. A detailed description of the interpolation modes can be found in
  the description of [`affine_trans_image`](affine_trans_image.md).
  The rectangle may protrude the input image. Gray values of pixels lying
  outside the input image are set to 0.
- *'false'*: The smallest surrounding rectangle of the input
  rectangle is cut out and the domain is set accordingly. The rectangle may
  exceed the input image boundaries. However, the size of the resulting cropped
  image part is determined by the portion of the rectangle which lies within the
  input image boundaries.
  For this method no interpolation is required. Therefore, the parameter
  *`Interpolation`* has no effect.

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte / int2 / uint2 / real)

Input image(s).

**`ImagePart`** (output_object)  (multichannel-)image(-array) `→` object (byte / int2 / uint2 / real)

Cropped image part(s).

**`Row`** (input_control)  rectangle2.center.y(-array) `→`  (real / integer)

Row index of the image crop center.

Default:
300.0

Suggested values:
10.0, 20.0, 50.0, 100.0, 200.0, 300.0, 400.0, 500.0

Value range:
`Row` (lin)

Recommended increment:
10.0

**`Column`** (input_control)  rectangle2.center.x(-array) `→`  (real / integer)

Column index of the image crop center.

Default:
200.0

Suggested values:
10.0, 20.0, 50.0, 100.0, 200.0, 300.0, 400.0, 500.0

Value range:
`Column` (lin)

Recommended increment:
10.0

**`Phi`** (input_control)  rectangle2.angle.rad(-array) `→`  (real / integer)

Orientation of the rectangle (arc measure).

Default:
0.0

Suggested values:
-1.178097, -0.785398, -0.392699, 0.0, 0.392699, 0.785398, 1.178097

Value range:
`-1.178097
≤
Phi
≤
1.178097` (lin)

**`Length1`** (input_control)  rectangle2.hwidth(-array) `→`  (real / integer)

First half edge length of the rectangle.

Default:
100.0

Suggested values:
3.0, 5.0, 10.0, 15.0, 20.0, 50.0, 100.0, 200.0, 300.0, 500.0

Value range:
`Length1` (lin)

Recommended increment:
10.0

**`Length2`** (input_control)  rectangle2.hheight(-array) `→`  (real / integer)

Second half edge length of the rectangle.

Default:
20.0

Suggested values:
1.0, 2.0, 3.0, 5.0, 10.0, 15.0, 20.0, 50.0, 100.0, 200.0

Value range:
`Length2` (lin)

Recommended increment:
10.0

**`AlignToAxis`** (input_control)  string `→`  (string)

Determines whether the cropped image part is aligned with
the coordinate axes.

Default:
'true'

List of values:
'false', 'true'

**`Interpolation`** (input_control)  string `→`  (string)

Interpolation method.

Default:
'constant'

List of values:
'bicubic', 'bilinear', 'constant', 'nearest_neighbor', 'weighted'

## Possible Successors

`disp_image`

## Alternatives

`crop_domain`,
`crop_rectangle1`,
`crop_part`,
`change_format`,
`reduce_domain`

## See also

`zoom_image_size`,
`zoom_image_factor`

## Module

Foundation
