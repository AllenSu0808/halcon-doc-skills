# if (Operator)

## Name

`if` — Conditional statement.

## Signature

`if( : : Condition : )`

## Description

`if` is a conditional statement that starts an `if` block.
The *`Condition`* parameter must evaluate to a Boolean or integer
expression.

If *`Condition`* evaluates to *'true'* (not *0*), the
following block body up to the next corresponding block statement
[`elseif`](elseif.md), [`else`](else.md), or [`endif`](endif.md) is executed.
Reaching the end of the block the execution continues after the
corresponding [`endif`](endif.md) statement.

If *`Condition`* evaluates to *'false'* (*0*), the
execution is continued at the next corresponding block statement
[`elseif`](elseif.md), [`else`](else.md), or [`endif`](endif.md).

## Parameters

**`Condition`** (input_control)  integer `→`  (integer)

Condition for the if statement.

Default:
1

## Result

If the condition is correct
`if` (as operator) returns 2 (
H_MSG_TRUE)
. Otherwise, an
exception is raised and an error code returned.

## Alternatives

`elseif`,
`else`

## See also

`for`,
`while`,
`until`

## Module

Foundation
