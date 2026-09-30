# close_window (Operator)

## Name

`close_window` — Close an output window.

## Signature

`close_window( : : WindowHandle : )`

## Description

`close_window` closes a window which have been opened by
[`open_window`](open_window.md). Afterwards the
output device or the window area, respectively, is ready to accept
new calls of [`open_window`](open_window.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- WindowHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`WindowHandle`** (input_control, state is modified)  window(-array) `→`  (handle)

Window handle.

## Result

If the output window is valid `close_window` returns 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

## Possible Predecessors

`open_window`

## See also

`open_window`

## Module

Foundation
