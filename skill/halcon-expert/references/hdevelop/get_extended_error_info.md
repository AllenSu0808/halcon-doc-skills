# get_extended_error_info (Operator)

## Name

`get_extended_error_info` — Returns the extended error information for the calling thread's last
HALCON error.

## Signature

`get_extended_error_info( : : : OperatorName, ErrorCode, ErrorMessage)`

## Description

`get_extended_error_info` returns the last error code that occurred
in the calling thread. *`OperatorName`* contains the operator name of
the HALCON operator that has set this error code. *`ErrorCode`* holds
the actual error code and *`ErrorMessage`* the corresponding
error message. If no error code has been set so far or a
HALCON error comes with no extended error information,
*`OperatorName`* and *`ErrorMessage`* contain an empty string
and *`ErrorCode`* is set to *0*.
Please refer to 'Result' slot of the
particular operator reference to determine whether and on which
occasion an operator provides extended error information.

`get_extended_error_info` is thread-local, i.e., the
extended error information is maintained on a per thread basis. Setting an
extended error code in
one thread does not affect the extended error information in any other
thread. This also implies that an error code can only be retrieved
within the thread that was calling the operator setting the
extended error. A thread-local extended error will be cleared
(and set again when applicable) as soon as an error occurs in any other
successive operator call within the same thread, if [`set_system`](set_system.md) is
called from within the same thread with the *'tsp_clear_extended_error'*
parameter, or the thread terminates.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`OperatorName`** (output_control)  string `→`  (string)

Operator that set the error code.

**`ErrorCode`** (output_control)  integer `→`  (integer)

Extended error code.

**`ErrorMessage`** (output_control)  string `→`  (string)

Extended error message.

## See also

`get_error_text`

## Module

none
