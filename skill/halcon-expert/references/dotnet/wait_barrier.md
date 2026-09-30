# WaitBarrier (Operator)

## Name

`WaitBarrier` — Wait on the release of a barrier synchronization object.

## Signature

`static void HOperatorSet.WaitBarrier(HTuple barrierHandle)`

`void HBarrier.WaitBarrier()`

## Description

`WaitBarrier` blocks the thread at a barrier object given by
*`barrierHandle`* until a specified number of threads have called the
same barrier object. This number is specified by parameter `teamSize`
during the creation
of the barrier object by [`CreateBarrier`](create_barrier.md).

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`barrierHandle`** (input_control)  barrier `→` [HBarrier](HBarrier.md), [HTuple](HTuple.md) (*IntPtr*)

Barrier synchronization object.

## Result

If the barrier handle is valid, the operator `WaitBarrier`
returns 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Successors

`ClearBarrier`

## Module

Foundation
