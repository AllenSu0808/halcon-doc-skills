# compare_obj (Operator)

## Name

`compare_obj` — Compare iconic objects regarding equality.

## Signature

`compare_obj(Objects1, Objects2 : : Epsilon : IsEqual)`

## Description

The operator `compare_obj` compares iconic objects regarding
equality. The iconic objects are passed in the two input parameters
*`Objects1`* and *`Objects2`* in form of (possibly mixed)
tuples of images, regions, or XLDs.
The n-th object in *`Objects1`* is compared to the n-th object in
*`Objects2`* (for all n).
If the two passed object tuples have the same length and if all objects
are equal, the parameter *`IsEqual`* is set to 1, otherwise to 0.

For a short description of the iconic objects that are available in HALCON
see the introduction of chapter [Object](toc_object.md).

Depending on the type of the input objects, different conditions must be
met for the equality of two objects. In the following, the conditions
for each possible iconic object are listed:

- **Images:** —

  For all channels, the gray values of the respective pixels must
  not differ by more than *`Epsilon`*. Note that images are
  only compared within their domain (ROI) and they are only equal
  if they have the same domain (ROI).
- **Regions:** —

  The regions must be equal. The parameter *`Epsilon`* has no
  effect for the comparison of regions.
- **XLD contours:** —

  XLD contours must have the same number of points and attributes.
  The point coordinates and the attribute values must not differ by
  more than *`Epsilon`*.
- **XLD polygons:** —

  XLD polygons must have the same number of line segments. The
  length and the orientation of these segments as well as the
  coordinates of the control points must not differ by more than
  *`Epsilon`*.
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

Note that `compare_obj` compares all objects regarding their
actual content. In contrast [`test_equal_obj`](test_equal_obj.md) compares only
regions regarding their actual content while for all other objects
their location in memory is compared.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Objects1`** (input_object)  object(-array) `→` object

Reference objects.

**`Objects2`** (input_object)  object(-array) `→` object

Test objects.

**`Epsilon`** (input_control)  number `→`  (real / integer)

Maximum allowed difference between two gray values or
coordinates etc.

Default:
0.0

Suggested values:
0.0, 1.e-5

**`IsEqual`** (output_control)  integer `→`  (integer)

Boolean result value.

## Result

The operator `compare_obj` returns the value 2 (
H_MSG_TRUE)
if the
parameters are correct. The behavior in case of empty input (no input
objects available) is set via the operator
`set_system(::'no_object_result',<Result>:)`. If the number of
objects differs an exception is raised.

## See also

`test_equal_obj`,
`test_equal_region`

## Module

Foundation
