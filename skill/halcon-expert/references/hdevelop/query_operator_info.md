# query_operator_info (Operator)

## Name

`query_operator_info` — Query slots concerning information with relation to the operator [`get_operator_info`](get_operator_info.md).

## Signature

`query_operator_info( : : : Slots)`

## Description

The operator `query_operator_info` returns the names of those online
texts (*`Slots`*) which are available online for each operator.
The information itself can be called up using

`get_operator_info(::<OperatorName>,<Slot>:<Information>)`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Slots`** (output_control)  string-array `→`  (string)

Slot names of the operator [`get_operator_info`](get_operator_info.md).

## Result

The operator `query_operator_info` always returns the value 2 (
H_MSG_TRUE)
.

## Possible Successors

`get_operator_info`

## See also

`get_operator_info`

## Module

Foundation
