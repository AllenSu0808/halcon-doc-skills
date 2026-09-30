# union_straight_contours_xld (Operator)

## Name

`union_straight_contours_xld` — Compute the union of neighboring straight contours that have a similar
direction.

## Signature

`def union_straight_contours_xld(contours: HObject, max_dist: float, max_diff: float, percent: float, mode: str, iterations: Union[int, str]) -> HObject`

## Description

`union_straight_contours_xld` merges neighboring XLD contours
*`contours`* if certain criteria are fulfilled. At each
iteration, at most two contours that fulfill the given criteria are
merged. The parameter *`iterations`* controls how often this
step is executed.

Two contours are merged if the shortest distance between their end
points (end points are the projections of the contours' first and
last points onto its regression line) is smaller than
*`max_dist`*, and if the difference in direction (i.e., the
regression lines' direction) is smaller than *`max_diff`*
(radians).

![figure](../assets/88d81e687cc73a9a.svg)

$a\le\texttt{MaxDist}$

![figure](../assets/20d477c7d2f415ee.svg)

$a\le\texttt{MaxDiff}$

If only one of the criteria is fulfilled, the decision on merging can
be influenced by the weighting factor *`percent`*, which
allows the exceeding of one limit to be balanced by the other value
remaining below the limit by the same amount. The end point
distance is weighted by *`percent`*, while the directional
difference is weighted by 100 - *`percent`*.

This means that two contours are merged if they fulfill the following
condition:

$\frac{shortest\ distance}{MaxDist} \cdot Percent + \frac{direction\ difference}{MaxDiff} \cdot (100 - Percent) \le 100$ ![figure](../assets/cded132a0973de1c.svg)

If, for example, two contours have an end point distance of 5.0 and
a directional difference of 0.5 (with the limits chosen being
*`max_dist`* = *4.0* and *`max_diff`* = *0.625*), both
values differ from the limits by 25%. By choosing
*`percent`* = *60*%, the larger end point distance is weighted
more than the smaller directional difference, and thus the contours
are not merged. Contrary, if *`percent`* = *40*% is chosen,
the contours are merged.

For *`percent`* = *100*%, only the end point distance is taken
into account, while for *`percent`* = *0*% only the difference
of direction is used. If *`percent`* = *50*% both criteria
are equally valid.

In case there are parallel contours, there is a danger of merging
neighboring contours. If this is to be avoided, *`mode`* =
*"noparallel"* has to be chosen, while otherwise *`mode`* =
*"paralleltoo"* suffices. For *`mode`* = *"every"*, contours are
merged unconditionally. All other parameters have no influence in
this case.

The parameters of the regression line are calculated anew for merged
contours.

## Attention

Before contours can be united by `union_straight_contours_xld`,
the parameters of the regression lines to the contours must be calculated
by calling [`regress_contours_xld`](regress_contours_xld.md).

Furthermore, note that `union_straight_contours_xld` can not compute
the union of contours with different contour point attributes.
This can be the case if different operators are used for the contour
extraction (e.g., [`lines_gauss`](lines_gauss.md) and [`lines_facet`](lines_facet.md)). For information
on the contour attributes and when they are defined, see the
respective operator reference. You can query the point attributes of your
contour using [`query_contour_attribs_xld`](query_contour_attribs_xld.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contours`** (input_object)  xld_cont-array `→` HObject

Input XLD contours.

**`union_contours`** (output_object)  xld_cont-array `→` HObject

Output XLD contours.

**`max_dist`** (input_control)  real `→` float

Maximum distance of the contours' endpoints.

Default:
5.0

**`max_diff`** (input_control)  angle.rad `→` float

Maximum difference in direction.

Default:
0.5

**`percent`** (input_control)  real `→` float

Weighting factor for the two selection criteria.

Default:
50.0

**`mode`** (input_control)  string `→` str

Should parallel contours be taken into account?

Default:
"noparallel"

List of values:
"every", "noparallel", "paralleltoo"

**`iterations`** (input_control)  string `→` Union[int, str]

Number of iterations or 'maximum'.

Default:
"maximum"

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "maximum"

Value range:
`1
≤
iterations
≤
500` (lin)

Minimum increment:
1

Recommended increment:
1

## Possible Predecessors

`regress_contours_xld`

## Alternatives

`union_collinear_contours_xld`,
`union_collinear_contours_ext_xld`,
`union_cocircular_contours_xld`,
`union_cotangential_contours_xld`,
`union_adjacent_contours_xld`

## See also

`fit_line_contour_xld`,
`get_contour_xld`,
`get_contour_attrib_xld`,
`gen_contours_skeleton_xld`,
`lines_gauss`,
`lines_facet`,
`edges_sub_pix`,
`get_regress_params_xld`,
`get_contour_global_attrib_xld`,
`query_contour_global_attribs_xld`

## Module

Foundation
