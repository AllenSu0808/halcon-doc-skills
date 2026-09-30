# UnionCollinearContoursXld (Operator)

## Name

`UnionCollinearContoursXld` — Unite approximately collinear contours.

## Signature

`static void HOperatorSet.UnionCollinearContoursXld(HObject contours, out HObject unionContours, HTuple maxDistAbs, HTuple maxDistRel, HTuple maxShift, HTuple maxAngle, HTuple mode)`

`HXLDCont HXLDCont.UnionCollinearContoursXld(double maxDistAbs, double maxDistRel, double maxShift, double maxAngle, string mode)`

## Description

The operator `UnionCollinearContoursXld` unites all contours
of the input XLD contour array *`contours`* that are
approximately collinear, i.e., which lie approximately on the same
straight line. The united contours consist of the concatenation of
the contour points of the respective input contours. They are returned,
together with the contours that could not be united with any other
contour, in the output XLD contour array *`unionContours`*.

**Typical applications**

`UnionCollinearContoursXld` can be used to bridge gaps in
extracted edges or lines, which may be caused, e.g., by locally low
image contrast. It can also be used to unite collinear edge or line
segments that are separated, e.g., because of junctions. Typically,
`UnionCollinearContoursXld` is part of the process of
grouping and selecting extracted edges or lines to achieve meaningful
entities.

**Example**

The following example shows the effect of
`UnionCollinearContoursXld`. On the left hand side, a set of
disconnected input contours is shown. The contours that lie on the
same border of the rectangle are approximately collinear. On the right
hand side, the result of `UnionCollinearContoursXld` shows
that the contours that were approximately collinear have been united.
Note that the contours that are approximately perpendicular to each
other have not been united.

|  |  |
| --- | --- |
| ![figure](../assets/87e864e60ba8cab4.svg) | ![figure](../assets/3ac61b5d3f127c70.svg) |
| ( 1) | ( 2) |

(1) Disconnected input contours. (2) Resulting contours, where
approximately collinear contours have been united.

**Parameters**

The parameters *`maxDistAbs`*, *`maxDistRel`*,
*`maxShift`*, and *`maxAngle`* are used to define the
conditions for the collinearity of two contours. The parameter
*`mode`* controls the handling of the attributes of the input
contours.

In principle, the measures for the first three parameters depend on
the order in which each pair of contours is evaluated, i.e., which
contour is used as reference contour that is to be joined with the
second contour. To avoid this dependency, the respective measures are
evaluated in both directions and the order of contours is chosen that
results in the smaller value for these measures. Note that in the
illustrations below, the contour on the left is always used as the
reference contour.

- ***`maxDistAbs`*** —

  The parameter *`maxDistAbs`* defines the maximum accepted
  absolute distance between the two contours. The distance is
  measured along the regression line of the reference contour. Thus, it
  is the length of the projection of the gap between the two contours
  onto the regression line of the reference contour.

  ![figure](../assets/88d81e687cc73a9a.svg)

  $a\le\texttt{MaxDistAbs}$
- ***`maxDistRel`*** —

  The parameter *`maxDistRel`* defines the maximum accepted
  relative distance between the two contours. The relative distance is
  calculated by dividing the distance a (see the description of the
  parameter *`maxDistAbs`*) by the length b of the reference
  contour.

  ![figure](../assets/06e8766ce365bcea.svg)

  $\frac{a}{b} \leq \mathrm{MaxDistRel$ ![figure](../assets/f17ff27af89a0b0e.svg)
- ***`maxShift`*** —

  The parameter *`maxShift`* defines the maximum distance of the
  second contour from the regression line of the reference contour.
  This distance is measured perpendicular to the regression line of
  the reference contour.

  ![figure](../assets/ec80c14f15373193.svg)

  $a\le\texttt{MaxShift}$
- ***`maxAngle`*** —

  The parameter *`maxAngle`* defines the maximum angle (in
  radians) between the regression lines of the two contours.

  ![figure](../assets/20d477c7d2f415ee.svg)

  $a\le\texttt{MaxAngle}$
- ***`mode`*** —

  The parameter *`mode`* controls the handling of the attributes
  that may be available for the input contours, e.g., if the contours
  have been created by [`EdgesSubPix`](edges_sub_pix.md).

  - ***"attr_keep"*** —

    All attributes are copied to the output contours.

    Global attributes are only kept for those contours that are not
    united with other contours. In general, it is not possible to
    determine the global attributes of a united contour from the
    global attributes of the individual contours.
  - ***"attr_forget"*** —

    The output contours will not contain any attributes. This mode may
    be chosen for performance reasons if the attributes will not be
    required for further calculations.

  To query, which attributes are available,
  [`QueryContourAttribsXld`](query_contour_attribs_xld.md) can be used.

**Implementation details**

The input contours are analyzed and united pairwise.
This pairwise process is repeated until there are no more unconnected
collinear contours left. If necessary, the order of the input contour
points is flipped, so that the end points of the contours that have
been connected are direct neighbors in the resulting point list.

Two contours are united only if all criteria are fulfilled, i.e., all
values must be lower than the specified thresholds. As another
precondition, contours must not overlap each other significantly (see
[`UnionCollinearContoursExtXld`](union_collinear_contours_ext_xld.md) for an illustration of overlap).
An overlap of at most 0.5 pixels is tolerated. To allow a larger overlap,
[`UnionCollinearContoursExtXld`](union_collinear_contours_ext_xld.md) can be used.

Besides finding pairs of contours to be united, it is
important for the behavior of `UnionCollinearContoursXld` to
determine the order in which contours are united.
For this, all contour pairs that may be united are rated by
calculating costs for their unification.
The costs are the sum of the measures, each normalized by the
respective threshold, defined by the parameters *`maxDistAbs`*,
*`maxDistRel`*, *`maxShift`*, and *`maxAngle`*.
The contour pair with the
lowest costs is united first. Then, the costs are updated with
respect to the newly created contour and the contour list is searched
for the next best pair of contours to be united.

Note that the definition of collinearity as used in
`UnionCollinearContoursXld` depends on the regression lines
of the input contours. To avoid unexpected results, make sure that the
input contours are approximately straight lines, e.g., by splitting
them into line segments with [`SegmentContoursXld`](segment_contours_xld.md). Note also
that closed contours are not united with any other contour.

**Limitations and alternatives**

`UnionCollinearContoursXld` can only be used if the contours
that should be joined lie approximately on a straight line. If the
contours lie approximately on a circle,
[`UnionCocircularContoursXld`](union_cocircular_contours_xld.md) can be used instead. If the
contours represent a free-form,
[`UnionCotangentialContoursXld`](union_cotangential_contours_xld.md) can be used. If only very
small gaps between the contours should be closed, regardless of the
orientation of the contours, [`UnionAdjacentContoursXld`](union_adjacent_contours_xld.md) can
be used.

If the parameter adjustments available with
`UnionCollinearContoursXld` are not sufficient,
[`UnionCollinearContoursExtXld`](union_collinear_contours_ext_xld.md) can be used to define the
criteria for the unification more specifically. Among others,
[`UnionCollinearContoursExtXld`](union_collinear_contours_ext_xld.md) allows to set the tolerance
for the overlap of contours as well as a limit for the total costs to
avoid the connection of contours that are close to the limits of all
criteria.

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

Maximum length of the gap between two contours, measured
along the regression line of the reference contour.

Default:
10.0

Value range:
`0.0
≤
maxDistAbs`

**`maxDistRel`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Maximum length of the gap between two contours, relative
to the length of the reference contour, both measured
along the regression line of the reference contour.

Default:
1.0

Value range:
`0.0
≤
maxDistRel`

**`maxShift`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Maximum distance of the second contour from the
regression line of the reference contour.

Default:
2.0

Value range:
`0.0
≤
maxShift`

**`maxAngle`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Maximum angle between the regression lines of two contours.

Default:
0.1

Value range:
`0.0
≤
maxAngle
≤
0.78539816339`

**`mode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Mode that defines the treatment of contour attributes, i.e.,
if the contour attributes are kept or discarded.

Default:
"attr_keep"

List of values:
"attr_forget", "attr_keep"

## Possible Predecessors

`EdgesSubPix`,
`LinesGauss`,
`SegmentContoursXld`,
`SelectContoursXld`,
`SelectShapeXld`,
`SplitContoursXld`,
`ThresholdSubPix`

## Possible Successors

`FitLineContourXld`,
`SelectContoursXld`,
`SelectShapeXld`

## Alternatives

`UnionCollinearContoursExtXld`,
`UnionStraightContoursXld`,
`UnionCocircularContoursXld`,
`UnionCotangentialContoursXld`,
`UnionAdjacentContoursXld`

## See also

`GetContourXld`,
`GetContourAttribXld`,
`QueryContourAttribsXld`

## Module

Foundation
