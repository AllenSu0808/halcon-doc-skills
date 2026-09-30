# SignalEvent (Operator)

## Name

`SignalEvent` — Unlock an event synchronization object.

## Signature

`static void HOperatorSet.SignalEvent(HTuple eventHandle)`

`void HEvent.SignalEvent()`

## Description

`SignalEvent` releases the event given in *`eventHandle`*.
Signaling an event that is already signaled has no effect.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`eventHandle`** (input_control)  event `→` [HEvent](HEvent.md), [HTuple](HTuple.md) (*IntPtr*)

Event synchronization object.

## Result

If the event handle is valid, the operator `SignalEvent`
returns 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`WaitEvent`

## Possible Successors

`WaitEvent`,
`ClearEvent`

## Module

Foundation
