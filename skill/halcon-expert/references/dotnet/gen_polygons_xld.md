# GenPolygonsXld (Operator)

## Name

`GenPolygonsXld` — Approximate XLD contours by polygons.

## Signature

`static void HOperatorSet.GenPolygonsXld(HObject contours, out HObject polygons, HTuple type, HTuple alpha)`

`HXLDPoly HXLDCont.GenPolygonsXld(string type, HTuple alpha)`

`HXLDPoly HXLDCont.GenPolygonsXld(string type, double alpha)`

## Description

`GenPolygonsXld` approximates XLD contours
(*`contours`*) by polygons. The type of the approximation
can be set by *`type`*. The threshold for the approximation
is set via *`alpha`*. The procedure is able to process open
as well as closed contours. The resulting approximating XLD
polygons are returned in *`polygons`*.

Contours can be approximated by the algorithm of Ramer, which
approximates contours such that the Euclidean distance of the
approximating polygon to the contour is at most *`alpha`* pixel
units.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contours`** (input_object)  xld_cont-array `→` [HXLDCont](HXLDCont.md)

Contours to be approximated.

**`polygons`** (output_object)  xld_poly-array `→` [HXLDPoly](HXLDPoly.md)

Approximating polygons.

**`type`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Type of approximation.

Default:
"ramer"

List of values:
"ramer"

**`alpha`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Threshold for the approximation.

Default:
2.0

Suggested values:
1.0, 1.5, 2.0, 3.0, 4.0

Restriction:
`Alpha > 0.0`

## Possible Predecessors

`GenContoursSkeletonXld`,
`LinesGauss`,
`LinesFacet`,
`EdgesSubPix`

## Possible Successors

`GenParallelsXld`,
`SplitContoursXld`

## See also

`GetRegionPolygon`

## Module

Foundation
