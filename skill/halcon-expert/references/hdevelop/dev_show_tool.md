# dev_show_tool (Operator)

## Name

`dev_show_tool` — Shows the specified tool.

## Signature

`dev_show_tool( : : ToolId, Action : )`

## Description

`dev_show_tool` executes the action *`Action`* on the tool
*`ToolId`*

Instead of using the *`ToolId`*, given during opening the tool,
you can use the name that has to be used in [`dev_open_tool`](dev_open_tool.md).
In that case an arbitrary tool, which fits the parameter
*`ToolId`*, is used.

*`Action`*

- ***'show'*:** —

  Activates the tool.
- ***'normal'*:** —

  Shows the tool, brings it to the front and activates it.
- ***'minimize'*:** —

  Minimizes the tool.
- ***'maximize'*:** —

  Maximizes the tool.
- ***'hide'*:** —

  Hides the tool.

## Attention

This operator is not supported for code export.

## Parameters

**`ToolId`** (input_control)  dev_tool `→`  (string)

Tool identifier.

**`Action`** (input_control)  string `→`  (string)

Action to execute.

## Example (HDevelop)

```
dev_open_tool ('matching_assistant', 0, 0, 'default','default', ToolId)
dev_show_tool (ToolId, 'minimize')
```

## Result

If the values of the specified parameters are correct,
`dev_show_tool` returns 2 (
H_MSG_TRUE)
. Otherwise, an
exception is raised and an error code returned.

## Possible Predecessors

`dev_set_tool_geometry`,
`dev_open_tool`

## See also

`dev_set_tool_geometry`

## Module

Foundation
