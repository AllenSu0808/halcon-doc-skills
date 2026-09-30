# GenContourPolygonRoundedXld (Operator)

## Name

`GenContourPolygonRoundedXld` — Generate an XLD contour with rounded corners from a polygon (given
as tuples).

## Signature

`static void HOperatorSet.GenContourPolygonRoundedXld(out HObject contour, HTuple row, HTuple col, HTuple radius, HTuple samplingInterval)`

`void HXLDCont.GenContourPolygonRoundedXld(HTuple row, HTuple col, HTuple radius, HTuple samplingInterval)`

`void HXLDCont.GenContourPolygonRoundedXld(HTuple row, HTuple col, HTuple radius, double samplingInterval)`

## Description

`GenContourPolygonRoundedXld` generates an XLD contour
*`contour`* with rounded corners from a polygon given in the
tuples *`row`* and *`col`*. The rounded corners are created in
form of arcs defined by *`radius`*. For every specified point of the
polygon there must be a corresponding rounding radius defined. In
case of a closed polygon the first and the last point have to be
defined identical with the radii of these points being equal. In
contrast, the radii of the first and last point of open polygons are
ignored. Finally, the *`samplingInterval`* parameter defines the
distance of the control points of the formed contour
*`contour`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contour`** (output_object)  xld_cont `→` [HXLDCont](HXLDCont.md)

Resulting contour.

**`row`** (input_control)  coordinates.y-array `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinates of the polygon.

Default:
[20,80,80,20,20]

Suggested values:
0, 1, 2, 3, 4, 5, 10, 20, 50, 100, 200, 500

**`col`** (input_control)  coordinates.x-array `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinates of the polygon.

Default:
[20,20,80,80,20]

Suggested values:
0, 1, 2, 3, 4, 5, 10, 20, 50, 100, 200, 500

**`radius`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Radii of the rounded corners.

Default:
[20,20,20,20,20]

Suggested values:
0, 1, 2, 5, 10, 20, 50

**`samplingInterval`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Distance of the samples.

Default:
1.0

Suggested values:
0.5, 1.0, 2.0, 5.0

## Possible Predecessors

`GetRegionContour`

## Possible Successors

`SmoothContoursXld`,
`GenPolygonsXld`

## See also

`GenContourPolygonXld`,
`GenContoursSkeletonXld`

## Module

Foundation
