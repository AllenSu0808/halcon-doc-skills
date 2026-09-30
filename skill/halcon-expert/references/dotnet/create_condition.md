# CreateCondition (Operator)

## Name

`CreateCondition` — Create a condition variable synchronization object.

## Signature

`static void HOperatorSet.CreateCondition(HTuple attribName, HTuple attribValue, out HTuple conditionHandle)`

`public HCondition(HTuple attribName, HTuple attribValue)`

`public HCondition(string attribName, string attribValue)`

`void HCondition.CreateCondition(HTuple attribName, HTuple attribValue)`

`void HCondition.CreateCondition(string attribName, string attribValue)`

## Description

A condition variable (short: “condition”) is a synchronization
device that allows threads to suspend execution and relinquish the
processors until some predicate on shared data is satisfied. The basic
operations on conditions are: signal the condition (when the predicate
becomes true), and wait for the condition, suspending the thread execution
until another thread signals the condition.

A condition variable must always be associated with a mutex, to avoid
the race condition where a thread prepares to wait on a condition variable
and another thread signals the condition just before the first
thread actually waits on it.

`CreateCondition` creates and initializes the condition variable
*`conditionHandle`*, using the condition attributes specified in
*`attribName`* and *`attribValue`*, or default attributes if
*`attribName`* is *""*.
The current implementation supports no
attributes for conditions, hence the *`attribName`* parameter must
be set to *""*.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`attribName`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Mutex attribute.

Default:
[]

**`attribValue`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Mutex attribute value.

Number of elements:
AttribValue == AttribName

Default:
[]

**`conditionHandle`** (output_control)  condition `→` [HCondition](HCondition.md), [HTuple](HTuple.md) (*IntPtr*)

Condition synchronization object.

## Result

`CreateCondition` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If necessary, an exception is raised.

## Possible Successors

`WaitCondition`,
`TimedWaitCondition`,
`SignalCondition`

## See also

`ClearCondition`

## Module

Foundation
