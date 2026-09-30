# dev_update_var (Operator)

## Name

`dev_update_var` — Switches the update of the variable window during program execution on or off.

## Signature

`dev_update_var( : : DisplayMode : )`

## Description

`dev_update_var` specifies the behavior of the variable window
during program execution.
If *`DisplayMode`* is set to *'on'*, which is the default,
the contents of the variable window (iconic and control variables)
is updated each time a variable is modified by the program.

If the mode is *'off'* the values of the control variables and the
icons of the iconic variables are not updated before the execution stops.

For measuring the execution time of a sequence of operators all
`update` options should be switched off in order to reduce the
influence of the runtime of GUI updates in HDevelop.
For this the operators [`dev_update_pc`](dev_update_pc.md), [`dev_update_time`](dev_update_time.md),
`dev_update_var`, and [`dev_update_window`](dev_update_window.md) or the
procedures `dev_update_on` and `dev_update_off`
can be used.

This option can also be controlled via the `Preferences` dialog:
`Edit` -> `Preferences`
-> `Runtime Settings`
-> `Update Variables`.

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
`dev_update_var` returns 2 (
H_MSG_TRUE)
. Otherwise, an
exception is raised and an error code returned.

## See also

`dev_update_pc`,
`dev_update_window`,
`dev_update_time`

## Module

Foundation
