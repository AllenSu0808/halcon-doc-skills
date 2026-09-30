# region_to_bin (Operator)

## Name

`region_to_bin` — Convert a region into a binary byte-image.

## Signature

`region_to_bin(Region : BinImage : ForegroundGray, BackgroundGray, Width, Height : )`

## Description

`region_to_bin` converts the input region given in
*`Region`* into a byte-image and assigns a gray
value of *`ForegroundGray`* to all pixels in the region. If
the input region is larger than the generated image, it is clipped
at the image borders. The background is set to
*`BackgroundGray`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Region`** (input_object)  region(-array) `→` object

Regions to be converted.

**`BinImage`** (output_object)  image `→` object (byte)

Result image of dimension Width * Height
containing the converted regions.

**`ForegroundGray`** (input_control)  integer `→`  (integer)

Gray value in which the regions are displayed.

Default:
255

Suggested values:
0, 1, 50, 100, 128, 150, 200, 254, 255

Value range:
`0
≤
ForegroundGray
≤
255` (lin)

Recommended increment:
1

**`BackgroundGray`** (input_control)  integer `→`  (integer)

Gray value in which the background is displayed.

Default:
0

Suggested values:
0, 1, 50, 100, 128, 150, 200, 254, 255

Value range:
`0
≤
BackgroundGray
≤
255` (lin)

Recommended increment:
1

**`Width`** (input_control)  extent.x `→`  (integer)

Width of the image to be generated.

Default:
512

Suggested values:
256, 512, 1024

Value range:
`1
≤
Width
≤
1024` (lin)

Minimum increment:
1

Recommended increment:
16

Restriction:
`Width >= 1`

**`Height`** (input_control)  extent.y `→`  (integer)

Height of the image to be generated.

Default:
512

Suggested values:
256, 512, 1024

Value range:
`1
≤
Height
≤
1024` (lin)

Minimum increment:
1

Recommended increment:
16

Restriction:
`Height >= 1`

## Complexity

O(2**`Height`***`Width`*).

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
