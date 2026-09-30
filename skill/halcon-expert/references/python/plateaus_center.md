# plateaus_center (Operator)

## Name

`plateaus_center` — Detect the centers of all gray value plateaus.

## Signature

`def plateaus_center(image: HObject) -> HObject`

## Description

`plateaus_center` extracts all points from *`image`* with a gray
value greater or equal to the gray value of its neighbors (8-neighborhood)
and returns them in *`plateaus`*. If more than one of these points are
connected (plateau), their center of gravity is returned. Each plateau
center is returned as a separate region.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`image`** (input_object)  singlechannelimage(-array) `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real)

Input image.

**`plateaus`** (output_object)  region-array `→` HObject

Centers of gravity of the extracted plateaus as
regions (one region for each plateau).

## Possible Predecessors

`binomial_filter`,
`gauss_filter`,
`smooth_image`

## Possible Successors

`area_center`,
`get_region_points`,
`select_shape`

## Alternatives

`plateaus`,
`nonmax_suppression_amp`,
`local_max`

## See also

`monotony`,
`topographic_sketch`,
`corner_response`,
`texture_laws`

## Module

Foundation
