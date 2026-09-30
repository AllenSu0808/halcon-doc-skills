# clear_event (Operator)

## Name

`clear_event` — Clear the event synchronization object.

## Signature

`def clear_event(event_handle: HHandle) -> None`

## Description

`clear_event` destroys the mutex object given by *`event_handle`*.
No threads should be waiting on the event at the time `clear_event` is
called. After calling `clear_event`, the event can no longer be used.
The handle *`event_handle`* becomes invalid.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- event_handle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`event_handle`** (input_control, state is modified)  event `→` HHandle

Event synchronization object.

## Result

If the event handle is valid, the operator `clear_event`
returns 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Possible Predecessors

`create_event`

## See also

`create_event`

## Module

Foundation
