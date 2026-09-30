# set_colored (Operator)

## Name

`set_colored` — Set multiple output colors.

## Signature

`set_colored( : : WindowHandle, NumberOfColors : )`

## Description

`set_colored` is a shortcut for certain
[`set_color`](set_color.md) calls. It allows the user to display a region
set in different colors. *`NumberOfColors`* defines the
number of colors that are used. Valid values for
*`NumberOfColors`* can be queried with
[`query_colored`](query_colored.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`NumberOfColors`** (input_control)  integer `→`  (integer)

Number of output colors.

Default:
12

List of values:
3, 6, 12

## Result

`set_colored` returns 2 (
H_MSG_TRUE)
if *`NumberOfColors`*
is correct and the window is valid. Otherwise an exception is
raised.

## Possible Predecessors

`query_colored`,
`set_color`

## Possible Successors

`disp_region`

## See also

`query_colored`,
`set_color`,
`disp_region`

## Module

Foundation
