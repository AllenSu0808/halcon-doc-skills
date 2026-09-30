# dev_get_exception_data (Operator)

## Name

`dev_get_exception_data` — Access the elements of an exception tuple.

## Signature

`dev_get_exception_data( : : Exception, Name : Value)`

## Description

The operator `dev_get_exception_data` enables to access specific
items of an exception tuple that was caught by the operator [`catch`](catch.md).
Except the error code that is always passed as the first element of the
exception tuple all other data of the exception tuple has to be accessed
exclusively via the operator `dev_get_exception_data`.
This is due to the fact that the order and the extent of the provided data
may change in future versions and may vary for the different code exports.

If an operator error occurred within HDevelop or HDevEngine, the caught
exception tuple contains the data items listed below.
This tuple has to be passed to the parameter *`Exception`*.
The name of the requested data slot has to be passed to the parameter
*`Name`*.
The requested data is returned in the parameter *`Value`*.
By passing a tuple of slot names to *`Name`* it is possible to
request several exception data items in a single call of
`dev_get_exception_data`.
In that case a corresponding data tuple is returned in *`Value`*.
For requested items that are not available an empty string
(*''*) is returned.

Note that the operator `dev_get_exception_data` is meant to be used
within HDevelop or HDevEngine. Some information is not available when the
operator is exported.

**Supported data slots:**

- ***'error_code'*:** —

  HALCON or user defined error code.
  A list of HALCON error codes (codes < 10000) can be found in the
  appendix of the “Extension Package Programmer's Manual”.
- ***'add_error_code'*:** —

  Additional HDevelop specific error code.
  These error codes specify whether an error was caught within
  the HALCON operator (code = 21000) or outside the operator, e.g.,
  during the evaluation and assignment of the parameter expressions.
  In the latter case the error code specifies the error type
  more precisely.
  The relevant error codes are listed in the
  `“HDevelop User's Guide”`.
- ***'error_message'*:** —

  HALCON error message.
- ***'add_error_message'*:** —

  Additional error message that describes the HDevelop specific
  error more precisely.
- ***'program_line'*:** —

  Number of the program line, where the error occurred.
- ***'operator'*:** —

  Name of the operator that threw the exception (if the exception was
  thrown in a protected procedure,
  '--protected--' is returned instead of
  the operator name).
- ***'call_stack_depth'*:** —

  Depth of the call stack (if the error occurred in 'main' a depth of 1
  is returned).
- ***'procedure'*:** —

  Name of the procedure where the error occurred.
- ***'user_data'*:** —

  User defined exception tuple.
  If an operator exception was caught and rethrown, this is the tuple
  that was appended to the caught exception tuple in the call of
  [`throw`](throw.md).
  In case of a completely user defined exception all tuple items except
  the first element containing the error code (>= 30000)
  are returned.
  If no user data was passed with the exception tuple, an empty tuple
  is returned.
  Note, that the user data tuple cannot be requested together with any
  other exception data in one `dev_get_exception_data` call.

## Parameters

**`Exception`** (input_control)  exception-array `→`  (integer / string)

Tuple containing the exception data or user defined
error codes.

**`Name`** (input_control)  attribute.name(-array) `→`  (string)

Name(s) of the requested exception data.

Default:
'error_code'

List of values:
'add_error_code', 'add_error_message', 'call_stack_depth', 'error_code', 'error_message', 'operator', 'procedure', 'program_line', 'user_data'

**`Value`** (output_control)  attribute.value-array `→`  (integer / string)

Requested exception data.

## Result

If the values of the specified parameters are correct,
`dev_get_exception_data` (as operator) returns 2 (
H_MSG_TRUE)
. Otherwise, an
exception is raised and an error code returned.

## Possible Predecessors

`catch`

## See also

`try`,
`catch`,
`endtry`,
`throw`,
`dev_set_check`

## Module

Foundation
