# change_domain (Operator)

## Name

`change_domain` — Change definition domain of an image.

## Signature

`change_domain(Image, NewDomain : ImageNew : : )`

## Description

The operator `change_domain` uses the indicated region as
the new definition domain. Unlike the operator
[`reduce_domain`](reduce_domain.md) it does not form the intersection of the
previous definition domain, i.e., the size of the matrix is not
changed. This implies in particular, that the region must not
exceed the image matrix, otherwise using such inconsistent iconic
objects during subsequent operations will likely lead to errors
or system crashes.

## Attention

Due to running time the transferred region is not checked for
consistency (i.e., whether it fits with the image matrix).
Incorrect regions lead to system hang-ups during subsequent
operations.

## Execution Information

- Supports objects on compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Input image.

**`NewDomain`** (input_object)  region `→` object

New definition domain.

**`ImageNew`** (output_object)  image(-array) `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Image with new definition domain.

## Possible Predecessors

`get_domain`

## Alternatives

`reduce_domain`

## See also

`full_domain`,
`get_domain`,
`intersection`

## Module

Foundation
