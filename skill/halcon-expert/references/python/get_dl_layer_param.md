# get_dl_layer_param (Operator)

## Name

`get_dl_layer_param` — Return the parameters of a deep learning layer.

## Signature

`def get_dl_layer_param(dllayer: HHandle, gen_param_name: str) -> Sequence[HTupleElementType]`

`def get_dl_layer_param_s(dllayer: HHandle, gen_param_name: str) -> HTupleElementType`

## Description

The operator `get_dl_layer_param` returns the parameter
*`gen_param_name`* of the deep learning layer *`dllayer`*
in *`gen_param_value`*.

Depending on the type of the layer, different parameter names
are valid.
Which generic and layer-specific parameters can be queried is described
in the specific references of the operators used for layer creation
(`create_dl_layer_*`).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dllayer`** (input_control)  dl_layer `→` HHandle

Layer.

**`gen_param_name`** (input_control)  attribute.name `→` str

Parameter to query.

Default:
"shape"

List of values:
"input_layer", "name", "shape", "type"

**`gen_param_value`** (output_control)  attribute.value(-array) `→` Sequence[HTupleElementType]

Value of the queried parameter.

## Module

Deep Learning Professional
