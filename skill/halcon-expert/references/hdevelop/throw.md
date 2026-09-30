# throw (Operator)

## Name

`throw` — Throws a user-defined exception or rethrows a caught exception.

## Signature

`throw( : : Exception : )`

## Description

With the help of the operators [`try`](try.md), [`catch`](catch.md), [`endtry`](endtry.md),
and `throw` it is possible to implement a dynamic exception handling
in HDevelop, which is comparable to the exception handling in C++
and C#. The basic concepts of the exception handling in HDevelop are
also described at the operators [`try`](try.md), and
[`dev_set_check`](dev_set_check.md) as well as in the `“HDevelop User's Guide”`.

The operator `throw` provides an opportunity to throw an exception
from an arbitrary place in the program.
This exception can be caught by the [`catch`](catch.md) operator of a
surrounding [`try`](try.md)-[`catch`](catch.md) block.
By this means the developer is able to define his own specific error or
exception states, for which the normal program execution is aborted in
order to continue with a specific cross-procedure exception handling,
e.g., for freeing resources or restarting from a defined state.

In such a user-defined exception a nearly arbitrary tuple can be thrown
as the *`Exception`* parameter, merely the first element of the tuple
should be set to a user-defined error code >= 30000.
If different user-defined exception states are possible, they can be
distinguished using different error codes (>= 30000) in the
first element or by using additional elements.

In addition, with the help of the operator `throw` it is possible to
rethrow an exception that was caught with the operator [`catch`](catch.md).
This may be sensible, for instance, if within an inner
[`try`](try.md)-[`catch`](catch.md)-[`endtry`](endtry.md) block (e.g., within an external
procedure) only specific exceptions can be handled in an adequate way and
all other exceptions must be passed to the caller, where they can be caught
and handled by an outer [`try`](try.md)-[`catch`](catch.md)-[`endtry`](endtry.md) block.

For rethrowing a caught exception, it is possible to pass the
*`Exception`* tuple that was caught by the [`catch`](catch.md) operator
directly to the *`Exception`* parameter of the `throw` operator.
Furthermore, it is possible to append arbitrary (but no iconic) user
data to the *`Exception`* tuple, that can be accessed after catching
the exception as *'user_data'* with the operator
[`dev_get_exception_data`](dev_get_exception_data.md):

|  |
| --- |
| [`try`](try.md) |
| ![figure](../assets/0f8e322aa1b0286d.svg)`...` |
| [`catch(Exception)`](catch.md) |
| ![figure](../assets/0f8e322aa1b0286d.svg)`...` |
| ![figure](../assets/0f8e322aa1b0286d.svg)`UserData := ...` |
| ![figure](../assets/0f8e322aa1b0286d.svg)`throw([Exception, UserData])` |
| [`endtry`](endtry.md) |

## Attention

The export of the operators [`try`](try.md), [`catch`](catch.md), [`endtry`](endtry.md),
and `throw` is not supported for the language C, but only for the
languages C++, C# and VisualBasic/.NET.
Only the latter support throwing exceptions across procedures.

## Parameters

**`Exception`** (input_control)  exception-array `→`  (integer / string)

Tuple returning the exception data or user defined
error codes.

## Result

If the values of the specified parameters are correct,
`throw` (as operator) returns 2 (
H_MSG_TRUE)
. Otherwise, an
exception is raised and an error code returned.

## See also

`try`,
`catch`,
`endtry`,
`dev_get_exception_data`,
`dev_set_check`

## Module

Foundation
