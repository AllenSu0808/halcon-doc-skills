# dev_close_tool (Operator)

## Name

`dev_close_tool` — Close the specified floating tool window.

## Signature

`dev_close_tool( : : ToolId : )`

## Description

`dev_close_tool` closes the tool with the *`ToolId`*.
Instead of using the *`ToolId`*, given during opening the tool,
you can use the name that has to be used in [`dev_open_tool`](dev_open_tool.md).
In that case a arbitrary tool, which fits the parameter
*`ToolId`*, is used.

## Attention

This operator only works for single floating tools, i.e.,
tools that are neither docked nor tabbed.

This operator is not supported for code export.

## Parameters

**`ToolId`** (input_control)  dev_tool `→`  (string)

Tool identifier.

## Example (HDevelop)

```
dev_open_tool ('matching_assistant', 0, 0, 'default','default', ToolId)
dev_close_tool (ToolId)
```

## Result

If the values of the specified parameters are correct,
[`dev_open_tool`](dev_open_tool.md) returns 2 (
H_MSG_TRUE)
. Otherwise, an
exception is raised and an error code returned.

## Possible Predecessors

`dev_set_tool_geometry`,
`dev_open_tool`

## Possible Successors

`dev_open_tool`

## See also

`dev_show_tool`

## Module

Foundation
