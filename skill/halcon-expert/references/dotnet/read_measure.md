# ReadMeasure (Operator)

## Name

`ReadMeasure` — Read a measure object from a file.

## Signature

`static void HOperatorSet.ReadMeasure(HTuple fileName, out HTuple measureHandle)`

`void HMeasure.ReadMeasure(string fileName)`

## Description

`ReadMeasure` reads a measure object, which has
been written with [`WriteMeasure`](write_measure.md) from
the file *`fileName`*. The default HALCON file
extension for a measure object is 'msr'. The values
contained in the read measure object are stored in a measure object
with the handle *`measureHandle`*.

For an explanation of the concept of 1D measuring see the introduction of
chapter [1D Measuring](toc_1dmeasuring.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`fileName`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

File name.

File extension:
.`msr`

**`measureHandle`** (output_control)  measure `→` [HMeasure](HMeasure.md), [HTuple](HTuple.md) (*IntPtr*)

Measure object handle.

## Result

If the parameters are valid, the operator
`ReadMeasure` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Successors

`MeasurePos`,
`MeasurePairs`

## See also

`WriteMeasure`

## Module

1D Metrology
