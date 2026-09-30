# dev_map_par (Operator)

## Name

`dev_map_par` — Open the dialog to specify the visualization parameters.

## Warning

**`dev_map_par` is obsolete and is only provided for
reasons of backward compatibility. New applications should use
[`dev_open_tool`](dev_open_tool.md) with `ToolName` set to
*'visualization_parameters_dialog'* instead.**

## Signature

`dev_map_par( : : : )`

## Description

`dev_map_par` opens the `Visualization Parameter` dialog.
This can also be achieved interactively via the menu
`Visualization` -> `Set Parameters...`
or the appropriate tool bar button.
The dialog is used to configure the visualization parameters that are used
to display iconic objects.

## Attention

This operator is not supported for code export.

## Example (HDevelop)

```
read_image (Image, 'fabrik')
threshold (Image, Region, 128, 255)
dev_map_par ()
```

## Result

`dev_map_par` returns always 2 (
H_MSG_TRUE)
.

## Possible Successors

`dev_unmap_par`

## Module

Foundation
