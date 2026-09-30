# reset_fuzzy_measure (Operator)

## Name

`reset_fuzzy_measure` — Reset a fuzzy function.

## Signature

`reset_fuzzy_measure( : : MeasureHandle, SetType : )`

## Description

`reset_fuzzy_measure` discards a fuzzy function of the
fuzzy set *`SetType`*. This function should have been set by
[`set_fuzzy_measure`](set_fuzzy_measure.md) before.

For an explanation of the concept of 1D measuring see the introduction of
chapter [1D Measuring](toc_1dmeasuring.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- MeasureHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`MeasureHandle`** (input_control, state is modified)  measure `→`  (handle)

Measure object handle.

**`SetType`** (input_control)  string `→`  (string)

Selection of the fuzzy set.

Default:
'contrast'

List of values:
'contrast', 'gray', 'position', 'position_pair', 'size'

## Possible Predecessors

`set_fuzzy_measure`

## Possible Successors

`fuzzy_measure_pos`,
`fuzzy_measure_pairs`

## See also

`set_fuzzy_measure`,
`set_fuzzy_measure_norm_pair`

## Module

1D Metrology
