# MomentsAnyXld (Operator)

## Name

`MomentsAnyXld` — Arbitrary geometric moments of contours or polygons.

## Signature

`static void HOperatorSet.MomentsAnyXld(HObject XLD, HTuple mode, HTuple pointOrder, HTuple area, HTuple centerRow, HTuple centerCol, HTuple p, HTuple q, out HTuple m)`

`HTuple HXLD.MomentsAnyXld(string mode, HTuple pointOrder, HTuple area, HTuple centerRow, HTuple centerCol, HTuple p, HTuple q)`

`double HXLD.MomentsAnyXld(string mode, string pointOrder, double area, double centerRow, double centerCol, int p, int q)`

## Description

`MomentsAnyXld` calculates arbitrary moments *`m`* of
the regions enclosed by the contours or polygons *`XLD`*. The
moments are computed by applying Green's theorem using only the
points on the contour or polygon, i.e., no region is generated
explicitly for the purpose of calculating the features. It is
assumed that the contours or polygons are closed. If this is not
the case `MomentsAnyXld` will artificially close the
contours or polygons.

It should be noted that `MomentsAnyXld` only returns useful
results if the contour or polygon encloses a region in the plane. In
particular, the contour or polygon must not intersect itself. This
is particularly important if open contours or polygons are passed
because they are closed automatically, which can produce a
self-intersection. To test whether the contours or polygons
intersect themselves, [`TestSelfIntersectionXld`](test_self_intersection_xld.md) can be
used. If the contour or polygon intersects itself, useful values
for the moments can be calculated with
[`MomentsAnyPointsXld`](moments_any_points_xld.md).

The computed moments are normalized depending on the desired mode
*`mode`*:

- **'unnormalized':** —

  No normalization. Let $R$ be the enclosed
  image region. Then the computed moment $M_{p,q}$ is
  equivalent to:

  $M_{p,q} = \int_{R}^{?} r^{p} c^{q} \, dr \, dc$ ![figure](../assets/d5f76e40df33eaaa.svg)
- **'unnormalized_central':** —

  Shift the region by its centroid
  $\left[ \bar{\mathbf{r}}, \bar{\mathbf{c}} \right] =$ ![figure](../assets/738ed11693cf5ce0.svg) [*`centerRow`*, *`centerCol`*]:

  $M_{p,q} = \int_{R}^{ } (r - \bar{r})^{p} (c - \bar{c})^{q} \, dr \, dc$ ![figure](../assets/df6eda4330afad19.svg)
- **'normalized':** —

  Normalization by the area $A=$ *`area`*
  of the enclosed image region:

  $M_{p,q} = \frac{1}{A} \int_{R}^{?} r^{p} c^{q} \, dr \, dc$ ![figure](../assets/2bb30ee03d5e67ae.svg)
- **'central':** —

  Normalization by the area $A=$ *`area`*
  of the enclosed image region and a shift of the region by it's centroid
  $\left[ \bar{\mathbf{r}}, \bar{\mathbf{c}} \right] =$ ![figure](../assets/738ed11693cf5ce0.svg) [*`centerRow`*, *`centerCol`*]:

  $M_{p,q} = \frac{1}{A} \int_{R}^{ } \left(r - \bar{r}\right)^{p} \left(c - \bar{c}\right)^{q} \, dr \, dc$ ![figure](../assets/2bfda6305a79d94d.svg)

For the normalization of the moments three specific moments are
used: The area *`area`* of the enclosed image region and the
coordinates *`centerRow`*,*`centerCol`* of it's centroid (this
values can be calculated with [`AreaCenterXld`](area_center_xld.md)). In addition to that
`MomentsAnyXld` expects information about the point order of
the input contours/polygons in *`pointOrder`*, see
[`AreaCenterXld`](area_center_xld.md) again.

If more than one contour or polygon is passed, *`m`* contains
all desired moments of the first contour/polygon followed by all the
moments of the second contour/polygon and so forth.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`XLD`** (input_object)  xld(-array) `→` [HXLD](HXLD.md)

Contours or polygons to be examined.

**`mode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Computation mode.

Default:
"unnormalized"

Suggested values:
"unnormalized", "unnormalized_central", "normalized", "central"

**`pointOrder`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Point order along the boundary.

Default:
"positive"

Suggested values:
"positive", "negative"

**`area`** (input_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Area enclosed by the contour or polygon.

**`centerRow`** (input_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the centroid.

**`centerCol`** (input_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the centroid.

**`p`** (input_control)  point.x(-array) `→` [HTuple](HTuple.md) (*int* / long)

First index of the desired moments
$M_{p,q}$.

Default:
1

Suggested values:
0, 1, 2, 3, 4

**`q`** (input_control)  point.x(-array) `→` [HTuple](HTuple.md) (*int* / long)

Second index of the desired moments
$M_{p,q}$.

Default:
1

Suggested values:
0, 1, 2, 3, 4

**`m`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

The computed moments.

## Complexity

Let n be the number of points of the contour or polygon.
Then the run time is O(n).

## Result

`MomentsAnyXld` returns 2 (
H_MSG_TRUE)
if the input is not empty. If
the input is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`. If
necessary, an exception is raised.

## Possible Predecessors

`AreaCenterXld`,
`GenContoursSkeletonXld`,
`SmoothContoursXld`,
`GenPolygonsXld`

## Alternatives

`MomentsXld`,
`MomentsAnyPointsXld`

## See also

`MomentsXld`,
`AreaCenterXld`,
`MomentsRegion2nd`,
`AreaCenter`

## Module

Foundation
