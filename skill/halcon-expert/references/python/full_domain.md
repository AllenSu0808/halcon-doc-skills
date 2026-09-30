# full_domain (Operator)

## Name

`full_domain` — Expand the domain of an image to maximum.

## Signature

`def full_domain(image: HObject) -> HObject`

## Description

The operator `full_domain` enters a rectangle with the
edge length of the image as new definition domain. This means that
all pixels of the matrix are included in further operations. Thus
the same definition domain is obtained as by reading or generating
an image. The size of the matrix is not changed.

## Execution Information

- Supports objects on compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Input image.

**`image_full`** (output_object)  image(-array) `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Image with maximum definition domain.

## Possible Predecessors

`get_domain`

## Alternatives

`change_domain`,
`reduce_domain`

## See also

`get_domain`,
`gen_rectangle1`

## Module

Foundation
