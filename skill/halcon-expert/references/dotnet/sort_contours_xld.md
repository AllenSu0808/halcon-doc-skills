# SortContoursXld (Operator)

## Name

`SortContoursXld` — Sort contours with respect to their relative position.

## Signature

`static void HOperatorSet.SortContoursXld(HObject contours, out HObject sortedContours, HTuple sortMode, HTuple order, HTuple rowOrCol)`

`HXLDCont HXLDCont.SortContoursXld(string sortMode, string order, string rowOrCol)`

## Description

The operator `SortContoursXld` sorts the contours
with respect to their relative position. *`rowOrCol`* specifies the
sorting criteria:
*"row"* sorts the contours with respect to the row coordinate of
their position first and, if the row coordinates are identical, with respect
to the column coordinate. In contrast, *"column"* sorts
contours according to the column coordinate first.
*`sortMode`* defines the position of a contour by individual reference
points. The following parameter values are available:

- ***"upper_left"*:** —

  The position is determined by the upper left corner of the
  surrounding rectangle.
- ***"upper_right"*:** —

  The position is determined by the upper right corner of the
  surrounding rectangle.
- ***"lower_left"*:** —

  The position is determined by the lower left corner of the
  surrounding rectangle.
- ***"lower_right"*:** —

  The position is determined by the lower right corner of the
  surrounding rectangle.
- ***"character"*:** —

  The position is determined by the upper left corner of the
  surrounding rectangle. In contrast to *"upper_left"*,
  the contours
  are also sorted according to the remaining coordinate, if they
  overlap in
  the direction of the coordinate which is specified by the
  parameter *`rowOrCol`*.

The parameter *`order`* determines whether the
sorting order is increasing or decreasing: using
*"true"* the order will be increasing, using
*"false"* the order will be decreasing.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contours`** (input_object)  xld_cont-array `→` [HXLDCont](HXLDCont.md)

Contours to be sorted.

**`sortedContours`** (output_object)  xld_cont-array `→` [HXLDCont](HXLDCont.md)

Sorted contours.

**`sortMode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Kind of sorting.

Default:
"upper_left"

List of values:
"character", "lower_left", "lower_right", "upper_left", "upper_right"

**`order`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Increasing or decreasing sorting order.

Default:
"true"

List of values:
"false", "true"

**`rowOrCol`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Sorting first with respect to row, then to column.

Default:
"row"

List of values:
"column", "row"

## Result

If the parameters are correct, the operator
`SortContoursXld` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception will be raised.

## See also

`SortRegion`

## Module

Foundation
