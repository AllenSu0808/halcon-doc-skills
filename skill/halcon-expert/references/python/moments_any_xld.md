# moments_any_xld (Operator)

## Name

`moments_any_xld` — Arbitrary geometric moments of contours or polygons.

## Signature

`def moments_any_xld(xld: HObject, mode: str, point_order: MaybeSequence[str], area: MaybeSequence[float], center_row: MaybeSequence[float], center_col: MaybeSequence[float], p: MaybeSequence[int], q: MaybeSequence[int]) -> Sequence[float]`

`def moments_any_xld_s(xld: HObject, mode: str, point_order: MaybeSequence[str], area: MaybeSequence[float], center_row: MaybeSequence[float], center_col: MaybeSequence[float], p: MaybeSequence[int], q: MaybeSequence[int]) -> float`

## Description

`moments_any_xld` calculates arbitrary moments *`m`* of
the regions enclosed by the contours or polygons *`xld`*. The
moments are computed by applying Green's theorem using only the
points on the contour or polygon, i.e., no region is generated
explicitly for the purpose of calculating the features. It is
assumed that the contours or polygons are closed. If this is not
the case `moments_any_xld` will artificially close the
contours or polygons.

It should be noted that `moments_any_xld` only returns useful
results if the contour or polygon encloses a region in the plane. In
particular, the contour or polygon must not intersect itself. This
is particularly important if open contours or polygons are passed
because they are closed automatically, which can produce a
self-intersection. To test whether the contours or polygons
intersect themselves, [`test_self_intersection_xld`](test_self_intersection_xld.md) can be
used. If the contour or polygon intersects itself, useful values
for the moments can be calculated with
[`moments_any_points_xld`](moments_any_points_xld.md).

The computed moments are normalized depending on the desired mode
*`mode`*:

- **'unnormalized':** —

  No normalization. Let $R$ be the enclosed
  image region. Then the computed moment $M_{p,q}$ is
  equivalent to:

  $M_{p,q} = \int_{R}^{?} r^{p} c^{q} \, dr \, dc$ ![figure](../assets/d5f76e40df33eaaa.svg)
- **'unnormalized_central':** —

  Shift the region by its centroid
  $\left[ \bar{\mathbf{r}}, \bar{\mathbf{c}} \right] =$ ![figure](../assets/738ed11693cf5ce0.svg) [*`center_row`*, *`center_col`*]:

  $M_{p,q} = \int_{R}^{ } (r - \bar{r})^{p} (c - \bar{c})^{q} \, dr \, dc$ ![figure](../assets/df6eda4330afad19.svg)
- **'normalized':** —

  Normalization by the area $A=$ *`area`*
  of the enclosed image region:

  $M_{p,q} = \frac{1}{A} \int_{R}^{?} r^{p} c^{q} \, dr \, dc$ ![figure](../assets/2bb30ee03d5e67ae.svg)
- **'central':** —

  Normalization by the area $A=$ *`area`*
  of the enclosed image region and a shift of the region by it's centroid
  $\left[ \bar{\mathbf{r}}, \bar{\mathbf{c}} \right] =$ ![figure](../assets/738ed11693cf5ce0.svg) [*`center_row`*, *`center_col`*]:

  $M_{p,q} = \frac{1}{A} \int_{R}^{ } \left(r - \bar{r}\right)^{p} \left(c - \bar{c}\right)^{q} \, dr \, dc$ ![figure](../assets/2bfda6305a79d94d.svg)

For the normalization of the moments three specific moments are
used: The area *`area`* of the enclosed image region and the
coordinates *`center_row`*,*`center_col`* of it's centroid (this
values can be calculated with [`area_center_xld`](area_center_xld.md)). In addition to that
`moments_any_xld` expects information about the point order of
the input contours/polygons in *`point_order`*, see
[`area_center_xld`](area_center_xld.md) again.

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

**`point_order`** (input_control)  string(-array) `→` MaybeSequence[str]

Point order along the boundary.

Default:
"positive"

Suggested values:
"positive", "negative"

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

`moments_any_xld` returns 2 (
H_MSG_TRUE)
if the input is not empty. If
the input is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`. If
necessary, an exception is raised.

## Possible Predecessors

`area_center_xld`,
`gen_contours_skeleton_xld`,
`smooth_contours_xld`,
`gen_polygons_xld`

## Alternatives

`moments_xld`,
`moments_any_points_xld`

## See also

`moments_xld`,
`area_center_xld`,
`moments_region_2nd`,
`area_center`

## Module

Foundation
