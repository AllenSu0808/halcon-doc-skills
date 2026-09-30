# rectangle1_domain (Operator)

## Name

`rectangle1_domain` — Reduce the domain of an image to a rectangle.

## Signature

`rectangle1_domain(Image : ImageReduced : Row1, Column1, Row2, Column2 : )`

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

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Input image.

**`ImageReduced`** (output_object)  (multichannel-)image(-array) `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Image with reduced definition domain.

**`Row1`** (input_control)  rectangle.origin.y `→`  (integer)

Line index of upper left corner of image area.

Default:
100

Suggested values:
10, 20, 50, 100, 200, 300, 500

Value range:
`0
≤
Row1
≤
1024`

**`Column1`** (input_control)  rectangle.origin.x `→`  (integer)

Column index of upper left corner of image area.

Default:
100

Suggested values:
10, 20, 50, 100, 200, 300, 500

Value range:
`0
≤
Column1
≤
1024`

**`Row2`** (input_control)  rectangle.origin.y `→`  (integer)

Line index of lower right corner of image area.

Default:
200

Suggested values:
10, 20, 50, 100, 200, 300, 500

Value range:
`0
≤
Row2
≤
1024`

**`Column2`** (input_control)  rectangle.origin.x `→`  (integer)

Column index of lower right corner of image area.

Default:
200

Suggested values:
10, 20, 50, 100, 200, 300, 500

Value range:
`0
≤
Column2
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
