# regiongrowing_mean (Operator)

## Name

`regiongrowing_mean` — Perform a region growing using mean gray values.

## Signature

`regiongrowing_mean(Image : Regions : StartRows, StartColumns, Tolerance, MinSize : )`

## Description

`regiongrowing_mean` performs a region growing using the mean
gray values of a region, starting from points given by
*`StartRows`* and *`StartColumns`*. At any point in
the process the mean gray value of the current region is calculated.
Gray values at the boundary of the region are added to the region if
they differ from the current mean by less than *`Tolerance`*.
Regions smaller than *`MinSize`* are suppressed.

If no starting points are given (empty tuples), the expansion
process starts at the upper leftmost point, and is continued with
the first unprocessed point after a region has been created.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Image`** (input_object)  singlechannelimage(-array) `→` object (byte / uint2 / int4)

Input image.

**`Regions`** (output_object)  region-array `→` object

Segmented regions.

**`StartRows`** (input_control)  point.y(-array) `→`  (integer)

Row coordinates of the starting points.

Default:
[]

Value range:
`0
≤
StartRows`

Minimum increment:
1

Recommended increment:
1

**`StartColumns`** (input_control)  point.x(-array) `→`  (integer)

Column coordinates of the starting points.

Default:
[]

Value range:
`0
≤
StartColumns`

Minimum increment:
1

Recommended increment:
1

**`Tolerance`** (input_control)  number `→`  (real)

Maximum deviation from the mean.

Default:
5.0

Suggested values:
0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 15.0, 17.0, 20.0, 25.0, 30.0, 40.0

Restriction:
`Tolerance > 0.0`

**`MinSize`** (input_control)  integer `→`  (integer)

Minimum size of a region.

Default:
100

Suggested values:
0, 10, 30, 50, 100, 500, 1000, 2000

Value range:
`0
≤
MinSize`

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
*'no_object_result'*, *'empty_region_result'*, and
*'store_empty_region'* with [`set_system`](set_system.md).
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
