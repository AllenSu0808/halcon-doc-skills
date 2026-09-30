# union_adjacent_contours_xld (Operator)

## Name

`union_adjacent_contours_xld` — Compute the union of contours whose end points are close together.

## Signature

`union_adjacent_contours_xld(Contours : UnionContours : MaxDistAbs, MaxDistRel, Mode : )`

## Description

The operator `union_adjacent_contours_xld` unifies all
contours of the input XLD contour array (*`Contours`*) whose
end points are close together.
The unified contour consists of the concatenation of the contour
points of the input contours.
If necessary, the order of these input contour points is flipped, so
that the end points of the contours that have to be connected are
direct neighbors in the resulting point list.
This operation is repeated until there are no more unconnected
adjacent contours left.
As a result all the contours that are newly created by unification,
as well as the input contours that could not be connected with any
other contour, are returned in *`UnionContours`*.

**Parameters**

The parameters *`MaxDistAbs`* and *`MaxDistRel`* are used to
define the conditions for the proximity of two contours. In principle, the
measures for these parameters depend on the order in which each pair of
contours is evaluated, i.e., which contour is used as reference contour
that is to be joined with the second contour. To avoid this dependency, the
respective measures are evaluated in both directions and the order of
contours is chosen that results in the smaller value for these measures.
Note that in the illustrations below, the contour on the left is always
used as the reference contour. The parameter *`Mode`* controls the
handling of the attributes of the input contours.

- ***`MaxDistAbs`*** —

  The parameter *`MaxDistAbs`* defines the maximum accepted
  absolute distance between the two contours. The distance is
  measured along the regression line of the reference contour. Thus, it
  is the length of the projection of the gap between the two contours
  onto the regression line of the reference contour.

  ![figure](../assets/88d81e687cc73a9a.svg)

  $a\le\texttt{MaxDistAbs}$
- ***`MaxDistRel`*** —

  The parameter *`MaxDistRel`* defines the maximum accepted
  relative distance between the two contours. The relative distance is
  calculated by dividing the distance a (see the description of the
  parameter *`MaxDistAbs`*) by the length b of the reference
  contour.

  ![figure](../assets/06e8766ce365bcea.svg)

  $\frac{a}{b} \leq \mathrm{MaxDistRel$ ![figure](../assets/f17ff27af89a0b0e.svg)

  The order for connecting adjacent contours depends mainly on the
  distance of the neighbored end points: the contours with the
  smallest distance are connected first.
  If there are two pairs of contours with the same distance, first
  the contour pair that does not contain the shortest contour is
  connected.
- ***`Mode`*** —

  Finally, by the parameter *`Mode`* it is possible to control
  how to handle the attributes that may come with input contours.
  For example, the operator [`edges_sub_pix`](edges_sub_pix.md) attaches to every
  contour point attributes like the local orientation, the edge
  response, and the edge direction.
  Choosing the default value *'attr_keep'*, all attributes are
  copied to the output, and - if a contour has to be flipped for
  connecting it with another one - they are adapted to the new
  orientation.
  With a great number of input contours, however, it may be sensible
  to ignore the attributes for performance reasons, if they are not
  needed for further calculations.
  For this the value *'attr_forget'* has to be passed.

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

Maximum distance of the contours' end points.

Default:
10.0

Value range:
`0.0
≤
MaxDistAbs`

**`MaxDistRel`** (input_control)  real `→`  (real)

Maximum distance of the contours' end points in
relation to the length of the longer contour.

Default:
1.0

Value range:
`0.0
≤
MaxDistRel`

**`Mode`** (input_control)  string `→`  (string)

Mode describing the treatment of the contours'
attributes.

Default:
'attr_keep'

List of values:
'attr_forget', 'attr_keep'

## Possible Predecessors

`split_contours_xld`,
`select_contours_xld`

## Alternatives

`union_collinear_contours_xld`,
`union_collinear_contours_ext_xld`,
`union_cocircular_contours_xld`,
`union_straight_contours_xld`,
`union_cotangential_contours_xld`

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
