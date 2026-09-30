# CreateDlLayerClassIdConversion (Operator)

## Name

`CreateDlLayerClassIdConversion` — Create a class ID conversion layer.

## Signature

`static void HOperatorSet.CreateDlLayerClassIdConversion(HTuple DLLayerInput, HTuple layerName, HTuple conversionMode, HTuple genParamName, HTuple genParamValue, out HTuple DLLayerClassIdConversion)`

`HDlLayer HDlLayer.CreateDlLayerClassIdConversion(string layerName, string conversionMode, HTuple genParamName, HTuple genParamValue)`

`HDlLayer HDlLayer.CreateDlLayerClassIdConversion(string layerName, string conversionMode, string genParamName, string genParamValue)`

## Description

The operator `CreateDlLayerClassIdConversion` creates a class ID
conversion layer whose handle is returned in *`DLLayerClassIdConversion`*.
The layer converts between the IDs used internally by the network and the
target / output class IDs.

The network internally uses consecutive integer values starting from 0
as IDs (the number of values depends on the model type). In case
the target / output class IDs differ from the internal IDs, this layer
can be used to convert between them. The target / output class IDs are
stored in the model parameter *"class_ids"* (see
[`GetDlModelParam`](get_dl_model_param.md) for more information on this parameter).
If no *"class_ids"* are set, this layer copies the input to the
output.

The parameter *`conversionMode`* specifies the conversion direction
and accepts the following values:

- *"from_class_id"*: Convert target / output class IDs into
  internal IDs.
  This mode is typically used after a target input layer.
- *"to_class_id"*: Convert internal IDs into target / output
  class IDs.
  This mode is typically used after an inference output layer.

The parameter *`DLLayerInput`* determines the feeding input layer and
expects the layer handle as value.

The parameter *`layerName`* sets an individual layer name.
Note that if creating a model using [`CreateDlModel`](create_dl_model.md) each layer of
the created network must have a unique name.

The following generic parameters *`genParamName`* and the corresponding
values *`genParamValue`* are supported:

- ***"is_inference_output"*:** —

  Determines whether [`ApplyDlModel`](apply_dl_model.md) will include the output of this
  layer in the dictionary `DLResultBatch` even without specifying this
  layer in `outputs` (*"true"*) or not (*"false"*).

  Default:
   *"false"*

Certain parameters of layers created using this operator
`CreateDlLayerClassIdConversion` can be set and retrieved using
further operators.
The following tables give an overview, which parameters can be set
using [`SetDlModelLayerParam`](set_dl_model_layer_param.md) and which ones can be retrieved
using [`GetDlModelLayerParam`](get_dl_model_layer_param.md) or [`GetDlLayerParam`](get_dl_layer_param.md). Note, the
operators [`SetDlModelLayerParam`](set_dl_model_layer_param.md) and [`GetDlModelLayerParam`](get_dl_model_layer_param.md)
require a model created by [`CreateDlModel`](create_dl_model.md).

| Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"input_layer"* (*`DLLayerInput`*) |  | `x` |
| *"name"* (*`layerName`*) | `x` | `x` |
| *"output_layer"* (*`DLLayerClassIdConversion`*) |  | `x` |
| *"shape"* |  | `x` |
| *"to_class_id"* (*`conversionMode`*) |  | `x` |
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

**`DLLayerInput`** (input_control)  dl_layer `→` [HDlLayer](HDlLayer.md), [HTuple](HTuple.md) (*IntPtr*)

Feeding layer.

**`layerName`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Name of the output layer.

**`conversionMode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Direction of the class ID conversion.

Default:
"from_class_id"

List of values:
"from_class_id", "to_class_id"

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Generic input parameter names.

Default:
[]

List of values:
"is_inference_output"

**`genParamValue`** (input_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Generic input parameter values.

Default:
[]

Suggested values:
"true", "false"

**`DLLayerClassIdConversion`** (output_control)  dl_layer `→` [HDlLayer](HDlLayer.md), [HTuple](HTuple.md) (*IntPtr*)

Class IDs conversion layer.

## Example (HDevelop)

```
* Example demonstrating the usage of
* create_dl_layer_class_id_conversion.
*
dev_update_off ()
set_system ('seed_rand', 42)
*
* Create simple segmentation model.
NumClasses := 3
InputShape := [32, 32, 3]
*
* Input feeding layers.
create_dl_layer_input ('image', InputShape, [], [], DLLayerInput)
create_dl_layer_input ('target', [InputShape[0],InputShape[1],1], [], [], \
                       DLLayerTarget)
create_dl_layer_class_id_conversion (DLLayerTarget, 'target_internal', \
                                     'from_class_id', [], [], \
                                     DLLayerTargetInternal)
* Feature extraction layers.
create_dl_layer_convolution (DLLayerInput, 'conv1', 3, 1, 1, 32, 1, \
                             'half_kernel_size', 'relu', [], [], \
                             DLLayerConv1)
create_dl_layer_convolution (DLLayerConv1, 'conv2', 3, 1, 1, 32, 1, \
                             'half_kernel_size', 'relu', [], [], \
                             DLLayerConv2)
* Output generation layers.
create_dl_layer_convolution (DLLayerConv2, 'conv_final', 1, 1, 1, \
                             NumClasses, 1, 'none', 'none', [], [], \
                             DLLayerConvFinal)
create_dl_layer_softmax (DLLayerConvFinal, 'softmax', [], [], \
                          DLLayerSoftMax)
create_dl_layer_depth_max (DLLayerSoftMax, 'output_internal', \
                           'argmax', [], [], DLLayerOutputInternal, _)
create_dl_layer_class_id_conversion (DLLayerOutputInternal, 'output', \
                                     'to_class_id', [], [], DLLayerOutput)
* Loss layer.
create_dl_layer_loss_cross_entropy (DLLayerSoftMax, DLLayerTargetInternal, \
                                    [], 'loss', 1.0, [], [], DLLayerLoss)
*
* Create the model.
create_dl_model ([DLLayerOutput, DLLayerLoss], DLModelHandle)
set_dl_model_param (DLModelHandle, 'type', 'segmentation')
set_dl_model_param (DLModelHandle, 'runtime', 'cpu')
*
* Test model on dummy example data.
read_image (Image, 'claudia')
zoom_image_size (Image, Image, InputShape[0], InputShape[1], 'constant')
convert_image_type (Image, Image, 'real')
*
* Fill target image with specific target class IDs.
ClassIDs := [42, 17, 5]
gen_image_const (Target, 'real', InputShape[0], InputShape[1])
paint_region (Target, Target, Target, ClassIDs[0], 'fill')
gen_rectangle1 (RectClass1, 1, 3, 16, 27)
paint_region (RectClass1, Target, Target, ClassIDs[1], 'fill')
gen_rectangle1 (RectClass2, 19, 1, 30, 30)
paint_region (RectClass2, Target, Target, ClassIDs[2], 'fill')
*
* Set class IDs in the model.
set_dl_model_param (DLModelHandle, 'class_ids', ClassIDs)
*
* Create test sample.
create_dict (DLSample)
set_dict_object (Image, DLSample, 'image')
set_dict_object (Target, DLSample, 'target')
*
* Train model for a few iterations. Note that training would not
* work without the first class ID conversion layer 'target_internal'.
for Idx := 1 to 100 by 1
    train_dl_model_batch (DLModelHandle, DLSample, DLTrainResult)
endfor
*
* Apply model on test image. With the second class ID conversion
* layer 'output', the image now contains values according to the
* target IDs in segmentation_image.
apply_dl_model (DLModelHandle, DLSample, [], DLApplyResult)
get_dict_object (SegmentationImage, DLApplyResult, 'output')
dev_display (SegmentationImage)
```

## Module

Deep Learning Professional
