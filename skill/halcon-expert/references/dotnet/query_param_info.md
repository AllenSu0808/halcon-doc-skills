# QueryParamInfo (Operator)

## Name

`QueryParamInfo` — Query slots of the online-information concerning the operator [`GetParamInfo`](get_param_info.md).

## Signature

`static void HOperatorSet.QueryParamInfo(out HTuple slots)`

`static HTuple HInfo.QueryParamInfo()`

## Description

The operator `QueryParamInfo` returns the names of those pieces of
information (*`slots`*) which are available online for each parameter
(online texts).
The online texts themselves can be called up using

`get_param_info(::<Procedurname>,<Parametername>,<Slot>:<Information>)`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`slots`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Slot names for the operator [`GetParamInfo`](get_param_info.md).

## Result

`QueryParamInfo` always returns the value 2 (
H_MSG_TRUE)
.

## Possible Successors

`GetParamInfo`

## See also

`GetParamInfo`

## Module

Foundation
