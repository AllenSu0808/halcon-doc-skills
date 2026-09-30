# dev_inspect_ctrl (Operator)

## Name

`dev_inspect_ctrl` — Open a window to inspect one or more control variables.

## Signature

`dev_inspect_ctrl( : : Variable : )`

## Description

`dev_inspect_ctrl` opens an inspection window to display the
contents of one or more control variables.

The standard inspection window displays the variable values with some optional
statistics in a table. The window title is generated from the given parameter
names. For some semantic types a special representation
exists, e.g., functions are displayed as function plot by default. For more
information, see the chapter `“Inspecting Variables”` in the
`“HDevelop User's Guide”`.

You can pass a tuple of variables in *`Variable`* to open an
inspection window for multiple variables. It is also possible to override
the default inspection mode by including a string literal as the first
element of the tuple:

- ***'tuple'*:** —

  Show the values in the default inspection window even if the
  semantic type of the variable has a special representation.
- ***'plot'*:** —

  Plot the values of numeric variables against their tuple index.
- ***'plot_xy'*:** —

  Plot the values of numeric variables as X-Y pairs. The number of
  variables must be even, with each pair of variables having the same
  length.

Note that no expressions are evaluated inside the call of
`dev_inspect_ctrl`, but only the contained parameter names are parsed.
Therefore, operations like, e.g., accessing a specific tuple range
or arithmetic tuple operations need to be done beforehand.

Normally, the window contents will be updated whenever the variables
change. However, the update behavior can be influenced by the operator
[`dev_update_var`](dev_update_var.md) and the `Update Variable` preference.

The window can be closed by pressing the `Close` button or by calling
[`dev_close_inspect_ctrl`](dev_close_inspect_ctrl.md).

## Attention

This operator is not supported for code export.

## Parameters

**`Variable`** (input_control)  integer(-array) `→`  (integer / real / string)

Name of the variable to be checked.

## Example (HDevelop)

```
read_image (Image, 'fabrik')
regiongrowing (Image, Regions, 3, 3, 6, 100)
area_center (Regions, Area, Row, Column)
dev_inspect_ctrl (Area)
dev_inspect_ctrl (['plot_xy', Row, Column])
```

## Result

If the values of the specified parameters are correct,
`dev_inspect_ctrl` returns 2 (
H_MSG_TRUE)
. Otherwise, an
exception is raised and an error code returned.

## See also

`dev_update_var`

## Module

Foundation
