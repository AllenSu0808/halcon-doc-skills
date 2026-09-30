# clear_window (Operator)

## Name

`clear_window` — Delete the contents of an output window.

## Signature

`def clear_window(window_handle: HHandle) -> None`

## Description

`clear_window` deletes all entries in the output window. The
window (background and edge) is reset to its original state.
Parameters assigned to this window (e.g., with [`set_color`](set_color.md),
[`set_paint`](set_paint.md), etc.) remain unmodified.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

## Result

If the output window is valid `clear_window` returns 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

## Possible Predecessors

`open_window`

## Alternatives

`clear_rectangle`,
`disp_rectangle1`

## See also

`open_window`

## Module

Foundation
