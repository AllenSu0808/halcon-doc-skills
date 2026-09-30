# sort_contours_xld (Operator)

## Name

`sort_contours_xld` — Sort contours with respect to their relative position.

## Signature

`sort_contours_xld(Contours : SortedContours : SortMode, Order, RowOrCol : )`

## Description

The operator `sort_contours_xld` sorts the contours
with respect to their relative position. *`RowOrCol`* specifies the
sorting criteria:
*'row'* sorts the contours with respect to the row coordinate of
their position first and, if the row coordinates are identical, with respect
to the column coordinate. In contrast, *'column'* sorts
contours according to the column coordinate first.
*`SortMode`* defines the position of a contour by individual reference
points. The following parameter values are available:

- ***'upper_left'*:** —

  The position is determined by the upper left corner of the
  surrounding rectangle.
- ***'upper_right'*:** —

  The position is determined by the upper right corner of the
  surrounding rectangle.
- ***'lower_left'*:** —

  The position is determined by the lower left corner of the
  surrounding rectangle.
- ***'lower_right'*:** —

  The position is determined by the lower right corner of the
  surrounding rectangle.
- ***'character'*:** —

  The position is determined by the upper left corner of the
  surrounding rectangle. In contrast to *'upper_left'*,
  the contours
  are also sorted according to the remaining coordinate, if they
  overlap in
  the direction of the coordinate which is specified by the
  parameter *`RowOrCol`*.

The parameter *`Order`* determines whether the
sorting order is increasing or decreasing: using
*'true'* the order will be increasing, using
*'false'* the order will be decreasing.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Contours`** (input_object)  xld_cont-array `→` object

Contours to be sorted.

**`SortedContours`** (output_object)  xld_cont-array `→` object

Sorted contours.

**`SortMode`** (input_control)  string `→`  (string)

Kind of sorting.

Default:
'upper_left'

List of values:
'character', 'lower_left', 'lower_right', 'upper_left', 'upper_right'

**`Order`** (input_control)  string `→`  (string)

Increasing or decreasing sorting order.

Default:
'true'

List of values:
'false', 'true'

**`RowOrCol`** (input_control)  string `→`  (string)

Sorting first with respect to row, then to column.

Default:
'row'

List of values:
'column', 'row'

## Result

If the parameters are correct, the operator
`sort_contours_xld` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception will be raised.

## See also

`sort_region`

## Module

Foundation
