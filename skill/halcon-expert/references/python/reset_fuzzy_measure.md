# reset_fuzzy_measure (Operator)

## Name

`reset_fuzzy_measure` — Reset a fuzzy function.

## Signature

`def reset_fuzzy_measure(measure_handle: HHandle, set_type: str) -> None`

## Description

`reset_fuzzy_measure` discards a fuzzy function of the
fuzzy set *`set_type`*. This function should have been set by
[`set_fuzzy_measure`](set_fuzzy_measure.md) before.

For an explanation of the concept of 1D measuring see the introduction of
chapter [1D Measuring](toc_1dmeasuring.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- measure_handle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`measure_handle`** (input_control, state is modified)  measure `→` HHandle

Measure object handle.

**`set_type`** (input_control)  string `→` str

Selection of the fuzzy set.

Default:
"contrast"

List of values:
"contrast", "gray", "position", "position_pair", "size"

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
