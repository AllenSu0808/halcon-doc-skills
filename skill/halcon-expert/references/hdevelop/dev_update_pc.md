# dev_update_pc (Operator)

## Name

`dev_update_pc` — Switches the update of the PC during program execution on or off.

## Signature

`dev_update_pc( : : DisplayMode : )`

## Description

`dev_update_pc` specifies the behavior of the PC
during program execution.
If *`DisplayMode`* is set to *'on'*, which is the default,
within the selected procedure the PC is always displayed left to the
currently executed operator.
In addition the program text is scrolled---if necessary---so that
the current operator is visible.

If the mode is *'off'* the PC is not visible during program execution
and the program text will not be scrolled automatically.
When the program stops the PC becomes visible again and the listing is
scrolled to the current PC position.

For measuring the execution time of a sequence of operators all
`update` options should be switched off in order to reduce the
influence of the runtime of GUI updates in HDevelop.
For this the operators `dev_update_pc`, [`dev_update_time`](dev_update_time.md),
[`dev_update_var`](dev_update_var.md), and [`dev_update_window`](dev_update_window.md) or the
procedures `dev_update_on` and `dev_update_off`
can be used.

This option can also be controlled via the `Preferences` dialog:
`Edit` -> `Preferences`
-> `Runtime Settings`
-> `Update Program Counter`.

## Attention

This operator is not supported for code export.

## Parameters

**`DisplayMode`** (input_control)  string `→`  (string)

Mode for runtime behavior.

Default:
'off'

List of values:
'off', 'on'

## Result

If the values of the specified parameters are correct,
`dev_update_pc` returns 2 (
H_MSG_TRUE)
. Otherwise, an
exception is raised and an error code returned.

## See also

`dev_update_time`,
`dev_update_window`,
`dev_update_var`

## Module

Foundation
