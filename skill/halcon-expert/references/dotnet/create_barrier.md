# CreateBarrier (Operator)

## Name

`CreateBarrier` — Create a barrier synchronization object.

## Signature

`static void HOperatorSet.CreateBarrier(HTuple attribName, HTuple attribValue, HTuple teamSize, out HTuple barrierHandle)`

`public HBarrier(HTuple attribName, HTuple attribValue, int teamSize)`

`public HBarrier(string attribName, string attribValue, int teamSize)`

`void HBarrier.CreateBarrier(HTuple attribName, HTuple attribValue, int teamSize)`

`void HBarrier.CreateBarrier(string attribName, string attribValue, int teamSize)`

## Description

A barrier is a synchronization object blocking a thread until a previous
defined number of threads have reached this barrier.
`CreateBarrier` allocates and initializes the barrier object returned
in *`barrierHandle`* according to the attributes specified in
*`attribName`* and *`attribValue`*.
*`attribName`* specifies the attribute class and *`attribValue`*
the kind of the barrier. The description beneath lists all barrier kinds
supported by following parameter classes:

- ***""*** —

  empty string sets the default attributes.
- ***"type"*** —

  specifies what happens if a thread waits at a barrier:

  - ***"sleep"*** —

    simply suspends the calling thread (default).
  - ***"spin"*** —

    a fast barrier implementation for short waits
    that waits busy.

The *`teamSize`* argument specifies the number of threads that must
call [`WaitBarrier`](wait_barrier.md) before any of them successfully return from
waiting. The value hold in *`teamSize`* must be greater than zero.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`attribName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Barrier attribute.

Default:
[]

List of values:
"type"

**`attribValue`** (input_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Barrier attribute value.

Number of elements:
AttribValue == AttribName

Default:
[]

List of values:
"sleep", "spin"

**`teamSize`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Barrier team size.

Default:
1

**`barrierHandle`** (output_control)  barrier `→` [HBarrier](HBarrier.md), [HTuple](HTuple.md) (*IntPtr*)

Barrier synchronization object.

## Result

`CreateBarrier` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If necessary, an exception is raised.

## Possible Successors

`WaitBarrier`,
`ClearBarrier`

## Module

Foundation
