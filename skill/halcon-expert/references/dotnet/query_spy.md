# QuerySpy (Operator)

## Name

`QuerySpy` — Inquiring for possible settings of the HALCON debugging tool.

## Signature

`static void HOperatorSet.QuerySpy(out HTuple classes, out HTuple values)`

`static HTuple HSystem.QuerySpy(out HTuple values)`

## Description

The operator `QuerySpy` returns all possible settings of spy, the
HALCON debugging tool,
i.e. all the available control modes (*`classes`*) as well as the
corresponding possible ways of setting (*`values`*).
For a more detailed description of spy see operator [`SetSpy`](set_spy.md).

## Attention

The values of *`values`* cannot be used as direct input for
[`SetSpy`](set_spy.md), as they are transmitted as a symbolic constant.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`classes`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Available control modes (see also [`SetSpy`](set_spy.md)).

**`values`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Corresponding state of the control modes.

## Result

`QuerySpy` always returns the value 2 (
H_MSG_TRUE)
.

## Possible Predecessors

`ResetObjDb`

## See also

`SetSpy`,
`GetSpy`

## Module

Foundation
