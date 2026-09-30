# CloseMeasure (Operator)

## Name

`CloseMeasure` — Delete a measure object.

## Signature

`static void HOperatorSet.CloseMeasure(HTuple measureHandle)`

`void HMeasure.CloseMeasure()`

## Description

`CloseMeasure` deletes the measure object given by
*`measureHandle`*. The memory used for the measure object is
freed.

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

## Result

If the parameter values are correct the operator `CloseMeasure`
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`GenMeasureRectangle2`,
`GenMeasureArc`,
`MeasurePos`,
`MeasurePairs`

## Alternatives

`ClearHandle`

## See also

`ClearHandle`

## Module

1D Metrology
