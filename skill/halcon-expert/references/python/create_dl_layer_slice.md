# create_dl_layer_slice (Operator)

## Name

`create_dl_layer_slice` — Create a slice layer.

## Signature

`def create_dl_layer_slice(dllayer_input: HHandle, layer_name: str, axes: MaybeSequence[Union[int, str]], start_indices: MaybeSequence[int], end_indices: MaybeSequence[int], steps: MaybeSequence[int], gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[int, float, str]]) -> HHandle`

## Description

The operator `create_dl_layer_slice` creates a slice layer that extracts
a single slice of a tensor along specified axes, based on the provided start
and end indices as well as the step size for the slicing operations.
The handle of the slice layer is returned in *`dllayer_slice`*.

The parameter *`dllayer_input`* determines the feeding input layer and
expects the layer handle as value.

The parameter *`layer_name`* sets an individual layer name.
Note that if creating a model using [`create_dl_model`](create_dl_model.md) each layer of
the created network must have a unique name.

The following parameters are used for the slice operation:

- ***"starts"*** —

  Determines the starting indices of the slice
  operation along the axes specified in *"axes"*. This parameter
  is set using *`start_indices`*.
- ***"ends"*** —

  Determines the ending indices of the slice
  operation along the axes specified in *"axes"*. This parameter
  is set using *`end_indices`*.
- ***"steps"*** —

  Determines the step size for the slicing
  operation along the axes specified in *"axes"*.
  The parameter *"steps"* must either be an empty
  tuple or have the same length as *"axes"*. If it is empty, the
  *"steps"* are set to *1* for all *"axes"*.
  This parameter is set using *`steps`*.
- ***"axes"*** —

  Specifies the axes along which the slicing
  operation is performed. The axes are defined in the format WHC,
  representing Width, Height, and Channel and can also be
  specified as strings. Slicing in the Batch dimension is not supported.
  This parameter is set using *`axes`*.

The slice layer allows slicing a tensor along specified axes, providing
flexible adjustment options.
To ensure correct operations *"starts"* and *"ends"* must have
the same length as the parameter *"axes"*.
Negative values in *"starts"* and *"ends"* are adjusted by
adding the size of the corresponding array dimension, effectively allowing
negative indexing for one iteration. After that, negative values are clamped
to prevent further out-of-bounds slicing.

Negative values in *"axes"* are adjusted by adding the total number of
dimensions of the tensor to the respective axis.
Negative value means counting dimensions from the back.
The accepted range is [$-r$, $r-1$] where $r$ = rank.
For slicing to the end of a dimension with unknown size, it is recommended
to pass in H_INT_MAX when slicing forward and H_INT_MIN when slicing backward.

**Handling of axes and indices**

- **Adjusting axes** —

  Negative values in the *"axes"* parameter are made non-negative by
  adding the rank of the input tensor $r$ to each negative axis:
  $$\text{ax es}[i]\leftarrow\text{ax es}[i]+r\text{if ax es}[i]<0$$
- **Adjusting 'starts' and 'ends'** —
  - **Negative Index Adjustment** —

    Negative values in *"starts"* and *"ends"* are adjusted
    by adding the respective tensor dimension size:

    *"starts"*[$i$] is adjusted by adding the tensor dimension size.
    $$\text{starts}[i]\leftarrow\text{starts}[i]+\text{dims}[\text{ax es}[i]]\text{if starts}[i]<0$$

    *"ends"*[$i$] is adjusted by adding the respective tensor dimension size.
    $$\text{ends}[i]\leftarrow\text{ends}[i]+\text{dims}[\text{ax es}[i]]\text{if ends}[i]<0$$
  - **Clamping 'starts' Values** —

    Adjusted *"starts"* values are clamped to the range:

    $$\text{starts}[i]\in[0,\text{dims}[\text{ax es}[i]]]$$
  - **Clamping 'ends' Values** —

    Adjusted *"ends"* values are clamped based on the step direction:

    - Positive Stepping:
      *"ends"* is clamped to the range [0, dims].

      $$\text{if steps}[i]>0:\text{ends}[i]\in[0,\text{dims}[\text{ax es}[i]]]$$
    - Negative Stepping:
      *"ends"* is clamped to the range [-1, dims - 1].
      $$\text{if steps}[i]<0:\text{ends}[i]\in[-1,\text{dims}[\text{ax es}[i]]-1]$$

The following generic parameters *`gen_param_name`* and the corresponding
values *`gen_param_value`* are supported:

- ***"axes_format"*:** —

  Compatibility parameter that determines whether the specified *`axes`*
  are given in WHCN format (default) or in NCHW format.
  The parameter changes how the specified axes are interpreted.
  For example, with axis *1* and *"axes_format"*
  *"nchw"*, slicing is performed along depth.
  If *"axes_format"* is set to *"whcn"* or left unspecified,
  slicing is performed along height.
  Instead of indices, strings can also be used to specify the axes.

  List of values:
   *"nchw"*, *"whcn"*

  Default:
   *"whcn"*
- ***"is_inference_output"*:** —

  Determines whether [`apply_dl_model`](apply_dl_model.md) will include the output of this
  layer in the dictionary `dlresult_batch` even without specifying this
  layer in `outputs` (*"true"*) or not (*"false"*).

  List of values:
   *"true"*, *"false"*

  Default:
   *"false"*

Certain parameters of layers created using this operator
`create_dl_layer_slice` can be set and retrieved using
further operators.
The following tables give an overview, which parameters can be set
using [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and which ones can be retrieved
using [`get_dl_model_layer_param`](get_dl_model_layer_param.md) or [`get_dl_layer_param`](get_dl_layer_param.md). Note, the
operators [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and [`get_dl_model_layer_param`](get_dl_model_layer_param.md)
require a model created by [`create_dl_model`](create_dl_model.md).

| Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"input_layer"* (*`dllayer_input`*) |  | `x` |
| *"name"* (*`layer_name`*) | `x` | `x` |
| *"axes"* |  | `x` |
| *"starts"* |  | `x` |
| *"ends"* |  | `x` |
| *"steps"* |  | `x` |
| *"output_layer"* (*`dllayer_slice`*) |  | `x` |
| *"shape"* |  | `x` |
| *"type"* |  | `x` |

| Generic Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"is_inference_output"* | `x` | `x` |
| *"num_trainable_params"* |  | `x` |

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dllayer_input`** (input_control)  dl_layer `→` HHandle

Feeding layer.

Default:
"DLLayerInput"

**`layer_name`** (input_control)  string `→` str

Name of the output layer.

**`axes`** (input_control)  number(-array) `→` MaybeSequence[Union[int, str]]

Axes used for slicing.

Default:
0

Suggested values:
0, "width", 1, "height", 2, "depth"

**`start_indices`** (input_control)  number(-array) `→` MaybeSequence[int]

Starting indices of corresponding axes (inclusive).

Default:
0

**`end_indices`** (input_control)  number(-array) `→` MaybeSequence[int]

Ending indices of corresponding axes (exclusive).

Default:
1

**`steps`** (input_control)  number(-array) `→` MaybeSequence[int]

Slicing steps.

Default:
[]

**`gen_param_name`** (input_control)  attribute.name(-array) `→` MaybeSequence[str]

Generic input parameter names.

Default:
[]

List of values:
"axes_format", "is_inference_output"

**`gen_param_value`** (input_control)  attribute.value(-array) `→` MaybeSequence[Union[int, float, str]]

Generic input parameter values.

Default:
[]

Suggested values:
"true", "false", "nchw", "whcn"

**`dllayer_slice`** (output_control)  dl_layer `→` HHandle

Output layer.

## Module

Deep Learning Professional
