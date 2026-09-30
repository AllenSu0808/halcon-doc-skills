# region_to_bin (Operator)

## Name

`region_to_bin` — Convert a region into a binary byte-image.

## Signature

`def region_to_bin(region: HObject, foreground_gray: int, background_gray: int, width: int, height: int) -> HObject`

## Description

`region_to_bin` converts the input region given in
*`region`* into a byte-image and assigns a gray
value of *`foreground_gray`* to all pixels in the region. If
the input region is larger than the generated image, it is clipped
at the image borders. The background is set to
*`background_gray`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region`** (input_object)  region(-array) `→` HObject

Regions to be converted.

**`bin_image`** (output_object)  image `→` HObject (byte)

Result image of dimension Width * Height
containing the converted regions.

**`foreground_gray`** (input_control)  integer `→` int

Gray value in which the regions are displayed.

Default:
255

Suggested values:
0, 1, 50, 100, 128, 150, 200, 254, 255

Value range:
`0
≤
foreground_gray
≤
255` (lin)

Recommended increment:
1

**`background_gray`** (input_control)  integer `→` int

Gray value in which the background is displayed.

Default:
0

Suggested values:
0, 1, 50, 100, 128, 150, 200, 254, 255

Value range:
`0
≤
background_gray
≤
255` (lin)

Recommended increment:
1

**`width`** (input_control)  extent.x `→` int

Width of the image to be generated.

Default:
512

Suggested values:
256, 512, 1024

Value range:
`1
≤
width
≤
1024` (lin)

Minimum increment:
1

Recommended increment:
16

Restriction:
`Width >= 1`

**`height`** (input_control)  extent.y `→` int

Height of the image to be generated.

Default:
512

Suggested values:
256, 512, 1024

Value range:
`1
≤
height
≤
1024` (lin)

Minimum increment:
1

Recommended increment:
16

Restriction:
`Height >= 1`

## Complexity

O(2**`height`***`width`*).

## Result

`region_to_bin` always returns 2 (
H_MSG_TRUE)
. The behavior in case
of empty input (no regions given) can be set via
`set_system('no_object_result',<Result>)`
and the behavior in case of an empty input region via
`set_system('empty_region_result',<Result>)`.
If necessary, an exception is raised.

## Possible Predecessors

`threshold`,
`connection`,
`regiongrowing`,
`pouring`

## Possible Successors

`get_grayval`

## Alternatives

`region_to_label`,
`paint_region`,
`set_grayval`

## See also

`gen_image_proto`,
`paint_gray`

## Module

Foundation
