# do_ocr_word_mlp (Operator)

## Name

`do_ocr_word_mlp` — Classify a related group of characters with an OCR classifier.

## Signature

`do_ocr_word_mlp(Character, Image : : OCRHandle, Expression, NumAlternatives, NumCorrections : Class, Confidence, Word, Score)`

## Description

`do_ocr_word_mlp` works like [`do_ocr_multi_class_mlp`](do_ocr_multi_class_mlp.md) insofar
as it computes the best class for each of the characters given by the
regions *`Character`* and the gray values *`Image`* with the
OCR classifier *`OCRHandle`*, and returns the classes in *`Class`*
and the corresponding confidences (probabilities) of the classes
in *`Confidence`*.

In contrast to [`do_ocr_multi_class_mlp`](do_ocr_multi_class_mlp.md), `do_ocr_word_mlp`
treats the group of characters as an entity which yields a *`Word`*
by concatenating the class names for each character region. This allows
to restrict the allowed classification results on a textual level by
specifying an *`Expression`* describing the expected word.

The *`Expression`* may restrict the word to belong to a predefined
lexicon created using [`create_lexicon`](create_lexicon.md) or [`import_lexicon`](import_lexicon.md),
by specifying the name of the lexicon in angular
brackets as in *'<mylexicon>'*. If the *`Expression`* is of
any other form, it is interpreted as a regular expression with the same
syntax as specified for [`tuple_regexp_match`](tuple_regexp_match.md). Note that you will
usually want to use an expression of the form
'^...$'
when using variable quantifiers like '*', to ensure that the entire word
is used in the expression. Also note that in contrast to
[`tuple_regexp_match`](tuple_regexp_match.md), `do_ocr_word_mlp` does **not**
support passing extra options in an expression tuple.

If the word derived from the best class for each character does not match
the *`Expression`*, `do_ocr_word_mlp` attempts to correct it by
considering the *`NumAlternatives`* best classes for each character.
The alternatives used are identical to those returned by
[`do_ocr_single_class_mlp`](do_ocr_single_class_mlp.md) for a single character. It does so by
testing all possible corrections for which the classification result
is changed for at most *`NumCorrections`* character regions.
Note that *`NumAlternatives`* and *`NumCorrections`* affect the
complexity of the algorithm, so that in some cases internal restrictions
are made. See the section 'Complexity' below for further information.

In case the *`Expression`* is a lexicon and the above procedure did
not yield a result, the most similar word in the lexicon is returned as long
as it requires less than *`NumCorrections`* edit operations for the
correction (see [`suggest_lexicon`](suggest_lexicon.md)).

The resulting word is graded by a *`Score`* between 0.0 (no correction
found) and 1.0 (original word correct). The *`Score`* is lowered by
adding a penalty according to the number of corrected characters and another
(minor) penalty depending on how many classes with higher confidences have
been ignored in order to match the *`Expression`*:

$$\texttt{Score}=1.0-\texttt{PenaltyCorrections}-\texttt{PenaltyAlternatives}$$
$$PenaltyCorrections = \alpha*num_corr PenaltyAlternatives = \alpha*\beta*num_alt$$ ![figure](../assets/89ef63e3079b9acf.svg)
with `num_corr` being the actual number of applied corrections and
`num_alt` the total number of discarded alternatives.
$$\alpha = \frac{1}{\text{NumCorrections} + 1} \\ \beta = \frac{1}{\text{NumCorrections} * (\text{NumAlternatives} - 1) + 2}$$ ![figure](../assets/24ee499d9eafa431.svg)

Note that this is a combinatorial score which does **not** reflect
the original *`Confidence`* of the best *`Class`*.

A string of the number
$'\setminus032'$ (alternatively
displayed as $'\setminus0x1A'$) in
*`Class`* signifies that the region has been classified as rejection
class.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Character`** (input_object)  region(-array) `→` object

Characters to be recognized.

**`Image`** (input_object)  singlechannelimage `→` object (byte / uint2)

Gray values of the characters.

**`OCRHandle`** (input_control)  ocr_mlp `→`  (handle)

Handle of the OCR classifier.

**`Expression`** (input_control)  string `→`  (string)

Expression describing the allowed word structure.

**`NumAlternatives`** (input_control)  integer `→`  (integer)

Number of classes per character considered for the
internal word correction.

Default:
3

Suggested values:
3, 4, 5

Value range:
`1
≤
NumAlternatives`

**`NumCorrections`** (input_control)  integer `→`  (integer)

Maximum number of corrected characters.

Default:
2

Suggested values:
1, 2, 3, 4, 5

Value range:
`0
≤
NumCorrections`

**`Class`** (output_control)  string(-array) `→`  (string)

Result of classifying the characters with the
MLP.

Number of elements:
Class == Character

**`Confidence`** (output_control)  real(-array) `→`  (real)

Confidence of the class of the characters.

Number of elements:
Confidence == Character

**`Word`** (output_control)  string `→`  (string)

Word text after classification and correction.

**`Score`** (output_control)  real `→`  (real)

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
`do_ocr_word_mlp` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`trainf_ocr_class_mlp`,
`read_ocr_class_mlp`

## Alternatives

`do_ocr_multi_class_mlp`

## See also

`create_ocr_class_mlp`,
`classify_class_mlp`

## Module

OCR/OCV
