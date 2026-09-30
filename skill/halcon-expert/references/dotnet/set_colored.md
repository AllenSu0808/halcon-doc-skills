# SetColored (Operator)

## Name

`SetColored` — Set multiple output colors.

## Signature

`static void HOperatorSet.SetColored(HTuple windowHandle, HTuple numberOfColors)`

`void HWindow.SetColored(int numberOfColors)`

## Description

`SetColored` is a shortcut for certain
[`SetColor`](set_color.md) calls. It allows the user to display a region
set in different colors. *`numberOfColors`* defines the
number of colors that are used. Valid values for
*`numberOfColors`* can be queried with
[`QueryColored`](query_colored.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`numberOfColors`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of output colors.

Default:
12

List of values:
3, 6, 12

## Result

`SetColored` returns 2 (
H_MSG_TRUE)
if *`numberOfColors`*
is correct and the window is valid. Otherwise an exception is
raised.

## Possible Predecessors

`QueryColored`,
`SetColor`

## Possible Successors

`DispRegion`

## See also

`QueryColored`,
`SetColor`,
`DispRegion`

## Module

Foundation
