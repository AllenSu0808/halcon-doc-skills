# write_dict (Operator)

## Name

`write_dict` — Write a dictionary to a file.

## Signature

`def write_dict(dict_handle: HHandle, file_name: str, gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[int, float, str]]) -> None`

## Description

`write_dict` writes the dictionary denoted by the
*`dict_handle`* to the file *`file_name`*.

The operator supports the file formats *"hdict"*
and *"json"* (see [`read_dict`](read_dict.md)).
The format is selected based on the filename ending or
by using the generic parameter *"file_type"* (see below).
If neither is conclusive or set, the file is written as *"hdict"*.

Note that due to restrictions of the *"json"*-format, some
information contained in dictionaries can not be stored in that
file format.
This includes iconic objects and handles that are not dictionaries.
By default, `write_dict` will return an error if the
dictionary contains such an item.
This behavior can be changed using the generic parameter
*"raise_error_if_content_not_serializable"* (see below).

A set of additional optional parameters can be set. The names and values
of the parameters are passed in *`gen_param_name`* and
*`gen_param_value`*, respectively. Some of the optional parameters
can only be set for a certain file type. The following values for
*`gen_param_name`* are possible:

- ***"raise_error_if_content_not_serializable"*:** —

  If *`dict_handle`* contains an item that can not be serialized,
  an exception is raised per default.
  This behavior is controlled by this parameter, for which
  *`gen_param_value`* can take the following values:

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
    determined by *"do_low_error"* in [`set_system`](set_system.md).
- ***"file_type"*:** —

  Sets the file type to be used.
  The corresponding entry in *`gen_param_value`* must be set to
  *"hdict"* (default) or *"json"*.
  If this parameter is not set, the file type is determined based
  on the ending of the file name.
  If that ending is not conclusive, the default *"hdict"*
  is used.
- ***"compact_json"*:** —

  Controls if JSON files are written in a compact format without
  additional whitespace, or human-readable with newlines and indentation.
  In both cases the file will contain the same information.
  The corresponding entry in *`gen_param_value`* must be set to
  *"true"* (default) or *"false"*.
- ***"use_json_arrays"*:** —

  Controls if `write_dict` should convert dictionaries into
  native JSON arrays where possible.
  For this, the dictionaries must only contain ascending integer keys
  starting at zero.
  The corresponding entry in *`gen_param_value`* must be set to
  *"true"* (default) or *"false"*.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dict_handle`** (input_control)  dict `→` HHandle

Dictionary handle.

Number of elements:
DictHandle == 1

**`file_name`** (input_control)  filename.write `→` str

File name.

File extension:
.`hdict`

**`gen_param_name`** (input_control)  attribute.name(-array) `→` MaybeSequence[str]

Name of the generic parameter.

Default:
[]

List of values:
"compact_json", "file_type", "raise_error_if_content_not_serializable", "use_json_arrays"

**`gen_param_value`** (input_control)  attribute.name(-array) `→` MaybeSequence[Union[int, float, str]]

Value of the generic parameter.

Default:
[]

Suggested values:
"hdict", "json", "true", "false", "low_level"

## Result

If the parameters are valid, the operator `write_dict` returns
the value 2 (
H_MSG_TRUE)
. If necessary an exception is raised.

## Possible Predecessors

`read_dict`,
`deserialize_handle`,
`create_dict`

## Possible Successors

`read_dict`,
`create_dict`

## See also

`read_dict`,
`serialize_handle`,
`deserialize_handle`,
`dict_to_json`

## Module

Foundation
