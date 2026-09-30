# CropRectangle1 (Operator)

## Name

`CropRectangle1` — Cut out one or more rectangular image areas.

## Signature

`static void HOperatorSet.CropRectangle1(HObject image, out HObject imagePart, HTuple row1, HTuple column1, HTuple row2, HTuple column2)`

`HImage HImage.CropRectangle1(HTuple row1, HTuple column1, HTuple row2, HTuple column2)`

`HImage HImage.CropRectangle1(int row1, int column1, int row2, int column2)`

## Description

The operator `CropRectangle1` cuts one or more rectangular areas
from each of the input images. The areas are indicated by rectangles,
which are defined by the coordinates of their upper left and their lower
right corners. The upper left corners must be within the image. At the right
side and at the bottom, the rectangles may exceed the image, but the domain
of the output images is set so that only the part that can be derived from
the input image is contained. If the rectangular areas fall within the image,
then each of the resulting images has the size of its corresponding
rectangle.

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte* / direction* / cyclic* / int1* / int2* / uint2* / int4* / int8 / real*) **allowed for compute devices*

Input image.

**`imagePart`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte* / direction* / cyclic* / int1* / int2* / uint2* / int4* / int8 / real*) **allowed for compute devices*

Image area.

**`row1`** (input_control)  rectangle.origin.y(-array) `→` [HTuple](HTuple.md) (*int* / long)

Line index of upper left corner of image area.

Default:
100

Suggested values:
10, 20, 50, 100, 200, 300, 500

Value range:
`0
≤
row1
≤
1024`

**`column1`** (input_control)  rectangle.origin.x(-array) `→` [HTuple](HTuple.md) (*int* / long)

Column index of upper left corner of image area.

Default:
100

Suggested values:
10, 20, 50, 100, 200, 300, 500

Value range:
`0
≤
column1
≤
1024`

**`row2`** (input_control)  rectangle.corner.y(-array) `→` [HTuple](HTuple.md) (*int* / long)

Line index of lower right corner of image area.

Default:
200

Suggested values:
10, 20, 50, 100, 200, 300, 500

Value range:
`0
≤
row2
≤
1024`

**`column2`** (input_control)  rectangle.corner.x(-array) `→` [HTuple](HTuple.md) (*int* / long)

Column index of lower right corner of image area.

Default:
200

Suggested values:
10, 20, 50, 100, 200, 300, 500

Value range:
`0
≤
column2
≤
1024`

## Possible Successors

`DispImage`

## Alternatives

`CropPart`,
`CropDomain`,
`ChangeFormat`,
`ReduceDomain`

## See also

`ZoomImageSize`,
`ZoomImageFactor`

## Module

Foundation
