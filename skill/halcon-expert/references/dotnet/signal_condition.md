# SignalCondition (Operator)

## Name

`SignalCondition` — Signal a condition synchronization object.

## Signature

`static void HOperatorSet.SignalCondition(HTuple conditionHandle)`

`void HCondition.SignalCondition()`

## Description

`SignalCondition` restarts one of the threads that are waiting on the
condition variable *`conditionHandle`*. If no threads are waiting on
*`conditionHandle`*, nothing happens. If several threads are waiting on
*`conditionHandle`*, exactly one is restarted, but it is not specified
which one.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`conditionHandle`** (input_control)  condition `→` [HCondition](HCondition.md), [HTuple](HTuple.md) (*IntPtr*)

Condition synchronization object.

## Result

If the condition handle is valid, the operator `SignalCondition`
returns 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Possible Predecessors

`CreateCondition`,
`WaitCondition`

## See also

`WaitCondition`,
`TimedWaitCondition`

## Module

Foundation
