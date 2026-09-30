# ClearCondition (Operator)

## Name

`ClearCondition` — Destroy a condition synchronization object.

## Signature

`static void HOperatorSet.ClearCondition(HTuple conditionHandle)`

`void HCondition.ClearCondition()`

## Description

`ClearCondition` destroys the condition object given in
*`conditionHandle`*. No threads should be waiting on the condition at
the time `ClearCondition` is called. After calling
`ClearCondition`, the condition can no longer be used.
The handle *`conditionHandle`* becomes invalid.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- conditionHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`conditionHandle`** (input_control, state is modified)  condition `→` [HCondition](HCondition.md), [HTuple](HTuple.md) (*IntPtr*)

Condition synchronization object.

## Result

If the condition handle is valid, the operator `ClearCondition`
returns 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateCondition`

## See also

`CreateCondition`

## Module

Foundation
