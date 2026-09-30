# rectangle1_domain (Operator)

## Name

`rectangle1_domain` — Reduce the domain of an image to a rectangle.

## Signature

`def rectangle1_domain(image: HObject, row_1: int, column_1: int, row_2: int, column_2: int) -> HObject`

## Description

The operator `rectangle1_domain` reduces the definition domain
of the given image to the specified rectangle.
The size of the matrix is not changed.

## Execution Information

- Supports objects on compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Input image.

**`image_reduced`** (output_object)  (multichannel-)image(-array) `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Image with reduced definition domain.

**`row_1`** (input_control)  rectangle.origin.y `→` int

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

**`column_1`** (input_control)  rectangle.origin.x `→` int

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

**`row_2`** (input_control)  rectangle.origin.y `→` int

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

**`column_2`** (input_control)  rectangle.origin.x `→` int

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

## Possible Predecessors

`get_domain`

## Alternatives

`change_domain`,
`reduce_domain`,
`add_channels`

## See also

`full_domain`,
`get_domain`,
`intersection`

## Module

Foundation
