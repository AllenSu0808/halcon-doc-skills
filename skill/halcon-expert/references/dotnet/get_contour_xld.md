# GetContourXld (Operator)

## Name

`GetContourXld` — Return the coordinates of an XLD contour.

## Signature

`static void HOperatorSet.GetContourXld(HObject contour, out HTuple row, out HTuple col)`

`void HXLDCont.GetContourXld(out HTuple row, out HTuple col)`

## Description

`GetContourXld` returns the following values of the XLD
contour *`contour`*:

|  |  |
| --- | --- |
| *`row`* | Row coordinate of the contour's points |
| *`col`* | Column coordinate of the contour's points |

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contour`** (input_object)  xld_cont `→` [HXLDCont](HXLDCont.md)

Input XLD contour.

**`row`** (output_control)  point.y-array `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the contour's points.

**`col`** (output_control)  point.x-array `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the contour's points.

## Possible Predecessors

`GenContoursSkeletonXld`,
`LinesGauss`,
`LinesFacet`,
`EdgesSubPix`

## See also

`GetContourAttribXld`,
`QueryContourAttribsXld`,
`GetContourGlobalAttribXld`,
`QueryContourGlobalAttribsXld`,
`GenContourPolygonXld`

## Module

Foundation
