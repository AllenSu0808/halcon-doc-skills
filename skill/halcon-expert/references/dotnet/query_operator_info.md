# QueryOperatorInfo (Operator)

## Name

`QueryOperatorInfo` — Query slots concerning information with relation to the operator [`GetOperatorInfo`](get_operator_info.md).

## Signature

`static void HOperatorSet.QueryOperatorInfo(out HTuple slots)`

`static HTuple HInfo.QueryOperatorInfo()`

## Description

The operator `QueryOperatorInfo` returns the names of those online
texts (*`slots`*) which are available online for each operator.
The information itself can be called up using

`get_operator_info(::<OperatorName>,<Slot>:<Information>)`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`slots`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Slot names of the operator [`GetOperatorInfo`](get_operator_info.md).

## Result

The operator `QueryOperatorInfo` always returns the value 2 (
H_MSG_TRUE)
.

## Possible Successors

`GetOperatorInfo`

## See also

`GetOperatorInfo`

## Module

Foundation
