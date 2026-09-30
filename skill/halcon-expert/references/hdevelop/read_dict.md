# read_dict (Operator)

## Name

`read_dict` — Read a dictionary from a file.

## Signature

`read_dict( : : FileName, GenParamName, GenParamValue : DictHandle)`

## Description

`read_dict` reads a dictionary from the file *`FileName`*
and returns the handle of the dictionary in *`DictHandle`*.

The operator supports the following file formats:

- ***'hdict'*:** —

  Binary HALCON format for dictionaries. Files with this format can be
  written by [`write_dict`](write_dict.md).
  The default file extension for this format is 'hdict'.
- ***'json'*:** —

  JSON (JavaScript Object Notation) file format.
  The default file extension for this format is 'json'.

If the given file does not exist, the operator attempts to find
the file by appending the default file extensions to the filename.
The file type is automatically recognized based on the file content
and the file ending (which have to be consistent).

A set of additional optional parameters can be set. The names and values
of the parameters are passed in *`GenParamName`* and
*`GenParamValue`*, respectively. Some of the optional parameters
can only be set for a certain file type. The following values for
*`GenParamName`* are possible:

- ***'json_value_true'*,
  *'json_value_false'*,
  *'json_value_null'*:** —

  Set the values that are used for JSON primitives.
  Valid JSON primitives are `'true'`, `'false'`, and
  `'null'`.
  When encountering such a primitive in a JSON file, the corresponding
  value in the read dictionary is set to the value defined with these
  parameters.
  The value passed in *`GenParamValue`* must be a tuple of length 1.

  The default values for primitives are
  *1* for `'true'`,
  *0* for `'false'`, and
  *'HNULL'* for `'null'`.
  These parameters only have an effect when reading a JSON file.
- ***'convert_json_arrays_to'*:** —

  This parameter controls which HALCON-internal data type is used
  to represent JSON arrays.
  Possible values for *`GenParamValue`* are:

  - ***'dict'* (default):** —

    JSON arrays are converted into HALCON-Dictionaries with consecutive
    integer keys starting at *0*.
    This is always possible, even if the JSON array contains further
    JSON arrays.
    However, using dictionaries might require more memory than storing
    the same data in HALCON tuples.
  - ***'tuple'*:** —

    JSON arrays are converted into HALCON tuples.
    If this is not possible, for example if an array contains an array,
    an exception is raised.
  - ***'tuple_if_possible'*:** —

    JSON arrays are converted into HALCON tuples if possible, and into
    HALCON dictionaries otherwise.

    Note that when using this option, the structure of the returned
    dictionary can change even if the JSON data follows the same schema.
    For example, an array of 2D point coordinates of the form
    *'{"pt": [[1,2], [3,4]]}'*
    would be converted into an outer dictionary which contains two
    tuples.
    However, if under the same schema no points are contained in the
    array, the corresponding entry in the JSON of the form
    *'{"pt": []}'*
    would be converted into a tuple instead of a dictionary.
    Code using the read dictionary must be prepared to deal with this
    kind of change in types.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`FileName`** (input_control)  filename.read `→`  (string)

File name.

File extension:
.`hdict`, .`json`

**`GenParamName`** (input_control)  attribute.name(-array) `→`  (string)

Name of the generic parameter.

Default:
[]

List of values:
'convert_json_arrays_to', 'json_value_false', 'json_value_null', 'json_value_true'

**`GenParamValue`** (input_control)  attribute.name(-array) `→`  (string / integer / real)

Value of the generic parameter.

Default:
[]

Suggested values:
0, 1, 'HNULL', 'true', 'false', 'dict', 'tuple', 'tuple_if_possible'

**`DictHandle`** (output_control)  dict `→`  (handle)

Dictionary handle.

Number of elements:
DictHandle == 1

## Result

If the parameters are valid, the operator `read_dict` returns
the value 2 (
H_MSG_TRUE)
. If necessary an exception is raised.

## Possible Predecessors

`write_dict`

## Alternatives

`json_to_dict`,
`create_dict`

## See also

`write_dict`,
`serialize_handle`,
`deserialize_handle`

## Module

Foundation
