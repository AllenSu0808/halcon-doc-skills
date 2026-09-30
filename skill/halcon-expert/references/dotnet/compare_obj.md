# CompareObj (Operator)

## Name

`CompareObj` — Compare iconic objects regarding equality.

## Signature

`static void HOperatorSet.CompareObj(HObject objects1, HObject objects2, HTuple epsilon, out HTuple isEqual)`

`int HObject.CompareObj(HObject objects2, HTuple epsilon)`

`int HObject.CompareObj(HObject objects2, double epsilon)`

`int HImage.CompareObj(HImage objects2, HTuple epsilon)`

`int HImage.CompareObj(HImage objects2, double epsilon)`

`int HRegion.CompareObj(HRegion objects2, HTuple epsilon)`

`int HRegion.CompareObj(HRegion objects2, double epsilon)`

`int HXLD.CompareObj(HXLD objects2, HTuple epsilon)`

`int HXLD.CompareObj(HXLD objects2, double epsilon)`

`int HXLDCont.CompareObj(HXLDCont objects2, HTuple epsilon)`

`int HXLDCont.CompareObj(HXLDCont objects2, double epsilon)`

`int HXLDPoly.CompareObj(HXLDPoly objects2, HTuple epsilon)`

`int HXLDPoly.CompareObj(HXLDPoly objects2, double epsilon)`

`int HXLDPara.CompareObj(HXLDPara objects2, HTuple epsilon)`

`int HXLDPara.CompareObj(HXLDPara objects2, double epsilon)`

`int HXLDModPara.CompareObj(HXLDModPara objects2, HTuple epsilon)`

`int HXLDModPara.CompareObj(HXLDModPara objects2, double epsilon)`

`int HXLDExtPara.CompareObj(HXLDExtPara objects2, HTuple epsilon)`

`int HXLDExtPara.CompareObj(HXLDExtPara objects2, double epsilon)`

## Description

The operator `CompareObj` compares iconic objects regarding
equality. The iconic objects are passed in the two input parameters
*`objects1`* and *`objects2`* in form of (possibly mixed)
tuples of images, regions, or XLDs.
The n-th object in *`objects1`* is compared to the n-th object in
*`objects2`* (for all n).
If the two passed object tuples have the same length and if all objects
are equal, the parameter *`isEqual`* is set to 1, otherwise to 0.

For a short description of the iconic objects that are available in HALCON
see the introduction of chapter [Object](toc_object.md).

Depending on the type of the input objects, different conditions must be
met for the equality of two objects. In the following, the conditions
for each possible iconic object are listed:

- **Images:** —

  For all channels, the gray values of the respective pixels must
  not differ by more than *`epsilon`*. Note that images are
  only compared within their domain (ROI) and they are only equal
  if they have the same domain (ROI).
- **Regions:** —

  The regions must be equal. The parameter *`epsilon`* has no
  effect for the comparison of regions.
- **XLD contours:** —

  XLD contours must have the same number of points and attributes.
  The point coordinates and the attribute values must not differ by
  more than *`epsilon`*.
- **XLD polygons:** —

  XLD polygons must have the same number of line segments. The
  length and the orientation of these segments as well as the
  coordinates of the control points must not differ by more than
  *`epsilon`*.
- **XLD parallels and extended XLD parallels:** —

  XLD parallels must have an identical index of the start and end
  line segment of the parallels of the first polygon (P1) and the
  second polygon (P2) as well as identical pointers to the
  underlying contours.
- **Modified XLD parallels:** —

  For modified XLD parallels, the same conditions apply as for XLD
  parallels and extended XLD parallels. Furthermore, the distances
  between the line segments of the parallel polygons must be
  identical.

Note that `CompareObj` compares all objects regarding their
actual content. In contrast [`TestEqualObj`](test_equal_obj.md) compares only
regions regarding their actual content while for all other objects
their location in memory is compared.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`objects1`** (input_object)  object(-array) `→` [HObject](HObject.md)

Reference objects.

**`objects2`** (input_object)  object(-array) `→` [HObject](HObject.md)

Test objects.

**`epsilon`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Maximum allowed difference between two gray values or
coordinates etc.

Default:
0.0

Suggested values:
0.0, 1.e-5

**`isEqual`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Boolean result value.

## Result

The operator `CompareObj` returns the value 2 (
H_MSG_TRUE)
if the
parameters are correct. The behavior in case of empty input (no input
objects available) is set via the operator
`set_system(::'no_object_result',<Result>:)`. If the number of
objects differs an exception is raised.

## See also

`TestEqualObj`,
`TestEqualRegion`

## Module

Foundation
