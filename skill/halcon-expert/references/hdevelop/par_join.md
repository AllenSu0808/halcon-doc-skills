# par_join (Operator)

## Name

`par_join` — Wait for subthreads that were started with the `par_start`
qualifier.

## Signature

`par_join( : : ThreadID : )`

## Description

The `par_join` operator is used to wait in the calling procedure
for all procedures or operators that have been started in separate
subthreads by adding the `par_start` qualifier to the according
program line.
The subthreads to wait for are identified by their thread ids that are
passed to the parameter *`ThreadID`*.

Attention: `par_start` is not an operator but a qualifier that is
added at the begin of the program line that has to be executed in parallel
to the calling procedure. The syntax is
`par_start <ThreadID> :`  followed by the actual procedure or
operator call.

## Parameters

**`ThreadID`** (input_control)  thread_id(-array) `→`  (integer)

Ids of all subthreads to wait for.

## Example (HDevelop)

```
* start two procedures in separate sub threads
par_start <ThreadID1> : producer_proc()
par_start <ThreadID2> : consumer_proc()
* wait until both procedures have finished
par_join ([ThreadID1, ThreadID2])
```

## Result

If the values of the specified parameters are correct,
`par_join` returns 2 (
H_MSG_TRUE)
. Otherwise, an
exception is raised and an error code returned.

## Module

Foundation
