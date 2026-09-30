# catch (Operator)

## Name

`catch` — Catches exceptions that were thrown in the preceding [`try`](try.md) block.

## Signature

`catch( : : : Exception)`

## Description

With the help of the operators [`try`](try.md), `catch`, [`endtry`](endtry.md),
and [`throw`](throw.md) it is possible to implement a dynamic exception handling
in HDevelop, which is comparable to the exception handling in C++
and C#. The basic concepts of the exception handling in HDevelop are
described at the operators [`try`](try.md), [`throw`](throw.md), and
[`dev_set_check`](dev_set_check.md) as well as in the `“HDevelop User's Guide”`.

The operator `catch` ends a block of watched program lines
and starts a block of program lines that have to be executed
in an error case.
If the [`try`](try.md)-`catch` block is executed without an
exception, the `catch`-[`endtry`](endtry.md) block is ignored and
program execution continues after the corresponding [`endtry`](endtry.md) operator.
In contrast, in an error case the program execution jumps directly from the
operator where the error occurred (or from the [`throw`](throw.md) operator) to the
`catch` operator of the surrounding [`try`](try.md)-`catch` block.
The output control parameter *`Exception`* returns a tuple that contains
a predefined set of data describing the error in case an operator error
occurred.
If the exception was thrown by the [`throw`](throw.md) operator, an
arbitrary user-defined tuple can be returned.

The most important data within the *`Exception`* tuple is the error
code.
Therefore, this is passed as the first item of the *`Exception`* tuple
and can be accessed directly with *`Exception`*[0].
However, all other data has to be accessed through the operator
[`dev_get_exception_data`](dev_get_exception_data.md), because the order and the extent of the
provided data may change in future versions and
may vary for different programming language exports.
Especially, it has to be taken into account that in the exported code there
are some items of the error tuple that are not available and others
that might not be determined until they are requested (like error messages).

If the exception was thrown by an operator error, a HALCON error
code (< 10000) or if the aborted operator belongs to an extension package,
a user-defined error code (> 10000) is returned as the error code.
A list of all HALCON error codes can be found in the appendix of the
“Extension Package Programmer's Manual”.
The first element of a user-defined *`Exception`* tuple
thrown by the operator [`throw`](throw.md) should be an error code
>= 30000.
Additional tuple elements can be chosen without any restrictions.

If an operator error occurred within HDevelop or HDevEngine, the following
information about the error is provided by the
*`Exception`* tuple:

- The HALCON error code.
- An additional HDevelop specific error code that specifies whether an
  error was caught within the HALCON operator (code = 21000) or
  outside the operator, e.g., during the evaluation and assignment of the
  parameter expressions.
  In the latter case the error code specifies the kind of error
  more precisely.
- The HALCON error message.
- An appropriate HDevelop-specific error message.
- The number of the program line, where the error occurred.
- The name of the operator that threw the exception (if the exception was
  thrown in a protected procedure,
  '--protected--' is returned instead of the
  operator name).
- The depth of the call stack (if the error occurred in 'main' a depth of 1
  is returned).
- The name of the procedure, where the error occurred.

In most cases, for an automatic exception handling it is sufficient to use
the HALCON error code.
Additional data is primarily passed in order to provide some information
about the error condition to the developer of the HDevelop program for
debugging reasons.
Attention: in the exported code, in general, information about the error
location will not be available.

## Attention

The export of the operators [`try`](try.md), `catch`, [`endtry`](endtry.md),
and [`throw`](throw.md) is not supported for the language C, but only for
the languages C++, C# and VisualBasic/.NET.
Only the latter support throwing exceptions across procedures.

## Parameters

**`Exception`** (output_control)  exception-array `→`  (integer / string)

Tuple returning the exception data.

## Result

`catch` always returns 2 (
H_MSG_TRUE)
.

## Possible Successors

`dev_get_exception_data`

## See also

`try`,
`endtry`,
`throw`,
`dev_get_exception_data`,
`dev_set_check`

## Module

Foundation
