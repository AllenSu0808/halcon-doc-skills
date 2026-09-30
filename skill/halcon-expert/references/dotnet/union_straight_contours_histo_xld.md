# UnionStraightContoursHistoXld (Operator)

## Name

`UnionStraightContoursHistoXld` — Compute the union of neighboring straight contours that have a similar
distance from a given line.

## Warning

**`UnionStraightContoursHistoXld` is obsolete and is only provided
for reasons of backward compatibility. New applications should use the
operators of the chapter 1D Measuring instead.**

## Signature

`static void HOperatorSet.UnionStraightContoursHistoXld(HObject contours, out HObject unionContours, out HObject selectedContours, HTuple refLineStartRow, HTuple refLineStartColumn, HTuple refLineEndRow, HTuple refLineEndColumn, HTuple width, HTuple maxWidth, HTuple filterSize, out HTuple histoValues)`

`HXLDCont HXLDCont.UnionStraightContoursHistoXld(out HXLDCont selectedContours, int refLineStartRow, int refLineStartColumn, int refLineEndRow, int refLineEndColumn, int width, int maxWidth, int filterSize, out HTuple histoValues)`

## Description

`UnionStraightContoursHistoXld` merges neighboring XLD
contours *`contours`* if certain criteria are fulfilled.

The maximum and minimum distances of the contours to a given
reference line are calculated. From this distances a histogram is
created. If the histogram should be smoothed, *`filterSize`*
must be greater than one. Afterwards, the resulting histogram is
divided into ranges (from minima to minima). Contours which lie in
the same range are concatenated to a new contour. If the width of
the range is greater than *`maxWidth`*, all contours in this range
are ignored (removed). If a contour lies in two ranges or more it is
ignored, too. If there are parallel contours, there is a
risk of merging neighboring contours.

The parameters of the regression lines are calculated newly for merged
contours.

The resulting contours cannot be displayed.

## Attention

Before contours can be united by `UnionStraightContoursHistoXld`,
the parameters of the regression lines to the contours must be calculated
by calling [`RegressContoursXld`](regress_contours_xld.md). Note further that already closed
contours are not considered for a union anymore.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contours`** (input_object)  xld_cont-array `→` [HXLDCont](HXLDCont.md)

Input XLD contours.

**`unionContours`** (output_object)  xld_cont-array `→` [HXLDCont](HXLDCont.md)

Output XLD contours.

**`selectedContours`** (output_object)  xld_cont-array `→` [HXLDCont](HXLDCont.md)

Output XLD contours.

**`refLineStartRow`** (input_control)  line.begin.y `→` [HTuple](HTuple.md) (*int* / long)

y coordinate of the starting point of the reference line.

Default:
0

**`refLineStartColumn`** (input_control)  line.begin.x `→` [HTuple](HTuple.md) (*int* / long)

x coordinate of the starting point of the reference line.

Default:
0

**`refLineEndRow`** (input_control)  line.end.y `→` [HTuple](HTuple.md) (*int* / long)

y coordinate of the endpoint of the reference line.

Default:
0

**`refLineEndColumn`** (input_control)  line.end.x `→` [HTuple](HTuple.md) (*int* / long)

x coordinate of the endpoint of the reference line.

Default:
0

**`width`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Maximum distance.

Default:
1

**`maxWidth`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Maximum width between two minima.

Default:
1

**`filterSize`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Size of smoothing filter

Default:
1

Value range:
`1
≤
filterSize
≤
63`

**`histoValues`** (output_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Output values of histogram.

## Module

Foundation
