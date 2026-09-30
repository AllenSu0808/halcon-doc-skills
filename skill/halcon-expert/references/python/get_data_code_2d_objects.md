# get_data_code_2d_objects (Operator)

## Name

`get_data_code_2d_objects` — Access iconic objects that were created during the search for
2D code symbols.

## Signature

`def get_data_code_2d_objects(data_code_handle: HHandle, candidate_handle: Union[int, str], object_name: str) -> HObject`

## Description

The operator `get_data_code_2d_objects` facilitates to access
iconic objects that were created during the last call of
[`find_data_code_2d`](find_data_code_2d.md) while searching and reading the 2D
code symbols.
Besides the name of the object (*`object_name`*), the 2D
code model (*`data_code_handle`*) must be passed to
`get_data_code_2d_objects`.
In addition, in *`candidate_handle`* a handle of a result
or candidate structure or a string identifying a group of candidates
(see [`get_data_code_2d_results`](get_data_code_2d_results.md)) must be passed.
These handles are returned by [`find_data_code_2d`](find_data_code_2d.md) for all
successfully decoded symbols and by [`get_data_code_2d_results`](get_data_code_2d_results.md)
for a group of candidates.
If these operators return several handles in a tuple, the individual
handles can be accessed by normal tuple operations.

For an explanation of the concept of the 2D code reader
see the introduction of chapter [Identification / 2D Code](toc_identification_datacode.md).

If *"discard_undecoded_candidates"* was set to *"yes"*
with [`set_data_code_2d_param`](set_data_code_2d_param.md), only results of successfully
decoded candidates can be accessed.

Some objects are not accessible without setting the model parameter
*"persistence"* to *1* (see
[`set_data_code_2d_param`](set_data_code_2d_param.md)).
The persistence must be set before calling
[`find_data_code_2d`](find_data_code_2d.md), either while creating the model with
[`create_data_code_2d_model`](create_data_code_2d_model.md) or with
[`set_data_code_2d_param`](set_data_code_2d_param.md).

Currently, the following iconic objects can be retrieved:

**Regions of the modules**

- All 2D code types:

  - ***"module_1_rois"*:** —

    All modules that were classified as foreground (set).
    If a symbol is decoded with *"deformation_tolerance"*=*"curved"*,
    an empty object is returned. See *"deformation_objects"*
    in [`get_data_code_2d_results`](get_data_code_2d_results.md) for module regions in this case.
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
*`candidate_handle`*.
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

**`data_code_objects`** (output_object)  object(-array) `→` HObject

Objects that are created as intermediate results
during the detection or evaluation of 2D codes.

**`data_code_handle`** (input_control)  datacode_2d `→` HHandle

Handle of the 2D code model.

**`candidate_handle`** (input_control)  integer `→` Union[int, str]

Handle of the 2D code candidate. Either an integer
(usually the ResultHandle of [`find_data_code_2d`](find_data_code_2d.md)) or
a string representing a group of candidates.

Default:
"all_candidates"

Suggested values:
0, 1, 2, "all_candidates", "all_results", "all_undecoded", "all_aborted"

**`object_name`** (input_control)  string `→` str

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

The operator `get_data_code_2d_objects` returns the value 2 (
H_MSG_TRUE)
if the given parameters are correct and the requested objects are
available for the last symbol search.
Otherwise, an exception is raised.

## Possible Predecessors

`find_data_code_2d`,
`query_data_code_2d_params`

## Possible Successors

`get_data_code_2d_results`

## See also

`query_data_code_2d_params`,
`get_data_code_2d_results`,
`get_data_code_2d_param`,
`set_data_code_2d_param`

## Module

Data Code
