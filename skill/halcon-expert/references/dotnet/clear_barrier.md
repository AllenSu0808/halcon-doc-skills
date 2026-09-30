# ClearBarrier (Operator)

## Name

`ClearBarrier` — Destroy a barrier synchronization object.

## Signature

`static void HOperatorSet.ClearBarrier(HTuple barrierHandle)`

`void HBarrier.ClearBarrier()`

## Description

`ClearBarrier` destroys the barrier object given in
*`barrierHandle`*. No threads should be waiting on the barrier at the
time `ClearBarrier` is called. After calling `ClearBarrier`,
the barrier can no longer be used.
The handle *`barrierHandle`* becomes invalid.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- barrierHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`barrierHandle`** (input_control, state is modified)  barrier `→` [HBarrier](HBarrier.md), [HTuple](HTuple.md) (*IntPtr*)

Barrier synchronization object.

## Result

If the barrier handle is valid, the operator `ClearBarrier` returns
2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateBarrier`

## See also

`CreateBarrier`

## Module

Foundation
