# DoOcrWordKnn (Operator)

## Name

`DoOcrWordKnn` — Classify a related group of characters with an OCR classifier.

## Signature

`static void HOperatorSet.DoOcrWordKnn(HObject character, HObject image, HTuple OCRHandle, HTuple expression, HTuple numAlternatives, HTuple numCorrections, out HTuple classVal, out HTuple confidence, out HTuple word, out HTuple score)`

`HTuple HRegion.DoOcrWordKnn(HImage image, HOCRKnn OCRHandle, string expression, int numAlternatives, int numCorrections, out HTuple confidence, out string word, out double score)`

`string HRegion.DoOcrWordKnn(HImage image, HOCRKnn OCRHandle, string expression, int numAlternatives, int numCorrections, out double confidence, out string word, out double score)`

`HTuple HOCRKnn.DoOcrWordKnn(HRegion character, HImage image, string expression, int numAlternatives, int numCorrections, out HTuple confidence, out string word, out double score)`

`string HOCRKnn.DoOcrWordKnn(HRegion character, HImage image, string expression, int numAlternatives, int numCorrections, out double confidence, out string word, out double score)`

## Description

`DoOcrWordKnn` works like [`DoOcrMultiClassKnn`](do_ocr_multi_class_knn.md) insofar
as it computes the best class for each of the characters given by the
regions *`character`* and the gray values *`image`* with the
OCR classifier *`OCRHandle`*, and returns the classes in *`classVal`*
and the corresponding confidences of the classes
in *`confidence`*. The confidences lie between 0.0 and 1.0.
The larger the value, the more reliable is the classification of the single
characters.

In contrast to [`DoOcrMultiClassKnn`](do_ocr_multi_class_knn.md), `DoOcrWordKnn`
treats the group of characters as an entity which yields a *`word`*
by concatenating the class names for each character region. This allows
to restrict the allowed classification results on a textual level by
specifying an *`expression`* describing the expected word.

The *`expression`* may restrict the word to belong to a predefined
lexicon created using [`CreateLexicon`](create_lexicon.md) or [`ImportLexicon`](import_lexicon.md),
by specifying the name of the lexicon in angular
brackets as in *"<mylexicon>"*. If the *`expression`* is of
any other form, it is interpreted as a regular expression with the same
syntax as specified for [`TupleRegexpMatch`](tuple_regexp_match.md). Note that you will
usually want to use an expression of the form
'^...$'
when using variable quantifiers like '*', to ensure that the entire word
is used in the expression. Also note that in contrast to
[`TupleRegexpMatch`](tuple_regexp_match.md), `DoOcrWordKnn` does **not**
support passing extra options in an expression tuple.

If the word derived from the best class for each character does not match
the *`expression`*, `DoOcrWordKnn` attempts to correct it by
considering the *`numAlternatives`* best classes for each character.
The alternatives used are identical to those returned by
[`DoOcrSingleClassKnn`](do_ocr_single_class_knn.md) for a single character. It does so by
testing all possible corrections for which the classification result
is changed for at most *`numCorrections`* character regions.
Note that *`numAlternatives`* and *`numCorrections`* affect the
complexity of the algorithm, so that in some cases internal restrictions
are made. See the section 'Complexity' below for further information.

In case the *`expression`* is a lexicon and the above procedure did
not yield a result, the most similar word in the lexicon is returned as long
as it requires less than *`numCorrections`* edit operations for the
correction (see [`SuggestLexicon`](suggest_lexicon.md)).

The resulting word is graded by a *`score`* between 0.0 (no correction
found) and 1.0 (original word correct). The *`score`* is lowered by
adding a penalty according to the number of corrected characters and another
(minor) penalty depending on how many classes with higher confidences have
been ignored in order to match the *`expression`*:

$$\texttt{Score}=1.0-\texttt{PenaltyCorrections}-\texttt{PenaltyAlternatives}$$
$$PenaltyCorrections = \alpha*num_corr PenaltyAlternatives = \alpha*\beta*num_alt$$ ![figure](../assets/89ef63e3079b9acf.svg)
with `num_corr` being the actual number of applied corrections and
`num_alt` the total number of discarded alternatives.
$$\alpha = \frac{1}{\text{NumCorrections} + 1} \\ \beta = \frac{1}{\text{NumCorrections} * (\text{NumAlternatives} - 1) + 2}$$ ![figure](../assets/24ee499d9eafa431.svg)

Note that this is a combinatorial score which does **not** reflect the
original *`confidence`* of the best *`classVal`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`character`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Characters to be recognized.

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / uint2)

Gray values of the characters.

**`OCRHandle`** (input_control)  ocr_knn `→` [HOCRKnn](HOCRKnn.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the OCR classifier.

**`expression`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Expression describing the allowed word structure.

**`numAlternatives`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of classes per character considered for the
internal word correction.

Default:
3

Suggested values:
3, 4, 5

Value range:
`1
≤
numAlternatives
≤
5`

**`numCorrections`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Maximum number of corrected characters.

Default:
2

Suggested values:
1, 2, 3, 4, 5

Value range:
`0
≤
numCorrections
≤
5`

**`classVal`** (output_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Result of classifying the characters with the
k-NN.

Number of elements:
Class == Character

**`confidence`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Confidence of the class of the characters.

Number of elements:
Confidence == Character

**`word`** (output_control)  string `→` [HTuple](HTuple.md) (*string*)

Word text after classification and correction.

**`score`** (output_control)  real `→` [HTuple](HTuple.md) (*double*)

Measure of similarity between corrected word
and uncorrected classification results.

## Complexity

The complexity of checking all possible corrections is of magnitude
$O((n\ast a)^{min(c,n)})$,
where a is the number of alternatives, n is the
number of character regions, and c is the number of allowed corrections.
However, to guard against a near-infinite loop in case of large n,
c is internally clipped to 5, 3, or 1 if
a*n >= 30, 60, or 90, respectively.

## Result

If the parameters are valid, the operator
`DoOcrWordKnn` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`TrainfOcrClassKnn`,
`ReadOcrClassKnn`

## Alternatives

`DoOcrMultiClassKnn`

## See also

`CreateOcrClassKnn`,
`ClassifyClassKnn`

## Module

OCR/OCV
