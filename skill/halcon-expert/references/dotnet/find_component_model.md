# FindComponentModel (Operator)

## Name

`FindComponentModel` — Find the best matches of a component model in an image.

## Warning

**`FindComponentModel` is obsolete and is only provided for
reasons of backward compatibility.
The operator will be removed with HALCON 26.11.**

## Signature

`static void HOperatorSet.FindComponentModel(HObject image, HTuple componentModelID, HTuple rootComponent, HTuple angleStartRoot, HTuple angleExtentRoot, HTuple minScore, HTuple numMatches, HTuple maxOverlap, HTuple ifRootNotFound, HTuple ifComponentNotFound, HTuple posePrediction, HTuple minScoreComp, HTuple subPixelComp, HTuple numLevelsComp, HTuple greedinessComp, out HTuple modelStart, out HTuple modelEnd, out HTuple score, out HTuple rowComp, out HTuple columnComp, out HTuple angleComp, out HTuple scoreComp, out HTuple modelComp)`

`HTuple HComponentModel.FindComponentModel(HImage image, HTuple rootComponent, HTuple angleStartRoot, HTuple angleExtentRoot, double minScore, int numMatches, double maxOverlap, string ifRootNotFound, string ifComponentNotFound, string posePrediction, HTuple minScoreComp, HTuple subPixelComp, HTuple numLevelsComp, HTuple greedinessComp, out HTuple modelEnd, out HTuple score, out HTuple rowComp, out HTuple columnComp, out HTuple angleComp, out HTuple scoreComp, out HTuple modelComp)`

`int HComponentModel.FindComponentModel(HImage image, int rootComponent, double angleStartRoot, double angleExtentRoot, double minScore, int numMatches, double maxOverlap, string ifRootNotFound, string ifComponentNotFound, string posePrediction, double minScoreComp, string subPixelComp, int numLevelsComp, double greedinessComp, out int modelEnd, out double score, out double rowComp, out double columnComp, out double angleComp, out double scoreComp, out int modelComp)`

`HTuple HImage.FindComponentModel(HComponentModel componentModelID, HTuple rootComponent, HTuple angleStartRoot, HTuple angleExtentRoot, double minScore, int numMatches, double maxOverlap, string ifRootNotFound, string ifComponentNotFound, string posePrediction, HTuple minScoreComp, HTuple subPixelComp, HTuple numLevelsComp, HTuple greedinessComp, out HTuple modelEnd, out HTuple score, out HTuple rowComp, out HTuple columnComp, out HTuple angleComp, out HTuple scoreComp, out HTuple modelComp)`

`int HImage.FindComponentModel(HComponentModel componentModelID, int rootComponent, double angleStartRoot, double angleExtentRoot, double minScore, int numMatches, double maxOverlap, string ifRootNotFound, string ifComponentNotFound, string posePrediction, double minScoreComp, string subPixelComp, int numLevelsComp, double greedinessComp, out int modelEnd, out double score, out double rowComp, out double columnComp, out double angleComp, out double scoreComp, out int modelComp)`

## Description

The operator `FindComponentModel` finds the best
*`numMatches`* instances of the component model
*`componentModelID`* in the input image *`image`*.

The result of the search can be visualized using
[`GetFoundComponentModel`](get_found_component_model.md).
Also the operator can be used to extract the component matches
of a certain component model instance.

### Further information about input parameters

- ***`componentModelID`*:** —

  Handle of the component model.

  The model must have been created previously by calling
  [`CreateTrainedComponentModel`](create_trained_component_model.md) or
  [`CreateComponentModel`](create_component_model.md), or read in using
  [`ReadComponentModel`](read_component_model.md).
- ***`rootComponent`*:** —

  Index of the root component.

  The components of the component model *`componentModelID`* are
  represented in a tree structure. The component that stands at the
  root of this search tree is the root component.

  The root component is searched within the full parameter space,
  i.e., at all allowed positions and in the allowed
  range of orientations (see below).
  In contrast, the remaining components are searched relative to the pose
  of their predecessor in the search tree within a restricted parameter space
  that is computed from the relations (recursive search).

  To what extent a model component is suited to act as root component depends
  on several factors. In principle, a model component that can be found
  in the image with a high probability, should be chosen. Therefore, a
  component that is sometimes occluded to a high degree or that is
  missing in some cases is not well suited to act as root
  component.
  For the behavior in such cases, see the entry *`ifRootNotFound`*
  below.

  A different possible criterion is the computation time
  that is associated with the root component during the search.
  A ranking of the model components that is
  based on the latter criterion is returned in `rootRanking`
  of the operator [`CreateTrainedComponentModel`](create_trained_component_model.md) or
  [`CreateComponentModel`](create_component_model.md), respectively.
  If the complete ranking is passed in *`rootComponent`*,
  the first value *`rootComponent`*[0] is automatically selected
  as the root component.
- ***`angleStartRoot`* and *`angleExtentRoot`*:** —

  Specify the allowed angle range (in [rad]) within which the root
  component is searched.

  If necessary, the range of rotations
  is clipped to the range given when the component model was created
  with [`CreateTrainedComponentModel`](create_trained_component_model.md) or
  [`CreateComponentModel`](create_component_model.md), respectively.
  The angle range for each component can be queried with
  [`GetShapeModelParams`](get_shape_model_params.md).
  The necessary handle of the corresponding shape model can be obtained using
  [`GetComponentModelParams`](get_component_model_params.md).
- ***`minScore`*:** —

  Determines what score a potential match of the component model must at
  least have to be regarded as an instance.

  If the component model can be expected never to be occluded in the images,
  *`minScore`* may be set as high as *0.8* or even *0.9*.
  The value of this parameter only slightly influences the computation time.
  An exception is the case of *`ifRootNotFound`* set to
  *"select_new_root"* (see below).
- ***`numMatches`*:** —

  Determines the maximum number of returned instances.

  If fewer than *`numMatches`* are found, only that number is
  returned, i.e., the parameter *`minScore`* takes precedence
  over *`numMatches`*.
  In case more than *`numMatches`* instances with a score greater than
  *`minScore`* are found in the image, only the best
  *`numMatches`* instances are returned.
  However, if all model instances exceeding *`minScore`* in the image
  should be found, *`numMatches`* must be set to *0*.
- ***`maxOverlap`*:** —

  Determines by what fraction two instances may at most overlap,
  whereby this fraction is a number between 0 and 1.

  In some cases, found instances only differ in the pose of one or a few
  components.
  If two instances overlap each other by more than
  *`maxOverlap`* only the best instance is returned.
  This means, for *`maxOverlap`* = *0*, the found instances may
  not overlap at all, while for *`maxOverlap`* = *1* no check for
  overlap is performed, and hence all instances are returned.
  The calculation of the overlap is based on the smallest enclosing
  rectangles of arbitrary orientation (see [`SmallestRectangle2`](smallest_rectangle2.md))
  of the found component instances.
- ***`ifRootNotFound`*:** —

  specifies the behavior of the operator when dealing with
  a missing or strongly occluded root component.

  Possible values:

  - *"stop_search"*:
    It is assumed that the root component is always found in the image.
    Consequently, for instances for which the root component could not
    be found the search for the remaining components is not continued.
  - *"select_new_root"*:
    Different components are successively chosen as the root component
    and searched within the full search space.
    The order in which the selection of the root component is performed
    corresponds to the order passed in `rootRanking`.
    The poses of the found instances of all root components are then used
    to start the recursive search for the remaining components.
    Hence, it is possible to find instances even if the original root
    component is not found.
    However, the computation time of the search increases significantly
    in comparison to the search when choosing *"stop_search"*.
    This is especially the case for small values of *`minScore`*,
    as more root components must be searched.
    If during the search more root components are needed as given in
    *`rootComponent`*, the root components are completed by
    the automatically computed order
    (see [`CreateTrainedComponentModel`](create_trained_component_model.md) or
    [`CreateComponentModel`](create_component_model.md)).
- ***`ifComponentNotFound`*:** —

  Specifies how components are searched when the predecessor component
  was not found (e.g., because she is missing or strongly occluded).

  Possible values:

  - *"prune_branch"*:
    Such components are not searched at all and are also treated as
    'not found'.
  - *"search_from_upper"*:
    Such components are searched relative to the pose of the predecessor
    component of the predecessor component.
  - *"search_from_best"*:
    Such components are searched relative to the pose of the already found
    component from which the relative search can be performed with minimum
    computational effort.
- ***`posePrediction`*:** —

  Determines whether the pose of not found components should be estimated.

  Possible values:

  - *"none"*:
    Only the poses of the found components are returned.
  - *"from_neighbors"*:
    The poses of not found components are estimated and returned with a score
    of *`scoreComp`* = *0.0*.
    The pose estimation is based on the poses of the found neighboring
    components in the search tree.
  - *"from_all"*:
    The poses of not found components are estimated and returned with a score
    of *`scoreComp`* = *0.0*.
    The pose estimation is based on the poses of all found components.
- ***`minScoreComp`*:** —

  Minimal necessary score of the components for the instances to be found.

  This parameter has the same meaning as `minScore` in
  [`FindShapeModel`](find_shape_model.md).

  Settable is either one element or the same number of elements as model
  components in *`componentModelID`*.
  In the first case the parameter is used for all components.
  In the second case, each parameter element refers to the corresponding
  component in *`componentModelID`*.
- ***`subPixelComp`*:** —

  Determines whether the extraction shall be done subpixel precise
  and in the given case the maximal allowed object deformation in pixels.

  This parameter has the same meaning as `subPixel` in
  [`FindShapeModel`](find_shape_model.md).
  Therefore the maximal allowed object deformation has to be given as
  integer in the same string.
  Settable is either one element or the same number of elements as model
  components in *`componentModelID`*.
  In the first case the parameter is used for all components.
  In the second case, each parameter element refers to the corresponding
  component in *`componentModelID`*.

  *Example:* *["least_squares", "max_deformation 2"]*.
- ***`numLevelsComp`*:** —

  Determine the pyramid levels for the components used in the matching.

  This parameter has the same meaning as `numLevels` in
  [`FindShapeModel`](find_shape_model.md).

  It determines the number of pyramid levels for the components
  to be used in the matching.
  Settable is either one element or the same number of elements as model
  components in *`componentModelID`*.
  In the first case the parameter is used for all components.
  In the second case, each parameter element refers to the corresponding
  component in *`componentModelID`*.

  Optional, one can set value pairs for this parameter:
  In this case, the first value still determines the number of pyramid levels
  to be used.
  The second value specifies the lowest pyramid level, to which the found
  matches are tracked.
  In doing so, one can set either a single value pair or a value pair for each
  model component in *`componentModelID`*.
  If different value pairs should be used for different components, they must
  be specified in the same tuple.
  In case *`componentModelID`* contains exactly two components and in
  *`numLevelsComp`* two values are set, these values are interpreted as
  different number of pyramid levels to be used and not as a value pair.

  *Example:* *`componentModelID`* contains two components, for
  which different pyramid levels shall be considered.
  For the first component 5 levels up to the level 2 shall be used.
  For the second component 4 levels up to the level 1 shall be used.
  In this case is *`numLevelsComp`* = *[5,2,4,1]*.
- ***`greedinessComp`*:** —

  “Greediness” of the search heuristic for the components: value from 0 to
  1. Thereby 0 means: safe but slow, 1: fast but matches may be missed.

  This parameter has the same meaning as `greediness` in
  [`FindShapeModel`](find_shape_model.md).

  Settable is either one element or the same number of elements as model
  components in *`componentModelID`*.
  In the first case the parameter is used for all components.
  In the second case, each parameter element refers to the corresponding
  component in *`componentModelID`*.

### Further information about output parameters

- ***`modelStart`* and *`modelEnd`*:** —

  Return the first and last index and therewith the index range
  of all component matches associated to the same instance of the
  component model.

  The component matches corresponding to the first found instance of the
  component model are given by the interval of indices
  [*`modelStart`*[0],*`modelEnd`*[0]].
  Thereby the indices refer to the values of the parameters *`rowComp`*,
  *`columnComp`*, *`angleComp`*, *`scoreComp`*, and
  *`modelComp`*.

  *Example:* The component model consists for three components.
  Two instances have been found on the image, where for one instance only two
  components (component 0 and component 2) could be found.
  Then the returned parameters could look like this:

  |  |  |
  | --- | --- |
  | *`rowComp`* = *[100,200,300,150,250]* | *`modelStart`* = *[0,3]* |
  | *`columnComp`* = *[200,210,220,400,425]* | *`modelEnd`* = *[2,4]* |
  | *`angleComp`* = *[0,0.1,-0.2,0.1,0.2]* | *`modelComp`* = *[0,1,2,0,2]* |
  | *`scoreComp`* = *[1,1,1,1,1]* | *`score`* = *[1,1]* |
  |  |

  From the right column it is visible, that in the left column:
  - Values with index 0 to 2 correspond to the components 0 to 2 of
    instance 1.
  - Values with index 3 to 4 correspond to the components 0 and 2 of
    instance 2.
- ***`score`*:** —

  Score of the found instances of the component model.

  *`score`* contains the weighted mean of the component scores,
  the values in *`scoreComp`*.
  The weighting is performed according to the number of model points
  within the respective component.
- ***`rowComp`*, *`columnComp`*, and *`angleComp`*:** —

  The position (*`rowComp`*, *`columnComp`*) and rotation
  (*`angleComp`*) of the model components of all found component
  model instances.

  The coordinates *`rowComp`* and *`columnComp`* are the
  coordinates of the component origin (reference point) in
  the search image.
  The component origin depends on the model creation:

  - with [`CreateTrainedComponentModel`](create_trained_component_model.md) by training:
    The component origin is the center of gravity of the respective
    returned contour region in `modelComponents` of the operator
    [`TrainModelComponents`](train_model_components.md).
  - with [`CreateComponentModel`](create_component_model.md) manually:
    The component origin is the center of gravity of the corresponding
    passed component region `componentRegions` of the operator
    [`CreateComponentModel`](create_component_model.md).

  Since the relations between the components in *`componentModelID`*
  refer to this reference point, the origin of the components must not be
  modified by using [`SetShapeModelOrigin`](set_shape_model_origin.md).
- ***`scoreComp`*:** —

  Score of each found component instance.

  The score is a number between 0 and 1, and is an approximate measure of how
  much of the component is visible in the image.
  If, for example, half of the component is occluded, the score cannot exceed
  0.5.
- ***`modelComp`*:** —

  Index of the found component.

  The tuple contains the indices of the respective model components
  (see [`CreateComponentModel`](create_component_model.md) and [`TrainModelComponents`](train_model_components.md),
  respectively).
  By this the values in *`rowComp`*, *`columnComp`*,
  *`angleComp`*, and *`scoreComp`* can be associated
  to the different model components.
  See also the example given for *`modelStart`* and *`modelEnd`*.

### Information concerning the search

Internally, the shape-based matching is used for the component-based
matching in order to search the individual components
(see [`FindShapeModel`](find_shape_model.md)).

The domain of the *`image`* determines the search space for the
reference point, i.e., the allowed positions, of the root component.

Usually the component model is searched only within those points of the
image domain in which the model fits completely into the image.
This means that the components will not be found if they extend beyond the
borders of the image, even if they would achieve a score greater than
*`minScoreComp`* (see above).

Note that, if for a certain pyramid level the component model touches the
image border, it might not be found even if it lies completely within the
original image.
As a rule of thumb, the model might not be found if its distance to
an image border falls below $2^{NumLevels-1}$.
This behavior can be changed with
`set_system('border_shape_models','true')`, which will cause
components that extend beyond the image border to be found if they achieve
a score greater than *`minScoreComp`*.
Here, points lying outside the image are regarded as being occluded, i.e.,
they lower the score.
It should be noted that this mode increases the runtime of the search.

Note further, that in rare cases, which occur typically only for artificial
images, the model might not be found also if for certain pyramid levels the
model touches the border of the reduced domain. Then, it may help to
enlarge the reduced domain by $2^{NumLevels-1}$ using,
e.g., [`DilationCircle`](dilation_circle.md).

When tracking the matches through the image pyramid, on each level,
some less promising matches are rejected based on *`numMatches`*. Thus,
it is possible that some matches are rejected that would have had a higher
score on the lowest pyramid level. Due to this, for example, the found
match for *`numMatches`* set to *1* might be
different from the match with the highest score returned when setting
*`numMatches`* to *0* or > *1*.

### Recommendations

If multiple objects with a similar score are expected, but only the one
with the highest score should be returned, it might be preferable to raise
*`numMatches`*, and then select the match with the highest score.

To get a meaningful score value and to avoid erroneous matches,
we recommend to always combine the allowance of a deformation with a
subpixel extraction that applies a least-squares adjustment.
If the subpixel extraction and/or the maximum object deformation is
specified separately for each component, for each component in
*`componentModelID`* exactly one value for the subpixel extraction
must be passed in *`subPixelComp`*.
After each value for the subpixel extraction optionally a second value can
be passed, which describes the maximum object deformation of the
corresponding mode. If for a certain component no value for the maximum
object deformation is passed, the component is searched without taking
deformations into account.
Further details can be found in the documentation of
[`FindShapeModels`](find_shape_models.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (input_object)  (multichannel-)image `→` [HImage](HImage.md) (byte / uint2)

Input image in which the component model should be
found.

**`componentModelID`** (input_control)  component_model `→` [HComponentModel](HComponentModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the component model.

**`rootComponent`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Index of the root component.

Suggested values:
0, 1, 2, 3, 4, 5, 6, 7, 8

**`angleStartRoot`** (input_control)  angle.rad(-array) `→` [HTuple](HTuple.md) (*double*)

Smallest rotation of the root component

Default:
-0.39

Suggested values:
-3.14, -1.57, -0.79, -0.39, -0.20, 0.0

**`angleExtentRoot`** (input_control)  angle.rad(-array) `→` [HTuple](HTuple.md) (*double*)

Extent of the rotation of the root component.

Default:
0.79

Suggested values:
6.28, 3.14, 1.57, 0.79, 0.39, 0.0

Restriction:
`AngleExtentRoot >= 0`

**`minScore`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Minimum score of the instances of the component
model to be found.

Default:
0.5

Suggested values:
0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Minimum increment:
0.01

Recommended increment:
0.05

Restriction:
`0 <= MinScore && MinScore <= 1`

**`numMatches`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of instances of the component model to be
found (or 0 for all matches).

Default:
1

Suggested values:
0, 1, 2, 3, 4, 5, 10, 20

**`maxOverlap`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Maximum overlap of the instances of the
component models to be found.

Default:
0.5

Suggested values:
0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Minimum increment:
0.01

Recommended increment:
0.05

Restriction:
`0 <= MaxOverlap && MaxOverlap <= 1`

**`ifRootNotFound`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Behavior if the root component is missing.

Default:
"stop_search"

List of values:
"select_new_root", "stop_search"

**`ifComponentNotFound`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Behavior if a component is missing.

Default:
"prune_branch"

List of values:
"prune_branch", "search_from_best", "search_from_upper"

**`posePrediction`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Pose prediction of components that are not found.

Default:
"none"

List of values:
"from_all", "from_neighbors", "none"

**`minScoreComp`** (input_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Minimum score of the instances of the components to
be found.

Default:
0.5

Suggested values:
0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Minimum increment:
0.01

Recommended increment:
0.05

Restriction:
`0 <= MinScoreComp && MinScoreComp <= 1`

**`subPixelComp`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Subpixel accuracy of the component poses if not
equal to *"none"*.

Default:
"least_squares"

Suggested values:
"none", "interpolation", "least_squares", "least_squares_high", "least_squares_very_high", "max_deformation 1", "max_deformation 2", "max_deformation 3", "max_deformation 4", "max_deformation 5", "max_deformation 6"

**`numLevelsComp`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Number of pyramid levels for the components used in
the matching
(and lowest pyramid level to use if
|*`numLevelsComp`*| = 2n).

Default:
0

List of values:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

**`greedinessComp`** (input_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

“Greediness” of the search heuristic for the
components (0: safe
but slow; 1: fast but matches may be missed).

Default:
0.9

Suggested values:
0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Minimum increment:
0.01

Recommended increment:
0.05

Restriction:
`0 <= GreedinessComp && GreedinessComp <= 1`

**`modelStart`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Start index of each found instance of the component
model in the tuples describing the component matches.

**`modelEnd`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

End index of each found instance of the component
model in the tuples describing the component matches.

**`score`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Score of the found instances of the component model.

**`rowComp`** (output_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the found component matches.

**`columnComp`** (output_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the found component matches.

**`angleComp`** (output_control)  angle.rad(-array) `→` [HTuple](HTuple.md) (*double*)

Rotation angle of the found component matches.

**`scoreComp`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Score of the found component matches.

**`modelComp`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Index of the found components.

## Result

If the parameter values are correct, the operator
`FindComponentModel` returns the value 2 (
H_MSG_TRUE)
. If the input
is empty (no input image available) the behavior can be set via
`set_system('no_object_result',<Result>)`.
If necessary, an exception is raised.

## Module

Matching
