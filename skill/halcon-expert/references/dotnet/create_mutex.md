# CreateMutex (Operator)

## Name

`CreateMutex` — Create a mutual exclusion synchronization object.

## Signature

`static void HOperatorSet.CreateMutex(HTuple attribName, HTuple attribValue, out HTuple mutexHandle)`

`public HMutex(HTuple attribName, HTuple attribValue)`

`public HMutex(string attribName, string attribValue)`

`void HMutex.CreateMutex(HTuple attribName, HTuple attribValue)`

`void HMutex.CreateMutex(string attribName, string attribValue)`

## Description

A mutex is a synchronization object that negotiates mutual exclusion among
threads of a single process to avoid simultaneous modifications on common
resources such as global variables. A mutex has two possible states:
unlocked, i.e., not owned by any thread, and locked, i.e., owned by one
certain thread. Threads attempting to lock a mutex that is already owned by
another thread, i.e., locked, wait until the owning thread unlocks the mutex
first. Unlike events, a thread has to own a mutex to unlock it.

`CreateMutex` allocates and initializes the mutex object according to
the attributes specified in *`attribName`* and *`attribValue`*.
*`attribName`* specifies the attribute class and *`attribValue`*
the kind of the mutex. The description beneath lists all mutex kinds
supported by following classes:

- ***""*** —

  empty string sets the default attributes.
- ***"type"*** —

  specifies what happens if a thread attempts to lock a
  mutex that is already owned:

  - ***"sleep"*** —

    simply suspends the calling thread (default). The
    behavior is undefined, if the thread is already owner of the mutex.
  - ***"spin"*** —

    a fast mutex implementation that is busy waiting
    for the signaled mutex. The behavior is undefined, if the thread is
    already owner of the mutex.
  - ***"recursive"*** —

    suspends the calling thread if the thread is
    not owner of the mutex. But a recursive mutex can be acquired again by
    the owning thread. A recursive mutex does not become unlocked until the
    number of unlock requests equals the number of successful lock requests.

The mutex is unlocked when created.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`attribName`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Mutex attribute class.

Default:
[]

List of values:
"type"

**`attribValue`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Mutex attribute kind.

Number of elements:
AttribValue == AttribName

Default:
[]

List of values:
"recursive", "sleep", "spin"

**`mutexHandle`** (output_control)  mutex `→` [HMutex](HMutex.md), [HTuple](HTuple.md) (*IntPtr*)

Mutex synchronization object.

## Result

`CreateMutex` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If necessary, an exception is raised.

## Possible Successors

`LockMutex`,
`ClearMutex`

## See also

`ClearMutex`

## Module

Foundation
