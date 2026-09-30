# GetMshape (Operator)

## Name

`GetMshape` — Query the current mouse pointer shape.

## Warning

**This operator does not work in an HDevelop graphics window opened with
`dev_open_window`.**

## Signature

`static void HOperatorSet.GetMshape(HTuple windowHandle, out HTuple cursor)`

`string HWindow.GetMshape()`

## Description

`GetMshape` returns the name of the pointer shape set for
the window. The mouse pointer shape can be used in the
operator [`SetMshape`](set_mshape.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`cursor`** (output_control)  string `→` [HTuple](HTuple.md) (*string*)

Mouse pointer name.

## Result

`GetMshape` returns the value 2 (
H_MSG_TRUE)
.

## Possible Predecessors

`OpenWindow`,
`QueryMshape`

## Possible Successors

`SetMshape`

## See also

`SetMshape`,
`QueryMshape`

## Module

Foundation
