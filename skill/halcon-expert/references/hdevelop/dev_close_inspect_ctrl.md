# dev_close_inspect_ctrl (Operator)

## Name

`dev_close_inspect_ctrl` — Close inspect window(s) of one or more control variables.

## Signature

`dev_close_inspect_ctrl( : : Variable : )`

## Description

`dev_close_inspect_ctrl` is the counterpart operator to
[`dev_inspect_ctrl`](dev_inspect_ctrl.md).
It closes the variable inspect window or windows corresponding to
the variables specified in *`Variable`*.
The parameter *`Variable`* can contain an expression (e.g., tuple)
with several variable names.
First, the operator `dev_close_inspect_ctrl` tries to find an inspect
window with an exact match of the listed variables.
If it is found, it will be closed.
If no exact match is found, the operator tries to remove for every listed
variable one column from the first matching inspect window.
By removing the last column of an inspect window the window is closed.

As an alternative, the inspect windows can be closed by pressing the
`Close`-button in the title bar.

## Attention

This operator only works for single floating inspect windows, i.e.,
inspect windows that are neither docked nor tabbed.

This operator is not supported for code export.

## Parameters

**`Variable`** (input_control)  real(-array) `→`  (real / integer / string)

Name of the variable which inspect window
has to be closed.

## Example (HDevelop)

```
Var := 1
dev_inspect_ctrl (Var)
Var := [1,2,3,9,5,6,7,8]
Var[3] := 4
stop ()
dev_close_inspect_ctrl (Var)
```

## Result

`dev_close_inspect_ctrl` returns always 2 (
H_MSG_TRUE)
.

## Possible Predecessors

`dev_inspect_ctrl`

## Module

Foundation
