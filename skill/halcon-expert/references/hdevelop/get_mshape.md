# get_mshape (Operator)

## Name

`get_mshape` — Query the current mouse pointer shape.

## Warning

**This operator does not work in an HDevelop graphics window opened with
`dev_open_window`.**

## Signature

`get_mshape( : : WindowHandle : Cursor)`

## Description

`get_mshape` returns the name of the pointer shape set for
the window. The mouse pointer shape can be used in the
operator [`set_mshape`](set_mshape.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`Cursor`** (output_control)  string `→`  (string)

Mouse pointer name.

## Result

`get_mshape` returns the value 2 (
H_MSG_TRUE)
.

## Possible Predecessors

`open_window`,
`query_mshape`

## Possible Successors

`set_mshape`

## See also

`set_mshape`,
`query_mshape`

## Module

Foundation
