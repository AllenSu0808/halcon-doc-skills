# UnionCollinearContoursExtXld (Operator)

## Name

`UnionCollinearContoursExtXld` — Compute the union of collinear contours
(operator with extended functionality).

## Signature

`static void HOperatorSet.UnionCollinearContoursExtXld(HObject contours, out HObject unionContours, HTuple maxDistAbs, HTuple maxDistRel, HTuple maxShift, HTuple maxAngle, HTuple maxOverlap, HTuple maxRegrError, HTuple maxCosts, HTuple weightDist, HTuple weightShift, HTuple weightAngle, HTuple weightLink, HTuple weightRegr, HTuple mode)`

`HXLDCont HXLDCont.UnionCollinearContoursExtXld(double maxDistAbs, double maxDistRel, double maxShift, double maxAngle, double maxOverlap, double maxRegrError, double maxCosts, double weightDist, double weightShift, double weightAngle, double weightLink, double weightRegr, string mode)`

## Description

Like [`UnionCollinearContoursXld`](union_collinear_contours_xld.md), the operator
`UnionCollinearContoursExtXld` detects all the
collinear contours within the input array containing straight
contours (*`contours`*) and returns the results in
*`unionContours`*.
The basic behavior is identical to the operator
[`UnionCollinearContoursXld`](union_collinear_contours_xld.md) and is described there.
`UnionCollinearContoursExtXld`, however, provides several
additional parameters to control the process of contour unification
more precisely.

**Parameters**

The parameters *`maxDistAbs`*, *`maxDistRel`*,
*`maxShift`*, and *`maxAngle`* operate as described for
the operator [`UnionCollinearContoursXld`](union_collinear_contours_xld.md).

- ***`maxOverlap`*** —

  In addition, the parameter *`maxOverlap`* allows to define an
  overlap between two contours, in order to connect contours
  which slightly overlap.
  Internally, the operator assures -- irrespective of the passed value
  for *`maxOverlap`* -- that the overlap is not bigger than a
  third of the length of both contours.

  ![figure](../assets/b695a075b8af5751.svg)

  $min(a,b)\le\texttt{MaxOverlap}$
- ***`maxRegrError`*** —

  The parameter *`maxRegrError`* is not used at the moment.
  Its aim is to assure that after the unification of two contours, the
  resulting contour does not deviate too much from its regression line.
  This parameter is by default switched off (*-1*), because
  of its high time consumption and because of the fact that it is
  normally not necessary.
  In some cases, however, result contours may be created with points
  diverging to much from the regression line (winding input contours,
  shift and angle differences close to the -- quite high adjusted --
  thresholds, recursive unification of a lot of small contours).
- ***`maxCosts`*** —

  With the help of the parameter *`maxCosts`* it is possible to
  limit the maximum costs for connecting two contours.
  So, not only contour pairs with one value beyond a certain threshold
  may be excluded from unification, but also contour pairs where all
  values are quite close to the limits.
  The costs are always normalized at a value between 0 and 1,
  where 1 means that all values exactly meet the threshold.
- ***`weightDist`*, *`weightShift`*, *`weightAngle`*,
  *`weightLink`*, and *`weightRegr`*** —

  The influence of the different values on the total costs is adjusted
  by passing appropriate weights with the parameters
  *`weightDist`*, *`weightShift`*, *`weightAngle`*,
  *`weightLink`*, *`weightRegr`*.
  Any positive number can be chosen for these weights, the resulting
  costs are always automatically normalized to fit the range from 0 to
  1.
  The parameter *`weightRegr`* is not used.
- ***`mode`*** —

  The parameter *`mode`* controls -- as for
  [`UnionCollinearContoursXld`](union_collinear_contours_xld.md) -- how to handle the attributes
  of the input contours.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contours`** (input_object)  xld_cont-array `→` [HXLDCont](HXLDCont.md)

Input XLD contours.

**`unionContours`** (output_object)  xld_cont-array `→` [HXLDCont](HXLDCont.md)

Output XLD contours.

**`maxDistAbs`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Maximum distance of the contours' end points in the
direction of the reference regression line.

Default:
10.0

Value range:
`0.0
≤
maxDistAbs`

**`maxDistRel`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Maximum distance of the contours' end points in the
direction of the reference regression line in
relation to the length of the contour which is
to be elongated.

Default:
1.0

Value range:
`0.0
≤
maxDistRel`

**`maxShift`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Maximum distance of the contour from the
reference regression line (i.e., perpendicular
to the line).

Default:
2.0

Value range:
`0.0
≤
maxShift`

**`maxAngle`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Maximum angle difference between the two contours.

Default:
0.1

Value range:
`0.0
≤
maxAngle
≤
0.78539816339`

**`maxOverlap`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Maximum range of the overlap.

Default:
0.0

Value range:
`0.0
≤
maxOverlap`

**`maxRegrError`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Maximum regression error of the resulting contours
(NOT USED).

Default:
-1.0

**`maxCosts`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Threshold for reducing the total costs of unification.

Default:
1.0

Value range:
`0.0
≤
maxCosts`

**`weightDist`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Influence of the distance in the line direction on the
total costs.

Default:
1.0

Value range:
`0.0
≤
weightDist`

**`weightShift`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Influence of the distance from the regression line on
the total costs.

Default:
1.0

Value range:
`0.0
≤
weightShift`

**`weightAngle`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Influence of the angle difference on the total costs.

Default:
1.0

Value range:
`0.0
≤
weightAngle`

**`weightLink`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Influence of the line disturbance by the linking
segment (overlap and angle difference) on the total
costs.

Default:
1.0

Value range:
`0.0
≤
weightLink`

**`weightRegr`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Influence of the regression error on the total
costs (NOT USED).

Default:
0.0

Value range:
`0.0
≤
weightRegr`

**`mode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Mode describing the treatment of the contours'
attributes

Default:
"attr_keep"

List of values:
"attr_forget", "attr_keep"

## Possible Predecessors

`SplitContoursXld`,
`SelectContoursXld`

## Alternatives

`UnionCollinearContoursXld`,
`UnionCocircularContoursXld`,
`UnionCotangentialContoursXld`,
`UnionAdjacentContoursXld`,
`UnionStraightContoursXld`

## See also

`EdgesSubPix`,
`ThresholdSubPix`,
`GenPolygonsXld`,
`SplitContoursXld`,
`SelectContoursXld`,
`GetContourXld`,
`GetContourAttribXld`

## Module

Foundation
