# try_wait_event (Operator)

## Name

`try_wait_event` — Lock an event synchronization object only if it is unlocked.

## Signature

`try_wait_event( : : EventHandle : Busy)`

## Description

`try_wait_event` behaves identically to [`wait_event`](wait_event.md), except
that it does not block the calling thread when waiting until the object is
signaled but returns immediately. The state of the event before entering
`try_wait_event` is returned in *`Busy`*. *1* indicates
that the event was non-signaled before calling `try_wait_event`,
*0* that the event was signaled.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`EventHandle`** (input_control)  event `→`  (handle)

Event synchronization object.

**`Busy`** (output_control)  number `→`  (integer)

Object already locked?

## Result

If the event handle is valid, the operator `try_wait_event`
returns 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_event`

## Possible Successors

`signal_event`

## See also

`wait_event`

## Module

Foundation
