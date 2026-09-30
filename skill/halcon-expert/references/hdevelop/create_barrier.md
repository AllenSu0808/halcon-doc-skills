# create_barrier (Operator)

## Name

`create_barrier` — Create a barrier synchronization object.

## Signature

`create_barrier( : : AttribName, AttribValue, TeamSize : BarrierHandle)`

## Description

A barrier is a synchronization object blocking a thread until a previous
defined number of threads have reached this barrier.
`create_barrier` allocates and initializes the barrier object returned
in *`BarrierHandle`* according to the attributes specified in
*`AttribName`* and *`AttribValue`*.
*`AttribName`* specifies the attribute class and *`AttribValue`*
the kind of the barrier. The description beneath lists all barrier kinds
supported by following parameter classes:

- ***''*** —

  empty string sets the default attributes.
- ***'type'*** —

  specifies what happens if a thread waits at a barrier:

  - ***'sleep'*** —

    simply suspends the calling thread (default).
  - ***'spin'*** —

    a fast barrier implementation for short waits
    that waits busy.

The *`TeamSize`* argument specifies the number of threads that must
call [`wait_barrier`](wait_barrier.md) before any of them successfully return from
waiting. The value hold in *`TeamSize`* must be greater than zero.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`AttribName`** (input_control)  attribute.name(-array) `→`  (string / integer / real)

Barrier attribute.

Default:
[]

List of values:
'type'

**`AttribValue`** (input_control)  attribute.value(-array) `→`  (string / integer / real)

Barrier attribute value.

Number of elements:
AttribValue == AttribName

Default:
[]

List of values:
'sleep', 'spin'

**`TeamSize`** (input_control)  number `→`  (integer)

Barrier team size.

Default:
1

**`BarrierHandle`** (output_control)  barrier `→`  (handle)

Barrier synchronization object.

## Result

`create_barrier` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If necessary, an exception is raised.

## Possible Successors

`wait_barrier`,
`clear_barrier`

## Module

Foundation
