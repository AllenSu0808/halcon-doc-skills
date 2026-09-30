# create_condition (Operator)

## Name

`create_condition` — Create a condition variable synchronization object.

## Signature

`def create_condition(attrib_name: MaybeSequence[Union[int, float, str]], attrib_value: MaybeSequence[Union[int, float, str]]) -> HHandle`

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

`create_condition` creates and initializes the condition variable
*`condition_handle`*, using the condition attributes specified in
*`attrib_name`* and *`attrib_value`*, or default attributes if
*`attrib_name`* is *""*.
The current implementation supports no
attributes for conditions, hence the *`attrib_name`* parameter must
be set to *""*.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`attrib_name`** (input_control)  number(-array) `→` MaybeSequence[Union[int, float, str]]

Mutex attribute.

Default:
[]

**`attrib_value`** (input_control)  number(-array) `→` MaybeSequence[Union[int, float, str]]

Mutex attribute value.

Number of elements:
AttribValue == AttribName

Default:
[]

**`condition_handle`** (output_control)  condition `→` HHandle

Condition synchronization object.

## Result

`create_condition` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If necessary, an exception is raised.

## Possible Successors

`wait_condition`,
`timed_wait_condition`,
`signal_condition`

## See also

`clear_condition`

## Module

Foundation
