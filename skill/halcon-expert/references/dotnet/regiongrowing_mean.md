# RegiongrowingMean (Operator)

## Name

`RegiongrowingMean` — Perform a region growing using mean gray values.

## Signature

`static void HOperatorSet.RegiongrowingMean(HObject image, out HObject regions, HTuple startRows, HTuple startColumns, HTuple tolerance, HTuple minSize)`

`HRegion HImage.RegiongrowingMean(HTuple startRows, HTuple startColumns, double tolerance, int minSize)`

`HRegion HImage.RegiongrowingMean(int startRows, int startColumns, double tolerance, int minSize)`

## Description

`RegiongrowingMean` performs a region growing using the mean
gray values of a region, starting from points given by
*`startRows`* and *`startColumns`*. At any point in
the process the mean gray value of the current region is calculated.
Gray values at the boundary of the region are added to the region if
they differ from the current mean by less than *`tolerance`*.
Regions smaller than *`minSize`* are suppressed.

If no starting points are given (empty tuples), the expansion
process starts at the upper leftmost point, and is continued with
the first unprocessed point after a region has been created.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`image`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / uint2 / int4)

Input image.

**`regions`** (output_object)  region-array `→` [HRegion](HRegion.md)

Segmented regions.

**`startRows`** (input_control)  point.y(-array) `→` [HTuple](HTuple.md) (*int* / long)

Row coordinates of the starting points.

Default:
[]

Value range:
`0
≤
startRows`

Minimum increment:
1

Recommended increment:
1

**`startColumns`** (input_control)  point.x(-array) `→` [HTuple](HTuple.md) (*int* / long)

Column coordinates of the starting points.

Default:
[]

Value range:
`0
≤
startColumns`

Minimum increment:
1

Recommended increment:
1

**`tolerance`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Maximum deviation from the mean.

Default:
5.0

Suggested values:
0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 15.0, 17.0, 20.0, 25.0, 30.0, 40.0

Restriction:
`Tolerance > 0.0`

**`minSize`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Minimum size of a region.

Default:
100

Suggested values:
0, 10, 30, 50, 100, 500, 1000, 2000

Value range:
`0
≤
minSize`

Minimum increment:
1

Recommended increment:
100

## Result

`RegiongrowingMean` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. The behavior with respect to the input images and output
regions can be determined by setting the values of the flags
*"no_object_result"*, *"empty_region_result"*, and
*"store_empty_region"* with [`SetSystem`](set_system.md).
If necessary, an exception is raised.

## Possible Predecessors

`BinomialFilter`,
`GaussFilter`,
`SigmaImage`,
`AnisotropicDiffusion`,
`MedianImage`,
`MeanImage`

## Possible Successors

`SelectShape`,
`ReduceDomain`,
`Opening`,
`ExpandRegion`

## Alternatives

`Regiongrowing`,
`RegiongrowingN`

## Module

Foundation
