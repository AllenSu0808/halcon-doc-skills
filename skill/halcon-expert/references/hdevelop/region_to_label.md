# region_to_label (Operator)

## Name

`region_to_label` — Convert regions to a label image.

## Signature

`region_to_label(Region : ImageLabel : Type, Width, Height : )`

## Description

`region_to_label` converts the input regions into a label
image according to their index (1..n), i.e., the first region is
painted with the gray value 1, the second the gray value 2, etc.
Only positive gray values are used. For byte-images the
index is entered modulo 256.

Regions larger than the generated image are clipped appropriately.
If regions overlap the regions with the higher image are entered
(i.e., they are painted in the order in which they are contained in
the input regions). If so desired, the regions can be made
non-overlapping by calling [`expand_region`](expand_region.md).

The background, i.e., the area not covered by any regions, is set to
0. This can be used to test in which image range no region is present.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Region`** (input_object)  region(-array) `→` object

Regions to be converted.

**`ImageLabel`** (output_object)  image `→` object (byte / int2 / int4)

Result image of dimension Width * Height
containing the converted regions.

**`Type`** (input_control)  string `→`  (string)

Pixel type of the result image.

Default:
'int2'

List of values:
'byte', 'int2', 'int4', 'int8'

**`Width`** (input_control)  extent.y `→`  (integer)

Width of the image to be generated.

Default:
512

Suggested values:
64, 128, 256, 512, 1024

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

**`Height`** (input_control)  extent.x `→`  (integer)

Height of the image to be generated.

Default:
512

Suggested values:
64, 128, 256, 512, 1024

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

`region_to_label` always returns 2 (
H_MSG_TRUE)
. The behavior in
case of empty input (no regions given) can be set via
`set_system('no_object_result',<Result>)`
and the behavior in case of an empty input region via
`set_system('empty_region_result',<Result>)`.
If necessary, an exception is raised.

## Possible Predecessors

`threshold`,
`regiongrowing`,
`connection`,
`expand_region`

## Possible Successors

`get_grayval`,
`get_image_pointer1`

## Alternatives

`region_to_bin`,
`paint_region`

## See also

`label_to_region`

## Module

Foundation
