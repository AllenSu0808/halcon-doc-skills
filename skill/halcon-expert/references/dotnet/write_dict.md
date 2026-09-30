# WriteDict (Operator)

## Name

`WriteDict` — Write a dictionary to a file.

## Signature

`static void HOperatorSet.WriteDict(HTuple dictHandle, HTuple fileName, HTuple genParamName, HTuple genParamValue)`

`void HDict.WriteDict(string fileName, HTuple genParamName, HTuple genParamValue)`

`void HDict.WriteDict(string fileName, string genParamName, string genParamValue)`

## Description

`WriteDict` writes the dictionary denoted by the
*`dictHandle`* to the file *`fileName`*.

The operator supports the file formats *"hdict"*
and *"json"* (see [`ReadDict`](read_dict.md)).
The format is selected based on the filename ending or
by using the generic parameter *"file_type"* (see below).
If neither is conclusive or set, the file is written as *"hdict"*.

Note that due to restrictions of the *"json"*-format, some
information contained in dictionaries can not be stored in that
file format.
This includes iconic objects and handles that are not dictionaries.
By default, `WriteDict` will return an error if the
dictionary contains such an item.
This behavior can be changed using the generic parameter
*"raise_error_if_content_not_serializable"* (see below).

A set of additional optional parameters can be set. The names and values
of the parameters are passed in *`genParamName`* and
*`genParamValue`*, respectively. Some of the optional parameters
can only be set for a certain file type. The following values for
*`genParamName`* are possible:

- ***"raise_error_if_content_not_serializable"*:** —

  If *`dictHandle`* contains an item that can not be serialized,
  an exception is raised per default.
  This behavior is controlled by this parameter, for which
  *`genParamValue`* can take the following values:

  - ***"true"*:** —

    The default behavior, errors are raised.
  - ***"false"*:** —

    The errors are suppressed.
    Depending on the file type an empty handle (*"hdict"*) or
    no entry at all (*"json"*) are written in place of the
    non serializable item.
  - ***"low_level"*:** —

    The file output is the same as for
    *"false"*.
    Additionally, low level errors are raised if non-serializable
    items are encountered.
    The behavior regarding HALCON low level errors is
    determined by *"do_low_error"* in [`SetSystem`](set_system.md).
- ***"file_type"*:** —

  Sets the file type to be used.
  The corresponding entry in *`genParamValue`* must be set to
  *"hdict"* (default) or *"json"*.
  If this parameter is not set, the file type is determined based
  on the ending of the file name.
  If that ending is not conclusive, the default *"hdict"*
  is used.
- ***"compact_json"*:** —

  Controls if JSON files are written in a compact format without
  additional whitespace, or human-readable with newlines and indentation.
  In both cases the file will contain the same information.
  The corresponding entry in *`genParamValue`* must be set to
  *"true"* (default) or *"false"*.
- ***"use_json_arrays"*:** —

  Controls if `WriteDict` should convert dictionaries into
  native JSON arrays where possible.
  For this, the dictionaries must only contain ascending integer keys
  starting at zero.
  The corresponding entry in *`genParamValue`* must be set to
  *"true"* (default) or *"false"*.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dictHandle`** (input_control)  dict `→` [HDict](HDict.md), [HTuple](HTuple.md) (*IntPtr*)

Dictionary handle.

Number of elements:
DictHandle == 1

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

File name.

File extension:
.`hdict`

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Name of the generic parameter.

Default:
[]

List of values:
"compact_json", "file_type", "raise_error_if_content_not_serializable", "use_json_arrays"

**`genParamValue`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Value of the generic parameter.

Default:
[]

Suggested values:
"hdict", "json", "true", "false", "low_level"

## Result

If the parameters are valid, the operator `WriteDict` returns
the value 2 (
H_MSG_TRUE)
. If necessary an exception is raised.

## Possible Predecessors

`ReadDict`,
`DeserializeHandle`,
`CreateDict`

## Possible Successors

`ReadDict`,
`CreateDict`

## See also

`ReadDict`,
`SerializeHandle`,
`DeserializeHandle`,
`DictToJson`

## Module

Foundation
