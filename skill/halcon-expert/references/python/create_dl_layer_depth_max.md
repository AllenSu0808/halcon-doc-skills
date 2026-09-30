# create_dl_layer_depth_max (Operator)

## Name

`create_dl_layer_depth_max` — Create a depth max layer.

## Signature

`def create_dl_layer_depth_max(dllayer_input: HHandle, layer_name: str, depth_max_mode: str, gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[int, float, str]]) -> Tuple[Sequence[HHandle], Sequence[HHandle]]`

`def create_dl_layer_depth_max_s(dllayer_input: HHandle, layer_name: str, depth_max_mode: str, gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[int, float, str]]) -> Tuple[HHandle, HHandle]`

## Description

The operator `create_dl_layer_depth_max` creates a depth max layer.

The parameter *`dllayer_input`* determines the feeding input layer and
expects the layer handle as value.

There are two possible output layers depending on *`depth_max_mode`*:

- *`dllayer_depth_max_arg`*: Handle to a depth max layer with mode
  *"argmax"*.
- *`dllayer_depth_max_value`*: Handle to a depth max layer with mode
  *"value"*.

Note, these parameters only need to be set in case such an output layer
is requested (see *`depth_max_mode`*).

The parameter *`layer_name`* defines the name of the output layer(s)
depending on *`depth_max_mode`*:

- *"argmax"*: name of *`dllayer_depth_max_arg`*.
- *"value"*: name of *`dllayer_depth_max_value`*.
- *"argmax_and_value"*: name of *`dllayer_depth_max_arg`*,
  while the layer *`dllayer_depth_max_value`* receives the same name
  with the suffix string *"_value"* appended to it.

Note that if creating a model using [`create_dl_model`](create_dl_model.md) each layer of the
created network must have a unique name.

The mode *`depth_max_mode`* indicates which depth max value is
actually returned as output.
The following values are supported:

- ***"argmax"*:** —

  The `depth` index of the maximal value is returned
  in *`dllayer_depth_max_arg`*.
- ***"value"*:** —

  The maximal value itself is returned in *`dllayer_depth_max_value`*.
- ***"argmax_and_value"*:** —

  Both are returned, the `depth` index of
  the maximal value in the output layer *`dllayer_depth_max_arg`*, and
  the maximal value itself in the output layer
  *`dllayer_depth_max_value`*.

The following generic parameters *`gen_param_name`* and the corresponding
values *`gen_param_value`* are supported:

- ***"is_inference_output"*:** —

  Determines whether [`apply_dl_model`](apply_dl_model.md) will include the output of this
  layer in the dictionary `dlresult_batch` even without specifying this
  layer in `outputs` (*"true"*) or not (*"false"*).

  Default:
   *"false"*

Certain parameters of layers created using this operator
`create_dl_layer_depth_max` can be set and retrieved using
further operators.
The following tables give an overview, which parameters can be set
using [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and which ones can be retrieved
using [`get_dl_model_layer_param`](get_dl_model_layer_param.md) or [`get_dl_layer_param`](get_dl_layer_param.md). Note, the
operators [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and [`get_dl_model_layer_param`](get_dl_model_layer_param.md)
require a model created by [`create_dl_model`](create_dl_model.md).

| Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"input_layer"* (*`dllayer_input`*) |  | `x` |
| *"mode"* (*`depth_max_mode`*) | `x` | `x` |
| *"name"* (*`layer_name`*) | `x` | `x` |
| *"output_layer"* (*`dllayer_depth_max_arg`* and/or *`dllayer_depth_max_value`*) |  | `x` |
| *"shape"* |  | `x` |
| *"type"* |  | `x` |

| Generic Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"is_inference_output"* |  | `x` |
| *"num_trainable_params"* |  | `x` |

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dllayer_input`** (input_control)  dl_layer `→` HHandle

Feeding layer.

**`layer_name`** (input_control)  string `→` str

Name of the output layer.

**`depth_max_mode`** (input_control)  string `→` str

Mode to indicate type of return value.

Default:
"argmax"

List of values:
"argmax", "argmax_and_value", "value"

**`gen_param_name`** (input_control)  attribute.name(-array) `→` MaybeSequence[str]

Generic input parameter names.

Default:
[]

List of values:
"is_inference_output"

**`gen_param_value`** (input_control)  attribute.value(-array) `→` MaybeSequence[Union[int, float, str]]

Generic input parameter values.

Default:
[]

Suggested values:
"true", "false"

**`dllayer_depth_max_arg`** (output_control)  dl_layer(-array) `→` Sequence[HHandle]

Optional, depth max layer with mode *"argmax"*.

**`dllayer_depth_max_value`** (output_control)  dl_layer(-array) `→` Sequence[HHandle]

Optional, depth max layer with mode *"value"*.

## Module

Deep Learning Professional
