# create_bar_code_model (Operator)

## Name

`create_bar_code_model` — Create a model of a bar code reader.

## Signature

`def create_bar_code_model(gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[float, int, str]]) -> HHandle`

## Description

The operator `create_bar_code_model` creates a generic model for
reading all types of supported bar code symbols. The result of this operator
is a handle to the bar code model (*`bar_code_handle`*), which is used
for all further operations on the bar code, like modifying the model,
reading a symbol, or accessing the results of the symbol search.

In general, bar codes will be found and decoded without any additional
adjustment of the parameters. Therefore, *`gen_param_name`* and
*`gen_param_value`* are empty tuples by default. In the case of poor
image quality or abnormal geometric characteristics of the bar code,
which requires special parameter settings for a successful decoding of
the bar code symbols, parameters can be adjusted already while creating
the bar code model. Alternatively, parameters can be changed later on as
well by applying the operator [`set_bar_code_param`](set_bar_code_param.md) or
[`set_bar_code_param_specific`](set_bar_code_param_specific.md). For a detailed
description of the available model parameters see [`set_bar_code_param`](set_bar_code_param.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`gen_param_name`** (input_control)  attribute.name(-array) `→` MaybeSequence[str]

Names of the generic parameters that can be
adjusted for the bar code model.

Default:
[]

List of values:
"barcode_height_min", "barcode_width_max", "barcode_width_min", "check_char", "composite_code", "element_size_max", "element_size_min", "element_size_variable", "max_code_length", "meas_thresh", "meas_thresh_abs", "min_code_length", "min_identical_scanlines", "num_scanlines", "orientation", "orientation_tol", "persistence", "quiet_zone", "start_stop_tolerance", "stop_after_result_num", "timeout", "train", "upce1_enable", "upce_encodation"

**`gen_param_value`** (input_control)  attribute.value(-array) `→` MaybeSequence[Union[float, int, str]]

Values of the generic parameters that can be
adjusted for the bar code model.

Default:
[]

Suggested values:
0, 0.1, 1, 1.5, 2, 8, 32, 45, "present", "absent", "none", "CC-A/B", "auto", "high", "low", "true", "false"

**`bar_code_handle`** (output_control)  barcode `→` HHandle

Handle for using and accessing the bar code model.

## Result

The operator `create_bar_code_model` returns the value 2 (
H_MSG_TRUE)
if the
given parameters are correct. Otherwise, an exception will be raised.

## Possible Successors

`find_bar_code`

## See also

`clear_bar_code_model`

## References

International Standard ISO/IEC 15420: “Information technology - Automatic
identification and data capture techniques -
Bar code symbology specification - EAN/UPC”;
Reference number ISO/IEC 15420:2000 (E);
ISO/IEC 2000.
  
International Standard ISO/IEC 16390: “Information technology - Automatic
identification and data capture techniques -
Bar code symbology specification - Interleaved 2 of 5”;
Reference number ISO/IEC 16390:1999 (E);
ISO/IEC 1999.
  
International Standard ISO/IEC 16388: “Information technology - Automatic
identification and data capture techniques -
Bar code symbology specification - Code 39”;
Reference number ISO/IEC 16388:1999 (E);
ISO/IEC 1999.
  
American National Standards Institute, Inc.(ANSI): “Uniform Symbology
Specification Code 93”;
ANSI/AIM-BC5-2000;
AIM 2000.
  
International Standard ISO/IEC 15417: “Information technology - Automatic
identification and data capture techniques -
Bar code symbology specification - Code 128”;
Reference number ISO/IEC 15417:2000 (E);
ISO/IEC 2000.
  
American National Standards Institute, Inc.(ANSI): “Uniform Symbology
Specification Codabar”;
ANSI/AIM-BC3-2000;
AIM 2000.
  
International Standard ISO/IEC 24724: “Information technology - Automatic
identification and data capture techniques -
Reduced Space Symbology (RSS) bar code symbology specification”;
Reference number ISO/IEC 24724:2006 (E);
ISO/IEC 2006.
  
International Standard ISO/IEC 24723: “Information technology - Automatic
identification and data capture techniques -
EAN.UCC Composite bar code symbology specification”;
Reference number ISO/IEC 24723:2006 (E);
ISO/IEC 2006.

## Module

Bar Code
