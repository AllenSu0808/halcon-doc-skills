# gen_region_histo (Operator)

## Name

`gen_region_histo` — Convert a histogram into a region.

## Signature

`def gen_region_histo(histogram: Sequence[int], row: int, column: int, scale: int) -> HObject`

## Description

`gen_region_histo` converts a histogram created with
[`gray_histo`](gray_histo.md), [`gray_histo_range`](gray_histo_range.md) ,or [`tuple_histo_range`](tuple_histo_range.md)
into a region. *`row`* and *`column`* define the position of the
center of the graphic.
*`scale`* allows scaling of the graphic, whereby *1* means
displaying all 256 values, *2* means displaying 128 values, *3*
means displaying only 64 values, etc.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region`** (output_object)  region `→` HObject

Region containing the histogram.

**`histogram`** (input_control)  histogram-array `→` Sequence[int]

Input histogram.

**`row`** (input_control)  point.y `→` int

Row coordinate of the center of the histogram.

Default:
255

Suggested values:
100, 200, 255, 300, 400

Value range:
`0
≤
row
≤
511`

**`column`** (input_control)  point.x `→` int

Column coordinate of the center of the histogram.

Default:
255

Suggested values:
100, 200, 255, 300, 400

Value range:
`0
≤
column
≤
511`

**`scale`** (input_control)  integer `→` int

Scale factor for the histogram.

Default:
1

Suggested values:
1, 2, 3, 4, 5, 6, 7

Value range:
`1
≤
scale
≤
10` (lin)

Minimum increment:
1

Recommended increment:
1

## Result

`gen_region_histo` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If necessary, an exception is raised.

## Possible Predecessors

`gray_histo`,
`gray_histo_range`,
`tuple_histo_range`

## See also

`disp_channel`

## Module

Foundation
