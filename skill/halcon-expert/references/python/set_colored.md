# set_colored (Operator)

## Name

`set_colored` — Set multiple output colors.

## Signature

`def set_colored(window_handle: HHandle, number_of_colors: int) -> None`

## Description

`set_colored` is a shortcut for certain
[`set_color`](set_color.md) calls. It allows the user to display a region
set in different colors. *`number_of_colors`* defines the
number of colors that are used. Valid values for
*`number_of_colors`* can be queried with
[`query_colored`](query_colored.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`number_of_colors`** (input_control)  integer `→` int

Number of output colors.

Default:
12

List of values:
3, 6, 12

## Result

`set_colored` returns 2 (
H_MSG_TRUE)
if *`number_of_colors`*
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
