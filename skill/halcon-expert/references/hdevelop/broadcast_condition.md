# broadcast_condition (Operator)

## Name

`broadcast_condition` — Signal a condition synchronization object.

## Signature

`broadcast_condition( : : ConditionHandle : )`

## Description

`broadcast_condition` restarts all the threads that are waiting on the
condition variable *`ConditionHandle`*. Nothing happens if no threads
are waiting on *`ConditionHandle`*.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ConditionHandle`** (input_control)  condition `→`  (handle)

Condition synchronization object.

## Result

If the condition handle is valid, the operator `broadcast_condition`
returns 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_condition`,
`wait_condition`

## See also

`wait_condition`,
`timed_wait_condition`

## Module

Foundation
