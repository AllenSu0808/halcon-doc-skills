# ClearWindow (Operator)

## Name

`ClearWindow` — Delete the contents of an output window.

## Signature

`static void HOperatorSet.ClearWindow(HTuple windowHandle)`

`void HWindow.ClearWindow()`

## Description

`ClearWindow` deletes all entries in the output window. The
window (background and edge) is reset to its original state.
Parameters assigned to this window (e.g., with [`SetColor`](set_color.md),
[`SetPaint`](set_paint.md), etc.) remain unmodified.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

## Result

If the output window is valid `ClearWindow` returns 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

## Possible Predecessors

`OpenWindow`

## Alternatives

`ClearRectangle`,
`DispRectangle1`

## See also

`OpenWindow`

## Module

Foundation
