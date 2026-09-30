# query_bar_code_params (Operator)

## Name

`query_bar_code_params` — Get the names of the parameters that can be used in set_bar_code* and
get_bar_code* operators for a given bar code model

## Signature

`def query_bar_code_params(bar_code_handle: HHandle, properties: str) -> Sequence[str]`

`def query_bar_code_params_s(bar_code_handle: HHandle, properties: str) -> str`

## Description

The operator `query_bar_code_params` returns parameter names
of the bar code model that correspond to the selection given in
*`properties`*. To explain this, here first some background:
After creating a bar code model, all parameters
are initially set *"general"*, i.e., they have the same values set
for each supported bar code type. During automatic parameter training or
after calling the operator [`set_bar_code_param_specific`](set_bar_code_param_specific.md) some
parameters might become bar code type specific at runtime. These parameters
can not be read with the general operator
[`get_bar_code_param`](get_bar_code_param.md) but must be read for a given bar code type with
[`get_bar_code_param_specific`](get_bar_code_param_specific.md). To make this access easy and generic,
the output *`gen_param_name`* of `query_bar_code_params` can be
used as input parameter *`gen_param_name`* in
[`get_bar_code_param`](get_bar_code_param.md) or [`get_bar_code_param_specific`](get_bar_code_param_specific.md), depending
on *`properties`*=*"*general"* or
*`properties`*=*"*specific"*.

Please note that you could
alternatively use a static tuple of
parameter names for [`get_bar_code_param`](get_bar_code_param.md) or
[`get_bar_code_param_specific`](get_bar_code_param_specific.md) (e.g., the parameter names described with
these operators), but this
is inflexible and therefore not recommended.

Possible values for *`properties`* are:

- ***"all"*:** —

  Returns the names of all parameters supported by the bar code
  reader. The names are independent of the bar code model given
  in *`bar_code_handle`*.
- ***"general"*:** —

  Returns the names of the parameters that contain the same values
  for all supported bar code types, i.e., there are no specific values
  set for certain bar code types, e.g., with
  [`set_bar_code_param_specific`](set_bar_code_param_specific.md). The values of only these
  parameters can be read with [`get_bar_code_param`](get_bar_code_param.md).

  Please note that the parameter name *"train"* is explicitly excluded
  here. *"train"* in a following call to [`get_bar_code_param`](get_bar_code_param.md)
  would return a multivalue tuple and therefore couldn't be used
  within one tuple in combination with other parameter names.
- ***"specific"*:** —

  Returns the names of the parameters that contain specific values
  for certain bar code types. The values of these parameters must
  be read with [`get_bar_code_param_specific`](get_bar_code_param_specific.md) instead of
  [`get_bar_code_param`](get_bar_code_param.md). Bar code type specific values can
  occur in conjunction with bar code autodiscrimination, described
  with the operator [`find_bar_code`](find_bar_code.md) or automatic parameter
  training.
- ***"trained_general"*:** —

  Returns the names of parameters that have already been trained
  and contain the same values for all supported bar code types.
  The training mode is described with the operator
  [`set_bar_code_param`](set_bar_code_param.md).
- ***"trained_specific"*:** —

  Returns the names of the parameters that have already been trained
  and contain specific values for certain bar code types.
  The training mode is described with the operator
  [`set_bar_code_param`](set_bar_code_param.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`bar_code_handle`** (input_control)  barcode `→` HHandle

Handle of the bar code model.

**`properties`** (input_control)  attribute.name `→` str

Properties of the parameters.

Default:
"trained_general"

List of values:
"all", "general", "specific", "trained_general", "trained_specific"

**`gen_param_name`** (output_control)  attribute.name(-array) `→` Sequence[str]

Names of the generic parameters.

## Example (HDevelop)

```
TrainParams := ['element_size_min', 'element_size_max', 'orientation']
Train3times := gen_tuple_const(|TrainParams|,'train')
create_bar_code_model (Train3times, TrainParams, BarCodeHandle)
find_bar_code (Image, SymbolRegions, BarCodeHandle, 'EAN-13', \
               DecodedDataStrings)
query_bar_code_params (BarCodeHandle, 'trained_general', NamesGen)
* returns NamesGen = ['element_size_max', 'element_size_min']
get_bar_code_param (BarCodeHandle, NamesGen, ValGen)
* returns e.g., ValGen = [4.0, 1.5]
query_bar_code_params (BarCodeHandle, 'trained_specific', NamesSpec)
* returns NamesSpec = ['orientation', 'orientation_tol']
get_bar_code_param_specific (BarCodeHandle, 'EAN-13', NamesSpec, ValSpec)
* returns e.g., ValSpec = [89.9127, 0.5]
```

## Result

The operator `query_bar_code_params` returns the value 2 (
H_MSG_TRUE)
if the
given parameters are correct. Otherwise, an exception is raised.

## Possible Predecessors

`find_bar_code`,
`decode_bar_code_rectangle2`

## Possible Successors

`get_bar_code_param`,
`get_bar_code_param_specific`

## Module

Bar Code
