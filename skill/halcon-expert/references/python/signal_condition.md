# signal_condition (Operator)

## Name

`signal_condition` — Signal a condition synchronization object.

## Signature

`def signal_condition(condition_handle: HHandle) -> None`

## Description

`signal_condition` restarts one of the threads that are waiting on the
condition variable *`condition_handle`*. If no threads are waiting on
*`condition_handle`*, nothing happens. If several threads are waiting on
*`condition_handle`*, exactly one is restarted, but it is not specified
which one.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`condition_handle`** (input_control)  condition `→` HHandle

Condition synchronization object.

## Result

If the condition handle is valid, the operator `signal_condition`
returns 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Possible Predecessors

`create_condition`,
`wait_condition`

## See also

`wait_condition`,
`timed_wait_condition`

## Module

Foundation
