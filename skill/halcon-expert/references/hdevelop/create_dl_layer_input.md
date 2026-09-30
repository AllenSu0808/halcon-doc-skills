# create_dl_layer_input (Operator)

## Name

`create_dl_layer_input` — Create an input layer.

## Signature

`create_dl_layer_input( : : LayerName, Shape, GenParamName, GenParamValue : DLLayerInput)`

## Description

The operator `create_dl_layer_input` creates an input layer with
spatial dimensions given by *`Shape`* whose handle is returned in
*`DLLayerInput`*.

The parameter *`LayerName`* sets an individual layer name.
Note that if creating a model using [`create_dl_model`](create_dl_model.md) each layer of
the created network must have a unique name.

When the created model is applied using e.g., [`apply_dl_model`](apply_dl_model.md) or
[`train_dl_model_batch`](train_dl_model_batch.md), it must be possible to map an input with its
corresponding input layer.
Operators applying a model expect a feeding dictionary `DLSample`,
see [Deep Learning / Model](toc_deeplearning_model.md).
The mentioned mapping is done using dictionary entries, where the key
matches the input layer name. Thus, for an input of this layer a sample
dictionary will need an entry with the key *`LayerName`* (except if the
*'input_type'* is set to *'constant'*, see below).

The parameter *`Shape`* defines the shape of the input values (the
values given in the feeding dictionary `DLSample`) and
must be a tuple of length three, containing `width`,
`height`, and `depth` of the input. The tuple values must be
given as integer values and have have different meaning
depending on the input type:

- for an input image the layer *`Shape`* defines the image size.
  Images shall be given with type `real`
  (for information on image types see [Image](toc_image.md)).
- for an input tuple its length will need to match the product of the
  individual values in *`Shape`*, i.e., `width` $\times$
  `height` $\times$ `depth`.

  Tuple values are distributed along the column- (`width`), row-
  (`height`), and `depth`-axes in this order.
  Input tuple values can be given either as `integer` or `real`.

The batch size has to be set later with
[`set_dl_model_param`](set_dl_model_param.md), once the model has been created by
[`create_dl_model`](create_dl_model.md).

The following generic parameters *`GenParamName`* and the corresponding
values *`GenParamValue`* are supported:

- ***'allow_smaller_tuple'*:** —

  For tuple inputs, setting
  *'allow_smaller_tuple'* to *'true'* allows to have an
  input tuple with less values than the total dimension given by
  *`Shape`*.
  E.g., this can be the case if an input corresponds to the number of
  objects within one image and the number of objects changes from
  image to image. If fewer than the maximum number of values given
  by the total dimension of *`Shape`* are present, the
  remaining values are set to zero.

  *`Shape`* should be set such that it fits the maximum expected
  length. For the example above this would be the maximum number of
  objects within one image present in the whole dataset.

  Default:
   *'false'*.
- ***'const_val'*:** —

  Constant output value.

  Restriction:
  Only an integer or float is settable. This value is only settable or
  gettable if *'input_type'* is set to *'constant'*.

  Default:
   *0.0*.
- ***'input_type'*:** —

  Defines the type of input that is expected.
  The following values are possible:

  - ***'default'*:** —

    The layer expects a number of input images
    corresponding to the batch size.
  - ***'region_to_bin'*:** —

    The layer
    expects a tuple of regions as input and internally converts it to a
    binary image where each region is encoded in one depth channel. Regions
    reaching out of the given dimensions are clipped to the width and height
    given by *`Shape`*. The maximum number of regions is defined by the
    depth of *`Shape`*. If fewer than the maximum number of regions are
    given, the output is filled up with empty (zero) images. For example,
    this can be the case if the regions are corresponding to objects within
    an image and the number of objects changes from image to image.
  - ***'constant'*:** —

    The layer does
    not expect any key value pair in the input
    dictionary. Instead all entries within the output of this layer are
    filled with the value given by *'const_val'*.

  Default:
   *'default'*.
- ***'keep_batch_size_const'*:** —

  For constant inputs, this parameter can be set to *'true'*, if the
  input should always keep its batch size constant, independent from changing
  the model batch size.

  Default:
   *'false'*.
- ***'is_inference_output'*:** —

  Determines whether [`apply_dl_model`](apply_dl_model.md) will include the output of this
  layer in the dictionary `DLResultBatch` even without specifying this
  layer in `Outputs` (*'true'*) or not (*'false'*).

  Default:
   *'false'*

Certain parameters of layers created using `create_dl_layer_input`
can be set and retrieved using further operators.
The following tables give an overview, which parameters can be set
using [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and which ones can be retrieved
using [`get_dl_model_layer_param`](get_dl_model_layer_param.md) or [`get_dl_layer_param`](get_dl_layer_param.md). Note, the
operators [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and [`get_dl_model_layer_param`](get_dl_model_layer_param.md)
require a model created by [`create_dl_model`](create_dl_model.md).

| Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *'input_layer'* |  | `x` |
| *'name'* (*`LayerName`*) | `x` | `x` |
| *'output_layer'* (*`DLLayerInput`*) |  | `x` |
| *'shape'* (*`Shape`*) |  | `x` |
| *'type'* |  | `x` |

| Generic Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *'allow_smaller_tuple'* |  | `x` |
| *'const_val'* | `(x)` | `(x)` |
| *'input_type'* |  | `x` |
| *'keep_batch_size_const'* | `x` | `x` |
| *'is_inference_output'* | `x` | `x` |
| *'num_trainable_params'* |  | `x` |

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`LayerName`** (input_control)  string `→`  (string)

Name of the output layer.

**`Shape`** (input_control)  number-array `→`  (integer)

Dimensions of the input (width, height, depth).

Default:
[224,224,3]

**`GenParamName`** (input_control)  attribute.name(-array) `→`  (string)

Generic input parameter names.

Default:
[]

List of values:
'allow_smaller_tuple', 'const_val', 'input_type', 'is_inference_output', 'keep_batch_size_const'

**`GenParamValue`** (input_control)  attribute.value(-array) `→`  (string / integer / real)

Generic input parameter values.

Default:
[]

Suggested values:
0.0, 'constant', 'default', 'false', 'region_to_bin', 'true'

**`DLLayerInput`** (output_control)  dl_layer `→`  (handle)

Input layer.

## Example (HDevelop)

```
* Create a model for summation.
create_dl_layer_input ('input_a', [2, 3, 4], [], [], DLLayerInputA)
create_dl_layer_input ('input_b', [2, 3, 4], [], [], DLLayerInputB)
create_dl_layer_elementwise ([DLLayerInputA, DLLayerInputB], 'sum', \
                              'sum', [], [], [], DLLayerElementWise)
create_dl_model (DLLayerElementWise, DLModel)
set_dl_model_param (DLModel, 'runtime', 'cpu')
*
* Add 'input_a' as an inference model output.
set_dl_model_layer_param (DLModel, 'input_a', 'is_inference_output', 'true')
*
* Feed input data as tuple (a) or image (b).
create_dict (Sample)
set_dict_tuple (Sample, 'input_a', [1:(2*3*4)])
gen_empty_obj (InputB)
for I := 1 to 4 by 1
    gen_image_const (Channel, 'real', 2, 3)
    get_region_points (Channel, Rows, Cols)
    set_grayval (Channel, Rows, Cols, gen_tuple_const(|Rows|, I))
    append_channel (InputB, Channel, InputB)
endfor
set_dict_object (InputB, Sample, 'input_b')
*
* Apply the model for summation and get results.
set_dl_model_param (DLModel, 'batch_size', 2)
apply_dl_model (DLModel, [Sample,Sample], [], Result)
get_dict_object (Sum, Result[0], 'sum')
get_dict_object (TupleInputA, Result[1], 'input_a')
```

## Possible Successors

`create_dl_layer_activation`,
`create_dl_layer_batch_normalization`,
`create_dl_layer_class_id_conversion`,
`create_dl_layer_class_id_conversion`,
`create_dl_layer_concat`,
`create_dl_layer_convolution`,
`create_dl_layer_dense`,
`create_dl_layer_depth_max`,
`create_dl_layer_dropout`,
`create_dl_layer_elementwise`,
`create_dl_layer_loss_cross_entropy`,
`create_dl_layer_loss_ctc`,
`create_dl_layer_loss_distance`,
`create_dl_layer_loss_focal`,
`create_dl_layer_loss_huber`,
`create_dl_layer_lrn`,
`create_dl_layer_pooling`,
`create_dl_layer_reduce`,
`create_dl_layer_reshape`,
`create_dl_layer_softmax`,
`create_dl_layer_transposed_convolution`,
`create_dl_layer_zoom_factor`,
`create_dl_layer_zoom_size`,
`create_dl_layer_zoom_to_layer_size`

## Module

Deep Learning Professional
