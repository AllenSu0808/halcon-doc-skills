# PointsLepetit (Operator)

## Name

`PointsLepetit` — Detect points of interest using the Lepetit operator.

## Signature

`static void HOperatorSet.PointsLepetit(HObject image, HTuple radius, HTuple checkNeighbor, HTuple minCheckNeighborDiff, HTuple minScore, HTuple subpix, out HTuple row, out HTuple column)`

`void HImage.PointsLepetit(int radius, int checkNeighbor, int minCheckNeighborDiff, int minScore, string subpix, out HTuple row, out HTuple column)`

## Description

`PointsLepetit` extracts points of interest like corners or
blob-like structures from *`image`*. The *`image`* is first
smoothed with a median of size 3x3. Then, all the gray values on a circle
with radius *`radius`* around an interest point candidate
(*m*) are examined. The absolute differences of two diagonally
opposed gray values (*m1,m2*) on the circle to the central pixel
*m* is computed. At least one of these differences has to be
larger than *`minCheckNeighborDiff`*. All diagonally opposed pixels
on the circle must fulfill that condition. To suppress detection of
points at edges that have a small curvature (aliasing), it is possible
to compute *`checkNeighbor`* further differences of circle point
neighbors of *m1* and *m2* to the center, that as well
fulfill the above criteria. By computing all gray value differences of
the circle points to the center, a mean gray value difference is
determined. That value has to be larger than *`minScore`* and
allows to restrict the results to points with high contrast. By computing
the score of all eight neighbors of m, it is possible to fit a quadratic
equation to that. The maxima of that equation determines a subpixel
accurate interest point position. By setting the parameter *`subpix`*
to 'interpolation' (default) or 'none', it is possible to turn that refinement
step on or off. The resulting points are returned in *`row`* and
*`column`*. The operator `PointsLepetit` can especially be
used for very fast interest point extraction. The results are however
less robust than points extracted by [`PointsHarris`](points_harris.md) for example.

## Attention

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on domain level.

## Parameters

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / uint2)

Input image.

**`radius`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Radius of the circle.

Default:
3

Suggested values:
3, 5, 6, 7, 8, 9, 10, 15

**`checkNeighbor`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of checked neighbors on the circle.

Default:
1

Suggested values:
1, 2, 3, 5

**`minCheckNeighborDiff`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Threshold of gray value difference to each circle
point.

Default:
15

Suggested values:
10, 15, 20, 25, 30, 35, 40, 45, 60, 80

**`minScore`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Threshold of gray value difference to all circle points.

Default:
30

Suggested values:
5, 10, 15, 20, 25, 30

**`subpix`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Subpixel accuracy of point coordinates.

Default:
"interpolation"

List of values:
"interpolation", "none"

**`row`** (output_control)  point.y-array `→` [HTuple](HTuple.md) (*int* / long / double)

Row-coordinates of the detected points.

**`column`** (output_control)  point.x-array `→` [HTuple](HTuple.md) (*int* / long / double)

Column-coordinates of the detected points.

## Possible Predecessors

`GaussFilter`

## Alternatives

`PointsFoerstner`,
`PointsHarris`,
`PointsHarrisBinomial`,
`PointsSojka`

## Module

Foundation
