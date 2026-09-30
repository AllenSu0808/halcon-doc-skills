# set_mshape (Operator)

## Name

`set_mshape` — Set the current mouse pointer shape.

## Warning

**This operator does not work in an HDevelop graphics window opened with
`dev_open_window`.**

## Signature

`def set_mshape(window_handle: HHandle, cursor: str) -> None`

## Description

`set_mshape` sets the shape of the mouse pointer for the
window. A list of the names of all available mouse pointer
shapes can be obtained by calling [`query_mshape`](query_mshape.md). The
mouse pointer shape given by *`cursor`* is used if the mouse
pointer enters the window, irrespective of which window is
the output window at present.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`cursor`** (input_control)  string `→` str

Mouse pointer name.

Default:
"arrow"

## Result

`set_mshape` returns the value 2 (
H_MSG_TRUE)
if
the mouse pointer shape *`cursor`* is defined for this
window. Otherwise, an exception is raised.

## Possible Predecessors

`open_window`,
`query_mshape`,
`get_mshape`

## See also

`get_mshape`,
`query_mshape`

## Module

Foundation
