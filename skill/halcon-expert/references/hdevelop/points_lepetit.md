# points_lepetit (Operator)

## Name

`points_lepetit` — Detect points of interest using the Lepetit operator.

## Signature

`points_lepetit(Image : : Radius, CheckNeighbor, MinCheckNeighborDiff, MinScore, Subpix : Row, Column)`

## Description

`points_lepetit` extracts points of interest like corners or
blob-like structures from *`Image`*. The *`Image`* is first
smoothed with a median of size 3x3. Then, all the gray values on a circle
with radius *`Radius`* around an interest point candidate
(*m*) are examined. The absolute differences of two diagonally
opposed gray values (*m1,m2*) on the circle to the central pixel
*m* is computed. At least one of these differences has to be
larger than *`MinCheckNeighborDiff`*. All diagonally opposed pixels
on the circle must fulfill that condition. To suppress detection of
points at edges that have a small curvature (aliasing), it is possible
to compute *`CheckNeighbor`* further differences of circle point
neighbors of *m1* and *m2* to the center, that as well
fulfill the above criteria. By computing all gray value differences of
the circle points to the center, a mean gray value difference is
determined. That value has to be larger than *`MinScore`* and
allows to restrict the results to points with high contrast. By computing
the score of all eight neighbors of m, it is possible to fit a quadratic
equation to that. The maxima of that equation determines a subpixel
accurate interest point position. By setting the parameter *`Subpix`*
to 'interpolation' (default) or 'none', it is possible to turn that refinement
step on or off. The resulting points are returned in *`Row`* and
*`Column`*. The operator `points_lepetit` can especially be
used for very fast interest point extraction. The results are however
less robust than points extracted by [`points_harris`](points_harris.md) for example.

## Attention

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on domain level.

## Parameters

**`Image`** (input_object)  singlechannelimage `→` object (byte / uint2)

Input image.

**`Radius`** (input_control)  integer `→`  (integer)

Radius of the circle.

Default:
3

Suggested values:
3, 5, 6, 7, 8, 9, 10, 15

**`CheckNeighbor`** (input_control)  integer `→`  (integer)

Number of checked neighbors on the circle.

Default:
1

Suggested values:
1, 2, 3, 5

**`MinCheckNeighborDiff`** (input_control)  integer `→`  (integer)

Threshold of gray value difference to each circle
point.

Default:
15

Suggested values:
10, 15, 20, 25, 30, 35, 40, 45, 60, 80

**`MinScore`** (input_control)  integer `→`  (integer)

Threshold of gray value difference to all circle points.

Default:
30

Suggested values:
5, 10, 15, 20, 25, 30

**`Subpix`** (input_control)  string `→`  (string)

Subpixel accuracy of point coordinates.

Default:
'interpolation'

List of values:
'interpolation', 'none'

**`Row`** (output_control)  point.y-array `→`  (integer / real)

Row-coordinates of the detected points.

**`Column`** (output_control)  point.x-array `→`  (integer / real)

Column-coordinates of the detected points.

## Possible Predecessors

`gauss_filter`

## Alternatives

`points_foerstner`,
`points_harris`,
`points_harris_binomial`,
`points_sojka`

## Module

Foundation
