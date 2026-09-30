# get_deep_counting_model_param (Operator)

## Name

`get_deep_counting_model_param` — Return the parameters of a Deep Counting model.

## Signature

`get_deep_counting_model_param( : : DeepCountingHandle, GenParamName : GenParamValue)`

## Description

The operator `get_deep_counting_model_param` returns the parameter values
of *`GenParamName`* for the Deep Counting model *`DeepCountingHandle`*
in *`GenParamValue`*.

Note that when changing parameters that influence the template creation,
[`prepare_deep_counting_model`](prepare_deep_counting_model.md) must be called again before
the model can be applied with [`apply_deep_counting_model`](apply_deep_counting_model.md).
The following table gives an overview,
which parameters can be set
using [`set_deep_counting_model_param`](set_deep_counting_model_param.md) or [`create_deep_counting_model`](create_deep_counting_model.md)
(`set`),
which can be retrieved using `get_deep_counting_model_param`
(`get`),
and which require re-running [`prepare_deep_counting_model`](prepare_deep_counting_model.md) after
changing them (`prepare`).

| *`GenParamName`* | `set` | `get` | Requires `prepare` |
| --- | --- | --- | --- |
| *'angle_start'* | `x` | `x` | `x` |
| *'angle_step'* | `x` | `x` | `x` |
| *'angle_end'* | `x` | `x` | `x` |
| *'backbone_model'* | `x` | `x` | `x` |
| *'device'* | `x` | `x` | `x` |
| *'max_overlap'* | `x` | `x` |  |
| *'min_score'* | `x` | `x` |  |
| *'scale_max'* | `x` | `x` | `x` |
| *'scale_min'* | `x` | `x` | `x` |
| *'scale_step'* | `x` | `x` | `x` |

In the following the parameters are described:

- ***'angle_start'*, *'angle_step'*, *'angle_end'*:** —

  Control the rotational augmentation.
  Templates passed to [`prepare_deep_counting_model`](prepare_deep_counting_model.md) are rotated from
  *'angle_start'* to *'angle_end'* in steps of
  *'angle_step'*.
  This allows [`apply_deep_counting_model`](apply_deep_counting_model.md) to better find rotated
  instances of the templates.

  The angles must be passed in radians.

  Suggested values:
   *0*, *-6.28*,
  *-3.14*, *3.14*, *6.28*

  Default:
   *'angle_start'* = *0*,
  *'angle_end'* = *0*,
  *'angle_step'* = *'rad(30)'*

  Restriction:
  $-2\pi$ <= *'angle_start'* <= *'angle_end'* <= $2\pi$,
  *'angle_step'* > *0*
- ***'backbone_model'*:** —

  The backbone used for the detection of the templates.
  The backbone is automatically created by [`create_deep_counting_model`](create_deep_counting_model.md).
  It can be obtained and written back in order to, for example,
  optimize it using [`optimize_dl_model_for_inference`](optimize_dl_model_for_inference.md).

  Note that the Deep Counting model will automatically set the input
  size of the backbone according to the template and image sizes.
  It has therefore no effect to change the backbone's input size,
  and it is not recommended to do so.
  Also note that the backbone can not be used for any other deep learning
  methods besides Deep Counting.
- ***'device'*:** —

  Handle of the device on which the backbone will be
  executed.

  If the backbone was already optimized for a device, setting
  *'device'* might not be necessary anymore, see
  [`optimize_dl_model_for_inference`](optimize_dl_model_for_inference.md) for details.

  To get a tuple of handles of all available potentially deep-learning
  capable hardware devices use [`query_available_dl_devices`](query_available_dl_devices.md).

  Default:
   Handle of the default device, thus the GPU with index
  *0*. If not available, this is an empty tuple.
- ***'max_overlap'*:** —

  The maximum allowed intersection over union (IoU) for two detected
  templates during counting.
  When two templates have an IoU higher than *'max_overlap'*,
  the one with lower confidence value gets suppressed.
  When set to *0*, no overlap at all is allowed.
  We refer to the chapter [Deep Learning / Advanced Object Detection](toc_deeplearning_objectdetection.md) for
  further explanations of the IoU.

  Suggested values:
   *0.3*, *0.5*,
  *0.7*, *1.0*

  Default:
   *'max_overlap'* = *0.5*

  Restriction:
   *0* <= *'max_overlap'* <= *1*
- ***'min_score'*:** —

  This parameter determines the minimum similarity of detected instances
  to the original templates.
  In other words, [`apply_deep_counting_model`](apply_deep_counting_model.md) ignores all detected
  instances with a similarity smaller than this value.
  The similarity computed by the Deep Counting model lies between
  *0* and *1*, where *0* means no similarity and
  *1* is a very high similarity.

  Suggested values:
   *0.2*, *0.3*,
  *0.4*, *0.5*

  Default:
   *'min_score'* = *0.4*

  Restriction:
   *0* < *'min_score'* <= *1*
- ***'scale_min'*, *'scale_step'*, *'scale_max'*:** —

  Control the scale augmentation.
  Templates passed to [`prepare_deep_counting_model`](prepare_deep_counting_model.md) are scaled from
  *'scale_min'* to *'scale_max'* in steps of
  *'scale_step'*.
  This allows [`apply_deep_counting_model`](apply_deep_counting_model.md) to better find scaled
  instances of the templates.

  Suggested values:
   *0.9*, *1.0*, *1.1*

  Default:
   *'scale_min'* = *1.0*,
  *'scale_max'* = *1.0*,
  *'scale_step'* = *0.1*

  Restriction:
   *0* < *'scale_min'* <= *'scale_max'*,
  *'scale_step'* > *0*

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DeepCountingHandle`** (input_control)  deep_counting `→`  (handle)

Handle of the Deep Counting model.

**`GenParamName`** (input_control)  attribute.name `→`  (string)

Name of the generic parameter.

Default:
'angle_start'

List of values:
'angle_end', 'angle_start', 'angle_step', 'backbone_model', 'device', 'max_overlap', 'min_score', 'scale_max', 'scale_min', 'scale_step'

**`GenParamValue`** (output_control)  attribute.name `→`  (real / string / integer)

Value of the generic parameter.

## Result

If the handle of the model is valid, the operator
`get_deep_counting_model_param` returns the value 2 (
H_MSG_TRUE)
. If necessary
an exception is raised.

## Possible Predecessors

`create_deep_counting_model`,
`set_deep_counting_model_param`,
`read_deep_counting_model`

## Possible Successors

`apply_deep_counting_model`

## See also

`set_deep_counting_model_param`

## Module

Matching
