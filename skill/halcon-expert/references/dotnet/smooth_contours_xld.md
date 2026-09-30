# SmoothContoursXld (Operator)

## Name

`SmoothContoursXld` — Smooth an XLD contour.

## Signature

`static void HOperatorSet.SmoothContoursXld(HObject contours, out HObject smoothedContours, HTuple numRegrPoints)`

`HXLDCont HXLDCont.SmoothContoursXld(int numRegrPoints)`

## Description

`SmoothContoursXld` smooths the input XLD contours
*`contours`* and returns the smoothed contours in
*`smoothedContours`*. The smoothing is done by projecting
the contours' points onto a local regression line (i.e., a
least-squares approximating line), which is computed from
*`numRegrPoints`* on each side of the current contour point.
This operator should be called, for example, before contours are
scaled.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contours`** (input_object)  xld_cont-array `→` [HXLDCont](HXLDCont.md)

Contour to be smoothed.

**`smoothedContours`** (output_object)  xld_cont-array `→` [HXLDCont](HXLDCont.md)

Smoothed contour.

**`numRegrPoints`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of points used to calculate the regression
line.

Default:
5

Suggested values:
3, 5, 7, 9

Restriction:
`NumRegrPoints >= 3 && odd(NumRegrPoints)`

## Possible Predecessors

`GenContoursSkeletonXld`,
`LinesGauss`,
`LinesFacet`,
`EdgesSubPix`

## Possible Successors

`AffineTransContourXld`,
`GenPolygonsXld`,
`LocalMaxContoursXld`

## See also

`GetContourXld`

## Module

Foundation
