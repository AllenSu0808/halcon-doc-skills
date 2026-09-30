# continue (Operator)

## Name

`continue` — Skip the current loop execution.

## Signature

`continue( : : : )`

## Description

`continue` skips the smallest enclosing [`for`](for.md), [`while`](while.md)
or [`repeat`](repeat.md)..[`until`](until.md) loop execution. Program execution is
continued at the
condition line of the loop or at the next line after the `continue`
statement in case no enclosing loop exists.

## Result

`continue` (as operators) always returns 2 (
H_MSG_TRUE)
.

## Alternatives

`break`

## See also

`for`,
`while`,
`repeat`,
`until`

## Module

Foundation
