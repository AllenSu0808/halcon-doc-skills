# ifelse (Operator)

## Name

`ifelse` — Conditional statement with alternative.

## Warning

**`ifelse` is obsolete and is only provided for
reasons of backward compatibility.
[`if`](if.md) should be used instead.**

## Signature

`ifelse( : : Condition : )`

## Description

`ifelse` is a conditional statement with an alternative.
If the condition is true (i.e., not *0*),
all expressions and calls between the head
and operator [`else`](else.md) are performed.
If the condition is false (i.e., *0*)
the part between [`else`](else.md) and [`endif`](endif.md) is executed.
Note that the operator is called `ifelse` and it is
displayed as `if` in the program text area.

## Parameters

**`Condition`** (input_control)  integer `→`  (integer)

Condition for the if statement.

Default:
1

## Result

If the condition is correct
`ifelse` (as operator) returns 2 (
H_MSG_TRUE)
. Otherwise, an
exception is raised and an error code returned.

## Alternatives

`if`

## See also

`else`,
`elseif`,
`for`,
`while`,
`repeat`,
`until`

## Module

Foundation
