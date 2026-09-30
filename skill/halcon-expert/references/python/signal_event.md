# signal_event (Operator)

## Name

`signal_event` — Unlock an event synchronization object.

## Signature

`def signal_event(event_handle: HHandle) -> None`

## Description

`signal_event` releases the event given in *`event_handle`*.
Signaling an event that is already signaled has no effect.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`event_handle`** (input_control)  event `→` HHandle

Event synchronization object.

## Result

If the event handle is valid, the operator `signal_event`
returns 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`wait_event`

## Possible Successors

`wait_event`,
`clear_event`

## Module

Foundation
