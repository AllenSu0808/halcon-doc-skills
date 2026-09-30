# CreateEvent (Operator)

## Name

`CreateEvent` — Create an event synchronization object.

## Signature

`static void HOperatorSet.CreateEvent(HTuple attribName, HTuple attribValue, out HTuple eventHandle)`

`public HEvent(HTuple attribName, HTuple attribValue)`

`public HEvent(string attribName, string attribValue)`

`void HEvent.CreateEvent(HTuple attribName, HTuple attribValue)`

`void HEvent.CreateEvent(string attribName, string attribValue)`

## Description

An event is a prelocked mutual exclusion that does not belong to a
thread, i.e., it can be signaled by a thread different from the locking
thread. This understanding is, e.g., close to the definition of an event in
WIN32-API or a semaphore with count 0 in POSIX threads.

`CreateEvent` allocates and initializes the event object according
to the attributes specified in *`attribName`* and *`attribValue`*.
*`attribName`* specifies the attribute class and *`attribValue`*
the kind of the event. The description beneath lists all mutex kinds
supported by following classes:

- ***""*** —

  empty string sets the default attributes.
- ***"type"*** —

  specifies what happens if a thread waits on a signal to
  an event:

  - ***"sleep"*** —

    simply suspends the calling thread (default).
  - ***"spin"*** —

    a fast event implementation that waits busy
    on a signal. This type is non recursive.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`attribName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Mutex attribute.

Default:
[]

List of values:
"type"

**`attribValue`** (input_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Mutex attribute value.

Number of elements:
AttribValue == AttribName

Default:
[]

List of values:
"sleep", "spin"

**`eventHandle`** (output_control)  event `→` [HEvent](HEvent.md), [HTuple](HTuple.md) (*IntPtr*)

Event synchronization object.

## Result

`CreateEvent` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If necessary, an exception is raised.

## Possible Successors

`WaitEvent`,
`SignalEvent`,
`ClearEvent`

## See also

`ClearEvent`

## Module

Foundation
