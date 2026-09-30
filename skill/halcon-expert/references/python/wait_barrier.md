# wait_barrier (Operator)

## Name

`wait_barrier` — Wait on the release of a barrier synchronization object.

## Signature

`def wait_barrier(barrier_handle: HHandle) -> None`

## Description

`wait_barrier` blocks the thread at a barrier object given by
*`barrier_handle`* until a specified number of threads have called the
same barrier object. This number is specified by parameter `team_size`
during the creation
of the barrier object by [`create_barrier`](create_barrier.md).

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`barrier_handle`** (input_control)  barrier `→` HHandle

Barrier synchronization object.

## Result

If the barrier handle is valid, the operator `wait_barrier`
returns 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Successors

`clear_barrier`

## Module

Foundation
