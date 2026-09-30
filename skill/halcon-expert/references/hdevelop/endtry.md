# endtry (Operator)

## Name

`endtry` — Ends a block where exceptions are handled.

## Signature

`endtry( : : : )`

## Description

With the help of the operators [`try`](try.md), [`catch`](catch.md), `endtry`,
and [`throw`](throw.md) it is possible to implement a dynamic exception handling
in HDevelop, which is comparable to the exception handling in C++
and C#. The basic concepts of the exception handling in HDevelop are
described at the operators [`try`](try.md), [`throw`](throw.md), and
[`dev_set_check`](dev_set_check.md) as well as in the `“HDevelop User's Guide”`.

The operator `endtry` closes the exception handling block that was
opened with the operators [`try`](try.md) and [`catch`](catch.md).

## Attention

The export of the operators [`try`](try.md), [`catch`](catch.md), `endtry`,
and [`throw`](throw.md) is not supported for the language C, but only for
the languages C++, C# and VisualBasic/.NET.
Only the latter support throwing exceptions across procedure.

## Result

`endtry` always returns 2 (
H_MSG_TRUE)
.

## See also

`try`,
`catch`,
`throw`,
`dev_get_exception_data`,
`dev_set_check`

## Module

Foundation
