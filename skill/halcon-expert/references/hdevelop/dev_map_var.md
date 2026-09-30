# dev_map_var (Operator)

## Name

`dev_map_var` — Open the variable window of HDevelop.

## Warning

**`dev_map_var` is obsolete and is only provided for
reasons of backward compatibility. New applications should use
[`dev_open_tool`](dev_open_tool.md) with `ToolName` set to
*'variable_window'* instead.**

## Signature

`dev_map_var( : : : )`

## Description

`dev_map_var` is used to re-show (map) the variable window on
the screen after it has been hidden (unmapped) by [`dev_unmap_var`](dev_unmap_var.md).

## Attention

This operator is not supported for code export.

## Result

`dev_map_var` always returns 2 (
H_MSG_TRUE)
.

## Possible Predecessors

`dev_unmap_var`

## Possible Successors

`dev_unmap_var`

## See also

`dev_map_par`,
`dev_map_prog`

## Module

Foundation
