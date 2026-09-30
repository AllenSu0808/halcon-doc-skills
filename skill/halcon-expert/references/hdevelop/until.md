# until (Operator)

## Name

`until` — Continue to execute the body as long as the condition is not true.

## Signature

`until( : : Condition : )`

## Description

`until` ends a [`repeat`](repeat.md)..`until` loop.
The [`repeat`](repeat.md)..`until` loop is executed as long as the
*`Condition`* parameter evaluates to *'false'* (*0*).
The body of the loop is executed at least once, because the condition
will be checked at the end of the body.

## Parameters

**`Condition`** (input_control)  integer `→`  (integer)

Condition for loop.

## Result

If the values of the specified parameters are correct,
`until` (as operator) returns 2 (
H_MSG_TRUE)
. Otherwise, an
exception is raised and an error code returned.

## Alternatives

`for`,
`while`

## See also

`repeat`,
`if`,
`elseif`,
`else`,
`break`,
`continue`

## Module

Foundation
