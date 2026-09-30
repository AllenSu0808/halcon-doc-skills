# union_straight_contours_histo_xld (Operator)

## Name

`union_straight_contours_histo_xld` — Compute the union of neighboring straight contours that have a similar
distance from a given line.

## Warning

**`union_straight_contours_histo_xld` is obsolete and is only provided
for reasons of backward compatibility. New applications should use the
operators of the chapter 1D Measuring instead.**

## Signature

`def union_straight_contours_histo_xld(contours: HObject, ref_line_start_row: int, ref_line_start_column: int, ref_line_end_row: int, ref_line_end_column: int, width: int, max_width: int, filter_size: int) -> Tuple[HObject, HObject, Sequence[int]]`

## Description

`union_straight_contours_histo_xld` merges neighboring XLD
contours *`contours`* if certain criteria are fulfilled.

The maximum and minimum distances of the contours to a given
reference line are calculated. From this distances a histogram is
created. If the histogram should be smoothed, *`filter_size`*
must be greater than one. Afterwards, the resulting histogram is
divided into ranges (from minima to minima). Contours which lie in
the same range are concatenated to a new contour. If the width of
the range is greater than *`max_width`*, all contours in this range
are ignored (removed). If a contour lies in two ranges or more it is
ignored, too. If there are parallel contours, there is a
risk of merging neighboring contours.

The parameters of the regression lines are calculated newly for merged
contours.

The resulting contours cannot be displayed.

## Attention

Before contours can be united by `union_straight_contours_histo_xld`,
the parameters of the regression lines to the contours must be calculated
by calling [`regress_contours_xld`](regress_contours_xld.md). Note further that already closed
contours are not considered for a union anymore.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contours`** (input_object)  xld_cont-array `→` HObject

Input XLD contours.

**`union_contours`** (output_object)  xld_cont-array `→` HObject

Output XLD contours.

**`selected_contours`** (output_object)  xld_cont-array `→` HObject

Output XLD contours.

**`ref_line_start_row`** (input_control)  line.begin.y `→` int

y coordinate of the starting point of the reference line.

Default:
0

**`ref_line_start_column`** (input_control)  line.begin.x `→` int

x coordinate of the starting point of the reference line.

Default:
0

**`ref_line_end_row`** (input_control)  line.end.y `→` int

y coordinate of the endpoint of the reference line.

Default:
0

**`ref_line_end_column`** (input_control)  line.end.x `→` int

x coordinate of the endpoint of the reference line.

Default:
0

**`width`** (input_control)  integer `→` int

Maximum distance.

Default:
1

**`max_width`** (input_control)  integer `→` int

Maximum width between two minima.

Default:
1

**`filter_size`** (input_control)  integer `→` int

Size of smoothing filter

Default:
1

Value range:
`1
≤
filter_size
≤
63`

**`histo_values`** (output_control)  integer-array `→` Sequence[int]

Output values of histogram.

## Module

Foundation
