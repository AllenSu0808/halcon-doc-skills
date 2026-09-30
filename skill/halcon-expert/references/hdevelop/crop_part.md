# crop_part (Operator)

## Name

`crop_part` — Cut out one or more rectangular image areas.

## Signature

`crop_part(Image : ImagePart : Row, Column, Width, Height : )`

## Description

The operator `crop_part` cuts one or more rectangular area from each
of the input images. The areas are indicated by rectangles, which are
defined by the coordinates of their upper left corner and by their size.
The upper left corners of the rectangles must be within the image. At the
right side and at the bottom, the rectangles may exceed the image, but the
domain of the output images is set so that only the part that can be derived
from the input image is contained. If the rectangular areas fall completely
within the image, then each of the resulting images has the size of its
corresponding rectangle.

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

**`Row`** (input_control)  rectangle.origin.y(-array) `→`  (integer)

Line index of upper left corner of image area.

Default:
100

Suggested values:
10, 20, 50, 100, 200, 300, 500

Value range:
`0
≤
Row
≤
1024`

**`Column`** (input_control)  rectangle.origin.x(-array) `→`  (integer)

Column index of upper left corner of image area.

Default:
100

Suggested values:
10, 20, 50, 100, 200, 300, 500

Value range:
`0
≤
Column
≤
1024`

**`Width`** (input_control)  rectangle.extent.x(-array) `→`  (integer)

Width of new image.

Default:
128

Suggested values:
32, 64, 128, 256, 512, 768

Value range:
`0
≤
Width
≤
1024`

**`Height`** (input_control)  rectangle.extent.y(-array) `→`  (integer)

Height of new image.

Default:
128

Suggested values:
32, 64, 128, 256, 512, 525

Value range:
`0
≤
Height
≤
1024`

## Possible Successors

`disp_image`

## Alternatives

`crop_rectangle1`,
`crop_domain`,
`change_format`,
`reduce_domain`

## See also

`zoom_image_size`,
`zoom_image_factor`

## Module

Foundation
