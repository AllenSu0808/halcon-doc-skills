# GetThreadingAttrib (Operator)

## Name

`GetThreadingAttrib` — Query the attributes of a threading / synchronization object.

## Signature

`static void HOperatorSet.GetThreadingAttrib(HTuple threadingHandle, out HTuple threadingClass, out HTuple attribName, out HTuple attribValue)`

## Description

`GetThreadingAttrib` determines the type of threading object passed
to *`threadingHandle`* and the attributes the threading object was
created with.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`threadingHandle`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Threading object.

**`threadingClass`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Class name of threading object.

**`attribName`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Name of an attribute.

**`attribValue`** (output_control)  number-array `→` [HTuple](HTuple.md) (*string* / int / long / double)

Value of the attribute.

## Result

If the threading handle is valid, the operator `GetThreadingAttrib`
returns 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Successors

`CreateMutex`,
`CreateEvent`,
`CreateCondition`,
`CreateBarrier`

## See also

`CreateMutex`,
`CreateEvent`,
`CreateCondition`,
`CreateBarrier`

## Module

Foundation
