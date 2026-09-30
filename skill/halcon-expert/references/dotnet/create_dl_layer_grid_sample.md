# CreateDlLayerGridSample (Operator)

## Name

`CreateDlLayerGridSample` — Create a grid sample layer.

## Signature

`static void HOperatorSet.CreateDlLayerGridSample(HTuple DLLayerInput, HTuple DLLayerGrid, HTuple layerName, HTuple genParamName, HTuple genParamValue, out HTuple DLLayerGridSample)`

`HDlLayer HDlLayer.CreateDlLayerGridSample(HDlLayer DLLayerGrid, string layerName, HTuple genParamName, HTuple genParamValue)`

`HDlLayer HDlLayer.CreateDlLayerGridSample(HDlLayer DLLayerGrid, string layerName, string genParamName, string genParamValue)`

## Description

The operator `CreateDlLayerGridSample` creates a grid sample layer,
which applies a spatial transformation to an input image or feature map.
The handle of the created grid sample layer is returned in
*`DLLayerGridSample`*.

A grid sample layer warps the input *`DLLayerInput`* based on a sampling
grid *`DLLayerGrid`*. This grid needs to specify spatially normalized
input pixel locations which are then used to interpolate the output values.
Pixel locations inside the input image or feature map must have values in
the range of $[-1,1]$.
Thus, the values $x=-1$, $y=-1$ must correspond to the
top-left pixel, while $x=1$, $y=1$ describe the bottom-right
pixel. Thereby, the extrema refer to the center points of the corner pixels.
The grid sample layer internally sets 'align_corners' to *1*, defining
the pixel centers as the grid reference points. The sampling grid
*`DLLayerGrid`* can be generated using [`CreateDlLayerAffineGrid`](create_dl_layer_affine_grid.md).

The grid sample layer uses bilinear interpolation to compute output values,
ensuring smooth transitions between pixel values.
For sampling grid locations outside of the input image or feature map the
corresponding values are set to 0.
The output of the grid sample layer has the same spatial dimensions as the input
grid.

The parameter *`layerName`* sets an individual layer name.
Note that if creating a model using [`CreateDlModel`](create_dl_model.md) each layer of
the created network must have a unique name.

The following generic parameters *`genParamName`* and the corresponding
values *`genParamValue`* are supported:

- ***"is_inference_output"*:** —

  Determines whether [`ApplyDlModel`](apply_dl_model.md) will include the output of this
  layer in the dictionary `DLResultBatch` even without specifying this
  layer in `outputs` (*"true"*) or not (*"false"*).

  List of values:
   *"true"*, *"false"*

  Default:
   *"false"*

Certain parameters of layers created using this operator
`CreateDlLayerGridSample` can be set and retrieved using
further operators.
The following tables give an overview, which parameters can be set
using [`SetDlModelLayerParam`](set_dl_model_layer_param.md) and which ones can be retrieved
using [`GetDlModelLayerParam`](get_dl_model_layer_param.md) or [`GetDlLayerParam`](get_dl_layer_param.md). Note, the
operators [`SetDlModelLayerParam`](set_dl_model_layer_param.md) and [`GetDlModelLayerParam`](get_dl_model_layer_param.md)
require a model created by [`CreateDlModel`](create_dl_model.md).

| Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"input_layer"* (*`DLLayerInput`*, *`DLLayerGrid`*) |  | `x` |
| *"name"* (*`layerName`*) | `x` | `x` |
| *"output_layer"* (*`DLLayerGridSample`*) |  | `x` |
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

**`DLLayerInput`** (input_control)  dl_layer `→` [HDlLayer](HDlLayer.md), [HTuple](HTuple.md) (*IntPtr*)

Input layer for image or feature map.

**`DLLayerGrid`** (input_control)  dl_layer `→` [HDlLayer](HDlLayer.md), [HTuple](HTuple.md) (*IntPtr*)

Input layer defining the sampling grid.

**`layerName`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Name of the output layer.

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

**`DLLayerGridSample`** (output_control)  dl_layer `→` [HDlLayer](HDlLayer.md), [HTuple](HTuple.md) (*IntPtr*)

Grid sample layer.

## Example (HDevelop)

```
read_image (Image, 'printer_chip/printer_chip_01')
convert_image_type (Image, Image, 'real')
get_image_size (Image, Width, Height)
* Create input layer for the image to be transformed.
create_dl_layer_input ('image', [Width,Height,1], [], [], DLLayerInputImage)
*
* Create an affine grid layer and define the size of its output grid with (Width/2, Height/2), which later
* determines the output image size.
create_dl_layer_input ('transformation', [3,2,1], [], [], DLLayerInputTransformation)
create_dl_layer_affine_grid (DLLayerInputTransformation, 'affine_grid', Width/2, Height/2, [], [], DLLayerAffineGrid)
*
* Create an affine transformation which represents a translation
* to the right by half the image width.
* As the affine grid layer uses normalized pixel positions in
* the range of [-1,1] the translation value must be normalized
* as well. Hence, translating by half the image width to the right
* corresponds to a translation value of -1 in x-direction.
hom_mat2d_identity (HomMat2DIdentity)
hom_mat2d_translate (HomMat2DIdentity, -1, 0, HomMat2DTranslate)
*
* Create grid sample layer with the affine grid as input
create_dl_layer_grid_sample (DLLayerInputImage, DLLayerAffineGrid, 'output', [], [], DLLayerGridSample)
*
* Create and apply dl model
create_dl_model (DLLayerGridSample, DLModelHandle)
DLSample := dict{image: Image, transformation: HomMat2DTranslate}
apply_dl_model (DLModelHandle, DLSample, [], DLResultBatch)
get_dict_object (ImageTranslated, DLResultBatch, 'output')
```

## Possible Predecessors

`CreateDlLayerAffineGrid`

## Module

Deep Learning Professional
