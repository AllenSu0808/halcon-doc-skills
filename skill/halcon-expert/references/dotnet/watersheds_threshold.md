# WatershedsThreshold (Operator)

## Name

`WatershedsThreshold` — Extract watershed basins from an image using a threshold.

## Signature

`static void HOperatorSet.WatershedsThreshold(HObject image, out HObject basins, HTuple threshold)`

`HRegion HImage.WatershedsThreshold(HTuple threshold)`

`HRegion HImage.WatershedsThreshold(int threshold)`

## Description

The operator `WatershedsThreshold` segments regions (basins)
that are separated from each other by a watershed that has a
height of at least *`threshold`*.

In the first step, `WatershedsThreshold` computes the watersheds
without applying a threshold, resulting in the same basins that would be
obtained when calling [`Watersheds`](watersheds.md) (for more details please refer to
the description of [`Watersheds`](watersheds.md)). In the second step, the basins are
successively merged if they are separated by a watershed that is smaller than
*`threshold`*. Let $B_{1}$ and $B_{2}$ be the minimum
gray values of two neighboring basins and W the minimum gray value
of the watershed that separates the two basins. The watershed is eliminated
and the two basins are merged if
$$\max \{W-B_{1},W-B_{2}\}<\texttt{Threshold}.$$
The thus obtained basins are returned in *`basins`*.

If *`threshold`* is set to *0*, `WatershedsThreshold` is
comparable to [`Watersheds`](watersheds.md) except that no watersheds but only expanded
basins are returned. If *`threshold`* is set to the maximum gray value
range of *`image`* then no two basins are separated by a watershed
exceeding *`threshold`*, and hence, *`basins`* will contain only
one region.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / uint2 / real)

Image to be segmented.

**`basins`** (output_object)  region-array `→` [HRegion](HRegion.md)

Segments found (dark basins).

**`threshold`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long / double)

Threshold for the watersheds.

Default:
10

Suggested values:
0, 5, 10, 20, 30, 50

Restriction:
`Threshold >= 0`

## Result

[`Watersheds`](watersheds.md) always returns 2 (
H_MSG_TRUE)
. The behavior with
respect to the input image and output regions can be determined by
setting the values of the flags *"no_object_result"*,
*"empty_region_result"*, and *"store_empty_region"*
with [`SetSystem`](set_system.md). If necessary, an exception is raised.

## Possible Predecessors

`BinomialFilter`,
`GaussFilter`,
`SmoothImage`,
`InvertImage`

## Possible Successors

`ExpandRegion`,
`SelectShape`,
`ReduceDomain`,
`Opening`

## Alternatives

`Watersheds`,
`Pouring`,
`WatershedsMarker`

## Module

Foundation
