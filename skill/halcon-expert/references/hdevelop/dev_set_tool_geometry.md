# dev_set_tool_geometry (Operator)

## Name

`dev_set_tool_geometry` — Sets the position and size of the specified tool.

## Signature

`dev_set_tool_geometry( : : ToolId, Row, Column, Width, Height : )`

## Description

`dev_set_tool_geometry` sets the position and dimension
of the tool with the id *`ToolId`*.

Instead of using the *`ToolId`*, given during opening the tool,
you can use the name that has to be used in [`dev_open_tool`](dev_open_tool.md).
In that case a arbitrary tool, which fits the parameter
*`ToolId`*, is used.

The parameters *`Row`* and *`Column`* can be used to modify the
position of the tool.
Note that the offset values specified under
`Edit` -> `Preferences` ->
`General Options` -> `General Options`
-> `Window open offset` are added to the row and
the column index, respectively. For more information, see the chapter
“Menu `Edit`” in the `“HDevelop User's Guide”`.
In order to unmodify the position *'default'*
can be passed.

The parameters *`Width`* and *`Height`* can be used to modify the
size of the tools. In order to unmodify the size *'default'* can
be passed. If *`Width`* and *`Height`* are less than the minimum
size of the tool the minimum size is used.

## Attention

This operator is not supported for code export.

## Parameters

**`ToolId`** (input_control)  dev_tool `→`  (string)

Tool identifier.

**`Row`** (input_control)  rectangle.origin.y `→`  (integer / string)

Row index of upper left corner.

Default:
'default'

Minimum increment:
1

Recommended increment:
1

**`Column`** (input_control)  rectangle.origin.x `→`  (integer / string)

Column index of upper left corner.

Default:
'default'

Minimum increment:
1

Recommended increment:
1

**`Width`** (input_control)  rectangle.extent.x `→`  (integer / string)

Width of the tool.

Default:
'default'

Minimum increment:
1

Recommended increment:
1

Restriction:
`Width > 0`

**`Height`** (input_control)  rectangle.extent.y `→`  (integer)

Height of the tool.

Default:
'default'

Minimum increment:
1

Recommended increment:
1

Restriction:
`Height > 0`

## Example (HDevelop)

```
dev_open_tool ('zoom_window', 0, 0, Width, 'default', ToolId)
dev_close_tool (ToolId)
```

## Result

If the values of the specified parameters are correct,
[`dev_open_tool`](dev_open_tool.md) returns 2 (
H_MSG_TRUE)
. Otherwise, an
exception is raised and an error code returned.

## Possible Predecessors

`dev_open_tool`

## Possible Successors

`dev_show_tool`,
`dev_close_tool`

## Alternatives

`dev_show_tool`

## See also

`dev_show_tool`

## Module

Foundation
