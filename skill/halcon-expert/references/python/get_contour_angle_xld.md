# get_contour_angle_xld (Operator)

## Name

`get_contour_angle_xld` — Calculate the direction of an XLD contour for each contour point.

## Signature

`def get_contour_angle_xld(contour: HObject, angle_mode: str, calc_mode: str, lookaround: int) -> Sequence[float]`

## Description

`get_contour_angle_xld` calculates for each point of the XLD
contour *`contour`* the direction of its tangent. Two modes
for the output values can be chosen: By passing *"abs"* for
*`angle_mode`*, the resulting angles are returned relative to
the horizontal axis as angles between 0 and $2\pi$
(counter-clockwise). By passing *"rel"*, the
angle difference to the previous contour point is
returned. In this case the range of values is between $-\pi$
and $\pi$, where negative values indicate a right turn and
positive values indicate a left turn.

There are three different ways of calculating the tangent direction
(*`calc_mode`*) of the contour point i using the
contour points in the interval from
$i-\texttt{Lookaround}$ to
$i+\texttt{Lookaround}$. By using *"range"*,
the angle of the line segment between the first and last point of
the interval is used. For *"mean"*, the average of all
angles between consecutive points of the contour is used. Finally,
for *"regress"*, the direction of the regression line (the
least squares fit of a line to the contour points in the interval)
is used. *`lookaround`* is a measure of how strongly the
contour is smoothed. The angles are returned in *`angles`*
in radians.

Due to the interval given by *`lookaround`*, the input contour
must have at least
$2\ast\texttt{Lookaround}+2$ points.
This minimum number of points is required so that the operator
always delivers reasonable output values for the different
parameter settings.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contour`** (input_object)  xld_cont `→` HObject

Input contour.

**`angle_mode`** (input_control)  string `→` str

Return type of the angles.

Default:
"abs"

List of values:
"abs", "rel"

**`calc_mode`** (input_control)  string `→` str

Method for computing the angles.

Default:
"range"

List of values:
"mean", "range", "regress"

**`lookaround`** (input_control)  integer `→` int

Number of points to take into account.

Default:
3

Restriction:
`Lookaround > 0`

**`angles`** (output_control)  real-array `→` Sequence[float]

Direction of the tangent to the contour points.

## Possible Predecessors

`gen_contours_skeleton_xld`,
`lines_gauss`,
`lines_facet`,
`edges_sub_pix`

## See also

`get_contour_xld`,
`get_contour_attrib_xld`

## Module

Foundation
