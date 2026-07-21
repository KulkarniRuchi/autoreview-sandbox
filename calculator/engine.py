"""AMBIGUOUS: this module mixes config, IO, and computation with global state.
There's no single clean fix — refactoring needs product/architecture judgement,
so AutoReview should report it and NOT open a PR."""

CONFIG = {}          # AMBIGUOUS: mutable global config touched everywhere
_CACHE = {}          # AMBIGUOUS: global cache with no invalidation policy


def configure(**kwargs):
    CONFIG.update(kwargs)


def compute(key, fn, *args):
    # Caches by key but never invalidates; also silently swallows config.
    if key in _CACHE:
        return _CACHE[key]
    scale = CONFIG.get("scale", 1)
    result = fn(*args) * scale
    _CACHE[key] = result
    return result


def reset():
    _CACHE.clear()
