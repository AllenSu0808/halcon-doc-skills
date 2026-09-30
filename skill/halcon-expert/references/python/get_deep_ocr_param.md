# get_deep_ocr_param (Operator)

## Name

`get_deep_ocr_param` — Return the parameters of a Deep OCR model.

## Signature

`def get_deep_ocr_param(deep_ocr_handle: HHandle, gen_param_name: str) -> Sequence[HTupleElementType]`

`def get_deep_ocr_param_s(deep_ocr_handle: HHandle, gen_param_name: str) -> HTupleElementType`

## Description

`get_deep_ocr_param` returns the parameter values
*`gen_param_value`* of *`gen_param_name`* for the Deep OCR model
*`deep_ocr_handle`*.

Parameters can apply to the whole model or be specific for a given component.
The following table gives an overview, which parameters can be set and
which ones retrieved as well as for which model part they apply.

| *`gen_param_name`* | Model | Det. comp. | Recog. comp. |
| --- | --- | --- | --- |
| *"device"* | $\texttt{s}$ | $\texttt{s}$ | $\texttt{s}$ |
| *"detection_device"* | $-$ | $\texttt{s g}$ | $-$ |
| *"detection_image_dimensions"* | $-$ | $\texttt{g}$ | $-$ |
| *"detection_image_height"* | $-$ | $\texttt{s g}$ | $-$ |
| *"detection_image_size"* | $-$ | $\texttt{s g}$ | $-$ |
| *"detection_image_width"* | $-$ | $\texttt{s g}$ | $-$ |
| *"detection_min_character_score"* | $-$ | $\texttt{s g}$ | $-$ |
| *"detection_min_link_score"* | $-$ | $\texttt{s g}$ | $-$ |
| *"detection_min_word_area"* | $-$ | $\texttt{s g}$ | $-$ |
| *"detection_min_word_score"* | $-$ | $\texttt{s g}$ | $-$ |
| *"detection_model"* | $-$ | $\texttt{s g}$ | $-$ |
| *"detection_optimize_for_inference"* | $-$ | $\texttt{s g}$ | $-$ |
| *"detection_orientation"* | $-$ | $\texttt{s g}$ | $-$ |
| *"detection_sort_by_line"* | $-$ | $\texttt{s g}$ | $-$ |
| *"detection_tiling"* | $-$ | $\texttt{s g}$ | $-$ |
| *"detection_tiling_overlap"* | $-$ | $\texttt{s g}$ | $-$ |
| *"recognition_alignment"* | $-$ | $-$ | $\texttt{s g}$ |
| *"recognition_alignment_available"* | $-$ | $-$ | $\texttt{g}$ |
| *"recognition_alphabet"* | $-$ | $-$ | $\texttt{s g}$ |
| *"recognition_alphabet_internal"* | $-$ | $-$ | $\texttt{s g}$ |
| *"recognition_alphabet_mapping"* | $-$ | $-$ | $\texttt{s g}$ |
| *"recognition_batch_size"* | $-$ | $-$ | $\texttt{s g}$ |
| *"recognition_device"* | $-$ | $-$ | $\texttt{s g}$ |
| *"recognition_image_dimensions"* | $-$ | $-$ | $\texttt{g}$ |
| *"recognition_image_height"* | $-$ | $-$ | $\texttt{g}$ |
| *"recognition_image_num_channels"* | $-$ | $-$ | $\texttt{g}$ |
| *"recognition_image_width"* | $-$ | $-$ | $\texttt{s g}$ |
| *"recognition_model"* | $-$ | $-$ | $\texttt{s g}$ |
| *"recognition_num_char_candidates"* | $-$ | $-$ | $\texttt{s g}$ |
| *"recognition_optimize_for_inference"* | $-$ | $-$ | $\texttt{s g}$ |
|  |

Thereby, the symbols and abbreviations denote the following :

- 's': The parameter can be set using [`set_deep_ocr_param`](set_deep_ocr_param.md).
- 'g': The parameter can be retrieved using `get_deep_ocr_param`.
- '-': The parameter is not applicable.
- Model: Entire Deep OCR model with all its components.
- Det. comp.: Detection component.
- Recog. comp.: Recognition component.

Only parameters that do not change the model architecture can be set after
the model has been optimized with [`optimize_dl_model_for_inference`](optimize_dl_model_for_inference.md).
A list of these parameters can be found at
[`optimize_dl_model_for_inference`](optimize_dl_model_for_inference.md).
In the following the parameters are described, sorted according to the part
of the model they apply to:

- **Entire model:** —
  - ***"device"*:** —

    Handle of the device on which the model will be executed.
    To get a tuple of handles of all available potentially Deep-OCR-capable
    compute devices use [`query_available_dl_devices`](query_available_dl_devices.md).

    Note, the device can be reset for an individual component, in which case
    only the possibly remaining part of the model (e.g., the remaining
    component) will be executed on the device of this handle.

    Default:
     Handle of the default device, thus the GPU with index
    *0* when querying a list using [`get_system`](get_system.md)
    with *"cuda_devices"*.
    If no device is available, this is an empty tuple.
- **Detection component:** —
  - ***"detection_device"*:** —

    This parameter will set the device on which the detection component of
    the Deep OCR model is executed. For a further description, see
    *"device"*.

    Default:
     The same value as for *"device"*.
  - ***"detection_image_dimensions"*:** —

    Tuple containing the image dimensions (*"detection_image_width"*,
    *"detection_image_height"*, number of channels) the detection
    component will process.

    The input image is scaled to *"detection_image_dimensions"*
    such that the original aspect ratio is preserved. The scaled image
    is padded with gray value *0* if necessary. Therefore, changing
    the *"detection_image_height"* or *"detection_image_width"*
    can influence the results.

    The number of channels must always be 3.

    Default:
     [*1024*, *1024*, *3*]
  - ***"detection_image_height"*:** —

    Height of the images the detection component will process.
    This means, the network preserves the aspect ratio of the input image by
    scaling it to a maximum of this height before processing it. Thus this size
    can influence the results.

    The model architecture requires that the height is a multiple of 32. If
    this is not the case, the height is rounded up to the nearest integer
    multiple of 32.

    Suggested values:
     *768*, *1024*, *1280*

    Default:
     *1024*
  - ***"detection_image_size"*:** —

    Tuple containing the image size (*"detection_image_width"*,
    *"detection_image_height"*) the detection component will
    process.

    Default:
     [*1024*, *1024*]
  - ***"detection_image_width"*:** —

    Width of the images the detection component will process.
    This means, the network preserves the aspect ratio of the input image by
    scaling it to a maximum of this width before processing it. Thus this size
    can influence the results.

    The model architecture requires that the width is a multiple of 32. If
    this is not the case, the width is rounded up to the nearest integer
    multiple of 32.

    Suggested values:
     *768*, *1024*, *1280*

    Default:
     *1024*
  - ***"detection_min_character_score"*:** —

    The parameter *"detection_min_character_score"* specifies the lower
    threshold used for the character score map to estimate the dimensions of
    the characters.
    By adjusting the parameter, suggested instances can be split up or
    neighboring instances can be merged.

    Value range:
     $\in[\textit{0},\textit{1}]$.

    Default:
     *0.5*
  - ***"detection_min_link_score"*:** —

    The parameter *"detection_min_link_score"* defines the minimum link
    score required between two localized characters to recognize these
    characters as coherent word.

    Value range:
     $\in[\textit{0},\textit{1}]$.

    Default:
     *0.3*
  - ***"detection_min_word_area"*:** —

    The parameter *"detection_min_word_area"* defines the minimum size
    that a localized word must have in order to be suggested.
    This parameter can be used to filter suggestions that are too small.

    Value range:
     $\ge\textit{0}$.

    Default:
     *10*.
  - ***"detection_min_word_score"*:** —

    The parameter *"detection_min_word_score"* defines the minimum
    score a localized instance must contain to be suggested as valid word.
    With this parameter uncertain words can be filtered out.

    Value range:
     $\in[\textit{0},\textit{1}]$.

    Default:
     *0.7*
  - ***"detection_model"*:** —

    The operator `get_deep_ocr_param` returns the handle of the Deep
    OCR model component for word detection.
    Using [`set_deep_ocr_param`](set_deep_ocr_param.md), it is possible to either specify a handle,
    filename or special string.
    *"default"* loads the default pretrained word
    detection component *"pretrained_deep_ocr_detection.hdl"*.
    *"compact"* loads the compact word detection
    component *"pretrained_deep_ocr_detection_compact.hdl"*,
    which offers faster inference while providing slightly lower
    accuracy compared to the default component.
    Any other string is treated as a model filename and loaded internally
    with batch size set to *1*.

    Please note that changing the detection component can also affect
    other model-specific parameters.

    Suggested values:
     *"default"*, *"compact"*

    Default:
     *"default"*
  - ***"detection_optimize_for_inference"*:** —

    Defines whether the detection component is optimized for inference.

    This parameter applies the behavior of [`get_dl_model_param`](get_dl_model_param.md) with
    parameter *"optimize_for_inference"* on the detection component.
  - ***"detection_orientation"*:** —

    This parameter allows to set a predefined orientation angle for the word
    detection. To revert to default behavior using the internal orientation
    estimation, *"detection_orientation"* is set to *"auto"*.

    Value range:
     $(-\pi,\pi]$.

    Default:
     *"auto"*
  - ***"detection_sort_by_line"*:** —

    The words are sorted line-wise based on the orientation of the localized
    word instances. If the parameter *"detection_sort_by_line"* is
    set to *"false"*, the results will not be sorted.

    Default:
     *"true"*
  - ***"detection_tiling"*:** —

    The input image is automatically split into overlapping tile images of
    size *"detection_image_size"*, which are processed separately by
    the detection component. This allows processing images that are much
    larger than the actual *"detection_image_size"* without having to
    zoom the input image.
    Thus, if *"detection_tiling"* = {'true'}, the input image will
    not be zoomed before processing it.

    Default:
     *"false"*
  - ***"detection_tiling_overlap"*:** —

    This parameter defines how much neighboring tiles overlap when input
    images are split (see *"detection_tiling"*). The overlap
    is given in pixels.

    Value range:
     $\ge\textit{0}$.

    Default:
     *64*
- **Recognition component:** —
  - ***"recognition_alignment"*:** —

    This parameter specifies whether word alignment is performed
    prior to recognizing the text. Enabling this feature (*"true"*)
    improves the recognition accuracy for inaccurately cropped words.
    Therefore, it can be used in scenarios where the position of the text
    within the image is only approximately known.

    The parameter *"recognition_alignment"* can only be set to
    *"true"* if the recognition component includes word alignment.
    To check whether the model supports alignment, use the parameter
    *"recognition_alignment_available"*.

    Note that in contrast to recognition of tightly cropped words,
    aligned recognition requires to be trained with samples containing
    real image backgrounds around the words. In this manner, the model
    learns to suppress false readings in the background which can be
    present after aligning inaccurately cropped words.

    List of values:
     *"true"*, *"false"*

    Default:
     *"false"*
  - ***"recognition_alignment_available"*:** —

    This parameter indicates whether the recognition component contains
    word alignment functionality. If it returns *"true"*, it means
    that word alignment can be enabled using the parameter
    *"recognition_alignment"*.

    List of values:
     *"true"*, *"false"*
  - ***"recognition_alphabet"*:** —

    The character set that can be recognized by the Deep OCR model.

    It contains all characters that are not mapped to the Blank character
    of the internal alphabet (see parameters
    *"recognition_alphabet_mapping"*
    and *"recognition_alphabet_internal"*).

    The alphabet can be changed or extended if needed. Changing the
    alphabet with this parameter will edit the internal alphabet and
    mapping in such a way that it tries to keep the length of the internal
    alphabet unchanged.
    After changing the alphabet, it is recommended to retrain the model on
    application specific data (see the HDevelop example
    `deep_ocr_recognition_training_workflow.hdev`).
    Previously unknown characters will need more training data.

    Note, that if the length of the internal alphabet changes, the last
    model layers have to be randomly initialized and thus the output of the
    model will be random strings (see
    *"recognition_alphabet_internal"*). In that case it is required to
    retrain the model.
  - ***"recognition_alphabet_internal"*:** —

    The full character set which the Deep OCR recognition component has
    been trained on.

    The first character of the internal alphabet is a special character.
    In the pretrained model this character is specified as Blank
    (U+2800) and is not to be confused with a space.
    The Blank is never returned in a word output but can occur in the
    reported character candidates. It is required and cannot be omitted.
    If the internal alphabet is changed, the first character has to be
    the Blank.
    Furthermore, if *"recognition_alphabet"* is used to change
    the alphabet, the Blank symbol is added automatically to the
    character set.

    The length of this tuple corresponds to the depth of the last
    convolution layer in the model. If the length changes, the last
    convolution layer and all layers after it have to be resized and
    potentially reinitialized randomly. After such a change, it is required
    to retrain the model (see HDevelop example
    `deep_ocr_recognition_training_workflow.hdev`).

    It is recommend to use the parameter *"recognition_alphabet"* to
    change the alphabet, as it will automatically try to preserve the
    length of the internal alphabet.
  - ***"recognition_alphabet_mapping"*:** —

    Tuple of integer indices.

    It is a mapping that is applied by the model during the decoding step
    of each word. The mapping overwrites a character of
    *"recognition_alphabet_internal"* with
    the character at the specified index in
    *"recognition_alphabet_internal"*.

    In the decoding step each prediction is mapped according to the index
    specified in this tuple.
    The tuple has to be of same length as the tuple
    *"recognition_alphabet_internal"*. Each integer index of the
    mapping has to be within *0* and
    |*"recognition_alphabet_internal"*|-1.

    In some applications it can be helpful to map certain characters onto
    other characters. E.g. if only numeric words occur in an application it
    might be helpful to map the character "O" to the "0" character
    without the need to retrain the model.

    If an entry contains a *0*, the corresponding character in
    *"recognition_alphabet_internal"* will not be decoded in the
    word.
  - ***"recognition_batch_size"*:** —

    Number of images in a batch that is transferred to device memory and
    processed in parallel in the recognition component. For further
    details, please refer to the reference documentation of
    [`apply_dl_model`](apply_dl_model.md) with respect to the parameter
    *"batch_size"*. This parameter can be used to optimize the
    runtime of [`apply_deep_ocr`](apply_deep_ocr.md) on a given dl device. If the
    recognition component has to process multiple inputs (words),
    processing multiple inputs in parallel can result in a faster execution
    of [`apply_deep_ocr`](apply_deep_ocr.md). Note, however, that a higher
    *"recognition_batch_size"* will require more device memory.

    Default:
     *1*
  - ***"recognition_device"*:** —

    This parameter will set the device on which the recognition component of
    the Deep OCR model is executed. For a further description, see
    *"device"*.

    Default:
     The same value as for *"device"*.
  - ***"recognition_image_dimensions"*:** —

    Tuple containing the image dimensions (*"recognition_image_width"*,
    *"recognition_image_height"*, number of channels)
    the recognition component will process.

    This means, the network will first zoom the input image part to
    *"recognition_image_height"* while maintaining the aspect ratio
    of the input. If the width of the resulting image is smaller than
    *"recognition_image_width"*, the image part is padded with
    gray value *0* on the right. If it is larger, the image is
    zoomed to *"recognition_image_width"*.

    The number of channels must always be 1.

    Default:
     [*120*, *32*, *1*]
  - ***"recognition_image_height"*:** —

    Height of the images the recognition component will process.

    Default:
     *32*
  - ***"recognition_image_num_channels"*:** —

    Number of image channels the recognition component will process.

    Default:
     *1*
  - ***"recognition_image_width"*:** —

    Width of the images the recognition component will process.

    Default:
     *120*
  - ***"recognition_model"*:** —

    The operator `get_deep_ocr_param` returns the handle of the Deep
    OCR model component for word recognition.

    Using [`set_deep_ocr_param`](set_deep_ocr_param.md), it is possible to either specify a handle,
    filename or special string.
    *"default"* loads the default pretrained word
    recognition component *"pretrained_deep_ocr_recognition.hdl"*.
    *"compact"* loads the compact word recognition
    component *"pretrained_deep_ocr_recognition_compact.hdl"*,
    which offers faster inference while providing slightly lower
    accuracy compared to the default component.
    Any other string is treated as a model filename and loaded internally
    with batch size set to *1*.

    Please note that changing the recognition component can also affect
    other model-specific parameters.

    Suggested values:
     *"default"*, *"compact"*

    Default:
     *"default"*
  - ***"recognition_num_char_candidates"*:** —

    Controls the number of reported character candidates in the result of the
    operator [`apply_deep_ocr`](apply_deep_ocr.md).

    Default:
     *3*
  - ***"recognition_optimize_for_inference"*:** —

    Defines whether the recognition component is optimized for inference.

    This parameter applies the behavior of [`get_dl_model_param`](get_dl_model_param.md) with
    parameter *"optimize_for_inference"* on the recognition component.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`deep_ocr_handle`** (input_control)  deep_ocr `→` HHandle

Handle of the Deep OCR model.

**`gen_param_name`** (input_control)  attribute.name `→` str

Name of the generic parameter.

Default:
"recognition_model"

List of values:
"detection_device", "detection_image_dimensions", "detection_image_height", "detection_image_size", "detection_image_width", "detection_min_character_score", "detection_min_link_score", "detection_min_word_area", "detection_min_word_score", "detection_model", "detection_optimize_for_inference", "detection_orientation", "detection_sort_by_line", "detection_tiling", "detection_tiling_overlap", "recognition_alignment", "recognition_alignment_available", "recognition_alphabet", "recognition_alphabet_internal", "recognition_alphabet_mapping", "recognition_batch_size", "recognition_device", "recognition_image_dimensions", "recognition_image_height", "recognition_image_num_channels", "recognition_image_width", "recognition_model", "recognition_num_char_candidates", "recognition_optimize_for_inference"

**`gen_param_value`** (output_control)  attribute.value(-array) `→` Sequence[HTupleElementType]

Value of the generic parameter.

## Result

If the parameters are valid, the operator `get_deep_ocr_param`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_deep_ocr`,
`set_deep_ocr_param`

## Possible Successors

`set_deep_ocr_param`,
`apply_deep_ocr`

## See also

`set_deep_ocr_param`

## Module

OCR/OCV
