# union_cocircular_contours_xld (Operator)

## Name

`union_cocircular_contours_xld` — Compute the union of contours that belong to the same circle.

## Signature

`union_cocircular_contours_xld(Contours : UnionContours : MaxArcAngleDiff, MaxArcOverlap, MaxTangentAngle, MaxDist, MaxRadiusDiff, MaxCenterDist, MergeSmallContours, Iterations : )`

## Description

The operator `union_cocircular_contours_xld` merges all
contours that belong to the same circle. The result is a set of
contours in which contours on the same circle are connected.

The algorithm tries to merge contours by first fitting circles to
each contour and then examining the result by means of radius, circle
center, and gap on the circular arc. The list of contours is processed
in sequence of increasing radii. Contours to which no circle could be
fitted are optionally merged in a second pass.

The threshold parameters are used to define whether contours belong
to the same circle. All thresholds must be fulfilled simultaneously
for two contours to be merged.

**Parameters**

- ***`MaxArcAngleDiff`*** —

  The parameter *`MaxArcAngleDiff`* defines the maximum angular distance
  in radians between the end point of one contour and the start point of
  a second contour on a circle.

  ![figure](../assets/65409ee6a818d351.svg)

  $a\le\texttt{MaxArcAngleDiff}$
- ***`MaxArcOverlap`*** —

  *`MaxArcOverlap`* denotes the maximum angle by which
  contours may overlap.

  ![figure](../assets/800a876e75e82403.svg)

  $a\le\texttt{MaxArcOverlap}$
- ***`MaxTangentAngle`*** —

  *`MaxTangentAngle`* describes the maximum
  angle between circle tangents and the connecting line of two
  contours.

  ![figure](../assets/b4fc82dbe43058e3.svg)

  $a\le\texttt{MaxTangentAngle}$
- ***`MaxDist`*** —

  *`MaxDist`* denotes the maximum absolute distance in
  pixels of the end and start points of two
  contours.

  ![figure](../assets/b7bf0568da827d62.svg)

  $a\le\texttt{MaxDist}$
- ***`MaxRadiusDiff`*** —

  *`MaxRadiusDiff`* is the maximum
  absolute difference of the radii of circles fitted to the
  contours.

  ![figure](../assets/a7da6eb11e65b009.svg)

  $a\le\texttt{MaxRadiusDiff}$
- ***`MaxCenterDist`*** —

  *`MaxCenterDist`* is the limit of the Euclidean
  distance of the circle centers.

  ![figure](../assets/53d200f6725657b0.svg)

  $a\le\texttt{MaxCenterDist}$
- ***`MergeSmallContours`*** —

  If the parameter *`MergeSmallContours`* is set to
  *'true'*, contours without fitted circles are also merged.
  For a small contour to match, each point of the contour needs to
  have a distance to the circle center which differs from the radius
  by not more then *`MaxRadiusDiff`*. The angle between a line
  between two consecutive points on the contour and the circle tangent
  must be within *`MaxTangentAngle`*. Additionally, the condition
  for *`MaxDist`* must be fulfilled for two contours to be merged.
- ***`Iterations`*** —

  Merging of contours leads to new circle parameters. Therefore, an
  iteration can lead to further merges. The parameter
  *`Iterations`* controls the number of iterations. More than two
  iterations are seldom needed.

For each possible merge of two contours a cost is calculated by
summing up the distances corresponding to the different threshold
values. For comparability, the distances are scaled by the
thresholds to a value between 0.0 and 1.0. If two or more
contour start points match to the same end point of another contour,
the contour with the lower cost is merged.

You should make sure that the input contours can be approximated by
lines and circular arcs, for example by preprocessing them with
[`split_contours_xld`](split_contours_xld.md).

## Attention

Note that already closed contours are not considered for a union
anymore. That is, even if a contour and the already closed contour share the
same circle, they are returned as separate contours.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Contours`** (input_object)  xld_cont-array `→` object

Contours to be merged.

**`UnionContours`** (output_object)  xld_cont-array `→` object

Merged contours.

**`MaxArcAngleDiff`** (input_control)  angle.rad `→`  (real / integer)

Maximum angular distance of two circular arcs.

Default:
0.5

Suggested values:
0.25, 0.5, 0.75, 1.0

**`MaxArcOverlap`** (input_control)  angle.rad `→`  (real / integer)

Maximum overlap of two circular arcs.

Default:
0.1

Suggested values:
0.0, 0.1, 0.2

**`MaxTangentAngle`** (input_control)  angle.rad `→`  (real / integer)

Maximum angle between the connecting line and the
tangents of circular arcs.

Default:
0.2

Suggested values:
0.1, 0.2, 0.3, 0.4, 0.5

**`MaxDist`** (input_control)  number `→`  (real / integer)

Maximum length of the gap between two circular
arcs in pixels.

Default:
30

Suggested values:
10, 30, 50, 70

**`MaxRadiusDiff`** (input_control)  number `→`  (real / integer)

Maximum radius difference of the circles fitted
to two arcs.

Default:
10

Suggested values:
10, 20, 30

**`MaxCenterDist`** (input_control)  number `→`  (real / integer)

Maximum center distance of the circles fitted
to two arcs.

Default:
10

Suggested values:
10, 20, 30

**`MergeSmallContours`** (input_control)  string `→`  (string)

Determine whether small contours without fitted
circles should also be merged.

Default:
'true'

List of values:
'false', 'true'

**`Iterations`** (input_control)  integer `→`  (integer)

Number of iterations.

Default:
1

Suggested values:
1, 2

## Complexity

O(n^2) for n contours.

## Result

`union_cocircular_contours_xld` returns 2 (
H_MSG_TRUE)
if all
parameters are correct.

## Possible Predecessors

`split_contours_xld`,
`select_contours_xld`

## Alternatives

`union_collinear_contours_xld`,
`union_cotangential_contours_xld`,
`union_straight_contours_xld`,
`union_adjacent_contours_xld`,
`union_collinear_contours_ext_xld`

## Module

Foundation
