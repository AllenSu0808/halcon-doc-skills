# FullDomain (Operator)

## Name

`FullDomain` — Expand the domain of an image to maximum.

## Signature

`static void HOperatorSet.FullDomain(HObject image, out HObject imageFull)`

`HImage HImage.FullDomain()`

## Description

The operator `FullDomain` enters a rectangle with the
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

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Input image.

**`imageFull`** (output_object)  image(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Image with maximum definition domain.

## Possible Predecessors

`GetDomain`

## Alternatives

`ChangeDomain`,
`ReduceDomain`

## See also

`GetDomain`,
`GenRectangle1`

## Module

Foundation
