# union_cotangential_contours_xld (Operator)

## Name

`union_cotangential_contours_xld` — Compute the union of cotangential contours.

## Signature

`def union_cotangential_contours_xld(contours: HObject, fit_clipping_length: float, fit_length: Union[float, str], max_tang_angle: float, max_dist: float, max_dist_perp: float, max_overlap: float, mode: str) -> HObject`

## Description

The operator `union_cotangential_contours_xld` unifies contours
of the input XLD contour array *`contours`* according to the local
curvatures at their endpoints.

**Parameters**

- ***`fit_clipping_length`*** —

  How does the union work?
  First, end pieces for each input contour in *`contours`* are
  determined.
  The parameter *`fit_clipping_length`* specifies the Euclidean length
  that is temporarily clipped at both ends of a contour. With this parameter,
  it is possible to ignore artifacts at the endings of the input contours.

  ![figure](../assets/7c9b54c8cdda1010.svg)

  $a\le\texttt{FitClippingLength}$
- ***`fit_length`*** —

  With the parameter *`fit_length`* the Euclidean length of the end pieces
  that will be examined for the union is given. At each
  end of a contour at least that many points are assigned to an end piece that
  its length is greater or equal to *`fit_length`*. The value
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

- ***`max_tang_angle`*** —

  The parameter *`max_tang_angle`* specifies the maximum angle between the
  tangents of two contours.

  ![figure](../assets/5799882e6d02d00b.svg)

  $a\le\texttt{MaxTangAngle}$
- ***`max_dist`*** —

  The maximum distance of two endpoints is given with the parameter
  *`max_dist`*.

  ![figure](../assets/a7078fe0a540f890.svg)

  $a\le\texttt{MaxDist}$
- ***`max_dist_perp`*** —

  The maximum distance perpendicular to the tangents is specified with the
  parameter *`max_dist_perp`*. This distance is the minimum of the
  distances of the endpoints of the contours perpendicular to the other
  contour.

  ![figure](../assets/1f9ef259cd53bf0e.svg)

  $min(a,b)\le\texttt{MaxDistPerp}$
- ***`max_overlap`*** —

  As a last threshold, the overlap of the contours is considered.
  The amount of the overlap is determined by the projection of one
  endpoint onto the tangent of another contour and vice versa. The distances
  between the endpoints and their projections
  must be shorter than *`max_overlap`*. Contrary to the other threshold
  values, *`max_overlap`* can become negative. Negative values denote
  the minimum distance of the endpoints in the direction of the
  tangents.

  ![figure](../assets/d34f89cef734131a.svg)

  $min(a,b)\le\texttt{MaxOverlap}$.
  In this case, $a$ and $b$ are negative. See the reference
  manual entry of [`union_collinear_contours_ext_xld`](union_collinear_contours_ext_xld.md) for an
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
operator [`union_adjacent_contours_xld`](union_adjacent_contours_xld.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contours`** (input_object)  xld_cont-array `→` HObject

Input XLD contours.

**`union_contours`** (output_object)  xld_cont-array `→` HObject

Output XLD contours.

**`fit_clipping_length`** (input_control)  real `→` float

Length of the part of a contour to skip for the
determination of tangents.

Default:
0.0

Value range:
`0.0
≤
fit_clipping_length`

**`fit_length`** (input_control)  real `→` Union[float, str]

Length of the part of a contour to use for the
determination of tangents.

Default:
30.0

Suggested values:
10.0, 20.0, 30.0, "auto"

Value range:
`0.0
≤
fit_length`

**`max_tang_angle`** (input_control)  angle.rad `→` float

Maximum angle difference between two contours'
tangents.

Default:
0.78539816

Value range:
`0.0
≤
max_tang_angle
≤
3.1415926`

**`max_dist`** (input_control)  real `→` float

Maximum distance of the contours' end points.

Default:
25.0

Suggested values:
5.0, 10.0, 25.0, 50.0

Value range:
`0.0
≤
max_dist`

**`max_dist_perp`** (input_control)  real `→` float

Maximum distance of the contours' end points
perpendicular to their tangents.

Default:
10.0

Suggested values:
2.0, 5.0, 10.0, 20.0

Value range:
`0.0
≤
max_dist_perp`

**`max_overlap`** (input_control)  real `→` float

Maximum overlap of two contours.

Default:
2.0

Suggested values:
2.0, 5.0, 10.0, 20.0

**`mode`** (input_control)  string `→` str

Mode describing the treatment of the contours'
attributes.

Default:
"attr_forget"

List of values:
"attr_forget", "attr_keep"

## Possible Predecessors

`split_contours_xld`,
`select_contours_xld`

## Alternatives

`union_collinear_contours_xld`,
`union_collinear_contours_ext_xld`,
`union_cocircular_contours_xld`,
`union_straight_contours_xld`,
`union_adjacent_contours_xld`

## See also

`edges_sub_pix`,
`threshold_sub_pix`,
`gen_polygons_xld`,
`get_contour_xld`,
`get_contour_attrib_xld`

## Module

Foundation
