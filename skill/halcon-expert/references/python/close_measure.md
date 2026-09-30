# close_measure (Operator)

## Name

`close_measure` — Delete a measure object.

## Signature

`def close_measure(measure_handle: HHandle) -> None`

## Description

`close_measure` deletes the measure object given by
*`measure_handle`*. The memory used for the measure object is
freed.

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

## Result

If the parameter values are correct the operator `close_measure`
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`gen_measure_rectangle2`,
`gen_measure_arc`,
`measure_pos`,
`measure_pairs`

## Alternatives

`clear_handle`

## See also

`clear_handle`

## Module

1D Metrology
