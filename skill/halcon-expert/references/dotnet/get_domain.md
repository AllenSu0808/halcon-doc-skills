# GetDomain (Operator)

## Name

`GetDomain` — Get the domain of an image.

## Signature

`static void HOperatorSet.GetDomain(HObject image, out HObject domain)`

`HRegion HImage.GetDomain()`

## Description

The operator `GetDomain` returns the definition domains
of all input images as a region.

## Execution Information

- Supports objects on compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Input images.

**`domain`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Definition domains of input images.

## Possible Successors

`ChangeDomain`,
`ReduceDomain`,
`FullDomain`

## See also

`ChangeDomain`,
`ReduceDomain`,
`FullDomain`

## Module

Foundation
