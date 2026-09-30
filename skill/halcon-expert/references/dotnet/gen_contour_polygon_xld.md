# GenContourPolygonXld (Operator)

## Name

`GenContourPolygonXld` — Generate an XLD contour from a polygon (given as tuples).

## Signature

`static void HOperatorSet.GenContourPolygonXld(out HObject contour, HTuple row, HTuple col)`

`public HXLDCont(HTuple row, HTuple col)`

`void HXLDCont.GenContourPolygonXld(HTuple row, HTuple col)`

## Description

`GenContourPolygonXld` generates an XLD contour
*`contour`* from a polygon given in the tuples *`row`*
and *`col`*. This operator is useful if contours have been
obtained from routines outside the core library, but higher level
operators, e.g., polygon approximation and extraction of parallels,
are to be performed on the contours.

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
[0,1,2,2,2]

Suggested values:
0, 1, 2, 3, 4, 5, 10, 20, 50, 100, 200, 500

**`col`** (input_control)  coordinates.x-array `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinates of the polygon.

Default:
[0,0,0,1,2]

Suggested values:
0, 1, 2, 3, 4, 5, 10, 20, 50, 100, 200, 500

## Possible Predecessors

`GetRegionContour`

## Possible Successors

`SmoothContoursXld`,
`GenPolygonsXld`

## See also

`GenContoursSkeletonXld`,
`GetContourXld`

## Module

Foundation
