# GetSampleNumClassTrainData (Operator)

## Name

`GetSampleNumClassTrainData` — Return the number of training samples stored in the training data.

## Signature

`static void HOperatorSet.GetSampleNumClassTrainData(HTuple classTrainDataHandle, out HTuple numSamples)`

`int HClassTrainData.GetSampleNumClassTrainData()`

## Description

`GetSampleNumClassTrainData` returns in *`numSamples`* the
number of training samples which are stored in the training data specified
by *`classTrainDataHandle`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`classTrainDataHandle`** (input_control)  class_train_data `→` [HClassTrainData](HClassTrainData.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of training data.

**`numSamples`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of stored training samples.

## Result

If *`classTrainDataHandle`* is valid, the operator
`GetSampleNumClassTrainData` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`AddSampleClassTrainData`

## Possible Successors

`GetSampleClassTrainData`

## See also

`CreateClassTrainData`

## Module

Foundation
