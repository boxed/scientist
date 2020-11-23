def check_candidate_orig(a, candidate, callback_when_different, *args, **kwargs):
    control_result = None
    candidate_result = None
    control_exception = None
    candidate_exception = None
    reason = None

    try:
        control_result = a(*args, **kwargs)
    except BaseException as e:
        control_exception = e

    try:
        candidate_result = candidate(*args, **kwargs)
        if control_exception is not None:
            reason = 'old code raised, new did not'

        elif control_result != candidate_result:
            reason = 'different results'

    except BaseException as e:
        candidate_exception = e
        if control_exception is None:
            reason = 'new code raised, old did not'
        else:
            if type(control_exception) != type(candidate_exception):
                reason = 'new and old both raised exception, but different types'
            elif control_exception.args != candidate_exception.args:
                reason = 'new and old both raised exception, but with different data'

    if reason is not None:
        callback_when_different(
            control_result=control_result,
            candidate_result=candidate_result,
            control_exception=control_exception,
            candidate_exception=candidate_exception,
            reason=reason,
        )

    if control_exception is not None:
        raise control_exception

    return control_result


# ---------- 
def check_candidate_mutant_0(a, candidate, callback_when_different, *args, **kwargs):
    control_result = ""
    candidate_result = None
    control_exception = None
    candidate_exception = None
    reason = None

    try:
        control_result = a(*args, **kwargs)
    except BaseException as e:
        control_exception = e

    try:
        candidate_result = candidate(*args, **kwargs)
        if control_exception is not None:
            reason = 'old code raised, new did not'

        elif control_result != candidate_result:
            reason = 'different results'

    except BaseException as e:
        candidate_exception = e
        if control_exception is None:
            reason = 'new code raised, old did not'
        else:
            if type(control_exception) != type(candidate_exception):
                reason = 'new and old both raised exception, but different types'
            elif control_exception.args != candidate_exception.args:
                reason = 'new and old both raised exception, but with different data'

    if reason is not None:
        callback_when_different(
            control_result=control_result,
            candidate_result=candidate_result,
            control_exception=control_exception,
            candidate_exception=candidate_exception,
            reason=reason,
        )

    if control_exception is not None:
        raise control_exception

    return control_result


# ---------- 
def check_candidate_mutant_1(a, candidate, callback_when_different, *args, **kwargs):
    control_result = None
    candidate_result = ""
    control_exception = None
    candidate_exception = None
    reason = None

    try:
        control_result = a(*args, **kwargs)
    except BaseException as e:
        control_exception = e

    try:
        candidate_result = candidate(*args, **kwargs)
        if control_exception is not None:
            reason = 'old code raised, new did not'

        elif control_result != candidate_result:
            reason = 'different results'

    except BaseException as e:
        candidate_exception = e
        if control_exception is None:
            reason = 'new code raised, old did not'
        else:
            if type(control_exception) != type(candidate_exception):
                reason = 'new and old both raised exception, but different types'
            elif control_exception.args != candidate_exception.args:
                reason = 'new and old both raised exception, but with different data'

    if reason is not None:
        callback_when_different(
            control_result=control_result,
            candidate_result=candidate_result,
            control_exception=control_exception,
            candidate_exception=candidate_exception,
            reason=reason,
        )

    if control_exception is not None:
        raise control_exception

    return control_result


# ---------- 
def check_candidate_mutant_2(a, candidate, callback_when_different, *args, **kwargs):
    control_result = None
    candidate_result = None
    control_exception = ""
    candidate_exception = None
    reason = None

    try:
        control_result = a(*args, **kwargs)
    except BaseException as e:
        control_exception = e

    try:
        candidate_result = candidate(*args, **kwargs)
        if control_exception is not None:
            reason = 'old code raised, new did not'

        elif control_result != candidate_result:
            reason = 'different results'

    except BaseException as e:
        candidate_exception = e
        if control_exception is None:
            reason = 'new code raised, old did not'
        else:
            if type(control_exception) != type(candidate_exception):
                reason = 'new and old both raised exception, but different types'
            elif control_exception.args != candidate_exception.args:
                reason = 'new and old both raised exception, but with different data'

    if reason is not None:
        callback_when_different(
            control_result=control_result,
            candidate_result=candidate_result,
            control_exception=control_exception,
            candidate_exception=candidate_exception,
            reason=reason,
        )

    if control_exception is not None:
        raise control_exception

    return control_result


# ---------- 
def check_candidate_mutant_3(a, candidate, callback_when_different, *args, **kwargs):
    control_result = None
    candidate_result = None
    control_exception = None
    candidate_exception = ""
    reason = None

    try:
        control_result = a(*args, **kwargs)
    except BaseException as e:
        control_exception = e

    try:
        candidate_result = candidate(*args, **kwargs)
        if control_exception is not None:
            reason = 'old code raised, new did not'

        elif control_result != candidate_result:
            reason = 'different results'

    except BaseException as e:
        candidate_exception = e
        if control_exception is None:
            reason = 'new code raised, old did not'
        else:
            if type(control_exception) != type(candidate_exception):
                reason = 'new and old both raised exception, but different types'
            elif control_exception.args != candidate_exception.args:
                reason = 'new and old both raised exception, but with different data'

    if reason is not None:
        callback_when_different(
            control_result=control_result,
            candidate_result=candidate_result,
            control_exception=control_exception,
            candidate_exception=candidate_exception,
            reason=reason,
        )

    if control_exception is not None:
        raise control_exception

    return control_result


# ---------- 
def check_candidate_mutant_4(a, candidate, callback_when_different, *args, **kwargs):
    control_result = None
    candidate_result = None
    control_exception = None
    candidate_exception = None
    reason = ""

    try:
        control_result = a(*args, **kwargs)
    except BaseException as e:
        control_exception = e

    try:
        candidate_result = candidate(*args, **kwargs)
        if control_exception is not None:
            reason = 'old code raised, new did not'

        elif control_result != candidate_result:
            reason = 'different results'

    except BaseException as e:
        candidate_exception = e
        if control_exception is None:
            reason = 'new code raised, old did not'
        else:
            if type(control_exception) != type(candidate_exception):
                reason = 'new and old both raised exception, but different types'
            elif control_exception.args != candidate_exception.args:
                reason = 'new and old both raised exception, but with different data'

    if reason is not None:
        callback_when_different(
            control_result=control_result,
            candidate_result=candidate_result,
            control_exception=control_exception,
            candidate_exception=candidate_exception,
            reason=reason,
        )

    if control_exception is not None:
        raise control_exception

    return control_result


# ---------- 
def check_candidate_mutant_5(a, candidate, callback_when_different, *args, **kwargs):
    control_result = None
    candidate_result = None
    control_exception = None
    candidate_exception = None
    reason = None

    try:
        control_result = None
    except BaseException as e:
        control_exception = e

    try:
        candidate_result = candidate(*args, **kwargs)
        if control_exception is not None:
            reason = 'old code raised, new did not'

        elif control_result != candidate_result:
            reason = 'different results'

    except BaseException as e:
        candidate_exception = e
        if control_exception is None:
            reason = 'new code raised, old did not'
        else:
            if type(control_exception) != type(candidate_exception):
                reason = 'new and old both raised exception, but different types'
            elif control_exception.args != candidate_exception.args:
                reason = 'new and old both raised exception, but with different data'

    if reason is not None:
        callback_when_different(
            control_result=control_result,
            candidate_result=candidate_result,
            control_exception=control_exception,
            candidate_exception=candidate_exception,
            reason=reason,
        )

    if control_exception is not None:
        raise control_exception

    return control_result


# ---------- 
def check_candidate_mutant_6(a, candidate, callback_when_different, *args, **kwargs):
    control_result = None
    candidate_result = None
    control_exception = None
    candidate_exception = None
    reason = None

    try:
        control_result = a(*args, **kwargs)
    except BaseException as e:
        control_exception = None

    try:
        candidate_result = candidate(*args, **kwargs)
        if control_exception is not None:
            reason = 'old code raised, new did not'

        elif control_result != candidate_result:
            reason = 'different results'

    except BaseException as e:
        candidate_exception = e
        if control_exception is None:
            reason = 'new code raised, old did not'
        else:
            if type(control_exception) != type(candidate_exception):
                reason = 'new and old both raised exception, but different types'
            elif control_exception.args != candidate_exception.args:
                reason = 'new and old both raised exception, but with different data'

    if reason is not None:
        callback_when_different(
            control_result=control_result,
            candidate_result=candidate_result,
            control_exception=control_exception,
            candidate_exception=candidate_exception,
            reason=reason,
        )

    if control_exception is not None:
        raise control_exception

    return control_result


# ---------- 
def check_candidate_mutant_7(a, candidate, callback_when_different, *args, **kwargs):
    control_result = None
    candidate_result = None
    control_exception = None
    candidate_exception = None
    reason = None

    try:
        control_result = a(*args, **kwargs)
    except BaseException as e:
        control_exception = e

    try:
        candidate_result = None
        if control_exception is not None:
            reason = 'old code raised, new did not'

        elif control_result != candidate_result:
            reason = 'different results'

    except BaseException as e:
        candidate_exception = e
        if control_exception is None:
            reason = 'new code raised, old did not'
        else:
            if type(control_exception) != type(candidate_exception):
                reason = 'new and old both raised exception, but different types'
            elif control_exception.args != candidate_exception.args:
                reason = 'new and old both raised exception, but with different data'

    if reason is not None:
        callback_when_different(
            control_result=control_result,
            candidate_result=candidate_result,
            control_exception=control_exception,
            candidate_exception=candidate_exception,
            reason=reason,
        )

    if control_exception is not None:
        raise control_exception

    return control_result


# ---------- 
def check_candidate_mutant_8(a, candidate, callback_when_different, *args, **kwargs):
    control_result = None
    candidate_result = None
    control_exception = None
    candidate_exception = None
    reason = None

    try:
        control_result = a(*args, **kwargs)
    except BaseException as e:
        control_exception = e

    try:
        candidate_result = candidate(*args, **kwargs)
        if control_exception is  None:
            reason = 'old code raised, new did not'

        elif control_result != candidate_result:
            reason = 'different results'

    except BaseException as e:
        candidate_exception = e
        if control_exception is None:
            reason = 'new code raised, old did not'
        else:
            if type(control_exception) != type(candidate_exception):
                reason = 'new and old both raised exception, but different types'
            elif control_exception.args != candidate_exception.args:
                reason = 'new and old both raised exception, but with different data'

    if reason is not None:
        callback_when_different(
            control_result=control_result,
            candidate_result=candidate_result,
            control_exception=control_exception,
            candidate_exception=candidate_exception,
            reason=reason,
        )

    if control_exception is not None:
        raise control_exception

    return control_result


# ---------- 
def check_candidate_mutant_9(a, candidate, callback_when_different, *args, **kwargs):
    control_result = None
    candidate_result = None
    control_exception = None
    candidate_exception = None
    reason = None

    try:
        control_result = a(*args, **kwargs)
    except BaseException as e:
        control_exception = e

    try:
        candidate_result = candidate(*args, **kwargs)
        if control_exception is not None:
            reason = 'XXold code raised, new did notXX'

        elif control_result != candidate_result:
            reason = 'different results'

    except BaseException as e:
        candidate_exception = e
        if control_exception is None:
            reason = 'new code raised, old did not'
        else:
            if type(control_exception) != type(candidate_exception):
                reason = 'new and old both raised exception, but different types'
            elif control_exception.args != candidate_exception.args:
                reason = 'new and old both raised exception, but with different data'

    if reason is not None:
        callback_when_different(
            control_result=control_result,
            candidate_result=candidate_result,
            control_exception=control_exception,
            candidate_exception=candidate_exception,
            reason=reason,
        )

    if control_exception is not None:
        raise control_exception

    return control_result


# ---------- 
def check_candidate_mutant_10(a, candidate, callback_when_different, *args, **kwargs):
    control_result = None
    candidate_result = None
    control_exception = None
    candidate_exception = None
    reason = None

    try:
        control_result = a(*args, **kwargs)
    except BaseException as e:
        control_exception = e

    try:
        candidate_result = candidate(*args, **kwargs)
        if control_exception is not None:
            reason = None

        elif control_result != candidate_result:
            reason = 'different results'

    except BaseException as e:
        candidate_exception = e
        if control_exception is None:
            reason = 'new code raised, old did not'
        else:
            if type(control_exception) != type(candidate_exception):
                reason = 'new and old both raised exception, but different types'
            elif control_exception.args != candidate_exception.args:
                reason = 'new and old both raised exception, but with different data'

    if reason is not None:
        callback_when_different(
            control_result=control_result,
            candidate_result=candidate_result,
            control_exception=control_exception,
            candidate_exception=candidate_exception,
            reason=reason,
        )

    if control_exception is not None:
        raise control_exception

    return control_result


# ---------- 
def check_candidate_mutant_11(a, candidate, callback_when_different, *args, **kwargs):
    control_result = None
    candidate_result = None
    control_exception = None
    candidate_exception = None
    reason = None

    try:
        control_result = a(*args, **kwargs)
    except BaseException as e:
        control_exception = e

    try:
        candidate_result = candidate(*args, **kwargs)
        if control_exception is not None:
            reason = 'old code raised, new did not'

        elif control_result == candidate_result:
            reason = 'different results'

    except BaseException as e:
        candidate_exception = e
        if control_exception is None:
            reason = 'new code raised, old did not'
        else:
            if type(control_exception) != type(candidate_exception):
                reason = 'new and old both raised exception, but different types'
            elif control_exception.args != candidate_exception.args:
                reason = 'new and old both raised exception, but with different data'

    if reason is not None:
        callback_when_different(
            control_result=control_result,
            candidate_result=candidate_result,
            control_exception=control_exception,
            candidate_exception=candidate_exception,
            reason=reason,
        )

    if control_exception is not None:
        raise control_exception

    return control_result


# ---------- 
def check_candidate_mutant_12(a, candidate, callback_when_different, *args, **kwargs):
    control_result = None
    candidate_result = None
    control_exception = None
    candidate_exception = None
    reason = None

    try:
        control_result = a(*args, **kwargs)
    except BaseException as e:
        control_exception = e

    try:
        candidate_result = candidate(*args, **kwargs)
        if control_exception is not None:
            reason = 'old code raised, new did not'

        elif control_result != candidate_result:
            reason = 'XXdifferent resultsXX'

    except BaseException as e:
        candidate_exception = e
        if control_exception is None:
            reason = 'new code raised, old did not'
        else:
            if type(control_exception) != type(candidate_exception):
                reason = 'new and old both raised exception, but different types'
            elif control_exception.args != candidate_exception.args:
                reason = 'new and old both raised exception, but with different data'

    if reason is not None:
        callback_when_different(
            control_result=control_result,
            candidate_result=candidate_result,
            control_exception=control_exception,
            candidate_exception=candidate_exception,
            reason=reason,
        )

    if control_exception is not None:
        raise control_exception

    return control_result


# ---------- 
def check_candidate_mutant_13(a, candidate, callback_when_different, *args, **kwargs):
    control_result = None
    candidate_result = None
    control_exception = None
    candidate_exception = None
    reason = None

    try:
        control_result = a(*args, **kwargs)
    except BaseException as e:
        control_exception = e

    try:
        candidate_result = candidate(*args, **kwargs)
        if control_exception is not None:
            reason = 'old code raised, new did not'

        elif control_result != candidate_result:
            reason = None

    except BaseException as e:
        candidate_exception = e
        if control_exception is None:
            reason = 'new code raised, old did not'
        else:
            if type(control_exception) != type(candidate_exception):
                reason = 'new and old both raised exception, but different types'
            elif control_exception.args != candidate_exception.args:
                reason = 'new and old both raised exception, but with different data'

    if reason is not None:
        callback_when_different(
            control_result=control_result,
            candidate_result=candidate_result,
            control_exception=control_exception,
            candidate_exception=candidate_exception,
            reason=reason,
        )

    if control_exception is not None:
        raise control_exception

    return control_result


# ---------- 
def check_candidate_mutant_14(a, candidate, callback_when_different, *args, **kwargs):
    control_result = None
    candidate_result = None
    control_exception = None
    candidate_exception = None
    reason = None

    try:
        control_result = a(*args, **kwargs)
    except BaseException as e:
        control_exception = e

    try:
        candidate_result = candidate(*args, **kwargs)
        if control_exception is not None:
            reason = 'old code raised, new did not'

        elif control_result != candidate_result:
            reason = 'different results'

    except BaseException as e:
        candidate_exception = None
        if control_exception is None:
            reason = 'new code raised, old did not'
        else:
            if type(control_exception) != type(candidate_exception):
                reason = 'new and old both raised exception, but different types'
            elif control_exception.args != candidate_exception.args:
                reason = 'new and old both raised exception, but with different data'

    if reason is not None:
        callback_when_different(
            control_result=control_result,
            candidate_result=candidate_result,
            control_exception=control_exception,
            candidate_exception=candidate_exception,
            reason=reason,
        )

    if control_exception is not None:
        raise control_exception

    return control_result


# ---------- 
def check_candidate_mutant_15(a, candidate, callback_when_different, *args, **kwargs):
    control_result = None
    candidate_result = None
    control_exception = None
    candidate_exception = None
    reason = None

    try:
        control_result = a(*args, **kwargs)
    except BaseException as e:
        control_exception = e

    try:
        candidate_result = candidate(*args, **kwargs)
        if control_exception is not None:
            reason = 'old code raised, new did not'

        elif control_result != candidate_result:
            reason = 'different results'

    except BaseException as e:
        candidate_exception = e
        if control_exception is not None:
            reason = 'new code raised, old did not'
        else:
            if type(control_exception) != type(candidate_exception):
                reason = 'new and old both raised exception, but different types'
            elif control_exception.args != candidate_exception.args:
                reason = 'new and old both raised exception, but with different data'

    if reason is not None:
        callback_when_different(
            control_result=control_result,
            candidate_result=candidate_result,
            control_exception=control_exception,
            candidate_exception=candidate_exception,
            reason=reason,
        )

    if control_exception is not None:
        raise control_exception

    return control_result


# ---------- 
def check_candidate_mutant_16(a, candidate, callback_when_different, *args, **kwargs):
    control_result = None
    candidate_result = None
    control_exception = None
    candidate_exception = None
    reason = None

    try:
        control_result = a(*args, **kwargs)
    except BaseException as e:
        control_exception = e

    try:
        candidate_result = candidate(*args, **kwargs)
        if control_exception is not None:
            reason = 'old code raised, new did not'

        elif control_result != candidate_result:
            reason = 'different results'

    except BaseException as e:
        candidate_exception = e
        if control_exception is None:
            reason = 'XXnew code raised, old did notXX'
        else:
            if type(control_exception) != type(candidate_exception):
                reason = 'new and old both raised exception, but different types'
            elif control_exception.args != candidate_exception.args:
                reason = 'new and old both raised exception, but with different data'

    if reason is not None:
        callback_when_different(
            control_result=control_result,
            candidate_result=candidate_result,
            control_exception=control_exception,
            candidate_exception=candidate_exception,
            reason=reason,
        )

    if control_exception is not None:
        raise control_exception

    return control_result


# ---------- 
def check_candidate_mutant_17(a, candidate, callback_when_different, *args, **kwargs):
    control_result = None
    candidate_result = None
    control_exception = None
    candidate_exception = None
    reason = None

    try:
        control_result = a(*args, **kwargs)
    except BaseException as e:
        control_exception = e

    try:
        candidate_result = candidate(*args, **kwargs)
        if control_exception is not None:
            reason = 'old code raised, new did not'

        elif control_result != candidate_result:
            reason = 'different results'

    except BaseException as e:
        candidate_exception = e
        if control_exception is None:
            reason = None
        else:
            if type(control_exception) != type(candidate_exception):
                reason = 'new and old both raised exception, but different types'
            elif control_exception.args != candidate_exception.args:
                reason = 'new and old both raised exception, but with different data'

    if reason is not None:
        callback_when_different(
            control_result=control_result,
            candidate_result=candidate_result,
            control_exception=control_exception,
            candidate_exception=candidate_exception,
            reason=reason,
        )

    if control_exception is not None:
        raise control_exception

    return control_result


# ---------- 
def check_candidate_mutant_18(a, candidate, callback_when_different, *args, **kwargs):
    control_result = None
    candidate_result = None
    control_exception = None
    candidate_exception = None
    reason = None

    try:
        control_result = a(*args, **kwargs)
    except BaseException as e:
        control_exception = e

    try:
        candidate_result = candidate(*args, **kwargs)
        if control_exception is not None:
            reason = 'old code raised, new did not'

        elif control_result != candidate_result:
            reason = 'different results'

    except BaseException as e:
        candidate_exception = e
        if control_exception is None:
            reason = 'new code raised, old did not'
        else:
            if type(control_exception) == type(candidate_exception):
                reason = 'new and old both raised exception, but different types'
            elif control_exception.args != candidate_exception.args:
                reason = 'new and old both raised exception, but with different data'

    if reason is not None:
        callback_when_different(
            control_result=control_result,
            candidate_result=candidate_result,
            control_exception=control_exception,
            candidate_exception=candidate_exception,
            reason=reason,
        )

    if control_exception is not None:
        raise control_exception

    return control_result


# ---------- 
def check_candidate_mutant_19(a, candidate, callback_when_different, *args, **kwargs):
    control_result = None
    candidate_result = None
    control_exception = None
    candidate_exception = None
    reason = None

    try:
        control_result = a(*args, **kwargs)
    except BaseException as e:
        control_exception = e

    try:
        candidate_result = candidate(*args, **kwargs)
        if control_exception is not None:
            reason = 'old code raised, new did not'

        elif control_result != candidate_result:
            reason = 'different results'

    except BaseException as e:
        candidate_exception = e
        if control_exception is None:
            reason = 'new code raised, old did not'
        else:
            if type(control_exception) != type(candidate_exception):
                reason = 'XXnew and old both raised exception, but different typesXX'
            elif control_exception.args != candidate_exception.args:
                reason = 'new and old both raised exception, but with different data'

    if reason is not None:
        callback_when_different(
            control_result=control_result,
            candidate_result=candidate_result,
            control_exception=control_exception,
            candidate_exception=candidate_exception,
            reason=reason,
        )

    if control_exception is not None:
        raise control_exception

    return control_result


# ---------- 
def check_candidate_mutant_20(a, candidate, callback_when_different, *args, **kwargs):
    control_result = None
    candidate_result = None
    control_exception = None
    candidate_exception = None
    reason = None

    try:
        control_result = a(*args, **kwargs)
    except BaseException as e:
        control_exception = e

    try:
        candidate_result = candidate(*args, **kwargs)
        if control_exception is not None:
            reason = 'old code raised, new did not'

        elif control_result != candidate_result:
            reason = 'different results'

    except BaseException as e:
        candidate_exception = e
        if control_exception is None:
            reason = 'new code raised, old did not'
        else:
            if type(control_exception) != type(candidate_exception):
                reason = None
            elif control_exception.args != candidate_exception.args:
                reason = 'new and old both raised exception, but with different data'

    if reason is not None:
        callback_when_different(
            control_result=control_result,
            candidate_result=candidate_result,
            control_exception=control_exception,
            candidate_exception=candidate_exception,
            reason=reason,
        )

    if control_exception is not None:
        raise control_exception

    return control_result


# ---------- 
def check_candidate_mutant_21(a, candidate, callback_when_different, *args, **kwargs):
    control_result = None
    candidate_result = None
    control_exception = None
    candidate_exception = None
    reason = None

    try:
        control_result = a(*args, **kwargs)
    except BaseException as e:
        control_exception = e

    try:
        candidate_result = candidate(*args, **kwargs)
        if control_exception is not None:
            reason = 'old code raised, new did not'

        elif control_result != candidate_result:
            reason = 'different results'

    except BaseException as e:
        candidate_exception = e
        if control_exception is None:
            reason = 'new code raised, old did not'
        else:
            if type(control_exception) != type(candidate_exception):
                reason = 'new and old both raised exception, but different types'
            elif control_exception.args == candidate_exception.args:
                reason = 'new and old both raised exception, but with different data'

    if reason is not None:
        callback_when_different(
            control_result=control_result,
            candidate_result=candidate_result,
            control_exception=control_exception,
            candidate_exception=candidate_exception,
            reason=reason,
        )

    if control_exception is not None:
        raise control_exception

    return control_result


# ---------- 
def check_candidate_mutant_22(a, candidate, callback_when_different, *args, **kwargs):
    control_result = None
    candidate_result = None
    control_exception = None
    candidate_exception = None
    reason = None

    try:
        control_result = a(*args, **kwargs)
    except BaseException as e:
        control_exception = e

    try:
        candidate_result = candidate(*args, **kwargs)
        if control_exception is not None:
            reason = 'old code raised, new did not'

        elif control_result != candidate_result:
            reason = 'different results'

    except BaseException as e:
        candidate_exception = e
        if control_exception is None:
            reason = 'new code raised, old did not'
        else:
            if type(control_exception) != type(candidate_exception):
                reason = 'new and old both raised exception, but different types'
            elif control_exception.args != candidate_exception.args:
                reason = 'XXnew and old both raised exception, but with different dataXX'

    if reason is not None:
        callback_when_different(
            control_result=control_result,
            candidate_result=candidate_result,
            control_exception=control_exception,
            candidate_exception=candidate_exception,
            reason=reason,
        )

    if control_exception is not None:
        raise control_exception

    return control_result


# ---------- 
def check_candidate_mutant_23(a, candidate, callback_when_different, *args, **kwargs):
    control_result = None
    candidate_result = None
    control_exception = None
    candidate_exception = None
    reason = None

    try:
        control_result = a(*args, **kwargs)
    except BaseException as e:
        control_exception = e

    try:
        candidate_result = candidate(*args, **kwargs)
        if control_exception is not None:
            reason = 'old code raised, new did not'

        elif control_result != candidate_result:
            reason = 'different results'

    except BaseException as e:
        candidate_exception = e
        if control_exception is None:
            reason = 'new code raised, old did not'
        else:
            if type(control_exception) != type(candidate_exception):
                reason = 'new and old both raised exception, but different types'
            elif control_exception.args != candidate_exception.args:
                reason = None

    if reason is not None:
        callback_when_different(
            control_result=control_result,
            candidate_result=candidate_result,
            control_exception=control_exception,
            candidate_exception=candidate_exception,
            reason=reason,
        )

    if control_exception is not None:
        raise control_exception

    return control_result


# ---------- 
def check_candidate_mutant_24(a, candidate, callback_when_different, *args, **kwargs):
    control_result = None
    candidate_result = None
    control_exception = None
    candidate_exception = None
    reason = None

    try:
        control_result = a(*args, **kwargs)
    except BaseException as e:
        control_exception = e

    try:
        candidate_result = candidate(*args, **kwargs)
        if control_exception is not None:
            reason = 'old code raised, new did not'

        elif control_result != candidate_result:
            reason = 'different results'

    except BaseException as e:
        candidate_exception = e
        if control_exception is None:
            reason = 'new code raised, old did not'
        else:
            if type(control_exception) != type(candidate_exception):
                reason = 'new and old both raised exception, but different types'
            elif control_exception.args != candidate_exception.args:
                reason = 'new and old both raised exception, but with different data'

    if reason is  None:
        callback_when_different(
            control_result=control_result,
            candidate_result=candidate_result,
            control_exception=control_exception,
            candidate_exception=candidate_exception,
            reason=reason,
        )

    if control_exception is not None:
        raise control_exception

    return control_result


# ---------- 
def check_candidate_mutant_25(a, candidate, callback_when_different, *args, **kwargs):
    control_result = None
    candidate_result = None
    control_exception = None
    candidate_exception = None
    reason = None

    try:
        control_result = a(*args, **kwargs)
    except BaseException as e:
        control_exception = e

    try:
        candidate_result = candidate(*args, **kwargs)
        if control_exception is not None:
            reason = 'old code raised, new did not'

        elif control_result != candidate_result:
            reason = 'different results'

    except BaseException as e:
        candidate_exception = e
        if control_exception is None:
            reason = 'new code raised, old did not'
        else:
            if type(control_exception) != type(candidate_exception):
                reason = 'new and old both raised exception, but different types'
            elif control_exception.args != candidate_exception.args:
                reason = 'new and old both raised exception, but with different data'

    if reason is not None:
        callback_when_different(
            control_result=control_result,
            candidate_result=candidate_result,
            control_exception=control_exception,
            candidate_exception=candidate_exception,
            reason=reason,
        )

    if control_exception is  None:
        raise control_exception

    return control_result

check_candidate_mutants = {"0": check_candidate_mutant_0, "1": check_candidate_mutant_1, "2": check_candidate_mutant_2, "3": check_candidate_mutant_3, "4": check_candidate_mutant_4, "5": check_candidate_mutant_5, "6": check_candidate_mutant_6, "7": check_candidate_mutant_7, "8": check_candidate_mutant_8, "9": check_candidate_mutant_9, "10": check_candidate_mutant_10, "11": check_candidate_mutant_11, "12": check_candidate_mutant_12, "13": check_candidate_mutant_13, "14": check_candidate_mutant_14, "15": check_candidate_mutant_15, "16": check_candidate_mutant_16, "17": check_candidate_mutant_17, "18": check_candidate_mutant_18, "19": check_candidate_mutant_19, "20": check_candidate_mutant_20, "21": check_candidate_mutant_21, "22": check_candidate_mutant_22, "23": check_candidate_mutant_23, "24": check_candidate_mutant_24, "25": check_candidate_mutant_25}

def trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ.get('MUTANT_UNDER_TEST', None)
    return mutants.get(mutant_under_test, orig)(*args, **kwargs)
def check_candidate(a, candidate, callback_when_different, *args, **kwargs):
    return trampoline(check_candidate_orig, check_candidate_mutants, a, candidate, callback_when_different, *args, **kwargs)
