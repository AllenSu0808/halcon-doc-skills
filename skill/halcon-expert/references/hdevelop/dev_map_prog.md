# dev_map_prog (Operator)

## Name

`dev_map_prog` — Make the main window of HDevelop visible.

## Warning

**`dev_map_prog` is obsolete and is only provided for
reasons of backward compatibility. New applications should use
[`dev_open_tool`](dev_open_tool.md) with `ToolName` set to
*'program_window'* instead.**

## Signature

`dev_map_prog( : : : )`

## Description

`dev_map_prog` is used to re-show (map) the main window
of HDevelop after it has been hidden (unmapped) by [`dev_unmap_prog`](dev_unmap_prog.md).

## Attention

This operator is not supported for code export.

Depending on the operating system or the window manager
the execution of `dev_map_prog` will result only in
a visible icon of the window. In this case it has to be opened
by the user with mouse interaction.

## Result

`dev_map_prog` always returns 2 (
H_MSG_TRUE)
.

## Possible Predecessors

`dev_unmap_prog`

## Possible Successors

`dev_unmap_prog`

## See also

`dev_map_par`,
`dev_map_var`

## Module

Foundation
