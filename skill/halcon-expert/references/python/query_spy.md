# query_spy (Operator)

## Name

`query_spy` — Inquiring for possible settings of the HALCON debugging tool.

## Signature

`def query_spy() -> Tuple[Sequence[str], Sequence[str]]`

## Description

The operator `query_spy` returns all possible settings of spy, the
HALCON debugging tool,
i.e. all the available control modes (*`classes`*) as well as the
corresponding possible ways of setting (*`values`*).
For a more detailed description of spy see operator [`set_spy`](set_spy.md).

## Attention

The values of *`values`* cannot be used as direct input for
[`set_spy`](set_spy.md), as they are transmitted as a symbolic constant.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`classes`** (output_control)  string-array `→` Sequence[str]

Available control modes (see also [`set_spy`](set_spy.md)).

**`values`** (output_control)  string-array `→` Sequence[str]

Corresponding state of the control modes.

## Result

`query_spy` always returns the value 2 (
H_MSG_TRUE)
.

## Possible Predecessors

`reset_obj_db`

## See also

`set_spy`,
`get_spy`

## Module

Foundation
