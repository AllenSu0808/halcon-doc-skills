# detach_background_from_window (Operator)

## Name

`detach_background_from_window` — Detach the background image from a HALCON window.

## Signature

`detach_background_from_window( : : WindowHandle : )`

## Description

This operator detaches the background image that was previously attached
with [`attach_background_to_window`](attach_background_to_window.md) from the HALCON window
defined in *`WindowHandle`*.
Thus the background of the window will be cleared.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

## Result

If the window exists and the specified parameters are correct
`detach_background_from_window` returns 2 (
H_MSG_TRUE)
. If necessary an
exception is raised.

## Possible Predecessors

`attach_background_to_window`

## Module

Foundation
