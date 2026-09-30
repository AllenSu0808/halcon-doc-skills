# DetachBackgroundFromWindow (Operator)

## Name

`DetachBackgroundFromWindow` — Detach the background image from a HALCON window.

## Signature

`static void HOperatorSet.DetachBackgroundFromWindow(HTuple windowHandle)`

`void HWindow.DetachBackgroundFromWindow()`

`static void HDrawingObject.DetachBackgroundFromWindow(HWindow windowHandle)`

## Description

This operator detaches the background image that was previously attached
with [`AttachBackgroundToWindow`](attach_background_to_window.md) from the HALCON window
defined in *`windowHandle`*.
Thus the background of the window will be cleared.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

## Result

If the window exists and the specified parameters are correct
`DetachBackgroundFromWindow` returns 2 (
H_MSG_TRUE)
. If necessary an
exception is raised.

## Possible Predecessors

`AttachBackgroundToWindow`

## Module

Foundation
