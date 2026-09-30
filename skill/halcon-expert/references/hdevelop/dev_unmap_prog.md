# dev_unmap_prog (Operator)

## Name

`dev_unmap_prog` — Hide the main window.

## Warning

**`dev_unmap_prog` is obsolete and is only provided for
reasons of backward compatibility. New applications should use
[`dev_close_tool`](dev_close_tool.md) with `ToolId` set to
*'program_window'* instead.**

## Signature

`dev_unmap_prog( : : : )`

## Description

`dev_unmap_prog` hides in MDI mode the main window and in SDI mode the
program window so that it is no longer visible.
It can be shown again by [`dev_map_prog`](dev_map_prog.md).

Attention: after hiding the main window there is no opportunity to enter
and execute the [`dev_map_prog`](dev_map_prog.md) operator.
So take care that `dev_unmap_prog` is only executed in continuous mode
with a reachable [`dev_map_prog`](dev_map_prog.md) operator.

## Attention

This operator is not supported for code export.

## Result

`dev_unmap_prog` always returns 2 (
H_MSG_TRUE)
.

## Possible Successors

`dev_map_prog`,
`stop`

## See also

`dev_map_par`,
`dev_map_prog`,
`dev_map_var`

## Module

Foundation
