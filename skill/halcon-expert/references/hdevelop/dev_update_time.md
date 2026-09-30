# dev_update_time (Operator)

## Name

`dev_update_time` — Switch time measurement for operators on or off.

## Signature

`dev_update_time( : : DisplayMode : )`

## Description

`dev_update_time` controls whether the execution time of
an operator is displayed.

For measuring the execution time of a sequence of operators all
`update` options should be switched off in order to reduce the
influence of the runtime of GUI updates in HDevelop.
For this the operators [`dev_update_pc`](dev_update_pc.md), `dev_update_time`,
[`dev_update_var`](dev_update_var.md), and [`dev_update_window`](dev_update_window.md) or the
procedures `dev_update_on` and `dev_update_off`
can be used.

This option can also be controlled via the `Preferences` dialog:
`Edit` -> `Preferences`
-> `Runtime Settings`
-> `Show Processing Time`.

## Attention

This operator is not supported for code export.

## Parameters

**`DisplayMode`** (input_control)  string `→`  (string)

Mode for graphic output.

Default:
'off'

List of values:
'off', 'on'

## Result

If the values of the specified parameters are correct,
`dev_update_time` returns 2 (
H_MSG_TRUE)
. Otherwise, an
exception is raised and an error code returned.

## See also

`dev_update_pc`,
`dev_update_window`,
`dev_update_var`

## Module

Foundation
