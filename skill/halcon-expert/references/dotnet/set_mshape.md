# SetMshape (Operator)

## Name

`SetMshape` — Set the current mouse pointer shape.

## Warning

**This operator does not work in an HDevelop graphics window opened with
`dev_open_window`.**

## Signature

`static void HOperatorSet.SetMshape(HTuple windowHandle, HTuple cursor)`

`void HWindow.SetMshape(string cursor)`

## Description

`SetMshape` sets the shape of the mouse pointer for the
window. A list of the names of all available mouse pointer
shapes can be obtained by calling [`QueryMshape`](query_mshape.md). The
mouse pointer shape given by *`cursor`* is used if the mouse
pointer enters the window, irrespective of which window is
the output window at present.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`cursor`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Mouse pointer name.

Default:
"arrow"

## Result

`SetMshape` returns the value 2 (
H_MSG_TRUE)
if
the mouse pointer shape *`cursor`* is defined for this
window. Otherwise, an exception is raised.

## Possible Predecessors

`OpenWindow`,
`QueryMshape`,
`GetMshape`

## See also

`GetMshape`,
`QueryMshape`

## Module

Foundation
