# Rectangle1Domain (Operator)

## Name

`Rectangle1Domain` — Reduce the domain of an image to a rectangle.

## Signature

`static void HOperatorSet.Rectangle1Domain(HObject image, out HObject imageReduced, HTuple row1, HTuple column1, HTuple row2, HTuple column2)`

`HImage HImage.Rectangle1Domain(int row1, int column1, int row2, int column2)`

## Description

The operator `Rectangle1Domain` reduces the definition domain
of the given image to the specified rectangle.
The size of the matrix is not changed.

## Execution Information

- Supports objects on compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Input image.

**`imageReduced`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Image with reduced definition domain.

**`row1`** (input_control)  rectangle.origin.y `→` [HTuple](HTuple.md) (*int* / long)

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

**`column1`** (input_control)  rectangle.origin.x `→` [HTuple](HTuple.md) (*int* / long)

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

**`row2`** (input_control)  rectangle.origin.y `→` [HTuple](HTuple.md) (*int* / long)

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

**`column2`** (input_control)  rectangle.origin.x `→` [HTuple](HTuple.md) (*int* / long)

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

## Possible Predecessors

`GetDomain`

## Alternatives

`ChangeDomain`,
`ReduceDomain`,
`AddChannels`

## See also

`FullDomain`,
`GetDomain`,
`Intersection`

## Module

Foundation
