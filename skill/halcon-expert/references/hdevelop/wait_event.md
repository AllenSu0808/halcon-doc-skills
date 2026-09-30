# wait_event (Operator)

## Name

`wait_event` — Lock an event synchronization object.

## Signature

`wait_event( : : EventHandle : )`

## Description

`wait_event` waits on the event object passed in *`EventHandle`*
until it is signaled. When the event is signaled, `wait_event`
succeeds and sets the state automatically to non-signaled again.
The kind of wait depends on the event's attributes
set during the creation in [`create_event`](create_event.md).

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`EventHandle`** (input_control)  event `→`  (handle)

Event synchronization object.

## Result

If the event handle is valid, the operator `wait_event` returns 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Possible Predecessors

`create_event`

## Possible Successors

`signal_event`

## Module

Foundation
