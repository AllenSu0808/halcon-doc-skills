# moments_any_points_xld (Operator)

## Name

`moments_any_points_xld` — Arbitrary geometric moments of contours or polygons treated as point
clouds.

## Signature

`def moments_any_points_xld(xld: HObject, mode: str, area: MaybeSequence[float], center_row: MaybeSequence[float], center_col: MaybeSequence[float], p: MaybeSequence[int], q: MaybeSequence[int]) -> Sequence[float]`

`def moments_any_points_xld_s(xld: HObject, mode: str, area: MaybeSequence[float], center_row: MaybeSequence[float], center_col: MaybeSequence[float], p: MaybeSequence[int], q: MaybeSequence[int]) -> float`

## Description

`moments_any_points_xld` calculates arbitrary moments
*`m`* of the point clouds given by the contours or polygons
*`xld`* (i.e., the order of the points in the contour or
polygon is not taken into account).

The computed moments are normalized depending on the desired mode
*`mode`*:

- **'unnormalized':** —

  No normalization.
  The computed moment $M_{p,q}$ is:
  $$M_{p,q} = \sum_{i=0}^{n-1} r_i^p C_i^q$$ ![figure](../assets/2d8b8950fd3e2461.svg)
- **'unnormalized_central':** —

  Shift the contour points by their centroid
  $\left[ \bar{r}, \bar{c} \right]$ ![figure](../assets/89496e8aa861c69e.svg)
  = [*`center_row`*, *`center_col`*]:
  $$M_{p,q} = \sum_{i=0}^{n-1} (r_i - \bar{r})^{p} (c_i - \bar{c})^{q}$$ ![figure](../assets/8cefc49246b9b5f9.svg)
- **'normalized':** —

  Normalization by the area A = *`area`*
  from *`xld`*:
  $$M_{p,q} = \frac{-1}{A} \sum_{i=0}^{n-1} r_i^p C_i^q$$ ![figure](../assets/06511300778a86df.svg)
- **'central':** —

  Normalization by the area A = *`area`*
  and a shift of the contour points by their centroid
  $\left[ \bar{r}, \bar{c} \right]$ ![figure](../assets/89496e8aa861c69e.svg)
  = [*`center_row`*, *`center_col`*]:
  $$M_{p,q} = \frac{1}{A} \sum_{i=0}^{n-1} (r_i - \bar{r})^p (c_i - \bar{c})^q$$ ![figure](../assets/fa45fd733e30c10d.svg)

For the normalization of the moments three specific values are
used: The area *`area`* and the coordinates
*`center_row`*,*`center_col`* of it's centroid (this values can be
computed with [`area_center_points_xld`](area_center_points_xld.md)).

If the contour or polygon is closed (end point = start point), the end point
of the contour or polygon is not taken into account to avoid that it receives
twice the weight of the other points.

[`moments_any_xld`](moments_any_xld.md) should be used if the contour *`xld`*
intersects itself or if it is not possible to close the contour using a line
from end to start point without self-intersection, because in this case
[`moments_any_xld`](moments_any_xld.md) does not produce useful results. To test whether the
contours or polygons intersect themselves,
[`test_self_intersection_xld`](test_self_intersection_xld.md) can be used.

If more than one contour or polygon is passed, *`m`* contains
all desired moments of the first contour/polygon followed by all the
moments of the second contour/polygon and so forth.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`xld`** (input_object)  xld(-array) `→` HObject

Contours or polygons to be examined.

**`mode`** (input_control)  string `→` str

Computation mode.

Default:
"unnormalized"

Suggested values:
"unnormalized", "unnormalized_central", "normalized", "central"

**`area`** (input_control)  real(-array) `→` MaybeSequence[float]

Area enclosed by the contour or polygon.

**`center_row`** (input_control)  point.y(-array) `→` MaybeSequence[float]

Row coordinate of the centroid.

**`center_col`** (input_control)  point.x(-array) `→` MaybeSequence[float]

Column coordinate of the centroid.

**`p`** (input_control)  point.x(-array) `→` MaybeSequence[int]

First index of the desired moments
$M_{p,q}$.

Default:
1

Suggested values:
0, 1, 2, 3, 4

**`q`** (input_control)  point.x(-array) `→` MaybeSequence[int]

Second index of the desired moments
$M_{p,q}$.

Default:
1

Suggested values:
0, 1, 2, 3, 4

**`m`** (output_control)  real(-array) `→` Sequence[float]

The computed moments.

## Complexity

Let n be the number of points of the contour or polygon.
Then the run time is O(n).

## Result

`moments_any_points_xld` returns 2 (
H_MSG_TRUE)
if the input is not
empty. If the input is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`. If necessary,
an exception is raised.

## Possible Predecessors

`area_center_points_xld`,
`gen_contours_skeleton_xld`,
`smooth_contours_xld`,
`gen_polygons_xld`

## Alternatives

`moments_points_xld`,
`moments_any_xld`

## See also

`moments_points_xld`,
`area_center_points_xld`,
`moments_region_2nd`,
`area_center`

## Module

Foundation
