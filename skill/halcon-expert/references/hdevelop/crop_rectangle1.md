# crop_rectangle1 (Operator)

## Name

`crop_rectangle1` — Cut out one or more rectangular image areas.

## Signature

`crop_rectangle1(Image : ImagePart : Row1, Column1, Row2, Column2 : )`

## Description

The operator `crop_rectangle1` cuts one or more rectangular areas
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

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte* / direction* / cyclic* / int1* / int2* / uint2* / int4* / int8 / real*) **allowed for compute devices*

Input image.

**`ImagePart`** (output_object)  (multichannel-)image(-array) `→` object (byte* / direction* / cyclic* / int1* / int2* / uint2* / int4* / int8 / real*) **allowed for compute devices*

Image area.

**`Row1`** (input_control)  rectangle.origin.y(-array) `→`  (integer)

Line index of upper left corner of image area.

Default:
100

Suggested values:
10, 20, 50, 100, 200, 300, 500

Value range:
`0
≤
Row1
≤
1024`

**`Column1`** (input_control)  rectangle.origin.x(-array) `→`  (integer)

Column index of upper left corner of image area.

Default:
100

Suggested values:
10, 20, 50, 100, 200, 300, 500

Value range:
`0
≤
Column1
≤
1024`

**`Row2`** (input_control)  rectangle.corner.y(-array) `→`  (integer)

Line index of lower right corner of image area.

Default:
200

Suggested values:
10, 20, 50, 100, 200, 300, 500

Value range:
`0
≤
Row2
≤
1024`

**`Column2`** (input_control)  rectangle.corner.x(-array) `→`  (integer)

Column index of lower right corner of image area.

Default:
200

Suggested values:
10, 20, 50, 100, 200, 300, 500

Value range:
`0
≤
Column2
≤
1024`

## Possible Successors

`disp_image`

## Alternatives

`crop_part`,
`crop_domain`,
`change_format`,
`reduce_domain`

## See also

`zoom_image_size`,
`zoom_image_factor`

## Module

Foundation
