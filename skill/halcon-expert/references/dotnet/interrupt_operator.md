# InterruptOperator (Operator)

## Name

`InterruptOperator` — Attempt to interrupt an operator running in a different thread.

## Signature

`static void HOperatorSet.InterruptOperator(HTuple HThreadID, HTuple mode)`

`static void HSystem.InterruptOperator(int HThreadID, string mode)`

## Description

`InterruptOperator` attempts to gracefully interrupt the operator
currently running in the HALCON thread represented by *`HThreadID`*.
If that currently running operator supports interruption, it will abort
its execution depending on *`mode`* (see below).
If the thread is currently not executing any operator, or if the
currently running operator does not support interruptions,
`InterruptOperator` is a no-op.
The execution of any future operator in the other thread is not affected.

The ID representing a thread can be obtained with
[`GetCurrentHthreadId`](get_current_hthread_id.md).

`InterruptOperator` supports currently only one type of interruption,
which can be set in *`mode`*.
Note that the corresponding type must
also be supported by the operator currently running in the other thread.
To determine if an operator is interruptible and which kind of
interrupts it supports, please see the
"Execution Information" section of the operator documentation or
query the information using the parameter *"interrupt_mode"* of
the operator [`GetOperatorInfo`](get_operator_info.md).

Some operators, for which no interruptibility is mentioned in the reference
documentation, can still be interrupted at some points of their execution.
However, such interruptabilities are not guaranteed and can change
without further notice between different versions of HALCON.

- ***"cancel"*:** —

  Abort the execution of the operator.
  All results computed by the operator are discarded and the
  operator returns the error code H_ERR_CANCEL (22).

## Attention

Note that not all operators support interruption.
If a given operator supports interruptions and which modes are supported is
described in the execution information section of the reference
documentation of the corresponding operator.

Also note that there is no hard guarantee about the granularity of the
interruption.
The granularity can depend on the operator, its input data and the speed of
the device.
It is typically finer than 10 ms.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`HThreadID`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Thread that runs the operator to interrupt.

**`mode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Interruption mode.

Default:
"cancel"

List of values:
"cancel"

## Example (HDevelop)

```
global tuple HThreadID
get_current_hthread_id (HThreadID)
* call some slow operator...

* In a different thread
wait_seconds(2)
* Interrupt the long-running operator in the other thread
interrupt_operator (HThreadID, 'cancel')
```

## Result

If all the operator parameters are valid, `InterruptOperator`
returns 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`GetCurrentHthreadId`

## Alternatives

`SetOperatorTimeout`

## See also

`GetCurrentHthreadId`,
`SetOperatorTimeout`

## Module

Foundation
