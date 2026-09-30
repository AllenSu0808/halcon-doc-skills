# dev_open_dialog (Operator)

## Name

`dev_open_dialog` — Open a modal HDevelop dialog.

## Signature

`dev_open_dialog( : : DialogName : )`

## Description

`dev_open_dialog` opens a modal HDevelop dialog type *`DialogName`*.
*`DialogName`* contains the name of the dialog which should
be opened.

The following dialogs, are supported:

| *`DialogName`* | Dialog |
| --- | --- |
| *'about_dialog'* | About dialog |
| *'duplicate_procedure_dialog'* | Duplicate Procedure dialog |
| *'export_dialog'* | Export dialog |
| *'open_graphics_windows_dialog'* | Open Graphics Window dialog |
| *'insert_visualization_code_dialog'* | Insert Visualization Code dialog |
| *'read_image_dialog'* | Read Image dialog |
| *'print_dialog'* | Print dialog |
| *'properties_dialog'* | Properties dialog |
| *'save_window_dialog'* | Save Graphic Window dialog |

## Attention

This operator is not supported for code export.

## Parameters

**`DialogName`** (input_control)  string `→`  (string)

Name of the dialog to be opened.

## Example (HDevelop)

```
dev_open_dialog ('print_dialog')
```

## Result

If the values of the specified parameters are correct,
[`dev_open_tool`](dev_open_tool.md) returns 2 (
H_MSG_TRUE)
. Otherwise, an
exception is raised and an error code returned.

## Module

Foundation
