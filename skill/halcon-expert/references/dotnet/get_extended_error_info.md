# GetExtendedErrorInfo (Operator)

## Name

`GetExtendedErrorInfo` — Returns the extended error information for the calling thread's last
HALCON error.

## Signature

`static void HOperatorSet.GetExtendedErrorInfo(out HTuple operatorName, out HTuple errorCode, out HTuple errorMessage)`

`static string HSystem.GetExtendedErrorInfo(out int errorCode, out string errorMessage)`

## Description

`GetExtendedErrorInfo` returns the last error code that occurred
in the calling thread. *`operatorName`* contains the operator name of
the HALCON operator that has set this error code. *`errorCode`* holds
the actual error code and *`errorMessage`* the corresponding
error message. If no error code has been set so far or a
HALCON error comes with no extended error information,
*`operatorName`* and *`errorMessage`* contain an empty string
and *`errorCode`* is set to *0*.
Please refer to 'Result' slot of the
particular operator reference to determine whether and on which
occasion an operator provides extended error information.

`GetExtendedErrorInfo` is thread-local, i.e., the
extended error information is maintained on a per thread basis. Setting an
extended error code in
one thread does not affect the extended error information in any other
thread. This also implies that an error code can only be retrieved
within the thread that was calling the operator setting the
extended error. A thread-local extended error will be cleared
(and set again when applicable) as soon as an error occurs in any other
successive operator call within the same thread, if [`SetSystem`](set_system.md) is
called from within the same thread with the *"tsp_clear_extended_error"*
parameter, or the thread terminates.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`operatorName`** (output_control)  string `→` [HTuple](HTuple.md) (*string*)

Operator that set the error code.

**`errorCode`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Extended error code.

**`errorMessage`** (output_control)  string `→` [HTuple](HTuple.md) (*string*)

Extended error message.

## See also

`GetErrorText`

## Module

none
