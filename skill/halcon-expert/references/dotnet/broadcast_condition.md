# BroadcastCondition (Operator)

## Name

`BroadcastCondition` — Signal a condition synchronization object.

## Signature

`static void HOperatorSet.BroadcastCondition(HTuple conditionHandle)`

`void HCondition.BroadcastCondition()`

## Description

`BroadcastCondition` restarts all the threads that are waiting on the
condition variable *`conditionHandle`*. Nothing happens if no threads
are waiting on *`conditionHandle`*.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`conditionHandle`** (input_control)  condition `→` [HCondition](HCondition.md), [HTuple](HTuple.md) (*IntPtr*)

Condition synchronization object.

## Result

If the condition handle is valid, the operator `BroadcastCondition`
returns 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateCondition`,
`WaitCondition`

## See also

`WaitCondition`,
`TimedWaitCondition`

## Module

Foundation
