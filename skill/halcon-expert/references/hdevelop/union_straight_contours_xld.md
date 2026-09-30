# union_straight_contours_xld (Operator)

## Name

`union_straight_contours_xld` — Compute the union of neighboring straight contours that have a similar
direction.

## Signature

`union_straight_contours_xld(Contours : UnionContours : MaxDist, MaxDiff, Percent, Mode, Iterations : )`

## Description

`union_straight_contours_xld` merges neighboring XLD contours
*`Contours`* if certain criteria are fulfilled. At each
iteration, at most two contours that fulfill the given criteria are
merged. The parameter *`Iterations`* controls how often this
step is executed.

Two contours are merged if the shortest distance between their end
points (end points are the projections of the contours' first and
last points onto its regression line) is smaller than
*`MaxDist`*, and if the difference in direction (i.e., the
regression lines' direction) is smaller than *`MaxDiff`*
(radians).

![figure](../assets/88d81e687cc73a9a.svg)

$a\le\texttt{MaxDist}$

![figure](../assets/20d477c7d2f415ee.svg)

$a\le\texttt{MaxDiff}$

If only one of the criteria is fulfilled, the decision on merging can
be influenced by the weighting factor *`Percent`*, which
allows the exceeding of one limit to be balanced by the other value
remaining below the limit by the same amount. The end point
distance is weighted by *`Percent`*, while the directional
difference is weighted by 100 - *`Percent`*.

This means that two contours are merged if they fulfill the following
condition:

$\frac{shortest\ distance}{MaxDist} \cdot Percent + \frac{direction\ difference}{MaxDiff} \cdot (100 - Percent) \le 100$ ![figure](../assets/cded132a0973de1c.svg)

If, for example, two contours have an end point distance of 5.0 and
a directional difference of 0.5 (with the limits chosen being
*`MaxDist`* = *4.0* and *`MaxDiff`* = *0.625*), both
values differ from the limits by 25%. By choosing
*`Percent`* = *60*%, the larger end point distance is weighted
more than the smaller directional difference, and thus the contours
are not merged. Contrary, if *`Percent`* = *40*% is chosen,
the contours are merged.

For *`Percent`* = *100*%, only the end point distance is taken
into account, while for *`Percent`* = *0*% only the difference
of direction is used. If *`Percent`* = *50*% both criteria
are equally valid.

In case there are parallel contours, there is a danger of merging
neighboring contours. If this is to be avoided, *`Mode`* =
*'noparallel'* has to be chosen, while otherwise *`Mode`* =
*'paralleltoo'* suffices. For *`Mode`* = *'every'*, contours are
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

**`Contours`** (input_object)  xld_cont-array `→` object

Input XLD contours.

**`UnionContours`** (output_object)  xld_cont-array `→` object

Output XLD contours.

**`MaxDist`** (input_control)  real `→`  (real)

Maximum distance of the contours' endpoints.

Default:
5.0

**`MaxDiff`** (input_control)  angle.rad `→`  (real)

Maximum difference in direction.

Default:
0.5

**`Percent`** (input_control)  real `→`  (real)

Weighting factor for the two selection criteria.

Default:
50.0

**`Mode`** (input_control)  string `→`  (string)

Should parallel contours be taken into account?

Default:
'noparallel'

List of values:
'every', 'noparallel', 'paralleltoo'

**`Iterations`** (input_control)  string `→`  (string / integer)

Number of iterations or 'maximum'.

Default:
'maximum'

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'maximum'

Value range:
`1
≤
Iterations
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
