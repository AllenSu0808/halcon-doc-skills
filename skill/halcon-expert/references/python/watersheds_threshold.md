# watersheds_threshold (Operator)

## Name

`watersheds_threshold` — Extract watershed basins from an image using a threshold.

## Signature

`def watersheds_threshold(image: HObject, threshold: Union[float, int]) -> HObject`

## Description

The operator `watersheds_threshold` segments regions (basins)
that are separated from each other by a watershed that has a
height of at least *`threshold`*.

In the first step, `watersheds_threshold` computes the watersheds
without applying a threshold, resulting in the same basins that would be
obtained when calling [`watersheds`](watersheds.md) (for more details please refer to
the description of [`watersheds`](watersheds.md)). In the second step, the basins are
successively merged if they are separated by a watershed that is smaller than
*`threshold`*. Let $B_{1}$ and $B_{2}$ be the minimum
gray values of two neighboring basins and W the minimum gray value
of the watershed that separates the two basins. The watershed is eliminated
and the two basins are merged if
$$\max \{W-B_{1},W-B_{2}\}<\texttt{Threshold}.$$
The thus obtained basins are returned in *`basins`*.

If *`threshold`* is set to *0*, `watersheds_threshold` is
comparable to [`watersheds`](watersheds.md) except that no watersheds but only expanded
basins are returned. If *`threshold`* is set to the maximum gray value
range of *`image`* then no two basins are separated by a watershed
exceeding *`threshold`*, and hence, *`basins`* will contain only
one region.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (input_object)  singlechannelimage `→` HObject (byte / uint2 / real)

Image to be segmented.

**`basins`** (output_object)  region-array `→` HObject

Segments found (dark basins).

**`threshold`** (input_control)  number `→` Union[float, int]

Threshold for the watersheds.

Default:
10

Suggested values:
0, 5, 10, 20, 30, 50

Restriction:
`Threshold >= 0`

## Result

[`watersheds`](watersheds.md) always returns 2 (
H_MSG_TRUE)
. The behavior with
respect to the input image and output regions can be determined by
setting the values of the flags *"no_object_result"*,
*"empty_region_result"*, and *"store_empty_region"*
with [`set_system`](set_system.md). If necessary, an exception is raised.

## Possible Predecessors

`binomial_filter`,
`gauss_filter`,
`smooth_image`,
`invert_image`

## Possible Successors

`expand_region`,
`select_shape`,
`reduce_domain`,
`opening`

## Alternatives

`watersheds`,
`pouring`,
`watersheds_marker`

## Module

Foundation
