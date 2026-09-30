# union_collinear_contours_ext_xld (Operator)

## Name

`union_collinear_contours_ext_xld` — Compute the union of collinear contours
(operator with extended functionality).

## Signature

`union_collinear_contours_ext_xld(Contours : UnionContours : MaxDistAbs, MaxDistRel, MaxShift, MaxAngle, MaxOverlap, MaxRegrError, MaxCosts, WeightDist, WeightShift, WeightAngle, WeightLink, WeightRegr, Mode : )`

## Description

Like [`union_collinear_contours_xld`](union_collinear_contours_xld.md), the operator
`union_collinear_contours_ext_xld` detects all the
collinear contours within the input array containing straight
contours (*`Contours`*) and returns the results in
*`UnionContours`*.
The basic behavior is identical to the operator
[`union_collinear_contours_xld`](union_collinear_contours_xld.md) and is described there.
`union_collinear_contours_ext_xld`, however, provides several
additional parameters to control the process of contour unification
more precisely.

**Parameters**

The parameters *`MaxDistAbs`*, *`MaxDistRel`*,
*`MaxShift`*, and *`MaxAngle`* operate as described for
the operator [`union_collinear_contours_xld`](union_collinear_contours_xld.md).

- ***`MaxOverlap`*** —

  In addition, the parameter *`MaxOverlap`* allows to define an
  overlap between two contours, in order to connect contours
  which slightly overlap.
  Internally, the operator assures -- irrespective of the passed value
  for *`MaxOverlap`* -- that the overlap is not bigger than a
  third of the length of both contours.

  ![figure](../assets/b695a075b8af5751.svg)

  $min(a,b)\le\texttt{MaxOverlap}$
- ***`MaxRegrError`*** —

  The parameter *`MaxRegrError`* is not used at the moment.
  Its aim is to assure that after the unification of two contours, the
  resulting contour does not deviate too much from its regression line.
  This parameter is by default switched off (*-1*), because
  of its high time consumption and because of the fact that it is
  normally not necessary.
  In some cases, however, result contours may be created with points
  diverging to much from the regression line (winding input contours,
  shift and angle differences close to the -- quite high adjusted --
  thresholds, recursive unification of a lot of small contours).
- ***`MaxCosts`*** —

  With the help of the parameter *`MaxCosts`* it is possible to
  limit the maximum costs for connecting two contours.
  So, not only contour pairs with one value beyond a certain threshold
  may be excluded from unification, but also contour pairs where all
  values are quite close to the limits.
  The costs are always normalized at a value between 0 and 1,
  where 1 means that all values exactly meet the threshold.
- ***`WeightDist`*, *`WeightShift`*, *`WeightAngle`*,
  *`WeightLink`*, and *`WeightRegr`*** —

  The influence of the different values on the total costs is adjusted
  by passing appropriate weights with the parameters
  *`WeightDist`*, *`WeightShift`*, *`WeightAngle`*,
  *`WeightLink`*, *`WeightRegr`*.
  Any positive number can be chosen for these weights, the resulting
  costs are always automatically normalized to fit the range from 0 to
  1.
  The parameter *`WeightRegr`* is not used.
- ***`Mode`*** —

  The parameter *`Mode`* controls -- as for
  [`union_collinear_contours_xld`](union_collinear_contours_xld.md) -- how to handle the attributes
  of the input contours.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Contours`** (input_object)  xld_cont-array `→` object

Input XLD contours.

**`UnionContours`** (output_object)  xld_cont-array `→` object

Output XLD contours.

**`MaxDistAbs`** (input_control)  real `→`  (real)

Maximum distance of the contours' end points in the
direction of the reference regression line.

Default:
10.0

Value range:
`0.0
≤
MaxDistAbs`

**`MaxDistRel`** (input_control)  real `→`  (real)

Maximum distance of the contours' end points in the
direction of the reference regression line in
relation to the length of the contour which is
to be elongated.

Default:
1.0

Value range:
`0.0
≤
MaxDistRel`

**`MaxShift`** (input_control)  real `→`  (real)

Maximum distance of the contour from the
reference regression line (i.e., perpendicular
to the line).

Default:
2.0

Value range:
`0.0
≤
MaxShift`

**`MaxAngle`** (input_control)  real `→`  (real)

Maximum angle difference between the two contours.

Default:
0.1

Value range:
`0.0
≤
MaxAngle
≤
0.78539816339`

**`MaxOverlap`** (input_control)  real `→`  (real)

Maximum range of the overlap.

Default:
0.0

Value range:
`0.0
≤
MaxOverlap`

**`MaxRegrError`** (input_control)  real `→`  (real)

Maximum regression error of the resulting contours
(NOT USED).

Default:
-1.0

**`MaxCosts`** (input_control)  real `→`  (real)

Threshold for reducing the total costs of unification.

Default:
1.0

Value range:
`0.0
≤
MaxCosts`

**`WeightDist`** (input_control)  real `→`  (real)

Influence of the distance in the line direction on the
total costs.

Default:
1.0

Value range:
`0.0
≤
WeightDist`

**`WeightShift`** (input_control)  real `→`  (real)

Influence of the distance from the regression line on
the total costs.

Default:
1.0

Value range:
`0.0
≤
WeightShift`

**`WeightAngle`** (input_control)  real `→`  (real)

Influence of the angle difference on the total costs.

Default:
1.0

Value range:
`0.0
≤
WeightAngle`

**`WeightLink`** (input_control)  real `→`  (real)

Influence of the line disturbance by the linking
segment (overlap and angle difference) on the total
costs.

Default:
1.0

Value range:
`0.0
≤
WeightLink`

**`WeightRegr`** (input_control)  real `→`  (real)

Influence of the regression error on the total
costs (NOT USED).

Default:
0.0

Value range:
`0.0
≤
WeightRegr`

**`Mode`** (input_control)  string `→`  (string)

Mode describing the treatment of the contours'
attributes

Default:
'attr_keep'

List of values:
'attr_forget', 'attr_keep'

## Possible Predecessors

`split_contours_xld`,
`select_contours_xld`

## Alternatives

`union_collinear_contours_xld`,
`union_cocircular_contours_xld`,
`union_cotangential_contours_xld`,
`union_adjacent_contours_xld`,
`union_straight_contours_xld`

## See also

`edges_sub_pix`,
`threshold_sub_pix`,
`gen_polygons_xld`,
`split_contours_xld`,
`select_contours_xld`,
`get_contour_xld`,
`get_contour_attrib_xld`

## Module

Foundation
