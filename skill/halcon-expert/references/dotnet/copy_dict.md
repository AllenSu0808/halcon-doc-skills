# CopyDict (Operator)

## Name

`CopyDict` — Copy a dictionary.

## Signature

`static void HOperatorSet.CopyDict(HTuple dictHandle, HTuple genParamName, HTuple genParamValue, out HTuple copiedDictHandle)`

`HDict HDict.CopyDict(HTuple genParamName, HTuple genParamValue)`

`HDict HDict.CopyDict(string genParamName, string genParamValue)`

## Description

`CopyDict` creates a deep copy (i.e., all contained handles and iconic
objects are deep copied) of the dictionary *`dictHandle`* in
the dictionary *`copiedDictHandle`*.

If *`dictHandle`* contains a handle that can not be copied or
that has been freed already, an exception is raised per default.
This behavior is controlled by *`genParamName`*
*"raise_error_if_content_not_serializable"*, and the corresponding
*`genParamValue`* can take the following values:

- ***"true"*:** —

  The default: Errors are raised and the copy process aborted.
- ***"low_level"*:** —

  Only low level errors are raised. Instead of the handle concerned an empty
  handle is copied in *`copiedDictHandle`* and the copy
  process will be continued. The behavior regarding HALCON low level errors
  is determined by *"do_low_error"* in [`SetSystem`](set_system.md).
- ***"false"*:** —

  The errors are suppressed. Instead of the handle concerned an empty
  handle is copied in *`copiedDictHandle`* and the copy process will be
  continued.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dictHandle`** (input_control)  dict `→` [HDict](HDict.md), [HTuple](HTuple.md) (*IntPtr*)

Dictionary handle.

Number of elements:
DictHandle == 1

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Name of the generic parameter.

Default:
[]

List of values:
"raise_error_if_content_not_serializable"

**`genParamValue`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Value of the generic parameter.

Default:
[]

Suggested values:
"true", "false", "low_level"

**`copiedDictHandle`** (output_control)  dict `→` [HDict](HDict.md), [HTuple](HTuple.md) (*IntPtr*)

Copied dictionary handle.

Number of elements:
CopiedDictHandle == 1

## Result

If the parameters are valid, the operator `CopyDict` returns
the value 2 (
H_MSG_TRUE)
. If necessary an exception is raised.

## Possible Predecessors

`ReadDict`,
`DeserializeHandle`,
`CreateDict`

## Possible Successors

`WriteDict`

## See also

`ReadDict`,
`WriteDict`,
`SerializeHandle`,
`DeserializeHandle`

## Module

Foundation
