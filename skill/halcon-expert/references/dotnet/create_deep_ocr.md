# CreateDeepOcr (Operator)

## Name

`CreateDeepOcr` — Create a Deep OCR model.

## Signature

`static void HOperatorSet.CreateDeepOcr(HTuple genParamName, HTuple genParamValue, out HTuple deepOcrHandle)`

`public HDlModelOcr(HTuple genParamName, HTuple genParamValue)`

`public HDlModelOcr(string genParamName, string genParamValue)`

`void HDlModelOcr.CreateDeepOcr(HTuple genParamName, HTuple genParamValue)`

`void HDlModelOcr.CreateDeepOcr(string genParamName, string genParamValue)`

## Description

`CreateDeepOcr` creates a Deep OCR model out of pretrained components
and returns its handle in *`deepOcrHandle`*.
The handle states all parameters needed to run an inference.

A Deep OCR model usually consists of two components that are searched in the
directory `$HALCONROOT/dl/` by default:

- `'detection_model'`: detects words (connected characters) in
  the image.
- `'recognition_model'`: recognizes the word in the detected
  image part.

The following options may be set using *`genParamName`* and according
*`genParamValue`*:

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
    subsequently using [`SetDeepOcrParam`](set_deep_ocr_param.md).

  Default:
   *"auto"*.

The character set, which the model can recognize through its recognition
component, can be retrieved using [`GetDeepOcrParam`](get_deep_ocr_param.md) with
*"recognition_alphabet"*.

To get an overview of the Deep OCR workflow see [OCR / Deep OCR](toc_ocr_deepocr.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Name of the generic parameter.

Default:
[]

List of values:
"mode"

**`genParamValue`** (input_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Value of the generic parameter.

Default:
[]

List of values:
"auto", "detection", "empty", "recognition"

**`deepOcrHandle`** (output_control)  deep_ocr `→` [HDlModelOcr](HDlModelOcr.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the Deep OCR model.

## Result

If the parameters are valid, the operator `CreateDeepOcr`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Successors

`WriteDeepOcr`,
`ApplyDeepOcr`,
`GetDeepOcrParam`,
`SetDeepOcrParam`

## Module

OCR/OCV
