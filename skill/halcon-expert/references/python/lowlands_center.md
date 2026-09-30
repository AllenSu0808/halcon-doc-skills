# lowlands_center (Operator)

## Name

`lowlands_center` — Detect the centers of all gray value lowlands.

## Signature

`def lowlands_center(image: HObject) -> HObject`

## Description

`lowlands_center` extracts all points from *`image`* with a gray
value less or equal to the gray value of its neighbors (8-neighborhood) and
returns them in *`lowlands`*. If more than one of these points are
connected (lowland), their center of gravity is returned. Each lowland is
returned as a separate region.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`image`** (input_object)  singlechannelimage(-array) `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real)

Image to be processed.

**`lowlands`** (output_object)  region-array `→` HObject

Centers of gravity of the extracted lowlands as
regions (one region for each lowland).

## Possible Predecessors

`binomial_filter`,
`gauss_filter`,
`smooth_image`

## Possible Successors

`area_center`,
`get_region_points`,
`select_shape`

## Alternatives

`lowlands`,
`gray_skeleton`,
`local_min`

## See also

`monotony`,
`topographic_sketch`,
`corner_response`,
`texture_laws`

## Module

Foundation
