# create_dl_layer_pooling (Operator)

## Name

`create_dl_layer_pooling` — Create a pooling layer.

## Signature

`create_dl_layer_pooling( : : DLLayerInput, LayerName, KernelSize, Stride, Padding, Mode, GenParamName, GenParamValue : DLLayerPooling)`

## Description

The operator `create_dl_layer_pooling` creates a pooling layer whose
handle is returned in *`DLLayerPooling`*.

The parameter *`DLLayerInput`* determines the feeding input layer and
expects the layer handle as value.

The parameter *`LayerName`* sets an individual layer name.
Note that if creating a model using [`create_dl_model`](create_dl_model.md) each layer of
the created network must have a unique name.

The parameter *`KernelSize`* specifies the filter kernel in the
dimensions `width` and `height`.

The parameter *`Stride`* specifies how the filter is shifted.

The values for *`KernelSize`* and *`Stride`*
can be set as

- a single value which is used for both dimensions
- a tuple `[width, height]` and `[column, row]`,
  respectively.

The parameter *`Padding`* determines the padding, thus
how many pixels with value 0 are appended on the border of the
processed input image. Supported values are:

- *'half_kernel_size'*: The number of appended pixels
  depends on the specifies *`KernelSize`*.
  More precisely, it is calculated as
  $\mathrm{KernelSize/2}$ ![figure](../assets/8d4511858617714b.svg),
  where for the padding on the left / right border the value of
  *`KernelSize`* in dimension `width` is regarded
  and for the padding on the upper / lower border the value of
  *`KernelSize`* in `height`.
- *'implicit'*: No pixels are appended on the left
  or on the top of the input image. The number of pixels appended on the
  right or lower border of the input image is
  $\texttt{Stride}-(input\_dim-\texttt{KernelSize})%\texttt{Stride}$,
  or zero if the kernel size is a divisor of the input dimension.
  $input\_dim$
  stands for the input `width` or `height`.
- *'none'*: No pixels are appended.
- Number of pixels: Specify the number of pixels
  appended on each border. To do so, the following tuple lengths are
  supported:

  - Single number: Padding in all four directions
    left/right/top/bottom.
  - Two numbers: Padding in left/right and top/bottom:
    `[l/r, t/b]`.
  - Four numbers: Padding on left, right, top, bottom side:
    `[l,r,t,b]`.

    Restriction:
     *'runtime'* *'gpu'* does
    not support asymmetric padding, i.e., the padding values for the
    left and right side must be equal, as well as the padding values for
    the top and bottom side.

  Restriction:
   The integer padding values must be smaller
  than the value set for *`KernelSize`* in the corresponding dimension.

The output dimensions of the pooling layer are given by
$$output_dim = \left\lceil \dfrac{input_dim + padding\_begin + padding\_end - KernelSize}{Stride} \right\rceil + 1$$ ![figure](../assets/4c92739bbd22bdcd.svg)
Thereby we use the following values:
$output\_dim$: output width,
$input\_dim$: input width,
$padding\_begin$: number of pixels added to the left/top of
the input image, and
$padding\_end$: number of pixels added to the right/bottom of
the input image.

The parameter *`Mode`* specifies the mode of the pooling operation.
Supported modes are:

- ***'average'*:** —

  The resulting pixel value is the average of
  all pixel values in the filter.
- ***'maximum'*:** —

  The resulting pixel value is the maximum of
  all pixel values in the filter.
- ***'global_average'*:** —

  Same as mode *'average'*, but
  without the knowledge of the spatial dimensions of the input, it is
  possible to define the desired output dimensions via the parameter
  *`KernelSize`*. E.g., if the average over all pixel values of the
  input shall be returned, set the *`KernelSize`* to *1* and the
  output `width` and `height` is equal to 1.
  The internally used kernel size and stride are calculated as follows:

  - If *`KernelSize`* is a divisor of the input dimensions:
    The internally used kernel size and stride are both set to the value
    $input\_dim/\texttt{KernelSize}$.
  - If *`KernelSize`* is not a divisor of the input dimension:
    The calculation of the internally used kernel size and stride depend on
    the generic parameter *'global_pooling_mode'*:

    - ***'overlapping'*:** —

      The internally used $stride$
      is set to
      ![figure](../assets/0a2dd61c51f670ae.svg).
      The internally used kernel size is then computed as
      $input\_dim-(\texttt{KernelSize}-1)\cdot stride$. This leads
      to overlapping kernels but the whole input image is taken into account
      for the computation of the output.
    - ***'non_overlapping'*:** —

      The internally used kernel size and
      stride are set to the same value ![figure](../assets/0a2dd61c51f670ae.svg). This leads to
      non-overlapping pooling kernels, but parts of the input image at the
      right or bottom border might not be considered when computing the
      output. In this mode, due to rounding the output size is not always
      equal to the size given by *`KernelSize`*.
    - ***'adaptive'*:** —

      In this mode, for each pixel
      $(k,l)$ of the output, the size of the corresponding pooling
      area within the input is computed adaptively, where $k$ are the
      row and $l$ are the column indices of the output. The row
      indices of the pooling area for pixels of the $k$-th output row
      are given by
      $\left[ k\cdot input\_dim/KernelSize , (k+1) \cdot input\_dim/KernelSize \right]$ ![figure](../assets/e139e3e82e9fad4a.svg), where
      in this case the height of the *`KernelSize`* is used. The
      computation of the column coordinates is done analogously. This means
      that neighboring pooling areas can have a different size which can lead
      to a less efficient implementation. However, the pooling areas are only
      overlapping by one pixel which is generally less overlap than for
      *'global_pooling_mode'* *'overlapping'*. The whole input
      image is taken into account for the computation of the output. For this
      mode, the parameter *`Padding`* must be set to *'none'*.

  For this mode the parameter *`Stride`* is ignored and calculated
  internally as described above.
- ***'global_maximum'*:** —

  Same as mode *'global_average'*,
  but the maximum is calculated instead of the average.

For more information about the pooling layer see the
`“Solution Guide on Classification”`.

The following generic parameters *`GenParamName`* and the corresponding
values *`GenParamValue`* are supported:

- ***'global_pooling_mode'*:** —

  Mode for calculation of the internally
  used kernel size and stride in case of global pooling (*`Mode`*
  *'global_average'* or *'global_maximum'*). See description
  above. In case of a non-global pooling the parameter is set to the value
  *'undefined'*.

  Default:
   *'overlapping'*
- ***'is_inference_output'*:** —

  Determines whether [`apply_dl_model`](apply_dl_model.md) will include the output of this
  layer in the dictionary `DLResultBatch` even without specifying
  this layer in `Outputs` (*'true'*) or not
  (*'false'*).

  Default:
   *'false'*

Certain parameters of layers created using this operator
`create_dl_layer_pooling` can be set and retrieved using
further operators.
The following tables give an overview, which parameters can be set
using [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and which ones can be retrieved
using [`get_dl_model_layer_param`](get_dl_model_layer_param.md) or [`get_dl_layer_param`](get_dl_layer_param.md). Note,
the operators [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and
[`get_dl_model_layer_param`](get_dl_model_layer_param.md) require a model created by
[`create_dl_model`](create_dl_model.md).

| Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *'global'* |  | `x` |
| *'global_pooling_mode'* |  | `x` |
| *'input_layer'* (*`DLLayerInput`*) |  | `x` |
| *'kernel_size'* (*`KernelSize`*) |  | `x` |
| *'name'* (*`LayerName`*) | `x` | `x` |
| *'output_layer'* (*`DLLayerPooling`*) |  | `x` |
| *'padding'* (*`Padding`*) |  | `x` |
| *'padding_type'* (*`Padding`*) |  | `x` |
| *'pooling_mode'* (*`Mode`*) |  | `x` |
| *'shape'* |  | `x` |
| *'stride'* (*`Stride`*) |  | `x` |
| *'type'* |  | `x` |

| Generic Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *'is_inference_output'* | `x` | `x` |
| *'num_trainable_params'* |  | `x` |

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DLLayerInput`** (input_control)  dl_layer `→`  (handle)

Feeding layer.

**`LayerName`** (input_control)  string `→`  (string)

Name of the output layer.

**`KernelSize`** (input_control)  number-array `→`  (integer)

Width and height of the filter kernels.

Default:
[2,2]

**`Stride`** (input_control)  number-array `→`  (integer)

Bi-dimensional amount of filter shift.

Default:
[2,2]

**`Padding`** (input_control)  number(-array) `→`  (string / integer)

Padding type or specific padding size.

Default:
'none'

Suggested values:
'none', 'half_kernel_size', 'implicit'

**`Mode`** (input_control)  number `→`  (string)

Mode of pooling operation.

Default:
'maximum'

List of values:
'average', 'global_average', 'global_maximum', 'maximum'

**`GenParamName`** (input_control)  attribute.name(-array) `→`  (string)

Generic input parameter names.

Default:
[]

List of values:
'global_pooling_mode', 'is_inference_output'

**`GenParamValue`** (input_control)  attribute.value(-array) `→`  (string / integer / real)

Generic input parameter values.

Default:
[]

Suggested values:
'adaptive', 'non_overlapping', 'overlapping', 'true', 'false', 1.0, 0.9, 0.0

**`DLLayerPooling`** (output_control)  dl_layer `→`  (handle)

Pooling layer.

## Module

Deep Learning Professional
