# UnionStraightContoursXld (Operator)

## Name

`UnionStraightContoursXld` — Compute the union of neighboring straight contours that have a similar
direction.

## Signature

`static void HOperatorSet.UnionStraightContoursXld(HObject contours, out HObject unionContours, HTuple maxDist, HTuple maxDiff, HTuple percent, HTuple mode, HTuple iterations)`

`HXLDCont HXLDCont.UnionStraightContoursXld(double maxDist, double maxDiff, double percent, string mode, HTuple iterations)`

`HXLDCont HXLDCont.UnionStraightContoursXld(double maxDist, double maxDiff, double percent, string mode, string iterations)`

## Description

`UnionStraightContoursXld` merges neighboring XLD contours
*`contours`* if certain criteria are fulfilled. At each
iteration, at most two contours that fulfill the given criteria are
merged. The parameter *`iterations`* controls how often this
step is executed.

Two contours are merged if the shortest distance between their end
points (end points are the projections of the contours' first and
last points onto its regression line) is smaller than
*`maxDist`*, and if the difference in direction (i.e., the
regression lines' direction) is smaller than *`maxDiff`*
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
*`maxDist`* = *4.0* and *`maxDiff`* = *0.625*), both
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

Before contours can be united by `UnionStraightContoursXld`,
the parameters of the regression lines to the contours must be calculated
by calling [`RegressContoursXld`](regress_contours_xld.md).

Furthermore, note that `UnionStraightContoursXld` can not compute
the union of contours with different contour point attributes.
This can be the case if different operators are used for the contour
extraction (e.g., [`LinesGauss`](lines_gauss.md) and [`LinesFacet`](lines_facet.md)). For information
on the contour attributes and when they are defined, see the
respective operator reference. You can query the point attributes of your
contour using [`QueryContourAttribsXld`](query_contour_attribs_xld.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contours`** (input_object)  xld_cont-array `→` [HXLDCont](HXLDCont.md)

Input XLD contours.

**`unionContours`** (output_object)  xld_cont-array `→` [HXLDCont](HXLDCont.md)

Output XLD contours.

**`maxDist`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Maximum distance of the contours' endpoints.

Default:
5.0

**`maxDiff`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double*)

Maximum difference in direction.

Default:
0.5

**`percent`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Weighting factor for the two selection criteria.

Default:
50.0

**`mode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Should parallel contours be taken into account?

Default:
"noparallel"

List of values:
"every", "noparallel", "paralleltoo"

**`iterations`** (input_control)  string `→` [HTuple](HTuple.md) (*string* / int / long)

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

`RegressContoursXld`

## Alternatives

`UnionCollinearContoursXld`,
`UnionCollinearContoursExtXld`,
`UnionCocircularContoursXld`,
`UnionCotangentialContoursXld`,
`UnionAdjacentContoursXld`

## See also

`FitLineContourXld`,
`GetContourXld`,
`GetContourAttribXld`,
`GenContoursSkeletonXld`,
`LinesGauss`,
`LinesFacet`,
`EdgesSubPix`,
`GetRegressParamsXld`,
`GetContourGlobalAttribXld`,
`QueryContourGlobalAttribsXld`

## Module

Foundation
