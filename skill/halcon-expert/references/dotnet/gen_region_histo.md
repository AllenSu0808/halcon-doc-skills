# GenRegionHisto (Operator)

## Name

`GenRegionHisto` — Convert a histogram into a region.

## Signature

`static void HOperatorSet.GenRegionHisto(out HObject region, HTuple histogram, HTuple row, HTuple column, HTuple scale)`

`void HRegion.GenRegionHisto(HTuple histogram, int row, int column, int scale)`

## Description

`GenRegionHisto` converts a histogram created with
[`GrayHisto`](gray_histo.md), [`GrayHistoRange`](gray_histo_range.md) ,or [`TupleHistoRange`](tuple_histo_range.md)
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

**`region`** (output_object)  region `→` [HRegion](HRegion.md)

Region containing the histogram.

**`histogram`** (input_control)  histogram-array `→` [HTuple](HTuple.md) (*int* / long)

Input histogram.

**`row`** (input_control)  point.y `→` [HTuple](HTuple.md) (*int* / long)

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

**`column`** (input_control)  point.x `→` [HTuple](HTuple.md) (*int* / long)

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

**`scale`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

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

`GenRegionHisto` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If necessary, an exception is raised.

## Possible Predecessors

`GrayHisto`,
`GrayHistoRange`,
`TupleHistoRange`

## See also

`DispChannel`

## Module

Foundation
