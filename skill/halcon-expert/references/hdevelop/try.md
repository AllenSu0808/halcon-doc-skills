# try (Operator)

## Name

`try` — Starts a program block where exceptions are detected and caught.

## Signature

`try( : : : )`

## Description

With the help of the operators `try`, [`catch`](catch.md), [`endtry`](endtry.md),
and [`throw`](throw.md) it is possible to implement a dynamic exception handling
in HDevelop, which is comparable to the exception handling in C++
and C#. By the operators `try`, [`catch`](catch.md), and [`endtry`](endtry.md)
two code blocks are formed: the first one (`try` .. [`catch`](catch.md))
contains the watched program lines that perform the normal program logic.
The second block ([`catch`](catch.md) .. [`endtry`](endtry.md)) contains the code
that has is executed if an exception occurs.

The operator `try` enables the exception handling for the following
program lines, i.e., the following code block up to the corresponding
[`catch`](catch.md) operator is watched for exceptions.
If during the execution of the subsequent program lines an error or another
exceptional state occurs, or if an exception is thrown explicitly by the
operator [`throw`](throw.md), the `try` block is left immediately
(or---depending on a user preference---after displaying an error message box)
and the program execution continues at the corresponding [`catch`](catch.md)
operator.
If the exception is thrown within a procedure that was called from the
`try` block (directly or via other procedure calls), the procedure
call and all intermediate procedure calls that are on the call stack above
the `try` block are immediately aborted (or, if applicable, also after
displaying an error message box).

Whether an error message box is displayed before the exception is thrown
or not, is controlled by the HDevelop preference
`'Suppress error message dialogs within try-catch blocks'`
that can be reached via
`Edit->Preferences->General Options->Experienced User`.
This message box also offers the opportunity to stop the program execution
before the exception is thrown in order to edit the possibly erroneous
operator call.

The program block that is watched for exceptions ends with the corresponding
[`catch`](catch.md) operator.
If within the watched `try` block no exception occurred, the following
[`catch`](catch.md) block is ignored and the program execution continues after
the corresponding [`endtry`](endtry.md) operator.

`try`-[`catch`](catch.md)-[`endtry`](endtry.md) blocks can be nested arbitrarily
into each other, within a procedure or over different procedure calls,
as long as any inner `try`-[`catch`](catch.md)-[`endtry`](endtry.md) block lies
completely *either* within an outer `try`-[`catch`](catch.md)
*or* a [`catch`](catch.md)-[`endtry`](endtry.md) block.
If an exception is thrown within an inner `try`-[`catch`](catch.md) block,
the exception handling is caught in the corresponding
[`catch`](catch.md)-[`endtry`](endtry.md) block. Hence, the exception is not
visible for the outer `try`-[`catch`](catch.md) blocks unless the
exception is rethrown explicitly by calling a [`throw`](throw.md) operator
from the [`catch`](catch.md) block.

If within a HALCON operator an error occurs, an exception tuple is created
and passed to the [`catch`](catch.md) operator that is responsible for catching
the exception.
The tuple collects information about the error such as the error code and
the error text.
After catching an exception, this information can be accessed with the
help of the operator [`dev_get_exception_data`](dev_get_exception_data.md).
For more information about the passed exception data, how to access them,
and considerations about the code export, see the description of that
operator.
The reference of the operator [`throw`](throw.md) describes how to throw
user-defined exception tuples.

HDevelop offers the opportunity to disable the handling of HALCON errors.
This can be achieved by calling the operator
`dev_set_check('~give_error')`
or by unchecking the check box *Give Error* on the dialog
`Edit->Preferences->Runtime Settings`.
If the error handling is switched off, in case of an HALCON error no
exception is thrown but the program execution is continued as normal at the
next operator.
In contrast to that, the operator [`throw`](throw.md) will always throw an
exception independently of the *'give_error'* setting.
The same applies if an error occurred during the evaluation of an
parameter expression.

## Attention

The export of the operators `try`, [`catch`](catch.md), [`endtry`](endtry.md),
and [`throw`](throw.md) is not supported for the language C, but only for
the languages C++, C# and VisualBasic/.NET.
Only the latter support throwing exceptions across procedures.

## Example (HDevelop)

```
try
  read_image (Image, 'may_be_not_available')
catch (Exception)
  if (Exception[0] == 5200)
    dev_get_exception_data (Exception, 'error_message', ErrMsg)
    set_tposition (3600, 24, 12)
    write_string (3600, ErrMsg)
    return ()
  else
    * rethrow the exception
    throw ([Exception,'unknown exception in myproc'])
  endif
endtry
```

## Result

`try` always returns 2 (
H_MSG_TRUE)
.

## Alternatives

`dev_set_check`

## See also

`catch`,
`endtry`,
`throw`,
`dev_get_exception_data`,
`dev_set_check`

## Module

Foundation
