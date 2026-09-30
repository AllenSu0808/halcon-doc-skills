# WaitEvent (Operator)

## Name

`WaitEvent` — Lock an event synchronization object.

## Signature

`static void HOperatorSet.WaitEvent(HTuple eventHandle)`

`void HEvent.WaitEvent()`

## Description

`WaitEvent` waits on the event object passed in *`eventHandle`*
until it is signaled. When the event is signaled, `WaitEvent`
succeeds and sets the state automatically to non-signaled again.
The kind of wait depends on the event's attributes
set during the creation in [`CreateEvent`](create_event.md).

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`eventHandle`** (input_control)  event `→` [HEvent](HEvent.md), [HTuple](HTuple.md) (*IntPtr*)

Event synchronization object.

## Result

If the event handle is valid, the operator `WaitEvent` returns 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Possible Predecessors

`CreateEvent`

## Possible Successors

`SignalEvent`

## Module

Foundation
