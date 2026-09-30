# TryWaitEvent (Operator)

## Name

`TryWaitEvent` — Lock an event synchronization object only if it is unlocked.

## Signature

`static void HOperatorSet.TryWaitEvent(HTuple eventHandle, out HTuple busy)`

`int HEvent.TryWaitEvent()`

## Description

`TryWaitEvent` behaves identically to [`WaitEvent`](wait_event.md), except
that it does not block the calling thread when waiting until the object is
signaled but returns immediately. The state of the event before entering
`TryWaitEvent` is returned in *`busy`*. *1* indicates
that the event was non-signaled before calling `TryWaitEvent`,
*0* that the event was signaled.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`eventHandle`** (input_control)  event `→` [HEvent](HEvent.md), [HTuple](HTuple.md) (*IntPtr*)

Event synchronization object.

**`busy`** (output_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Object already locked?

## Result

If the event handle is valid, the operator `TryWaitEvent`
returns 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateEvent`

## Possible Successors

`SignalEvent`

## See also

`WaitEvent`

## Module

Foundation
