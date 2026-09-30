# ResetFuzzyMeasure (Operator)

## Name

`ResetFuzzyMeasure` — Reset a fuzzy function.

## Signature

`static void HOperatorSet.ResetFuzzyMeasure(HTuple measureHandle, HTuple setType)`

`void HMeasure.ResetFuzzyMeasure(string setType)`

## Description

`ResetFuzzyMeasure` discards a fuzzy function of the
fuzzy set *`setType`*. This function should have been set by
[`SetFuzzyMeasure`](set_fuzzy_measure.md) before.

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

**`setType`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Selection of the fuzzy set.

Default:
"contrast"

List of values:
"contrast", "gray", "position", "position_pair", "size"

## Possible Predecessors

`SetFuzzyMeasure`

## Possible Successors

`FuzzyMeasurePos`,
`FuzzyMeasurePairs`

## See also

`SetFuzzyMeasure`,
`SetFuzzyMeasureNormPair`

## Module

1D Metrology
