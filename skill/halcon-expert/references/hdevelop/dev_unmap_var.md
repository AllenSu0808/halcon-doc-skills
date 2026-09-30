# dev_unmap_var (Operator)

## Name

`dev_unmap_var` — Hides the variable window.

## Warning

**`dev_unmap_var` is obsolete and is only provided for
reasons of backward compatibility. New applications should use
[`dev_close_tool`](dev_close_tool.md) with `ToolId` set to
*'variable_window'* instead.**

## Signature

`dev_unmap_var( : : : )`

## Description

`dev_unmap_var` hides the variable window.
This can also be achieved interactively by pressing the `Close`
button on the window's title bar.
The window can be opened again by [`dev_map_var`](dev_map_var.md) or interactively via
the `Window` menu.

## Attention

This operator is not supported for code export.

## Result

`dev_unmap_var` always returns 2 (
H_MSG_TRUE)
.

## Possible Successors

`dev_map_var`

## See also

`dev_map_par`,
`dev_map_prog`

## Module

Foundation
