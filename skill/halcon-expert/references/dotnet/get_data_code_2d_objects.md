# GetDataCode2dObjects (Operator)

## Name

`GetDataCode2dObjects` — Access iconic objects that were created during the search for
2D code symbols.

## Signature

`static void HOperatorSet.GetDataCode2dObjects(out HObject dataCodeObjects, HTuple dataCodeHandle, HTuple candidateHandle, HTuple objectName)`

`HObject HDataCode2D.GetDataCode2dObjects(HTuple candidateHandle, string objectName)`

`HObject HDataCode2D.GetDataCode2dObjects(int candidateHandle, string objectName)`

## Description

The operator `GetDataCode2dObjects` facilitates to access
iconic objects that were created during the last call of
[`FindDataCode2d`](find_data_code_2d.md) while searching and reading the 2D
code symbols.
Besides the name of the object (*`objectName`*), the 2D
code model (*`dataCodeHandle`*) must be passed to
`GetDataCode2dObjects`.
In addition, in *`candidateHandle`* a handle of a result
or candidate structure or a string identifying a group of candidates
(see [`GetDataCode2dResults`](get_data_code_2d_results.md)) must be passed.
These handles are returned by [`FindDataCode2d`](find_data_code_2d.md) for all
successfully decoded symbols and by [`GetDataCode2dResults`](get_data_code_2d_results.md)
for a group of candidates.
If these operators return several handles in a tuple, the individual
handles can be accessed by normal tuple operations.

For an explanation of the concept of the 2D code reader
see the introduction of chapter [Identification / 2D Code](toc_identification_datacode.md).

If *"discard_undecoded_candidates"* was set to *"yes"*
with [`SetDataCode2dParam`](set_data_code_2d_param.md), only results of successfully
decoded candidates can be accessed.

Some objects are not accessible without setting the model parameter
*"persistence"* to *1* (see
[`SetDataCode2dParam`](set_data_code_2d_param.md)).
The persistence must be set before calling
[`FindDataCode2d`](find_data_code_2d.md), either while creating the model with
[`CreateDataCode2dModel`](create_data_code_2d_model.md) or with
[`SetDataCode2dParam`](set_data_code_2d_param.md).

Currently, the following iconic objects can be retrieved:

**Regions of the modules**

- All 2D code types:

  - ***"module_1_rois"*:** —

    All modules that were classified as foreground (set).
    If a symbol is decoded with *"deformation_tolerance"*=*"curved"*,
    an empty object is returned. See *"deformation_objects"*
    in [`GetDataCode2dResults`](get_data_code_2d_results.md) for module regions in this case.
- All 2D code types except DotCode:

  - ***"module_0_rois"*:** —

    All modules that were classified as background (not set).
    The special handling for *"deformation_tolerance"*=*"curved"*
    denoted above applies as well.

These region arrays correspond to the areas that were used for the
classification.
The returned object is a region array.
Hence it cannot be requested for a group of candidates.
Therefore, a single result handle must be passed in
*`candidateHandle`*.
The model persistence must be *1* for this object.
In addition, requesting the module ROIs makes sense only for symbols
that were detected as valid symbols.
For other candidates, whose processing was aborted earlier, the
module ROIs are not available.

**XLD contour**

- All 2D code types:

  - ***"candidate_xld"*:** —

    An XLD contour that surrounds the candidate or decoded symbol.
- Data Matrix ECC 200 and QR Code:

  - ***"candidate_xld_deformed"*:** —

    A more accurate XLD contour that surrounds the decoded symbol,
    if decoded with *"deformation_tolerance"*=*"curved"*.
    Otherwise the same contour as *"candidate_xld"*.

This object can be requested for any group of results or for any
single candidate or symbol handle.
The persistence setting is of no relevance.

**Pyramid images**

- ***"search_image"*:** —

  Pyramid image, in which the candidate was found.
- ***"process_image"*:** —

  Pyramid image, in which the candidate was investigated more closely.

The persistence setting is also not relevant here.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dataCodeObjects`** (output_object)  object(-array) `→` [HObject](HObject.md)

Objects that are created as intermediate results
during the detection or evaluation of 2D codes.

**`dataCodeHandle`** (input_control)  datacode_2d `→` [HDataCode2D](HDataCode2D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 2D code model.

**`candidateHandle`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long / string)

Handle of the 2D code candidate. Either an integer
(usually the ResultHandle of [`FindDataCode2d`](find_data_code_2d.md)) or
a string representing a group of candidates.

Default:
"all_candidates"

Suggested values:
0, 1, 2, "all_candidates", "all_results", "all_undecoded", "all_aborted"

**`objectName`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Name of the iconic object to return.

Default:
"candidate_xld"

List of values:
"candidate_xld", "candidate_xld_deformed", "module_0_rois", "module_1_rois", "process_image", "search_image"

## Example (HDevelop)

```
* Example demonstrating how to access the iconic objects of the 2D code
* search.

* Create a model for reading Data Matrix ECC 200 codes
create_data_code_2d_model ('Data Matrix ECC 200', [], [], DataCodeHandle)
set_data_code_2d_param (DataCodeHandle, 'default_parameters', \
                        'maximum_recognition')
set_data_code_2d_param (DataCodeHandle, 'persistence', 1)
* Read an image
read_image (Image, 'datacode/ecc200/ecc200_disturbed_012')
* Read the symbol in the image
find_data_code_2d (Image, SymbolXLDs, DataCodeHandle, [], [], \
                   ResultHandles, DecodedDataStrings)

* Get the handles of all candidates that were detected as a symbol but
* could not be read
get_data_code_2d_results (DataCodeHandle, 'all_undecoded', 'handle', \
                          HandlesUndecoded)

* For every undecoded symbol, get the contour and the classified
* module regions
for I := 0 to |HandlesUndecoded| - 1 by 1
  * Display image.
  dev_display (Image)
  dev_set_draw ('margin')
  * Get the contour of the symbol.
  dev_set_color ('blue')
  get_data_code_2d_objects (SymbolXLD, DataCodeHandle, \
                            HandlesUndecoded[I], 'candidate_xld')
  dev_display (SymbolXLD)
  * Get the module regions of the foreground modules
  dev_set_color ('green')
  get_data_code_2d_objects (ModuleFG, DataCodeHandle, \
                            HandlesUndecoded[I], 'module_1_rois')
  dev_display (ModuleFG)
  * Get the module regions of the background modules
  dev_set_color ('red')
  get_data_code_2d_objects (ModuleBG, DataCodeHandle, \
                            HandlesUndecoded[I], 'module_0_rois')
  dev_display (ModuleBG)
  * Stop for inspecting the image.
  stop ()
endfor

* Clear the model
clear_data_code_2d_model (DataCodeHandle)
```

## Result

The operator `GetDataCode2dObjects` returns the value 2 (
H_MSG_TRUE)
if the given parameters are correct and the requested objects are
available for the last symbol search.
Otherwise, an exception is raised.

## Possible Predecessors

`FindDataCode2d`,
`QueryDataCode2dParams`

## Possible Successors

`GetDataCode2dResults`

## See also

`QueryDataCode2dParams`,
`GetDataCode2dResults`,
`GetDataCode2dParam`,
`SetDataCode2dParam`

## Module

Data Code
