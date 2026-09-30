# json_to_dict (Operator)

## Name

`json_to_dict` — Transform a JSON string into a dictionary.

## Signature

`def json_to_dict(json_string: MaybeSequence[str], gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[int, float, str]]) -> Sequence[HHandle]`

`def json_to_dict_s(json_string: MaybeSequence[str], gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[int, float, str]]) -> HHandle`

## Description

`json_to_dict` transforms the string passed in *`json_string`*,
which must be valid JSON, into a dictionary and returns the handle of
the dictionary in *`dict_handle`*.

Several optional parameters can be set that control the values of
JSON constants. Those parameters can be set via *`gen_param_name`*
and *`gen_param_value`* and are described in the documentation of
[`read_dict`](read_dict.md).

`json_to_dict` can transform several strings at once.
For this, *`json_string`* must contain a tuple of strings.
The output *`dict_handle`* will then contain one dictionary
per input string.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`json_string`** (input_control)  string(-array) `→` MaybeSequence[str]

String in JSON format.

Default:
["{"key":"value"}"]

**`gen_param_name`** (input_control)  attribute.name(-array) `→` MaybeSequence[str]

Name of the generic parameter.

Default:
[]

List of values:
"convert_json_arrays_to", "json_value_false", "json_value_null", "json_value_true"

**`gen_param_value`** (input_control)  attribute.name(-array) `→` MaybeSequence[Union[int, float, str]]

Value of the generic parameter.

Default:
[]

Suggested values:
0, 1, "HNULL", "true", "false", "dict", "tuple", "tuple_if_possible"

**`dict_handle`** (output_control)  dict(-array) `→` Sequence[HHandle]

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
This is especially the case if *`json_string`* does not contain
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
