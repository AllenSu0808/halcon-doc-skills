# ContourPointNumXld (Operator)

## Name

`ContourPointNumXld` — Return the number of points in an XLD contour.

## Signature

`static void HOperatorSet.ContourPointNumXld(HObject contour, out HTuple length)`

`HTuple HXLDCont.ContourPointNumXld()`

## Description

`ContourPointNumXld` returns the length of the input
contour *`contour`*, i.e., its number of points, in
*`length`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contour`** (input_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Input XLD contour.

**`length`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Number of contour points.

## Possible Predecessors

`GenContoursSkeletonXld`,
`LinesGauss`,
`LinesFacet`,
`EdgesSubPix`

## Possible Successors

`GetContourXld`,
`GetContourAttribXld`

## Alternatives

`GetRegressParamsXld`

## See also

`QueryContourAttribsXld`

## Module

Foundation
