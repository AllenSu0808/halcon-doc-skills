# GetSpy (Operator)

## Name

`GetSpy` — Current configuration of the HALCON debugging-tool.

## Signature

`static void HOperatorSet.GetSpy(HTuple classVal, out HTuple value)`

`static HTuple HSystem.GetSpy(string classVal)`

## Description

The operator `GetSpy` returns the current configuration of spy,
the HALCON debugging tool.
The available control modes (possible choices for *`classVal`*) as well
as the corresponding tuning possibilities (possible values for
*`value`*) can be called up by using the operator
[`QuerySpy`](query_spy.md).
You will find a more detailed description under [`SetSpy`](set_spy.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`classVal`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Control mode

Default:
"mode"

List of values:
"db", "input_control", "internal", "log_file", "mode", "operator", "output_control", "parameter_values", "time"

**`value`** (output_control)  string `→` [HTuple](HTuple.md) (*string* / int / long / double)

State of the control mode.

## Result

The operator `GetSpy` returns the value 2 (
H_MSG_TRUE)
if the
parameter *`classVal`* is correct.
Otherwise an exception is raised.

## Possible Predecessors

`ResetObjDb`

## See also

`SetSpy`,
`QuerySpy`

## Module

Foundation
