# copy_dict (Operator)

## Name

`copy_dict` — Copy a dictionary.

## Signature

`copy_dict( : : DictHandle, GenParamName, GenParamValue : CopiedDictHandle)`

## Description

`copy_dict` creates a deep copy (i.e., all contained handles and iconic
objects are deep copied) of the dictionary *`DictHandle`* in
the dictionary *`CopiedDictHandle`*.

If *`DictHandle`* contains a handle that can not be copied or
that has been freed already, an exception is raised per default.
This behavior is controlled by *`GenParamName`*
*'raise_error_if_content_not_serializable'*, and the corresponding
*`GenParamValue`* can take the following values:

- ***'true'*:** —

  The default: Errors are raised and the copy process aborted.
- ***'low_level'*:** —

  Only low level errors are raised. Instead of the handle concerned an empty
  handle is copied in *`CopiedDictHandle`* and the copy
  process will be continued. The behavior regarding HALCON low level errors
  is determined by *'do_low_error'* in [`set_system`](set_system.md).
- ***'false'*:** —

  The errors are suppressed. Instead of the handle concerned an empty
  handle is copied in *`CopiedDictHandle`* and the copy process will be
  continued.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DictHandle`** (input_control)  dict `→`  (handle)

Dictionary handle.

Number of elements:
DictHandle == 1

**`GenParamName`** (input_control)  attribute.name(-array) `→`  (string)

Name of the generic parameter.

Default:
[]

List of values:
'raise_error_if_content_not_serializable'

**`GenParamValue`** (input_control)  attribute.name(-array) `→`  (string / integer / real)

Value of the generic parameter.

Default:
[]

Suggested values:
'true', 'false', 'low_level'

**`CopiedDictHandle`** (output_control)  dict `→`  (handle)

Copied dictionary handle.

Number of elements:
CopiedDictHandle == 1

## Result

If the parameters are valid, the operator `copy_dict` returns
the value 2 (
H_MSG_TRUE)
. If necessary an exception is raised.

## Possible Predecessors

`read_dict`,
`deserialize_handle`,
`create_dict`

## Possible Successors

`write_dict`

## See also

`read_dict`,
`write_dict`,
`serialize_handle`,
`deserialize_handle`

## Module

Foundation
