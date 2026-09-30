# CloseWindow (Operator)

## Name

`CloseWindow` — Close an output window.

## Signature

`static void HOperatorSet.CloseWindow(HTuple windowHandle)`

`static void HWindow.CloseWindow(HWindow[] windowHandle)`

`void HWindow.CloseWindow()`

## Description

`CloseWindow` closes a window which have been opened by
[`OpenWindow`](open_window.md). Afterwards the
output device or the window area, respectively, is ready to accept
new calls of [`OpenWindow`](open_window.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- windowHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`windowHandle`** (input_control, state is modified)  window(-array) `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

## Result

If the output window is valid `CloseWindow` returns 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

## Possible Predecessors

`OpenWindow`

## See also

`OpenWindow`

## Module

Foundation
