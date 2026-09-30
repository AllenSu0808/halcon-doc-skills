# GetErrorText (Operator)

## Name

`GetErrorText` — Inquiry after the error text of a HALCON error number.

## Signature

`static void HOperatorSet.GetErrorText(HTuple errorCode, out HTuple errorMessage)`

`static string HSystem.GetErrorText(int errorCode)`

## Description

The operator `GetErrorText` returns the error message for the
corresponding HALCON error code. This is indeed the same text
which will be given during an exception. The operator
`GetErrorText` is especially useful if the error treatment
is programmed by the users themselves
(see also `set_check(::'~give_error':)`).

## Attention

Unknown error codes will trigger a standard message.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`errorCode`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

HALCON error code.

Restriction:
`1 <= ErrorCode && ErrorCode <= 36000`

**`errorMessage`** (output_control)  string `→` [HTuple](HTuple.md) (*string*)

Corresponding error message.

## Example (C)

```
Herror   err;
char       message[MAX_STRING];

set_check("~give_error");
err = send_region(region,socket);
set_check("give_error");
if (err != H_MSG_TRUE) {
get_error_text((Hlong)err,message);
  fprintf(stderr,"my error message: %s\n",message);
  exit(1);
}
```

## Result

The operator `GetErrorText` returns the value 2 (
H_MSG_TRUE)
, if
the parameters are correct.
Otherwise an exception will be raised.

## Possible Predecessors

`SetCheck`

## See also

`SetCheck`

## Module

none
