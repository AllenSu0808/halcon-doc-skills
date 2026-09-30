# WriteMeasure (Operator)

## Name

`WriteMeasure` — Write a measure object to a file.

## Signature

`static void HOperatorSet.WriteMeasure(HTuple measureHandle, HTuple fileName)`

`void HMeasure.WriteMeasure(string fileName)`

## Description

`WriteMeasure` writes a measure object that has been
created by, e.g., [`GenMeasureRectangle2`](gen_measure_rectangle2.md)
to the file *`fileName`*. The measure object
is defined by the handle *`measureHandle`*. The measure
object can be read with [`ReadMeasure`](read_measure.md). The default
HALCON file extension for a measure object is 'msr'.

For an explanation of the concept of 1D measuring see the introduction of
chapter [1D Measuring](toc_1dmeasuring.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`measureHandle`** (input_control)  measure `→` [HMeasure](HMeasure.md), [HTuple](HTuple.md) (*IntPtr*)

Measure object handle.

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

File name.

File extension:
.`msr`

## Result

If the parameters are valid, the operator
`WriteMeasure` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`GenMeasureRectangle2`,
`GenMeasureArc`

## See also

`ReadMeasure`

## Module

1D Metrology
