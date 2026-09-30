# ClearScatteredDataInterpolator (Operator)

## Name

`ClearScatteredDataInterpolator` — Clear a scattered data interpolator.

## Signature

`static void HOperatorSet.ClearScatteredDataInterpolator(HTuple scatteredDataInterpolatorHandle)`

`static void HScatteredDataInterpolator.ClearScatteredDataInterpolator(HScatteredDataInterpolator[] scatteredDataInterpolatorHandle)`

`void HScatteredDataInterpolator.ClearScatteredDataInterpolator()`

## Description

`ClearScatteredDataInterpolator` clears the scattered data
interpolator given by *`scatteredDataInterpolatorHandle`* and frees all
memory required for the interpolator.
After calling `ClearScatteredDataInterpolator`, the scattered
data interpolator can no longer be used.
The handle *`scatteredDataInterpolatorHandle`* becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- scatteredDataInterpolatorHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`scatteredDataInterpolatorHandle`** (input_control, state is modified)  scattered_data_interpolator(-array) `→` [HScatteredDataInterpolator](HScatteredDataInterpolator.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the scattered data interpolator

## Result

If the parameters are valid, the operator
`ClearScatteredDataInterpolator` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Possible Predecessors

`CreateScatteredDataInterpolator`,
`InterpolateScatteredData`

## Module

Foundation
