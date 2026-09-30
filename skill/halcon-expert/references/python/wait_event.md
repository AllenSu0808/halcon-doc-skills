# wait_event (Operator)

## Name

`wait_event` — Lock an event synchronization object.

## Signature

`def wait_event(event_handle: HHandle) -> None`

## Description

`wait_event` waits on the event object passed in *`event_handle`*
until it is signaled. When the event is signaled, `wait_event`
succeeds and sets the state automatically to non-signaled again.
The kind of wait depends on the event's attributes
set during the creation in [`create_event`](create_event.md).

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`event_handle`** (input_control)  event `→` HHandle

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
