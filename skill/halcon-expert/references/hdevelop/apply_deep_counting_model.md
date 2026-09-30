# apply_deep_counting_model (Operator)

## Name

`apply_deep_counting_model` — Apply a Deep Counting model on a set of images for inference.

## Signature

`apply_deep_counting_model(Image : : DeepCountingHandle : Count, DeepCountingResult)`

## Description

`apply_deep_counting_model` applies the Deep Counting model given by
*`DeepCountingHandle`* on the tuple of input images *`Image`*.
A tuple with the number of found instances per input image is
returned in *`Count`*.
Additional information about the counted instances is returned in
*`DeepCountingResult`*, which contains a tuple of dictionaries,
again one per input image.
Note that templates of the objects to be counted must be set
beforehand using [`prepare_deep_counting_model`](prepare_deep_counting_model.md).
Note that the inference time of `apply_deep_counting_model` depends
on the number of defined templates in [`prepare_deep_counting_model`](prepare_deep_counting_model.md).

Please see the chapter [Matching / Deep Counting](toc_matching_deepcounting.md)
for further information.

The procedure `dev_display_deep_count_results` can be used to
visualize the detected instances.

The settings *'min_score'* and *'max_overlap'*
can be used to set the minimum similarity of the instances
to the templates as well as the allowed overlap of instances.
Details can be found in [`get_deep_counting_model_param`](get_deep_counting_model_param.md).

The dictionary returned in *`DeepCountingResult`* contains
additional information about the detected and counted object instances.
It contains the following keys, where each key contains a tuple of values,
one for each detection. If no instances were detected, i.e. the count
is *0*, those tuples are empty.

- ***'area'*:** —

  Approximate area of the detected templates in pixels.
- ***'row'*, *'column'*:** —

  Approximate location in row and column coordinates of the instances in
  the input image.
- ***'score'*:** —

  Similarity score of the detected instances, i.e., their approximate
  similarity with the most similar template provided to
  [`prepare_deep_counting_model`](prepare_deep_counting_model.md).
- ***'template_index'*:** —

  Index of the template with the highest similarity to the detected
  instance.
  This can be used to find out which templates were counted.
- ***'angle'*, *'scale'*:** —

  The angle and scale of the template with the highest similarity
  to the detected instance.
  If rotational or scale augmentations were enabled during the call of
  [`prepare_deep_counting_model`](prepare_deep_counting_model.md), these values can be used
  to find out which rotation angle and scale creates a template that is
  most similar to the detected instance.

## Attention

Deep Counting does not take into account whether an image has
a reduced domain.

System requirements:
To run this operator on GPU (see [`get_deep_counting_model_param`](get_deep_counting_model_param.md)),
cuDNN and cuBLAS are required.
For further details, please refer to the `“Installation Guide”`,
paragraph “Requirements for Deep Learning and Deep-Learning-Based Methods”.
Alternatively, this operator can also be run on CPU.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte / real)

Input image.

**`DeepCountingHandle`** (input_control)  deep_counting `→`  (handle)

Handle of the Deep Counting model.

**`Count`** (output_control)  integer(-array) `→`  (integer)

Number of counted objects.

**`DeepCountingResult`** (output_control)  dict(-array) `→`  (handle)

Tuple of result dictionaries.

## Result

If the parameters are valid, the operator `apply_deep_counting_model`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_deep_counting_model`,
`set_deep_counting_model_param`,
`get_deep_counting_model_param`,
`prepare_deep_counting_model`

## See also

`prepare_deep_counting_model`

## Module

Matching
