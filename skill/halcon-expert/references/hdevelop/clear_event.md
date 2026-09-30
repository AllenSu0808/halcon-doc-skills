# clear_event (Operator)

## Name

`clear_event` — Clear the event synchronization object.

## Signature

`clear_event( : : EventHandle : )`

## Description

`clear_event` destroys the mutex object given by *`EventHandle`*.
No threads should be waiting on the event at the time `clear_event` is
called. After calling `clear_event`, the event can no longer be used.
The handle *`EventHandle`* becomes invalid.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- EventHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`EventHandle`** (input_control, state is modified)  event `→`  (handle)

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
