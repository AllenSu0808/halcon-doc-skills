# CloseContoursXld (Operator)

## Name

`CloseContoursXld` — Close an XLD contour.

## Signature

`static void HOperatorSet.CloseContoursXld(HObject contours, out HObject closedContours)`

`HXLDCont HXLDCont.CloseContoursXld()`

## Description

`CloseContoursXld` closes all XLD contours given in
*`contours`*. The resulting contours are returned in
*`closedContours`*. To obtain meaningful results, it is strongly
recommended to select contours with [`SelectContoursXld`](select_contours_xld.md) that have end
points that are not further apart than a certain maximum distance before
passing them to `CloseContoursXld`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contours`** (input_object)  xld_cont-array `→` [HXLDCont](HXLDCont.md)

Contours to be closed.

**`closedContours`** (output_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Closed contours.

## Possible Predecessors

`SelectContoursXld`

## Possible Successors

`AreaCenterXld`,
`CircularityXld`,
`CompactnessXld`,
`ConvexityXld`,
`EccentricityXld`,
`EllipticAxisXld`,
`MomentsXld`,
`MomentsAnyXld`,
`OrientationXld`,
`SelectShapeXld`,
`TestXldPoint`

## Module

Foundation
