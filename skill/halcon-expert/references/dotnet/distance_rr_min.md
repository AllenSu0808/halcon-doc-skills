# DistanceRrMin (Operator)

## Name

`DistanceRrMin` — Minimum distance between the contour pixels of two regions each.

## Signature

`static void HOperatorSet.DistanceRrMin(HObject regions1, HObject regions2, out HTuple minDistance, out HTuple row1, out HTuple column1, out HTuple row2, out HTuple column2)`

`HTuple HRegion.DistanceRrMin(HRegion regions2, out HTuple row1, out HTuple column1, out HTuple row2, out HTuple column2)`

`double HRegion.DistanceRrMin(HRegion regions2, out int row1, out int column1, out int row2, out int column2)`

## Description

The operator `DistanceRrMin` calculates the minimum distance
of pairs of regions. If several regions are passed in
*`regions1`* and *`regions2`* the distance between the
contour pixels of each i-th element is calculated and then forms the
i-th entry in the output parameter *`minDistance`*. The
Euclidean distance is used. The parameters (*`row1`*,
*`column1`*) and (*`row2`*, *`column2`*) indicate
the position on the contour of *`regions1`* and
*`regions2`*, respectively, that have the minimum distance.

The calculation is carried out by comparing all contour pixels (see
[`GetRegionContour`](get_region_contour.md)). This means in particular that
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

**`regions1`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Regions to be examined.

**`regions2`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Regions to be examined.

**`minDistance`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Minimum distance between contours of the regions.

Assertion:
`0 <= MinDistance`

**`row1`** (output_control)  point.y(-array) `→` [HTuple](HTuple.md) (*int* / long)

Line index on contour in *`regions1`*.

**`column1`** (output_control)  point.x(-array) `→` [HTuple](HTuple.md) (*int* / long)

Column index on contour in *`regions1`*.

**`row2`** (output_control)  point.y(-array) `→` [HTuple](HTuple.md) (*int* / long)

Line index on contour in *`regions2`*.

**`column2`** (output_control)  point.x(-array) `→` [HTuple](HTuple.md) (*int* / long)

Column index on contour in *`regions2`*.

## Complexity

If N1,N2 are the lengths of the contours the runtime
complexity is O(N1 * N2).

## Result

The operator `DistanceRrMin` returns the value 2 (
H_MSG_TRUE)
if the
input is not empty. Otherwise an exception is raised.

## Possible Predecessors

`Threshold`,
`Regiongrowing`,
`Connection`

## Alternatives

`DistanceRrMinDil`,
`Dilation1`,
`Intersection`

## Module

Foundation
