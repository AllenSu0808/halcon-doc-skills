# SelectXldPoint (Operator)

## Name

`SelectXldPoint` — Choose all contours or polygons containing a given point.

## Signature

`static void HOperatorSet.SelectXldPoint(HObject XLDs, out HObject destXLDs, HTuple row, HTuple column)`

`HXLD HXLD.SelectXldPoint(HTuple row, HTuple column)`

`HXLD HXLD.SelectXldPoint(double row, double column)`

`HXLDCont HXLDCont.SelectXldPoint(HTuple row, HTuple column)`

`HXLDCont HXLDCont.SelectXldPoint(double row, double column)`

`HXLDPoly HXLDPoly.SelectXldPoint(HTuple row, HTuple column)`

`HXLDPoly HXLDPoly.SelectXldPoint(double row, double column)`

`HXLDPara HXLDPara.SelectXldPoint(HTuple row, HTuple column)`

`HXLDPara HXLDPara.SelectXldPoint(double row, double column)`

`HXLDModPara HXLDModPara.SelectXldPoint(HTuple row, HTuple column)`

`HXLDModPara HXLDModPara.SelectXldPoint(double row, double column)`

`HXLDExtPara HXLDExtPara.SelectXldPoint(HTuple row, HTuple column)`

`HXLDExtPara HXLDExtPara.SelectXldPoint(double row, double column)`

## Description

The operator `SelectXldPoint` selects all contours or polygons from
*`XLDs`*
containing the test point (*`row`*,*`column`*).
If the contours or polygons overlap, more than one contour or polygon might
contain the point.
In this case, all these contours or polygons are returned.
If no contour or polygon contains the indicated point, an
empty object is returned.
It is assumed that the contours or polygons are closed. If this is not the
case, `SelectXldPoint` will artificially close the contours or
polygons.
Nevertheless, it is strongly recommended to pass only meaningful and closed
contours or polygons in *`XLDs`* by calling [`SelectContoursXld`](select_contours_xld.md)
with the parameter *"closed"* before calling
`SelectXldPoint`.

## Attention

If the test point is on the border of a contour or polygon,
`SelectXldPoint` will deliver unpredictable results, i.e., the
contour or polygon may be or may not be added to *`destXLDs`*,
depending on arbitrary factors such as how
the polygon is oriented with respect to the coordinate system. Note further
that for points in the near proximity of the contour or polygon sides, a
reliable classification is practically impossible because of numerical
inaccuracies.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`XLDs`** (input_object)  xld(-array) `→` [HXLD](HXLD.md)

Contours or polygons to be examined.

**`destXLDs`** (output_object)  xld(-array) `→` [HXLD](HXLD.md)

All contours or polygons containing the test
point.

**`row`** (input_control)  point.y `→` [HTuple](HTuple.md) (*double* / int / long)

Line coordinate of the test point.

Default:
100.0

**`column`** (input_control)  point.x `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the test point.

Default:
100.0

## Result

The operator `SelectXldPoint` returns the value 2 (
H_MSG_TRUE)
if the parameters are correct.
The behavior in case of empty input (no input contours or polygons
available) is set via the operator
`set_system('no_object_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`SelectContoursXld`,
`CloseContoursXld`,
`ThresholdSubPix`

## Alternatives

`TestXldPoint`

## Module

Foundation
