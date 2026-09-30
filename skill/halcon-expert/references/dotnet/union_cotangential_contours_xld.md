# UnionCotangentialContoursXld (Operator)

## Name

`UnionCotangentialContoursXld` — Compute the union of cotangential contours.

## Signature

`static void HOperatorSet.UnionCotangentialContoursXld(HObject contours, out HObject unionContours, HTuple fitClippingLength, HTuple fitLength, HTuple maxTangAngle, HTuple maxDist, HTuple maxDistPerp, HTuple maxOverlap, HTuple mode)`

`HXLDCont HXLDCont.UnionCotangentialContoursXld(double fitClippingLength, HTuple fitLength, double maxTangAngle, double maxDist, double maxDistPerp, double maxOverlap, string mode)`

`HXLDCont HXLDCont.UnionCotangentialContoursXld(double fitClippingLength, double fitLength, double maxTangAngle, double maxDist, double maxDistPerp, double maxOverlap, string mode)`

## Description

The operator `UnionCotangentialContoursXld` unifies contours
of the input XLD contour array *`contours`* according to the local
curvatures at their endpoints.

**Parameters**

- ***`fitClippingLength`*** —

  How does the union work?
  First, end pieces for each input contour in *`contours`* are
  determined.
  The parameter *`fitClippingLength`* specifies the Euclidean length
  that is temporarily clipped at both ends of a contour. With this parameter,
  it is possible to ignore artifacts at the endings of the input contours.

  ![figure](../assets/7c9b54c8cdda1010.svg)

  $a\le\texttt{FitClippingLength}$
- ***`fitLength`*** —

  With the parameter *`fitLength`* the Euclidean length of the end pieces
  that will be examined for the union is given. At each
  end of a contour at least that many points are assigned to an end piece that
  its length is greater or equal to *`fitLength`*. The value
  *"auto"* can be used here. The operator then tries to segment
  the contours into straights and arcs and takes the first and last segment
  as end pieces. As this is computationally intensive, it is recommended to use
  numerically specified values for the lengths whenever possible.

  ![figure](../assets/5c240cf67afe89de.svg)

  $a\le\texttt{FitLength}$

The operator tries to fit a circle into each end piece.
Then, the endpoints of the input contours are determined that lie
near enough to these circles (measured against
the root mean square error of the circle fit). The tangents at these points
correspond to the local curvature at the endings of the input contours.

If a circle fit fails, the operator tries to fit a regression line. Then,
the local curvature of the endings of a contour corresponds to the
direction of the regression line through the points of the end pieces.

![figure](../assets/57f3f5e8220a9a10.svg)

The input contours are going to be unified according to the
calculated local curvatures at their endpoints. Two contours are
considered for the union if multiple thresholds are fulfilled at the same
time:

- ***`maxTangAngle`*** —

  The parameter *`maxTangAngle`* specifies the maximum angle between the
  tangents of two contours.

  ![figure](../assets/5799882e6d02d00b.svg)

  $a\le\texttt{MaxTangAngle}$
- ***`maxDist`*** —

  The maximum distance of two endpoints is given with the parameter
  *`maxDist`*.

  ![figure](../assets/a7078fe0a540f890.svg)

  $a\le\texttt{MaxDist}$
- ***`maxDistPerp`*** —

  The maximum distance perpendicular to the tangents is specified with the
  parameter *`maxDistPerp`*. This distance is the minimum of the
  distances of the endpoints of the contours perpendicular to the other
  contour.

  ![figure](../assets/1f9ef259cd53bf0e.svg)

  $min(a,b)\le\texttt{MaxDistPerp}$
- ***`maxOverlap`*** —

  As a last threshold, the overlap of the contours is considered.
  The amount of the overlap is determined by the projection of one
  endpoint onto the tangent of another contour and vice versa. The distances
  between the endpoints and their projections
  must be shorter than *`maxOverlap`*. Contrary to the other threshold
  values, *`maxOverlap`* can become negative. Negative values denote
  the minimum distance of the endpoints in the direction of the
  tangents.

  ![figure](../assets/d34f89cef734131a.svg)

  $min(a,b)\le\texttt{MaxOverlap}$.
  In this case, $a$ and $b$ are negative. See the reference
  manual entry of [`UnionCollinearContoursExtXld`](union_collinear_contours_ext_xld.md) for an
  illustration with positive values for $a$ and $b$.

It is possible, that a single contour is closed by this operator or
multiple contours are merged into a single closed contour,
if the criteria named above are fulfilled for the end pieces. Be aware that
already closed contours are not considered for a union anymore.

If all thresholds are fulfilled between contours, a score value is
calculated. The closer the calculated values for the angles and distances are
to 0, the
higher is the score value. The unification is then executed in the order of
the score values. Thus, if there are multiple candidates for the unification,
the best fitting contours are merged first.

The parameter *`mode`* states, whether existing attributes of the
input contours should be copied to the output contours. *"attr_keep"*
copies the attributes, which can have negative impacts on the performance of
the operator.
*"attr_forget"* causes the operator to ignore existing attributes.
For further details see the description of the parameter Mode of the
operator [`UnionAdjacentContoursXld`](union_adjacent_contours_xld.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contours`** (input_object)  xld_cont-array `→` [HXLDCont](HXLDCont.md)

Input XLD contours.

**`unionContours`** (output_object)  xld_cont-array `→` [HXLDCont](HXLDCont.md)

Output XLD contours.

**`fitClippingLength`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Length of the part of a contour to skip for the
determination of tangents.

Default:
0.0

Value range:
`0.0
≤
fitClippingLength`

**`fitLength`** (input_control)  real `→` [HTuple](HTuple.md) (*double* / string)

Length of the part of a contour to use for the
determination of tangents.

Default:
30.0

Suggested values:
10.0, 20.0, 30.0, "auto"

Value range:
`0.0
≤
fitLength`

**`maxTangAngle`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double*)

Maximum angle difference between two contours'
tangents.

Default:
0.78539816

Value range:
`0.0
≤
maxTangAngle
≤
3.1415926`

**`maxDist`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Maximum distance of the contours' end points.

Default:
25.0

Suggested values:
5.0, 10.0, 25.0, 50.0

Value range:
`0.0
≤
maxDist`

**`maxDistPerp`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Maximum distance of the contours' end points
perpendicular to their tangents.

Default:
10.0

Suggested values:
2.0, 5.0, 10.0, 20.0

Value range:
`0.0
≤
maxDistPerp`

**`maxOverlap`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Maximum overlap of two contours.

Default:
2.0

Suggested values:
2.0, 5.0, 10.0, 20.0

**`mode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Mode describing the treatment of the contours'
attributes.

Default:
"attr_forget"

List of values:
"attr_forget", "attr_keep"

## Possible Predecessors

`SplitContoursXld`,
`SelectContoursXld`

## Alternatives

`UnionCollinearContoursXld`,
`UnionCollinearContoursExtXld`,
`UnionCocircularContoursXld`,
`UnionStraightContoursXld`,
`UnionAdjacentContoursXld`

## See also

`EdgesSubPix`,
`ThresholdSubPix`,
`GenPolygonsXld`,
`GetContourXld`,
`GetContourAttribXld`

## Module

Foundation
