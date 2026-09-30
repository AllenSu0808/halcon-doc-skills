# local_max (Operator)

## Name

`local_max` — Detect all local maxima in an image.

## Signature

`def local_max(image: HObject) -> HObject`

## Description

`local_max` extracts all points from *`image`* having a gray
value larger than the gray value of all its neighbors and returns them in
*`local_maxima`*. The neighborhood used can be set by
`set_system(::'neighborhood',<4/8>)`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`image`** (input_object)  singlechannelimage(-array) `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real)

Input image.

**`local_maxima`** (output_object)  region(-array) `→` HObject

Extracted local maxima as a region.

Number of elements:
LocalMaxima == Image

## Possible Predecessors

`binomial_filter`,
`gauss_filter`,
`smooth_image`

## Possible Successors

`get_region_points`,
`connection`

## Alternatives

`nonmax_suppression_amp`,
`plateaus`,
`plateaus_center`

## See also

`monotony`,
`topographic_sketch`,
`corner_response`,
`texture_laws`

## Module

Foundation
