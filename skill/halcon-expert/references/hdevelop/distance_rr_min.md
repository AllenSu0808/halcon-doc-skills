# distance_rr_min (Operator)

## Name

`distance_rr_min` — Minimum distance between the contour pixels of two regions each.

## Signature

`distance_rr_min(Regions1, Regions2 : : : MinDistance, Row1, Column1, Row2, Column2)`

## Description

The operator `distance_rr_min` calculates the minimum distance
of pairs of regions. If several regions are passed in
*`Regions1`* and *`Regions2`* the distance between the
contour pixels of each i-th element is calculated and then forms the
i-th entry in the output parameter *`MinDistance`*. The
Euclidean distance is used. The parameters (*`Row1`*,
*`Column1`*) and (*`Row2`*, *`Column2`*) indicate
the position on the contour of *`Regions1`* and
*`Regions2`*, respectively, that have the minimum distance.

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

**`Regions1`** (input_object)  region(-array) `→` object

Regions to be examined.

**`Regions2`** (input_object)  region(-array) `→` object

Regions to be examined.

**`MinDistance`** (output_control)  real(-array) `→`  (real)

Minimum distance between contours of the regions.

Assertion:
`0 <= MinDistance`

**`Row1`** (output_control)  point.y(-array) `→`  (integer)

Line index on contour in *`Regions1`*.

**`Column1`** (output_control)  point.x(-array) `→`  (integer)

Column index on contour in *`Regions1`*.

**`Row2`** (output_control)  point.y(-array) `→`  (integer)

Line index on contour in *`Regions2`*.

**`Column2`** (output_control)  point.x(-array) `→`  (integer)

Column index on contour in *`Regions2`*.

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
