# get_spy (Operator)

## Name

`get_spy` — Current configuration of the HALCON debugging-tool.

## Signature

`def get_spy(class_val: str) -> Union[str, int, float]`

## Description

The operator `get_spy` returns the current configuration of spy,
the HALCON debugging tool.
The available control modes (possible choices for *`class`*) as well
as the corresponding tuning possibilities (possible values for
*`value`*) can be called up by using the operator
[`query_spy`](query_spy.md).
You will find a more detailed description under [`set_spy`](set_spy.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`class`** (input_control)  string `→` str

Control mode

Default:
"mode"

List of values:
"db", "input_control", "internal", "log_file", "mode", "operator", "output_control", "parameter_values", "time"

**`value`** (output_control)  string `→` Union[str, int, float]

State of the control mode.

## Result

The operator `get_spy` returns the value 2 (
H_MSG_TRUE)
if the
parameter *`class`* is correct.
Otherwise an exception is raised.

## Possible Predecessors

`reset_obj_db`

## See also

`set_spy`,
`query_spy`

## Module

Foundation
