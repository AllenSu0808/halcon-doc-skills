# reduce_domain (Operator)

## Name

`reduce_domain` — Reduce the domain of an image.

## Signature

`def reduce_domain(image: HObject, region: HObject) -> HObject`

## Description

The operator `reduce_domain` reduces the definition domain of the given image
to the indicated region. The new definition domain is calculated as
the intersection of the old definition domain with the region.
Thus, the new definition domain can be a subset of the region. The
size of the matrix is not changed.

## Execution Information

- Supports objects on compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Input image.

**`region`** (input_object)  region `→` HObject

New definition domain.

**`image_reduced`** (output_object)  image(-array) `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Image with reduced definition domain.

## Possible Predecessors

`get_domain`

## Alternatives

`change_domain`,
`rectangle1_domain`,
`add_channels`

## See also

`full_domain`,
`get_domain`,
`intersection`

## Module

Foundation
