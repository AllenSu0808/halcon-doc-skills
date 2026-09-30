# dict_to_json (Operator)

## Name

`dict_to_json` — Transform a dictionary into a JSON string.

## Signature

`def dict_to_json(dict_handle: MaybeSequence[HHandle], gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[int, float, str]]) -> Sequence[str]`

`def dict_to_json_s(dict_handle: MaybeSequence[HHandle], gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[int, float, str]]) -> str`

## Description

`dict_to_json` transforms the dictionary passed in
*`dict_handle`* into a JSON string and returns that string
in *`json_string`*.

Several optional parameters can be set that control the creation of
the JSON strings.
Those parameters can be set via *`gen_param_name`*
and *`gen_param_value`* and are described in the documentation of
[`write_dict`](write_dict.md):

- *"raise_error_if_content_not_serializable"*,
- *"compact_json"*,
- *"use_json_arrays"*.

`dict_to_json` can transform several dictionaries at once.
For this, *`dict_handle`* must contain a tuple of dictionaries.
The output *`json_string`* will then contain one string
per input dictionary.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dict_handle`** (input_control)  dict(-array) `→` MaybeSequence[HHandle]

Dictionary handle.

**`gen_param_name`** (input_control)  attribute.name(-array) `→` MaybeSequence[str]

Name of the generic parameter.

Default:
[]

List of values:
"compact_json", "raise_error_if_content_not_serializable", "use_json_arrays"

**`gen_param_value`** (input_control)  attribute.name(-array) `→` MaybeSequence[Union[int, float, str]]

Value of the generic parameter.

Default:
[]

Suggested values:
"true", "false"

**`json_string`** (output_control)  string(-array) `→` Sequence[str]

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
