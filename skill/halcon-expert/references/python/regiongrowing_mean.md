# regiongrowing_mean (Operator)

## Name

`regiongrowing_mean` — Perform a region growing using mean gray values.

## Signature

`def regiongrowing_mean(image: HObject, start_rows: MaybeSequence[int], start_columns: MaybeSequence[int], tolerance: float, min_size: int) -> HObject`

## Description

`regiongrowing_mean` performs a region growing using the mean
gray values of a region, starting from points given by
*`start_rows`* and *`start_columns`*. At any point in
the process the mean gray value of the current region is calculated.
Gray values at the boundary of the region are added to the region if
they differ from the current mean by less than *`tolerance`*.
Regions smaller than *`min_size`* are suppressed.

If no starting points are given (empty tuples), the expansion
process starts at the upper leftmost point, and is continued with
the first unprocessed point after a region has been created.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`image`** (input_object)  singlechannelimage(-array) `→` HObject (byte / uint2 / int4)

Input image.

**`regions`** (output_object)  region-array `→` HObject

Segmented regions.

**`start_rows`** (input_control)  point.y(-array) `→` MaybeSequence[int]

Row coordinates of the starting points.

Default:
[]

Value range:
`0
≤
start_rows`

Minimum increment:
1

Recommended increment:
1

**`start_columns`** (input_control)  point.x(-array) `→` MaybeSequence[int]

Column coordinates of the starting points.

Default:
[]

Value range:
`0
≤
start_columns`

Minimum increment:
1

Recommended increment:
1

**`tolerance`** (input_control)  number `→` float

Maximum deviation from the mean.

Default:
5.0

Suggested values:
0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 15.0, 17.0, 20.0, 25.0, 30.0, 40.0

Restriction:
`Tolerance > 0.0`

**`min_size`** (input_control)  integer `→` int

Minimum size of a region.

Default:
100

Suggested values:
0, 10, 30, 50, 100, 500, 1000, 2000

Value range:
`0
≤
min_size`

Minimum increment:
1

Recommended increment:
100

## Result

`regiongrowing_mean` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. The behavior with respect to the input images and output
regions can be determined by setting the values of the flags
*"no_object_result"*, *"empty_region_result"*, and
*"store_empty_region"* with [`set_system`](set_system.md).
If necessary, an exception is raised.

## Possible Predecessors

`binomial_filter`,
`gauss_filter`,
`sigma_image`,
`anisotropic_diffusion`,
`median_image`,
`mean_image`

## Possible Successors

`select_shape`,
`reduce_domain`,
`opening`,
`expand_region`

## Alternatives

`regiongrowing`,
`regiongrowing_n`

## Module

Foundation
