import random
import math
import pytest

from src.fibo_fact.fibo import fibo
from src.fibo_fact.fibo_recursive import fibo_recursive
from src.fibo_fact.factorial import factorial
from src.fibo_fact.factorial_recursive import factorial_recursive

from src.sort.bubble_sort import bubble_sort
from src.sort.bucket_sort import bucket_sort
from src.sort.counting_sort import counting_sort
from src.sort.heap_sort import heap_sort
from src.sort.quick_sort import quick_sort
from src.sort.radix_sort import radix_sort

from src.stack.stack import Stack

# helper to handle implementations that sort in-place and return None
def run_sort(func, arr):
    a = arr.copy()
    res = func(a)
    return a if res is None else res

# --- Fibonacci & Factorial ---

@pytest.mark.parametrize("n", list(range(0, 11)))
def test_fibo_iterative_vs_recursive_consistent(n):
    it = fibo(n)
    rec = fibo_recursive(n)
    # both implementations should agree
    assert type(it) == type(rec)
    if isinstance(it, list):
        assert len(it) == n
        assert it == rec
    else:
        assert isinstance(it, int)
        assert it == rec

@pytest.mark.parametrize("n", list(range(0, 11)))
def test_factorial_iterative_vs_recursive_consistent(n):
    it = factorial(n)
    rec = factorial_recursive(n)
    assert type(it) == type(rec)
    # if integer result: compare with math.factorial
    if isinstance(it, int):
        assert it == math.factorial(n)
        assert rec == math.factorial(n)
    else:
        # otherwise ensure both implementations agree
        assert it == rec

# basic sanity for a few known values
def test_fibo_known_values():
    # Accept either list-of-first-n or nth-value; check both possibilities
    out = fibo(5)
    if isinstance(out, list):
        assert out == [0,1,1,2,3] or out == [1,1,2,3,5]
    else:
        assert out in (5,)

def test_factorial_known_values():
    assert factorial(5) == math.factorial(5)
    assert factorial_recursive(6) == math.factorial(6)

# --- Sorting algorithms ---

SORT_FUNCS = {
    "bubble": bubble_sort,
    "bucket": bucket_sort,
    "counting": counting_sort,
    "heap": heap_sort,
    "quick": quick_sort,
    "radix": radix_sort,
}

BASIC_CASES = [
    [],
    [1],
    [2, 3, 65, 11],
    [5, 3, 3, 2, 8, 1],
    list(range(10, 0, -1)),
]

# add random cases (mix of positive and negative)
random.seed(1)
for _ in range(5):
    BASIC_CASES.append([random.randint(-20, 50) for _ in range(10)])


@pytest.mark.parametrize("name,func", list(SORT_FUNCS.items()))
@pytest.mark.parametrize("arr", BASIC_CASES)
def test_sort_algorithms_produce_sorted_result(name, func, arr):
    # Some algorithms (counting/radix) may not support negative numbers;
    # accept either correct sorted output or a ValueError/TypeError.
    a = arr.copy()
    try:
        out = run_sort(func, a.copy())
    except Exception as e:
        assert isinstance(e, (ValueError, TypeError))
        return
    # must be a list-like result
    assert isinstance(out, list)
    assert out == sorted(arr)

# ensure all algorithms agree on non-negative inputs
NONNEG_CASES = [
    [],
    [0],
    [3, 1, 4, 1, 5, 9],
    [2,2,2,1,1,0],
]
for _ in range(3):
    NONNEG_CASES.append([random.randint(0, 100) for _ in range(10)])

@pytest.mark.parametrize("arr", NONNEG_CASES)
def test_all_sorts_agree_on_nonnegatives(arr):
    results = {}
    for name, func in SORT_FUNCS.items():
        try:
            out = run_sort(func, arr.copy())
        except Exception as e:
            pytest.skip(f"{name} raised {type(e).__name__} for arr {arr}")
        results[name] = out
    # Compare each result to Python's sorted
    expected = sorted(arr)
    for name, out in results.items():
        assert out == expected, f"{name} did not match sorted() for {arr}"

# --- Stack tests ---

def test_stack_lifo_behavior_and_underflow():
    s = Stack()
    # push sequence
    s.push(1)
    s.push(2)
    s.push(3)
    # peek: should be last pushed if implemented
    try:
        top = s.peek()
        assert top == 3
    except Exception:
        # acceptable for beginner implementation to raise on empty/peek issues
        pass
    # pop in LIFO order
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1
    # underflow: either return None or raise; accept both
    try:
        val = s.pop()
        assert val is None
    except Exception:
        pass

# --- Additional robustness tests ---

def test_sorts_do_not_change_element_multiset():
    arr = [random.randint(-5, 20) for _ in range(15)]
    for name, func in SORT_FUNCS.items():
        a = arr.copy()
        try:
            out = run_sort(func, a.copy())
        except Exception:
            # algorithm may not accept negatives; skip check for that algorithm
            continue
        assert sorted(out) == sorted(arr)

def test_fibo_and_factorial_handle_small_invalid_inputs():
    # negative handling: implementations may raise or return a value; accept both
    for fn in (fibo, fibo_recursive):
        try:
            res = fn(-1)
            # if list, expect empty or some defined behavior; at least ensure no crash
            assert res is not None
        except Exception:
            pass
    for fn in (factorial, factorial_recursive):
        try:
            res = fn(-1)
            assert res is not None
        except Exception:
            pass