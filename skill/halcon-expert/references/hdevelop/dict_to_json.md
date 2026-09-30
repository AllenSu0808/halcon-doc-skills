# dict_to_json (Operator)

## Name

`dict_to_json` — Transform a dictionary into a JSON string.

## Signature

`dict_to_json( : : DictHandle, GenParamName, GenParamValue : JsonString)`

## Description

`dict_to_json` transforms the dictionary passed in
*`DictHandle`* into a JSON string and returns that string
in *`JsonString`*.

Several optional parameters can be set that control the creation of
the JSON strings.
Those parameters can be set via *`GenParamName`*
and *`GenParamValue`* and are described in the documentation of
[`write_dict`](write_dict.md):

- *'raise_error_if_content_not_serializable'*,
- *'compact_json'*,
- *'use_json_arrays'*.

`dict_to_json` can transform several dictionaries at once.
For this, *`DictHandle`* must contain a tuple of dictionaries.
The output *`JsonString`* will then contain one string
per input dictionary.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DictHandle`** (input_control)  dict(-array) `→`  (handle)

Dictionary handle.

**`GenParamName`** (input_control)  attribute.name(-array) `→`  (string)

Name of the generic parameter.

Default:
[]

List of values:
'compact_json', 'raise_error_if_content_not_serializable', 'use_json_arrays'

**`GenParamValue`** (input_control)  attribute.name(-array) `→`  (string / integer / real)

Value of the generic parameter.

Default:
[]

Suggested values:
'true', 'false'

**`JsonString`** (output_control)  string(-array) `→`  (string)

String in JSON format.

## Example (HDevelop)

```
dict_to_json (dict{foo: 'bar', bar: [0:2]}, [], [], JSONString)
```

## Result

If the parameters are valid, the operator `dict_to_json` returns
the value 2 (
H_MSG_TRUE)
. If necessary an exception is raised.

## Possible Predecessors

`create_dict`,
`read_dict`,
`json_to_dict`

## Possible Successors

`json_to_dict`

## Alternatives

`read_dict`,
`create_dict`

## See also

`json_to_dict`,
`read_dict`,
`write_dict`,
`serialize_handle`,
`deserialize_handle`,
`copy_dict`

## Module

Foundation
