# crop_rectangle1 (Operator)

## Name

`crop_rectangle1` — Cut out one or more rectangular image areas.

## Signature

`def crop_rectangle1(image: HObject, row_1: MaybeSequence[int], column_1: MaybeSequence[int], row_2: MaybeSequence[int], column_2: MaybeSequence[int]) -> HObject`

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

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte* / direction* / cyclic* / int1* / int2* / uint2* / int4* / int8 / real*) **allowed for compute devices*

Input image.

**`image_part`** (output_object)  (multichannel-)image(-array) `→` HObject (byte* / direction* / cyclic* / int1* / int2* / uint2* / int4* / int8 / real*) **allowed for compute devices*

Image area.

**`row_1`** (input_control)  rectangle.origin.y(-array) `→` MaybeSequence[int]

Line index of upper left corner of image area.

Default:
100

Suggested values:
10, 20, 50, 100, 200, 300, 500

Value range:
`0
≤
row_1
≤
1024`

**`column_1`** (input_control)  rectangle.origin.x(-array) `→` MaybeSequence[int]

Column index of upper left corner of image area.

Default:
100

Suggested values:
10, 20, 50, 100, 200, 300, 500

Value range:
`0
≤
column_1
≤
1024`

**`row_2`** (input_control)  rectangle.corner.y(-array) `→` MaybeSequence[int]

Line index of lower right corner of image area.

Default:
200

Suggested values:
10, 20, 50, 100, 200, 300, 500

Value range:
`0
≤
row_2
≤
1024`

**`column_2`** (input_control)  rectangle.corner.x(-array) `→` MaybeSequence[int]

Column index of lower right corner of image area.

Default:
200

Suggested values:
10, 20, 50, 100, 200, 300, 500

Value range:
`0
≤
column_2
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
