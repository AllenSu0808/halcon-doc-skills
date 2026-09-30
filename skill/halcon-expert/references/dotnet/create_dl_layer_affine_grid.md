# CreateDlLayerAffineGrid (Operator)

## Name

`CreateDlLayerAffineGrid` — Create an affine grid layer.

## Signature

`static void HOperatorSet.CreateDlLayerAffineGrid(HTuple DLLayerInput, HTuple layerName, HTuple width, HTuple height, HTuple genParamName, HTuple genParamValue, out HTuple DLLayerAffineGrid)`

`HDlLayer HDlLayer.CreateDlLayerAffineGrid(string layerName, int width, int height, HTuple genParamName, HTuple genParamValue)`

`HDlLayer HDlLayer.CreateDlLayerAffineGrid(string layerName, int width, int height, string genParamName, string genParamValue)`

## Description

The operator `CreateDlLayerAffineGrid` creates an affine grid layer
which returns a 2D sampling grid parameterized by an affine transformation matrix.
The handle of the affine grid layer is returned in *`DLLayerAffineGrid`*.
Usually, sampling grids are fed into grid sample layers to apply affine
transformations to images or feature maps, see [`CreateDlLayerGridSample`](create_dl_layer_grid_sample.md).

The parameter *`DLLayerInput`* determines the feeding input layer and
expects the layer handle as value. The input consists of a batch of 2D affine
transformation matrices (Height = 2, Width = 3). They are passed in the format WHC,
representing Width, Height, and Channel, where Channel must always be 1.
See [`AffineTransImageSize`](affine_trans_image_size.md) for more information about affine
transformations.

The parameter *`layerName`* sets an individual layer name.
Note that if creating a model using [`CreateDlModel`](create_dl_model.md) each layer of
the created network must have a unique name.

The parameters *`width`* and *`height`* define the output size.
Given a batch of N affine transformation input matrices, the affine grid layer
returns a batch of sampling grids of dimension (*`height`*, *`width`*, 2)
in the format CHW representing Channel, Height, and Width.

For an affine transformation matrix
$$\begin{bmatrix}a & b & c\\ d & e & f\end{bmatrix}$$ ![figure](../assets/a185031d016577fc.svg)
a point $(x,y)$ in an image of size (*`width`*, *`height`*)
is mapped to $(x^{\prime},y^{\prime})$ by

$$\begin{pmatrix} x' \\ y' \\ 1 \end{pmatrix} = \begin{pmatrix} a & b & c \\ d & e & f \\ 0 & 0 & 1 \end{pmatrix} \cdot \begin{pmatrix} x \\ y \\ 1 \end{pmatrix}$$ ![figure](../assets/115a65ae3c1a984b.svg)
where $x$ refers to the column coordinate and $y$ to the row
coordinate. Hence, for the affine input matrix of a batch ($b$), the
output tensor values $(b,y,x,0)$ and
$(b,y,x,1)$ corresponds to the column and row values
$x^{\prime}$ and $y^{\prime}$ of the point $(x,y)$ after
transformation.

The sampling grid locations $(x,y)$ are normalized by the spatial
dimensions *`width`* and *`height`* to get values in the range of
$[-1,1]$. Thus, the values $x=-1$, $y=-1$
correspond to the top-left pixel, while $x=1$, $y=1$ describe
the bottom-right pixel. Thereby, the extrema refer to the center points of
the corner pixels.

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
`CreateDlLayerAffineGrid` can be set and retrieved using
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
| *"grid_size"* (*`width`*, *`height`*) |  | `x` |
| *"output_layer"* (*`DLLayerAffineGrid`*) |  | `x` |
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

Input layer for a batch of affine transformation matrices of shape [3,2,1].

**`layerName`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Name of the output layer.

**`width`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Width of the returned grid.

Default:
256

**`height`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Height of the returned grid.

Default:
256

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

**`DLLayerAffineGrid`** (output_control)  dl_layer `→` [HDlLayer](HDlLayer.md), [HTuple](HTuple.md) (*IntPtr*)

Affine grid layer.

## Example (HDevelop)

```
* Create affine grid layer for images of size (3,5).
create_dl_layer_input ('input', [3,2,1], [], [], DLLayerInput)
create_dl_layer_affine_grid (DLLayerInput, 'affine_grid', 5, 3, ['is_inference_output'], ['true'], DLLayerAffineGrid)
*
* Create an affine transformation which represents a translation
* to the right by one pixel.
* As the affine grid layer uses normalized pixel positions in
* the range of [-1,1] the translation value must be normalized
* as well. For Width = 5 the normalized column values are
* [-1, -0.5, 0.0, 0.5, 1.0]. Hence, translating by one pixel
* to the right corresponds to a translation value of 0.5 in
* x-direction.
hom_mat2d_identity (HomMat2DIdentity)
hom_mat2d_translate (HomMat2DIdentity, 0.5, 0, HomMat2DTranslate)
*
* For better visualization add permutation layer to get an
* output image of size (3,5) where the first channel describes
* the transformed (normalized) column coordinates and the second
* channel describes the transformed (normalized) row coordinates.
create_dl_layer_permutation (DLLayerAffineGrid, 'permute', ['height','depth','width','batch'], [], [], DLLayerPermutation)
*
* Create and apply dl model
create_dl_model (DLLayerPermutation, DLModelHandle)
DLSample := dict{input: HomMat2DTranslate}
apply_dl_model (DLModelHandle, DLSample, [], DLResultBatch)
```

## Possible Predecessors

`CreateDlLayerInput`

## Possible Successors

`CreateDlLayerGridSample`,
`CreateDlLayerPermutation`

## See also

`AffineTransImageSize`

## Module

Deep Learning Professional
