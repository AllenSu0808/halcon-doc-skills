# ReduceDomain (Operator)

## Name

`ReduceDomain` — Reduce the domain of an image.

## Signature

`static void HOperatorSet.ReduceDomain(HObject image, HObject region, out HObject imageReduced)`

`HImage HImage.ReduceDomain(HRegion region)`

## Description

The operator `ReduceDomain` reduces the definition domain of the given image
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

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Input image.

**`region`** (input_object)  region `→` [HRegion](HRegion.md)

New definition domain.

**`imageReduced`** (output_object)  image(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Image with reduced definition domain.

## Possible Predecessors

`GetDomain`

## Alternatives

`ChangeDomain`,
`Rectangle1Domain`,
`AddChannels`

## See also

`FullDomain`,
`GetDomain`,
`Intersection`

## Module

Foundation
