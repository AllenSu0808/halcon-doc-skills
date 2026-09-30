# clear_scattered_data_interpolator (Operator)

## Name

`clear_scattered_data_interpolator` — Clear a scattered data interpolator.

## Signature

`def clear_scattered_data_interpolator(scattered_data_interpolator_handle: MaybeSequence[HHandle]) -> None`

## Description

`clear_scattered_data_interpolator` clears the scattered data
interpolator given by *`scattered_data_interpolator_handle`* and frees all
memory required for the interpolator.
After calling `clear_scattered_data_interpolator`, the scattered
data interpolator can no longer be used.
The handle *`scattered_data_interpolator_handle`* becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- scattered_data_interpolator_handle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`scattered_data_interpolator_handle`** (input_control, state is modified)  scattered_data_interpolator(-array) `→` MaybeSequence[HHandle]

Handle of the scattered data interpolator

## Result

If the parameters are valid, the operator
`clear_scattered_data_interpolator` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Possible Predecessors

`create_scattered_data_interpolator`,
`interpolate_scattered_data`

## Module

Foundation
