# local_min (Operator)

## Name

`local_min` — Detect all local minima in an image.

## Signature

`def local_min(image: HObject) -> HObject`

## Description

`local_min` extracts all points from *`image`* having a gray
value smaller than the gray value of all its neighbors and returns them in
*`local_minima`*. The neighborhood used can be set by
`set_system(::'neighborhood',<4/8>)`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`image`** (input_object)  singlechannelimage(-array) `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real)

Image to be processed.

**`local_minima`** (output_object)  region(-array) `→` HObject

Extracted local minima as regions.

Number of elements:
LocalMinima == Image

## Possible Predecessors

`binomial_filter`,
`gauss_filter`,
`smooth_image`

## Possible Successors

`get_region_points`,
`connection`

## Alternatives

`gray_skeleton`,
`lowlands`,
`lowlands_center`

## See also

`monotony`,
`topographic_sketch`,
`corner_response`,
`texture_laws`

## Module

Foundation
