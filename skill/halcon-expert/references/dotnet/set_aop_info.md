# SetAopInfo (Operator)

## Name

`SetAopInfo` — Set AOP information for operators.

## Signature

`static void HOperatorSet.SetAopInfo(HTuple operatorName, HTuple indexName, HTuple indexValue, HTuple infoName, HTuple infoValue)`

`static void HSystem.SetAopInfo(HTuple operatorName, HTuple indexName, HTuple indexValue, string infoName, HTuple infoValue)`

`static void HSystem.SetAopInfo(string operatorName, string indexName, string indexValue, string infoName, int infoValue)`

## Description

HALCON supports a mechanism to adapt the behavior of automatic
parallelization of image processing operators (AOP) to the machine's
hardware capability. The
information for this adaption can be obtained by the operator
[`OptimizeAop`](optimize_aop.md) and can also be partly read by the operator
`SetAopInfo`.

To address specific AOP information the operator's optimization data
is indexed within
a 3-ary hierarchy that can be obtained by [`QueryAopInfo`](query_aop_info.md). The
three hierarchy stages are indexed by the operator name, passed in
*`operatorName`*, the iconic type, and
a parameter string value denoting a special mode or method supported by
the indexed operator. The latter two indices are passed by
*`indexName`*
and *`indexValue`*. *`indexName`* holds the dimension
identifier whereas *`indexValue`* addresses the index as returned
in [`QueryAopInfo`](query_aop_info.md). It is also possible to address multiple indices
on the same stage to set a specific information value to multiple knowledge
sets. Omitting an index name or passing an empty string as index value
addresses this stage in all. E.g., passing *""* to
*`operatorName`*, the tuple *["iconic_type","iconic_type"]* to
*`indexName`*, and the tuple *["byte","uint2"]* to
*`indexValue`* addresses all operators processing byte or uint2
images.

`SetAopInfo` sets the specific information parts of an operator's
AOP knowledge passed in *`infoValue`*. The scope of information is
specified by *`infoName`* and supports the following:

- ***"max_threads"*** —

  sets the maximum allowed thread number
  this operator is allowed to run with the specified iconic type and
  parameter value.
- ***"split_level"*** —

  sets the allowed data
  split levels of the automatic parallelization for this operator, the
  specified iconic type and parameter value. Possible levels are
  *"split_tuple"*, *"split_channel"*,
  *"split_domain"*, and *"split_partial"*.

## Attention

`SetAopInfo` modifies the AOP system knowledge. These modifications
will also be stored by [`WriteAopKnowledge`](write_aop_knowledge.md). It is advisable to
have a backup knowledge file before modifying the system knowledge.

## Execution Information

- Multithreading type: exclusive (runs in parallel only with independent operators).
- Multithreading scope: local (may only be called from the same thread in which the window, model, or tool instance was created).
- Processed without parallelization.

## Parameters

**`operatorName`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string* / int / long)

Operator to set information to

Default:
""

**`indexName`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string* / int / long)

Further specific index

Default:
""

Suggested values:
"iconic_type", ["iconic_type","parameter:0"]

**`indexValue`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string* / int / long)

Further specific address

Number of elements:
IndexName == IndexValue

Default:
""

Suggested values:
"byte", ["uint2",""]

**`infoName`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Scope of information

Default:
"max_threads"

Suggested values:
"max_threads", "model"

**`infoValue`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

AOP information value

## Result

`SetAopInfo` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If necessary, an exception is raised.

## Module

Foundation
