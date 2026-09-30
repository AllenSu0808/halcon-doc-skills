# QueryMshape (Operator)

## Name

`QueryMshape` — Query all available mouse pointer shapes.

## Warning

**This operator does not work in an HDevelop graphics window opened with
`dev_open_window`.**

## Signature

`static void HOperatorSet.QueryMshape(HTuple windowHandle, out HTuple shapeNames)`

`HTuple HWindow.QueryMshape()`

## Description

`QueryMshape` returns the names of all available mouse
pointer shapes for the window. These can be used in the
operator [`SetMshape`](set_mshape.md). If no mouse pointers are
available, the empty tuple is returned.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`shapeNames`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Available mouse pointer names.

## Result

`QueryMshape` returns the value 2 (
H_MSG_TRUE)
.

## Possible Predecessors

`OpenWindow`,
`GetMshape`

## Possible Successors

`SetMshape`

## See also

`SetMshape`,
`GetMshape`

## Module

Foundation
