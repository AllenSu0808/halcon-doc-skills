# query_mshape (Operator)

## Name

`query_mshape` — Query all available mouse pointer shapes.

## Warning

**This operator does not work in an HDevelop graphics window opened with
`dev_open_window`.**

## Signature

`query_mshape( : : WindowHandle : ShapeNames)`

## Description

`query_mshape` returns the names of all available mouse
pointer shapes for the window. These can be used in the
operator [`set_mshape`](set_mshape.md). If no mouse pointers are
available, the empty tuple is returned.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`ShapeNames`** (output_control)  string-array `→`  (string)

Available mouse pointer names.

## Result

`query_mshape` returns the value 2 (
H_MSG_TRUE)
.

## Possible Predecessors

`open_window`,
`get_mshape`

## Possible Successors

`set_mshape`

## See also

`set_mshape`,
`get_mshape`

## Module

Foundation
