# RegionToLabel (Operator)

## Name

`RegionToLabel` — Convert regions to a label image.

## Signature

`static void HOperatorSet.RegionToLabel(HObject region, out HObject imageLabel, HTuple type, HTuple width, HTuple height)`

`HImage HRegion.RegionToLabel(string type, int width, int height)`

## Description

`RegionToLabel` converts the input regions into a label
image according to their index (1..n), i.e., the first region is
painted with the gray value 1, the second the gray value 2, etc.
Only positive gray values are used. For byte-images the
index is entered modulo 256.

Regions larger than the generated image are clipped appropriately.
If regions overlap the regions with the higher image are entered
(i.e., they are painted in the order in which they are contained in
the input regions). If so desired, the regions can be made
non-overlapping by calling [`ExpandRegion`](expand_region.md).

The background, i.e., the area not covered by any regions, is set to
0. This can be used to test in which image range no region is present.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Regions to be converted.

**`imageLabel`** (output_object)  image `→` [HImage](HImage.md) (byte / int2 / int4)

Result image of dimension Width * Height
containing the converted regions.

**`type`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Pixel type of the result image.

Default:
"int2"

List of values:
"byte", "int2", "int4", "int8"

**`width`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long)

Width of the image to be generated.

Default:
512

Suggested values:
64, 128, 256, 512, 1024

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

**`height`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

Height of the image to be generated.

Default:
512

Suggested values:
64, 128, 256, 512, 1024

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

`RegionToLabel` always returns 2 (
H_MSG_TRUE)
. The behavior in
case of empty input (no regions given) can be set via
`set_system('no_object_result',<Result>)`
and the behavior in case of an empty input region via
`set_system('empty_region_result',<Result>)`.
If necessary, an exception is raised.

## Possible Predecessors

`Threshold`,
`Regiongrowing`,
`Connection`,
`ExpandRegion`

## Possible Successors

`GetGrayval`,
`GetImagePointer1`

## Alternatives

`RegionToBin`,
`PaintRegion`

## See also

`LabelToRegion`

## Module

Foundation
