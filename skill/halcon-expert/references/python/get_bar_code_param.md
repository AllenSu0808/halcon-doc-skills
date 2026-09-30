# get_bar_code_param (Operator)

## Name

`get_bar_code_param` — Get one or several parameters that describe the bar code model.

## Signature

`def get_bar_code_param(bar_code_handle: HHandle, gen_param_name: MaybeSequence[str]) -> Sequence[Union[float, int, str]]`

`def get_bar_code_param_s(bar_code_handle: HHandle, gen_param_name: MaybeSequence[str]) -> Union[float, int, str]`

## Description

The operator `get_bar_code_param` allows to query parameters
of a bar code model, which are of relevance for a successful search and
decoding of a respective class of bar codes.

The names of the desired parameters are passed in the generic
parameter *`gen_param_name`* and the corresponding values are
returned in *`gen_param_value`*.
All of these parameters can be set and changed at any time with the
operator [`set_bar_code_param`](set_bar_code_param.md).

Parameters that have been set bar code type specifically by
[`set_bar_code_param_specific`](set_bar_code_param_specific.md) or by automatic parameter training
cannot be read with `get_bar_code_param`, but must
be read with [`get_bar_code_param_specific`](get_bar_code_param_specific.md). All parameters listed
with the operator [`get_bar_code_param_specific`](get_bar_code_param_specific.md) can always
be set specifically. Which parameters are actually set specifically can be
determined at runtime with the operator [`query_bar_code_params`](query_bar_code_params.md).

The following parameters can be queried - ordered by different
categories:

**Size of the bar code elements:**

- ***"element_size_min"*:** —

  Minimum size of the base bar code elements, i.e.,
  the minimum width of the narrowest bars and spaces for the specific
  bar code type.
- ***"element_size_max"*:** —

  Maximum size of the base bar code elements, i.e.,
  the maximum width of the narrowest bars and spaces for the specific
  bar code type.
- ***"element_size_variable"*:** —

  Specifies if the element size varies across a single bar code.
- ***"barcode_height_min"*:** —

  Minimum height of the bar code.
- ***"barcode_width_min"*:** —

  Minimum bar code width.
- ***"barcode_width_max"*:** —

  Maximum bar code width.

**Scanning settings:**

- ***"num_scanlines"*:** —

  Maximum number of scans per (candidate) bar code.
- ***"min_identical_scanlines"*:** —

  Minimum number of decoded scanlines which return
  identical data to read the bar code successfully.
- ***"majority_voting"*:** —

  Decode result selection mode. Specifies whether majority voting is used
  in the selection of different scanline results.
- ***"stop_after_result_num"*:** —

  Number of successfully decoded bar codes after which the decoding
  will stop. *0* is the default where the reader tries
  to decode all candidates.
- ***"orientation"*:** —

  Accepted orientation of the decoded bar codes.
- ***"orientation_tol"*:** —

  Tolerance of the accepted orientation.
- ***"quiet_zone"*:** —

  Quiet zone verification mode.
- ***"start_stop_tolerance"*:** —

  Start/Stop search criteria tolerance.
- ***"min_code_length"*:** —

  Minimum number of decoded characters.
- ***"max_code_length"*:** —

  Maximum number of decoded characters.
- ***"merge_scanlines"*:** —

  Determines whether merged scanlines are computed if not enough scanlines
  could be decoded individually. Thus, occluded or damaged bar codes can
  be read.

**Appearance of the bar code in the image:**

- ***"meas_thresh"*:** —

  Relative threshold for the detection of edges in the bar code region.
- ***"meas_thresh_abs"*:** —

  Absolute threshold for the detection of edges in the bar code region.
- ***"contrast_min"*:** —

  Minimum contrast between the foreground and the background of the bar
  code elements.

**Print quality inspection-specific values:**

- ***"quality_isoiec15416_reflectance_reference"*:** —

  Reference gray value to normalize the reflectances used to assess the
  quality grades Symbol Contrast, Minimum Reflectance, and
  Minimum Edge Contrast.

**Values that only apply to certain code types:**

- ***"check_char"*:** —

  Handling of an optional check character.
- ***"composite_code"*:** —

  Presence and type of a 2D composite code appended to the bar code.
- ***"upce_encodation"*:** —

  Output format for UPC-E bar codes (with number system 0 or 1).
- ***"upce1_enable"*:** —

  Enables the decoding of UPC-E bar codes with number system 1.
- ***"strict_ean13_upc_a"*:** —

  Defines the distinction of EAN-13 and UPC-A codes.

**Miscellaneous:**

- ***"timeout"*:** —

  Timeout for [`find_bar_code`](find_bar_code.md)
- ***"persistence"*:** —

  Persistence mode of the bar code model.
- ***"train"*:** —

  Returns the *names* of the trained parameters. The returned
  tuple can be passed as *`gen_param_name`* to a further call to
  `get_bar_code_param` to get the *values* of the trained
  parameters.

Further details on these parameters can be found with the
description of the operator [`set_bar_code_param`](set_bar_code_param.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`bar_code_handle`** (input_control)  barcode `→` HHandle

Handle of the bar code model.

**`gen_param_name`** (input_control)  attribute.name(-array) `→` MaybeSequence[str]

Names of the generic parameters that are to be
queried for the bar code model.

Default:
"element_size_min"

List of values:
"barcode_height_min", "barcode_width_max", "barcode_width_min", "check_char", "composite_code", "contrast_min", "element_size_max", "element_size_min", "element_size_variable", "majority_voting", "max_code_length", "meas_thresh", "meas_thresh_abs", "merge_scanlines", "min_code_length", "min_identical_scanlines", "num_scanlines", "orientation", "orientation_tol", "persistence", "quality_isoiec15416_reflectance_reference", "quiet_zone", "small_elements_robustness", "start_stop_tolerance", "stop_after_result_num", "strict_ean13_upc_a", "timeout", "train", "upce1_enable", "upce_encodation"

**`gen_param_value`** (output_control)  attribute.name(-array) `→` Sequence[Union[float, int, str]]

Values of the generic parameters.

## Result

The operator `get_bar_code_param` returns the value 2 (
H_MSG_TRUE)
if the
given parameters are correct. Otherwise, an exception will be raised.

## Possible Predecessors

`create_bar_code_model`,
`set_bar_code_param`

## Possible Successors

`set_bar_code_param`

## Alternatives

`get_bar_code_param_specific`

## Module

Bar Code
