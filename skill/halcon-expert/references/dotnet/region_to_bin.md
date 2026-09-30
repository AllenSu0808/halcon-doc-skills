# RegionToBin (Operator)

## Name

`RegionToBin` — Convert a region into a binary byte-image.

## Signature

`static void HOperatorSet.RegionToBin(HObject region, out HObject binImage, HTuple foregroundGray, HTuple backgroundGray, HTuple width, HTuple height)`

`HImage HRegion.RegionToBin(int foregroundGray, int backgroundGray, int width, int height)`

## Description

`RegionToBin` converts the input region given in
*`region`* into a byte-image and assigns a gray
value of *`foregroundGray`* to all pixels in the region. If
the input region is larger than the generated image, it is clipped
at the image borders. The background is set to
*`backgroundGray`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Regions to be converted.

**`binImage`** (output_object)  image `→` [HImage](HImage.md) (byte)

Result image of dimension Width * Height
containing the converted regions.

**`foregroundGray`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Gray value in which the regions are displayed.

Default:
255

Suggested values:
0, 1, 50, 100, 128, 150, 200, 254, 255

Value range:
`0
≤
foregroundGray
≤
255` (lin)

Recommended increment:
1

**`backgroundGray`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Gray value in which the background is displayed.

Default:
0

Suggested values:
0, 1, 50, 100, 128, 150, 200, 254, 255

Value range:
`0
≤
backgroundGray
≤
255` (lin)

Recommended increment:
1

**`width`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

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

**`height`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long)

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

`RegionToBin` always returns 2 (
H_MSG_TRUE)
. The behavior in case
of empty input (no regions given) can be set via
`set_system('no_object_result',<Result>)`
and the behavior in case of an empty input region via
`set_system('empty_region_result',<Result>)`.
If necessary, an exception is raised.

## Possible Predecessors

`Threshold`,
`Connection`,
`Regiongrowing`,
`Pouring`

## Possible Successors

`GetGrayval`

## Alternatives

`RegionToLabel`,
`PaintRegion`,
`SetGrayval`

## See also

`GenImageProto`,
`PaintGray`

## Module

Foundation
