# GetCurrentHthreadId (Operator)

## Name

`GetCurrentHthreadId` — Return the HALCON thread ID of the current thread.

## Signature

`static void HOperatorSet.GetCurrentHthreadId(out HTuple HThreadID)`

`static int HSystem.GetCurrentHthreadId()`

## Description

`GetCurrentHthreadId` returns a thread ID that represents the
currently running thread in *`HThreadID`*.
This ID is identical to the windows thread ID or the POSIX thread ID on UNIX
platforms and is also returned by the par_start operation of the HDevEngine.
It can later be used to interrupt operators that are executed
in this thread using [`InterruptOperator`](interrupt_operator.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`HThreadID`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

ID representing the current thread.

## Example (HDevelop)

```
global tuple HThreadID
get_current_hthread_id (HThreadID)
* call some slow operator...

* In a different thread
wait_seconds(2)
* Interrupt the long-running operator in the other thread
interrupt_operator (HThreadID, 'break')
```

## Result

If the current thread can be determined, `GetCurrentHthreadId`
returns 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Successors

`InterruptOperator`

## See also

`InterruptOperator`,
`SetOperatorTimeout`

## Module

Foundation
