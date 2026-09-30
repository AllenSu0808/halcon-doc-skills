# get_current_hthread_id (Operator)

## Name

`get_current_hthread_id` — Return the HALCON thread ID of the current thread.

## Signature

`def get_current_hthread_id() -> int`

## Description

`get_current_hthread_id` returns a thread ID that represents the
currently running thread in *`hthread_id`*.
This ID is identical to the windows thread ID or the POSIX thread ID on UNIX
platforms and is also returned by the par_start operation of the HDevEngine.
It can later be used to interrupt operators that are executed
in this thread using [`interrupt_operator`](interrupt_operator.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`hthread_id`** (output_control)  integer `→` int

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

If the current thread can be determined, `get_current_hthread_id`
returns 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Successors

`interrupt_operator`

## See also

`interrupt_operator`,
`set_operator_timeout`

## Module

Foundation
