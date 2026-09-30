# create_deep_ocr (Operator)

## Name

`create_deep_ocr` — Create a Deep OCR model.

## Signature

`def create_deep_ocr(gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[int, float, str]]) -> HHandle`

## Description

`create_deep_ocr` creates a Deep OCR model out of pretrained components
and returns its handle in *`deep_ocr_handle`*.
The handle states all parameters needed to run an inference.

A Deep OCR model usually consists of two components that are searched in the
directory `$HALCONROOT/dl/` by default:

- `'detection_model'`: detects words (connected characters) in
  the image.
- `'recognition_model'`: recognizes the word in the detected
  image part.

The following options may be set using *`gen_param_name`* and according
*`gen_param_value`*:

- ***"mode"*:** —

  Specify a mode and with it, which component is
  executed. Supported values:

  - ***"detection"*:** —

    Perform only the detection part.
    Hence, the model will merely localize the word regions within the image.
  - ***"recognition"*:** —

    Perform only the recognition part.
    The model expects a tight crop of a single word. If the alignment is
    enabled, the word crop can be wider, less precise and include background.
    Before the actual recognition, the alignment applies a transformation step
    to accurately position the word.
  - ***"auto"*:** —

    Perform both parts, detection of the words and their
    recognition.
  - ***"empty"*:** —

    This mode creates an empty Deep OCR model handle.
    Neither recognition nor detection model components are instantiated.
    Recognition and detection components can be set
    subsequently using [`set_deep_ocr_param`](set_deep_ocr_param.md).

  Default:
   *"auto"*.

The character set, which the model can recognize through its recognition
component, can be retrieved using [`get_deep_ocr_param`](get_deep_ocr_param.md) with
*"recognition_alphabet"*.

To get an overview of the Deep OCR workflow see [OCR / Deep OCR](toc_ocr_deepocr.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`gen_param_name`** (input_control)  attribute.name(-array) `→` MaybeSequence[str]

Name of the generic parameter.

Default:
[]

List of values:
"mode"

**`gen_param_value`** (input_control)  attribute.value(-array) `→` MaybeSequence[Union[int, float, str]]

Value of the generic parameter.

Default:
[]

List of values:
"auto", "detection", "empty", "recognition"

**`deep_ocr_handle`** (output_control)  deep_ocr `→` HHandle

Handle of the Deep OCR model.

## Result

If the parameters are valid, the operator `create_deep_ocr`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Successors

`write_deep_ocr`,
`apply_deep_ocr`,
`get_deep_ocr_param`,
`set_deep_ocr_param`

## Module

OCR/OCV
