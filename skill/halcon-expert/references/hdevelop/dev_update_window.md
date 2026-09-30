# dev_update_window (Operator)

## Name

`dev_update_window` — Switches the automatic output of iconic output objects into the graphics
window during program execution on or off.

## Signature

`dev_update_window( : : DisplayMode : )`

## Description

`dev_update_window` specifies whether all iconic objects that are
returned by an operator call have to be displayed in the active graphics
window (*`DisplayMode`* = *'on'*---default) or not
(*`DisplayMode`* = *'off'*).

This option has no influence on the object output in single step mode.
After the execution of a single operator the iconic output objects are
always displayed in the active graphics window.

This option should be set to *'off'*, if only selected objects
should to be displayed in the graphics window.
In this case the objects should be displayed by [`dev_display`](dev_display.md).

For measuring the execution time of a sequence of operators all
`update` options should be switched off in order to reduce the
influence of the runtime of GUI updates in HDevelop.
For this the operators [`dev_update_pc`](dev_update_pc.md), [`dev_update_time`](dev_update_time.md),
[`dev_update_var`](dev_update_var.md), and `dev_update_window` or the
procedures `dev_update_on` and `dev_update_off`
can be used.

This option can also be controlled via the `Preferences` dialog:
`Edit` -> `Preferences`
-> `Runtime Settings`
-> `Update Window`.

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
`dev_update_window` returns 2 (
H_MSG_TRUE)
. Otherwise, an
exception is raised and an error code returned.

## Possible Successors

`dev_display`

## See also

`dev_update_pc`,
`dev_update_var`,
`dev_update_time`

## Module

Foundation
