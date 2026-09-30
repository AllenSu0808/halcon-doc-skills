# query_param_info (Operator)

## Name

`query_param_info` — Query slots of the online-information concerning the operator [`get_param_info`](get_param_info.md).

## Signature

`def query_param_info() -> Sequence[str]`

## Description

The operator `query_param_info` returns the names of those pieces of
information (*`slots`*) which are available online for each parameter
(online texts).
The online texts themselves can be called up using

`get_param_info(::<Procedurname>,<Parametername>,<Slot>:<Information>)`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`slots`** (output_control)  string-array `→` Sequence[str]

Slot names for the operator [`get_param_info`](get_param_info.md).

## Result

`query_param_info` always returns the value 2 (
H_MSG_TRUE)
.

## Possible Successors

`get_param_info`

## See also

`get_param_info`

## Module

Foundation
