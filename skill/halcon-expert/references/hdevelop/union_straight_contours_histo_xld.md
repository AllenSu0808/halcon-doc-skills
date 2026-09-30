# union_straight_contours_histo_xld (Operator)

## Name

`union_straight_contours_histo_xld` — Compute the union of neighboring straight contours that have a similar
distance from a given line.

## Warning

**`union_straight_contours_histo_xld` is obsolete and is only provided
for reasons of backward compatibility. New applications should use the
operators of the chapter 1D Measuring instead.**

## Signature

`union_straight_contours_histo_xld(Contours : UnionContours, SelectedContours : RefLineStartRow, RefLineStartColumn, RefLineEndRow, RefLineEndColumn, Width, MaxWidth, FilterSize : HistoValues)`

## Description

`union_straight_contours_histo_xld` merges neighboring XLD
contours *`Contours`* if certain criteria are fulfilled.

The maximum and minimum distances of the contours to a given
reference line are calculated. From this distances a histogram is
created. If the histogram should be smoothed, *`FilterSize`*
must be greater than one. Afterwards, the resulting histogram is
divided into ranges (from minima to minima). Contours which lie in
the same range are concatenated to a new contour. If the width of
the range is greater than *`MaxWidth`*, all contours in this range
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

**`Contours`** (input_object)  xld_cont-array `→` object

Input XLD contours.

**`UnionContours`** (output_object)  xld_cont-array `→` object

Output XLD contours.

**`SelectedContours`** (output_object)  xld_cont-array `→` object

Output XLD contours.

**`RefLineStartRow`** (input_control)  line.begin.y `→`  (integer)

y coordinate of the starting point of the reference line.

Default:
0

**`RefLineStartColumn`** (input_control)  line.begin.x `→`  (integer)

x coordinate of the starting point of the reference line.

Default:
0

**`RefLineEndRow`** (input_control)  line.end.y `→`  (integer)

y coordinate of the endpoint of the reference line.

Default:
0

**`RefLineEndColumn`** (input_control)  line.end.x `→`  (integer)

x coordinate of the endpoint of the reference line.

Default:
0

**`Width`** (input_control)  integer `→`  (integer)

Maximum distance.

Default:
1

**`MaxWidth`** (input_control)  integer `→`  (integer)

Maximum width between two minima.

Default:
1

**`FilterSize`** (input_control)  integer `→`  (integer)

Size of smoothing filter

Default:
1

Value range:
`1
≤
FilterSize
≤
63`

**`HistoValues`** (output_control)  integer-array `→`  (integer)

Output values of histogram.

## Module

Foundation
