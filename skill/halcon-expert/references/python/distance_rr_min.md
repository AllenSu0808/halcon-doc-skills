# distance_rr_min (Operator)

## Name

`distance_rr_min` — Minimum distance between the contour pixels of two regions each.

## Signature

`def distance_rr_min(regions_1: HObject, regions_2: HObject) -> Tuple[Sequence[float], Sequence[int], Sequence[int], Sequence[int], Sequence[int]]`

`def distance_rr_min_s(regions_1: HObject, regions_2: HObject) -> Tuple[float, int, int, int, int]`

## Description

The operator `distance_rr_min` calculates the minimum distance
of pairs of regions. If several regions are passed in
*`regions_1`* and *`regions_2`* the distance between the
contour pixels of each i-th element is calculated and then forms the
i-th entry in the output parameter *`min_distance`*. The
Euclidean distance is used. The parameters (*`row_1`*,
*`column_1`*) and (*`row_2`*, *`column_2`*) indicate
the position on the contour of *`regions_1`* and
*`regions_2`*, respectively, that have the minimum distance.

The calculation is carried out by comparing all contour pixels (see
[`get_region_contour`](get_region_contour.md)). This means in particular that
holes in the regions are ignored. Furthermore, it is not checked
whether one region lies completely within the other region. In this
case, a minimum distance > 0 is returned. It is also not checked
whether both regions contain a nonempty intersection. In the latter
case, a minimum distance of 0 or > 0 can be returned, depending on
whether the contours of the regions contain a common point or not.

## Attention

Both input parameters must contain the same number of regions. The
regions must not be empty.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`regions_1`** (input_object)  region(-array) `→` HObject

Regions to be examined.

**`regions_2`** (input_object)  region(-array) `→` HObject

Regions to be examined.

**`min_distance`** (output_control)  real(-array) `→` Sequence[float]

Minimum distance between contours of the regions.

Assertion:
`0 <= MinDistance`

**`row_1`** (output_control)  point.y(-array) `→` Sequence[int]

Line index on contour in *`regions_1`*.

**`column_1`** (output_control)  point.x(-array) `→` Sequence[int]

Column index on contour in *`regions_1`*.

**`row_2`** (output_control)  point.y(-array) `→` Sequence[int]

Line index on contour in *`regions_2`*.

**`column_2`** (output_control)  point.x(-array) `→` Sequence[int]

Column index on contour in *`regions_2`*.

## Complexity

If N1,N2 are the lengths of the contours the runtime
complexity is O(N1 * N2).

## Result

The operator `distance_rr_min` returns the value 2 (
H_MSG_TRUE)
if the
input is not empty. Otherwise an exception is raised.

## Possible Predecessors

`threshold`,
`regiongrowing`,
`connection`

## Alternatives

`distance_rr_min_dil`,
`dilation1`,
`intersection`

## Module

Foundation
