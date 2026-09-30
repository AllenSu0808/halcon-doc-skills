# dev_unmap_par (Operator)

## Name

`dev_unmap_par` — Closes the dialog to specify the visualization parameters.

## Warning

**`dev_unmap_par` is obsolete and is only provided for
reasons of backward compatibility. New applications should use
[`dev_close_tool`](dev_close_tool.md) with `ToolId` set to
*'visualization_parameters_dialog'* instead.**

## Signature

`dev_unmap_par( : : : )`

## Description

`dev_unmap_par` closes the `Visualization Parameter` dialog.
This can also be achieved interactively by pressing the `Close`
button on the dialog's title bar.
The dialog can be opened again by [`dev_map_par`](dev_map_par.md).

## Attention

This operator is not supported for code export.

## Result

`dev_unmap_par` always returns 2 (
H_MSG_TRUE)
.

## Possible Successors

`dev_map_par`

## See also

`dev_map_par`,
`dev_map_prog`,
`dev_map_var`

## Module

Foundation
