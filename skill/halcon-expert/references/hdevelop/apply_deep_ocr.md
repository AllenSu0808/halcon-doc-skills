# apply_deep_ocr (Operator)

## Name

`apply_deep_ocr` — Apply a Deep OCR model on a set of images for inference.

## Signature

`apply_deep_ocr(Image : : DeepOcrHandle, Mode : DeepOcrResult)`

## Description

`apply_deep_ocr` applies the Deep OCR model given by
*`DeepOcrHandle`* on the tuple of input images *`Image`*.
The operator returns *`DeepOcrResult`*, a tuple with a result
dictionary for every input image.

The operator `apply_deep_ocr` poses requirements on the input
*`Image`*:

- Image type: byte.
- Number of channels: 1 or 3.

Further, the operator `apply_deep_ocr` will preprocess the given
*`Image`* to match the model specifications.
This means, the byte images will be normalized and converted to type real.
Further, for *`Mode`* = *'auto'* or *'detection'*
the input image *`Image`* is padded to the model input dimensions and,
in case it has only one channel, converted into a three-channel image.
For *`Mode`* = *'recognition'*, three-channel images are
automatically converted to single-channel images.

The parameter *`Mode`* specifies a mode and with it, which component is
executed. Supported values:

- ***'auto'* (A):** —

  Perform both parts, detection of the word and its
  recognition.
- ***'detection'* (DET):** —

  Perform only the detection part.
  Hence, the model will merely localize the word regions within the image.
- ***'recognition'* (REC):** —

  Perform only the recognition part.
  The model expects a tight crop of a single word. If the alignment is
  enabled, the word crop can be wider, less precise and include background.
  Before the actual recognition, the alignment applies a transformation step
  to accurately position the word.

Note, the model must have been created with the desired component, see
[`create_deep_ocr`](create_deep_ocr.md).

The output dictionary *`DeepOcrResult`* can have entries according to the
applied *`Mode`* (marked by its abbreviation):

- **`image` (A, DET, REC):** —

  Preprocessed image.
- **`image_aligned` (REC):** —

  Aligned word image if
  *'recognition_alignment'* is *'true'*.
- **`score_maps` (A, DET):** —

  Scores given as image with four channels:

  - Character score: Score for the character detection.
  - Link score: Score for the connection of detected character centers to
    a connected word.
  - Orientation 1: Sine component of the predicted word orientation.
  - Orientation 2: Cosine component of the predicted word orientation.
- **`words` (A, DET):** —

  Dictionary containing the following entries.
  Thereby, the entries are tuples with a value for every found word.

  - `word` (A): Recognized word.
  - `char_candidates` (A):
    A dictionary with information for every character of every recognized
    word. The dictionary contains for every word a key/value pair: The
    index of the word as key and a tuple of dictionaries as value. Each of
    these character dictionaries contains the following key/value
    pairs:

    - `'candidate'`: Tuple with the best
      *'recognition_num_char_candidates'* candidates.
    - `'confidence'`: Softmax based confidence values of the
      best candidates. Note, these values are not calibrated and should
      be used with care. They can vary significantly for different models.
  - `word_image` (A): Preprocessed image part containing the word.
  - `word_image_aligned` (A): Aligned image part containing the
    word if *'recognition_alignment'* is *'true'*.
  - `row` (A, DET): Localized word: Center point, row coordinate.
  - `col` (A, DET): Localized word: Center point, column
    coordinate.
  - `phi` (A, DET): Localized word: Angle phi.
  - `length1` (A, DET): Localized word: Half length of edge 1.
  - `length2` (A, DET): Localized word: Half length of edge 2.
  - `line_index` (A, DET): Line index of localized word if
    *'detection_sort_by_line'* set to *'true'*.

  The word localization is given by the parameters of an oriented rectangle,
  see [`gen_rectangle2`](gen_rectangle2.md) for further information.
- **`word_boxes_on_image` (A, DET):** —

  Dictionary with the word
  localization on the coordinate system of the preprocessed images placed in
  `image`. The entries are tuples with a value for every found word.

  - `row` (A, DET): Localized word: Center point, row coordinate.
  - `col` (A, DET): Localized word: Center point, column
    coordinate.
  - `phi` (A, DET): Localized word: Angle phi.
  - `length1` (A, DET): Localized word: Half length of edge 1.
  - `length2` (A, DET): Localized word: Half length of edge 2.

  The word localization is given by the parameters of an oriented rectangle,
  see [`gen_rectangle2`](gen_rectangle2.md) for further information.
- **`word_boxes_on_score_maps` (A, DET):** —

  Dictionary with the word
  localization on the coordinate system of the score images placed in
  `score_maps`. The entries are the same as for
  `word_boxes_on_image` above.
- **`word` (REC):** —

  Recognized word.
- **`char_candidates` (REC):** —

  A tuple of dictionaries with information for every character in the
  recognized word.

  Each of these character dictionaries contains the following key/value pairs:

  - `'candidate'`: Tuple with the best
    *'recognition_num_char_candidates'* candidates.
  - `'confidence'`: Softmax based confidence values of the best
    candidates. Note, these values are not calibrated and should be used
    with care. They can vary significantly for different models.

The recognition component can be retrained with custom data in order to
further enhance the performance. See [OCR / Deep OCR](toc_ocr_deepocr.md) for more
information.

## Attention

System requirements:
To run this operator on GPU (see [`get_deep_ocr_param`](get_deep_ocr_param.md)), cuDNN and cuBLAS
are required.
For further details, please refer to the `“Installation Guide”`,
paragraph “Requirements for Deep Learning and Deep-Learning-Based Methods”.
Alternatively, this operator can also be run on CPU.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

This operator supports canceling timeouts and interrupts.

This operator supports breaking timeouts and interrupts.

## Parameters

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte)

Input image.

**`DeepOcrHandle`** (input_control)  deep_ocr `→`  (handle)

Handle of the Deep OCR model.

**`Mode`** (input_control)  string `→`  (string)

Inference mode.

Default:
[]

List of values:
'auto', 'detection', 'recognition'

**`DeepOcrResult`** (output_control)  dict(-array) `→`  (handle)

Tuple of result dictionaries.

## Result

If the parameters are valid, the operator `apply_deep_ocr`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`get_deep_ocr_param`,
`set_deep_ocr_param`,
`create_deep_ocr`

## Module

OCR/OCV
