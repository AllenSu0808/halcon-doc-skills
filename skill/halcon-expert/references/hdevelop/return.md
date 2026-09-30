# return (Operator)

## Name

`return` — Terminate procedure call.

## Signature

`return( : : : )`

## Description

`return` terminates the current procedure call and
returns to the calling procedure. Program execution is continued at
the next active program line after the procedure call in the calling
procedure. If the current procedure is the main procedure, program
execution is finished and the program counter jumps to the end of the
program. Note that every
procedure except the main procedure has to contain at least one reachable
`return` operator line in order to be able to return from a call to
the procedure.

## Result

`return` always returns 2 (
H_MSG_TRUE)
.

## Module

Foundation
