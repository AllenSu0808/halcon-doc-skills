# sort_region (Operator)

## Name

`sort_region` — Sorting of regions with respect to their relative position.

## Signature

`def sort_region(regions: HObject, sort_mode: MaybeSequence[Union[int, float, str]], order: str, row_or_col: str) -> HObject`

## Description

The operator `sort_region` sorts the regions
with respect to their relative position.
All sorting methods with the exception of *"character"*
use one point of the region. With the help of the parameter
*`row_or_col`* = *"row"* these points will be
sorted according to their row and then according to their
column. By using *"column"*, the column value will
be used first.
The following values are available for the parameter
*`sort_mode`*:

- ***"character"*** —

  The regions are treated like characters, which can be read
  horizontally or vertically. They are sorted according
  to the reading direction given by *`row_or_col`* with
  the following specifications:

  - *"row"*: Regarded as rows, the reading
    direction is firstly from left to right and then from
    top to bottom.
  - *"column"*: Regarded as columns, the reading
    direction is firstly from top to bottom and then from left
    to right.

  For *`sort_mode`* *"character"*, a second numeric value
  can be passed to *`sort_mode`* in addition to *"character"*.
  This value specifies the maximum percentage of overlap. This overlap
  depends on the parameter *`row_or_col`* and is determined as
  follows:

  - *`row_or_col`* = *"row"*: overlap of row coordinates
    between two regions
  - *`row_or_col`* = *"column"*: overlap of column
    coordinates between two regions,

  whereas the percentage of overlap is calculated using the smaller one
  of the overlapping regions (with respect to the specified axis).
  Regions that do not overlap in their coordinates or have an overlap
  of less than the set percentage are seen as being in different rows
  (or columns, respectively) and sorted accordingly. In case the overlap
  is larger, the regions are seen as being in the same row (or column)
  instead and therefore sorted within the row (or column). For example
  when this additional parameter is set to 0, all regions that overlap
  in their row (or column) coordinates are sorted within the same row
  (or column). The default value of this parameter is 15 which means
  that adjacent rows (or columns) can have an overlap of maximum 15%
  in order to be considered as different rows (or columns).
  Note that for *`order`* = *"false"*, the characters
  are sorted in a reversed order to the one described above.
- ***"first_point"*** —

  The point with the lowest column value in the first row
  of the region.
- ***"last_point"*** —

  The point with the highest column value in the last row
  of the region.
- ***"upper_left"*** —

  Upper left corner of the surrounding rectangle.
- ***"upper_right"*** —

  Upper right corner of the surrounding rectangle.
- ***"lower_left"*** —

  Lower left corner of the surrounding rectangle.
- ***"lower_right"*** —

  Lower right corner of the surrounding rectangle.

The parameter *`order`* determines whether the
sorting order is increasing or decreasing: using
*"true"* the order will be increasing, using
*"false"* the order will be decreasing.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`regions`** (input_object)  region-array `→` HObject

Regions to be sorted.

**`sorted_regions`** (output_object)  region-array `→` HObject

Sorted regions.

**`sort_mode`** (input_control)  tuple(-array) `→` MaybeSequence[Union[int, float, str]]

Kind of sorting.

Default:
"first_point"

List of values:
"character", "first_point", "last_point", "lower_left", "lower_right", "upper_left", "upper_right"

**`order`** (input_control)  string `→` str

Increasing or decreasing sorting order.

Default:
"true"

List of values:
"false", "true"

**`row_or_col`** (input_control)  string `→` str

Sorting first with respect to row, then to column.

Default:
"row"

List of values:
"column", "row"

## Result

If the parameters are correct, the operator
`sort_region` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception will be raised.

## Possible Successors

`do_ocr_multi_class_mlp`,
`do_ocr_single_class_mlp`

## Module

Foundation
