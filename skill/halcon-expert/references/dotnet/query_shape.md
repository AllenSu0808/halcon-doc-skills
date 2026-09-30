# QueryShape (Operator)

## Name

`QueryShape` — Query the region display modes.

## Signature

`static void HOperatorSet.QueryShape(out HTuple displayShape)`

`static HTuple HInfo.QueryShape()`

## Description

`QueryShape` returns the names of all region display
modes (e.g., 'original', 'circle', 'rectangle1',
'rectangle2', 'ellipse', etc.) for the window. They are used
by [`SetShape`](set_shape.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`displayShape`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string*)

region display mode names.

## Result

`QueryShape` returns 2 (
H_MSG_TRUE)
, if the window is valid.
Otherwise an exception is raised.

## Possible Successors

`GetShape`,
`SetShape`,
`DispRegion`

## See also

`SetShape`,
`GetShape`,
`DispRegion`

## Module

Foundation
