# json_to_dict (Operator)

## Name

`json_to_dict` — Transform a JSON string into a dictionary.

## Signature

`json_to_dict( : : JsonString, GenParamName, GenParamValue : DictHandle)`

## Description

`json_to_dict` transforms the string passed in *`JsonString`*,
which must be valid JSON, into a dictionary and returns the handle of
the dictionary in *`DictHandle`*.

Several optional parameters can be set that control the values of
JSON constants. Those parameters can be set via *`GenParamName`*
and *`GenParamValue`* and are described in the documentation of
[`read_dict`](read_dict.md).

`json_to_dict` can transform several strings at once.
For this, *`JsonString`* must contain a tuple of strings.
The output *`DictHandle`* will then contain one dictionary
per input string.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`JsonString`** (input_control)  string(-array) `→`  (string)

String in JSON format.

Default:
['{"key":"value"}']

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

**`DictHandle`** (output_control)  dict(-array) `→`  (handle)

Dictionary handle.

## Example (HDevelop)

```
json_to_dict ('{"capacity": "medium", "image_height": 1024, "image_width": 1024}', [], [], DictHandle)
```

## Result

If the parameters are valid, the operator `json_to_dict` returns
the value 2 (
H_MSG_TRUE)
. If necessary an exception is raised.
This is especially the case if *`JsonString`* does not contain
valid JSON.

## Possible Successors

`write_dict`,
`copy_dict`

## Alternatives

`read_dict`,
`create_dict`

## See also

`read_dict`,
`write_dict`,
`serialize_handle`,
`deserialize_handle`

## Module

Foundation
