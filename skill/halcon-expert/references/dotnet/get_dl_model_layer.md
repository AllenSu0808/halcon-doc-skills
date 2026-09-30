# GetDlModelLayer (Operator)

## Name

`GetDlModelLayer` — Create a deep copy of the layers and all
of their graph ancestors in a given deep learning model.

## Signature

`static void HOperatorSet.GetDlModelLayer(HTuple DLModelHandle, HTuple layerNames, out HTuple DLLayers)`

`static HDlLayer[] HDlLayer.GetDlModelLayer(HDlModel DLModelHandle, HTuple layerNames)`

`void HDlLayer.GetDlModelLayer(HDlModel DLModelHandle, string layerNames)`

`HDlLayer[] HDlModel.GetDlModelLayer(HTuple layerNames)`

`HDlLayer HDlModel.GetDlModelLayer(string layerNames)`

## Description

The operator `GetDlModelLayer` creates a deep copy of every layer
named in *`layerNames`* and all their
graph ancestors in the deep learning model *`DLModelHandle`*.
You can retrieve the unique layer names using [`GetDlModelParam`](get_dl_model_param.md) with
its option *"summary"*.

You might use the output layers returned in *`DLLayers`* as inputs to
the `create_dl_layer_*` and [`CreateDlModel`](create_dl_model.md) operators in order
to create novel model architectures based on existing models.

If you want to get multiple layers of a single model, these layers have to be
specified as a *`layerNames`* tuple in a single call to
`GetDlModelLayer`. Doing so, you avoid multiple deep copies of graph
ancestors that are potentially shared by the layers.

*Example:*

|  |
| --- |
| `GetDlModelLayer(DLModelHandleOrig, ["layer_name_3", "layer_name_6"], DLLayersOutput)` |
| [`CreateDlModel([DLLayersOutput], DLModelHandle)`](create_dl_model.md) |

Please note, that the output layers are copies. They contain the same weights
and settings as in the given input model but they are unique copies.
You cannot alter the existing model by changing the output layers.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`DLModelHandle`** (input_control)  dl_model `→` [HDlModel](HDlModel.md), [HTuple](HTuple.md) (*IntPtr*)

Deep learning model.

**`layerNames`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Names of the layers to be copied.

**`DLLayers`** (output_control)  dl_layer(-array) `→` [HDlLayer](HDlLayer.md), [HTuple](HTuple.md) (*IntPtr*)

Copies of layers and all of their ancestors.

## Possible Predecessors

`ReadDlModel`

## Possible Successors

`CreateDlModel`,
`CreateDlLayerActivation`,
`CreateDlLayerBatchNormalization`,
`CreateDlLayerClassIdConversion`,
`CreateDlLayerClassIdConversion`,
`CreateDlLayerConcat`,
`CreateDlLayerConvolution`,
`CreateDlLayerDense`,
`CreateDlLayerDepthMax`,
`CreateDlLayerDropout`,
`CreateDlLayerElementwise`,
`CreateDlLayerLossCrossEntropy`,
`CreateDlLayerLossCtc`,
`CreateDlLayerLossDistance`,
`CreateDlLayerLossFocal`,
`CreateDlLayerLossHuber`,
`CreateDlLayerLrn`,
`CreateDlLayerPooling`,
`CreateDlLayerReduce`,
`CreateDlLayerReshape`,
`CreateDlLayerSoftmax`,
`CreateDlLayerTransposedConvolution`,
`CreateDlLayerZoomFactor`,
`CreateDlLayerZoomSize`,
`CreateDlLayerZoomToLayerSize`

## Module

Deep Learning Professional
