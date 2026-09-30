# create_event (Operator)

## Name

`create_event` — Create an event synchronization object.

## Signature

`create_event( : : AttribName, AttribValue : EventHandle)`

## Description

An event is a prelocked mutual exclusion that does not belong to a
thread, i.e., it can be signaled by a thread different from the locking
thread. This understanding is, e.g., close to the definition of an event in
WIN32-API or a semaphore with count 0 in POSIX threads.

`create_event` allocates and initializes the event object according
to the attributes specified in *`AttribName`* and *`AttribValue`*.
*`AttribName`* specifies the attribute class and *`AttribValue`*
the kind of the event. The description beneath lists all mutex kinds
supported by following classes:

- ***''*** —

  empty string sets the default attributes.
- ***'type'*** —

  specifies what happens if a thread waits on a signal to
  an event:

  - ***'sleep'*** —

    simply suspends the calling thread (default).
  - ***'spin'*** —

    a fast event implementation that waits busy
    on a signal. This type is non recursive.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`AttribName`** (input_control)  attribute.name(-array) `→`  (string / integer / real)

Mutex attribute.

Default:
[]

List of values:
'type'

**`AttribValue`** (input_control)  attribute.value(-array) `→`  (string / integer / real)

Mutex attribute value.

Number of elements:
AttribValue == AttribName

Default:
[]

List of values:
'sleep', 'spin'

**`EventHandle`** (output_control)  event `→`  (handle)

Event synchronization object.

## Result

`create_event` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If necessary, an exception is raised.

## Possible Successors

`wait_event`,
`signal_event`,
`clear_event`

## See also

`clear_event`

## Module

Foundation
