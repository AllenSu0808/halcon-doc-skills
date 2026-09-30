# LocalMaxContoursXld (Operator)

## Name

`LocalMaxContoursXld` — Select XLD contours with a local maximum of gray values.

## Signature

`static void HOperatorSet.LocalMaxContoursXld(HObject contours, HObject image, out HObject localMaxContours, HTuple minPercent, HTuple minDiff, HTuple distance)`

`HXLDCont HXLDCont.LocalMaxContoursXld(HImage image, HTuple minPercent, int minDiff, int distance)`

`HXLDCont HXLDCont.LocalMaxContoursXld(HImage image, int minPercent, int minDiff, int distance)`

## Description

`LocalMaxContoursXld` selects XLD contours from the
contours passed in *`contours`*, which have a local maximum
in gray values across the direction of the contour. In order to be
selected, at least *`minPercent`* of the contour points must
have a local maximum perpendicular to the direction of the contour.
The contours' direction is determined by fitting a regression line
through five neighboring points of the contour. In order to decide
whether there is a local maximum for a contour point, a gray value
profile that is *`distance`* points wide and perpendicular to the
contour is computed on both sides of the contour. If the gray value
at the contour point is at least *`minDiff`* larger than the
gray value at at least one point on each side of the profile, the
contour point is labeled as a local maximum. The selected contours
are returned in *`localMaxContours`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contours`** (input_object)  xld_cont-array `→` [HXLDCont](HXLDCont.md)

XLD contours to be examined.

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte)

Corresponding gray value image.

**`localMaxContours`** (output_object)  xld_cont-array `→` [HXLDCont](HXLDCont.md)

Selected contours.

**`minPercent`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long / double)

Minimum percentage of maximum points.

Default:
70

Suggested values:
60, 70, 75, 80, 85, 90, 95

Restriction:
`0.0 <= MinPercent && MinPercent <= 100.0`

**`minDiff`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Minimum amount by which the gray value at the
maximum must be larger than in the profile.

Default:
15

Suggested values:
5, 8, 10, 12, 15, 20

Restriction:
`0 <= MinDiff && MinDiff <= 255`

**`distance`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Maximum width of profile used to check for maxima.

Default:
4

Suggested values:
2, 3, 4, 5, 6

Restriction:
`Distance >= 1`

## Possible Predecessors

`GenContoursSkeletonXld`,
`LinesGauss`,
`LinesFacet`,
`EdgesSubPix`

## Possible Successors

`GenPolygonsXld`

## See also

`SmoothContoursXld`

## Module

Foundation
