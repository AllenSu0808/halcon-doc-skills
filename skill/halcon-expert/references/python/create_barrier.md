# create_barrier (Operator)

## Name

`create_barrier` — Create a barrier synchronization object.

## Signature

`def create_barrier(attrib_name: MaybeSequence[Union[int, float, str]], attrib_value: MaybeSequence[Union[int, float, str]], team_size: int) -> HHandle`

## Description

A barrier is a synchronization object blocking a thread until a previous
defined number of threads have reached this barrier.
`create_barrier` allocates and initializes the barrier object returned
in *`barrier_handle`* according to the attributes specified in
*`attrib_name`* and *`attrib_value`*.
*`attrib_name`* specifies the attribute class and *`attrib_value`*
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

The *`team_size`* argument specifies the number of threads that must
call [`wait_barrier`](wait_barrier.md) before any of them successfully return from
waiting. The value hold in *`team_size`* must be greater than zero.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`attrib_name`** (input_control)  attribute.name(-array) `→` MaybeSequence[Union[int, float, str]]

Barrier attribute.

Default:
[]

List of values:
"type"

**`attrib_value`** (input_control)  attribute.value(-array) `→` MaybeSequence[Union[int, float, str]]

Barrier attribute value.

Number of elements:
AttribValue == AttribName

Default:
[]

List of values:
"sleep", "spin"

**`team_size`** (input_control)  number `→` int

Barrier team size.

Default:
1

**`barrier_handle`** (output_control)  barrier `→` HHandle

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
