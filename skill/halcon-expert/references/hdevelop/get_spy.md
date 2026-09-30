# get_spy (Operator)

## Name

`get_spy` — Current configuration of the HALCON debugging-tool.

## Signature

`get_spy( : : Class : Value)`

## Description

The operator `get_spy` returns the current configuration of spy,
the HALCON debugging tool.
The available control modes (possible choices for *`Class`*) as well
as the corresponding tuning possibilities (possible values for
*`Value`*) can be called up by using the operator
[`query_spy`](query_spy.md).
You will find a more detailed description under [`set_spy`](set_spy.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Class`** (input_control)  string `→`  (string)

Control mode

Default:
'mode'

List of values:
'db', 'input_control', 'internal', 'log_file', 'mode', 'operator', 'output_control', 'parameter_values', 'time'

**`Value`** (output_control)  string `→`  (string / integer / real)

State of the control mode.

## Result

The operator `get_spy` returns the value 2 (
H_MSG_TRUE)
if the
parameter *`Class`* is correct.
Otherwise an exception is raised.

## Possible Predecessors

`reset_obj_db`

## See also

`set_spy`,
`query_spy`

## Module

Foundation
