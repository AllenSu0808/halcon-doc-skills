# GetDlModelLayerGradients (Operator)

## Name

`GetDlModelLayerGradients` — Get the gradients of a Deep Learning model layer.

## Signature

`static void HOperatorSet.GetDlModelLayerGradients(out HObject gradients, HTuple DLModelHandle, HTuple layerName)`

`HImage HDlModel.GetDlModelLayerGradients(string layerName)`

## Description

The operator `GetDlModelLayerGradients` returns in *`gradients`* the
gradients of the specified *`layerName`* of the model
*`DLModelHandle`*.

*`gradients`* is a tuple of `batch_size` many objects,
where every object is an image having the size
(`width`, `height`, `depth`) of the given *`layerName`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`gradients`** (output_object)  image(-array) `→` [HImage](HImage.md) (real)

Output gradients.

**`DLModelHandle`** (input_control)  dl_model `→` [HDlModel](HDlModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the deep learning model.

**`layerName`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Name of the layer to be queried.

## Module

Deep Learning Professional
