# TranslateMeasure (Operator)

## Name

`TranslateMeasure` — Translate a measure object.

## Signature

`static void HOperatorSet.TranslateMeasure(HTuple measureHandle, HTuple row, HTuple column)`

`void HMeasure.TranslateMeasure(HTuple row, HTuple column)`

`void HMeasure.TranslateMeasure(double row, double column)`

## Description

`TranslateMeasure` translates the reference point of the
measure object given by *`measureHandle`* to the point
(*`row`*, *`column`*). If the measure object and the
translated measure object lie completely within the image, the
measure object is shifted to the new reference point in an efficient
manner. Otherwise, the measure object is generated anew with
[`GenMeasureRectangle2`](gen_measure_rectangle2.md) or [`GenMeasureArc`](gen_measure_arc.md) using the
parameters that were specified when the measure object was created
and the new reference point.

For an explanation of the concept of 1D measuring see the introduction of
chapter [1D Measuring](toc_1dmeasuring.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- measureHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`measureHandle`** (input_control, state is modified)  measure `→` [HMeasure](HMeasure.md), [HTuple](HTuple.md) (*IntPtr*)

Measure object handle.

**`row`** (input_control)  point.y `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the new reference point.

Default:
50.0

Suggested values:
10.0, 20.0, 50.0, 100.0, 200.0, 300.0, 400.0, 500.0

Value range:
`0.0
≤
row
≤
511.0` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

**`column`** (input_control)  point.x `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the new reference point.

Default:
100.0

Suggested values:
10.0, 20.0, 50.0, 100.0, 200.0, 300.0, 400.0, 500.0

Value range:
`0.0
≤
column
≤
511.0` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

## Result

If the parameter values are correct the operator
`TranslateMeasure` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.

## Possible Predecessors

`GenMeasureRectangle2`,
`GenMeasureArc`

## Possible Successors

`MeasurePos`,
`MeasurePairs`,
`FuzzyMeasurePos`,
`FuzzyMeasurePairs`,
`FuzzyMeasurePairing`,
`MeasureThresh`

## Alternatives

`GenMeasureRectangle2`,
`GenMeasureArc`

## See also

`CloseMeasure`

## Module

1D Metrology
