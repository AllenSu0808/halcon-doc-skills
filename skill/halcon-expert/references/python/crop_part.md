# crop_part (Operator)

## Name

`crop_part` — Cut out one or more rectangular image areas.

## Signature

`def crop_part(image: HObject, row: MaybeSequence[int], column: MaybeSequence[int], width: MaybeSequence[int], height: MaybeSequence[int]) -> HObject`

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

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte* / direction* / cyclic* / int1* / int2* / uint2* / int4* / int8 / real*) **allowed for compute devices*

Input image.

**`image_part`** (output_object)  (multichannel-)image(-array) `→` HObject (byte* / direction* / cyclic* / int1* / int2* / uint2* / int4* / int8 / real*) **allowed for compute devices*

Image area.

**`row`** (input_control)  rectangle.origin.y(-array) `→` MaybeSequence[int]

Line index of upper left corner of image area.

Default:
100

Suggested values:
10, 20, 50, 100, 200, 300, 500

Value range:
`0
≤
row
≤
1024`

**`column`** (input_control)  rectangle.origin.x(-array) `→` MaybeSequence[int]

Column index of upper left corner of image area.

Default:
100

Suggested values:
10, 20, 50, 100, 200, 300, 500

Value range:
`0
≤
column
≤
1024`

**`width`** (input_control)  rectangle.extent.x(-array) `→` MaybeSequence[int]

Width of new image.

Default:
128

Suggested values:
32, 64, 128, 256, 512, 768

Value range:
`0
≤
width
≤
1024`

**`height`** (input_control)  rectangle.extent.y(-array) `→` MaybeSequence[int]

Height of new image.

Default:
128

Suggested values:
32, 64, 128, 256, 512, 525

Value range:
`0
≤
height
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
