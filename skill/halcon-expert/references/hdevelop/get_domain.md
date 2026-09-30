# get_domain (Operator)

## Name

`get_domain` — Get the domain of an image.

## Signature

`get_domain(Image : Domain : : )`

## Description

The operator `get_domain` returns the definition domains
of all input images as a region.

## Execution Information

- Supports objects on compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Input images.

**`Domain`** (output_object)  region(-array) `→` object

Definition domains of input images.

## Possible Successors

`change_domain`,
`reduce_domain`,
`full_domain`

## See also

`change_domain`,
`reduce_domain`,
`full_domain`

## Module

Foundation
