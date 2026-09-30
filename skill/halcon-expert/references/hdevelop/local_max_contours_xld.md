# local_max_contours_xld (Operator)

## Name

`local_max_contours_xld` — Select XLD contours with a local maximum of gray values.

## Signature

`local_max_contours_xld(Contours, Image : LocalMaxContours : MinPercent, MinDiff, Distance : )`

## Description

`local_max_contours_xld` selects XLD contours from the
contours passed in *`Contours`*, which have a local maximum
in gray values across the direction of the contour. In order to be
selected, at least *`MinPercent`* of the contour points must
have a local maximum perpendicular to the direction of the contour.
The contours' direction is determined by fitting a regression line
through five neighboring points of the contour. In order to decide
whether there is a local maximum for a contour point, a gray value
profile that is *`Distance`* points wide and perpendicular to the
contour is computed on both sides of the contour. If the gray value
at the contour point is at least *`MinDiff`* larger than the
gray value at at least one point on each side of the profile, the
contour point is labeled as a local maximum. The selected contours
are returned in *`LocalMaxContours`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Contours`** (input_object)  xld_cont-array `→` object

XLD contours to be examined.

**`Image`** (input_object)  singlechannelimage `→` object (byte)

Corresponding gray value image.

**`LocalMaxContours`** (output_object)  xld_cont-array `→` object

Selected contours.

**`MinPercent`** (input_control)  number `→`  (integer / real)

Minimum percentage of maximum points.

Default:
70

Suggested values:
60, 70, 75, 80, 85, 90, 95

Restriction:
`0.0 <= MinPercent && MinPercent <= 100.0`

**`MinDiff`** (input_control)  integer `→`  (integer)

Minimum amount by which the gray value at the
maximum must be larger than in the profile.

Default:
15

Suggested values:
5, 8, 10, 12, 15, 20

Restriction:
`0 <= MinDiff && MinDiff <= 255`

**`Distance`** (input_control)  integer `→`  (integer)

Maximum width of profile used to check for maxima.

Default:
4

Suggested values:
2, 3, 4, 5, 6

Restriction:
`Distance >= 1`

## Possible Predecessors

`gen_contours_skeleton_xld`,
`lines_gauss`,
`lines_facet`,
`edges_sub_pix`

## Possible Successors

`gen_polygons_xld`

## See also

`smooth_contours_xld`

## Module

Foundation
