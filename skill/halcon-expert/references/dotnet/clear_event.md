# ClearEvent (Operator)

## Name

`ClearEvent` — Clear the event synchronization object.

## Signature

`static void HOperatorSet.ClearEvent(HTuple eventHandle)`

`void HEvent.ClearEvent()`

## Description

`ClearEvent` destroys the mutex object given by *`eventHandle`*.
No threads should be waiting on the event at the time `ClearEvent` is
called. After calling `ClearEvent`, the event can no longer be used.
The handle *`eventHandle`* becomes invalid.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- eventHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`eventHandle`** (input_control, state is modified)  event `→` [HEvent](HEvent.md), [HTuple](HTuple.md) (*IntPtr*)

Event synchronization object.

## Result

If the event handle is valid, the operator `ClearEvent`
returns 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Possible Predecessors

`CreateEvent`

## See also

`CreateEvent`

## Module

Foundation
