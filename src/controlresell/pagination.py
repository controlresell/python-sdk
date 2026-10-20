"""Pagination by opaque cursor."""

from __future__ import annotations

from collections.abc import Callable, Iterator
from typing import Any


def paginate(fetch_page: Callable[[str | None], Any]) -> Iterator[Any]:
    """Every element of a list paginated by cursor, page after page, as it is iterated.

    ``fetch_page`` gets the cursor of the page to read (``None`` for the first one) and must send the same filters
    each time; the cursor is opaque. A page has ``data`` and ``next_cursor`` (``None`` or unset on the last one).
    """
    cursor: str | None = None
    while True:
        page = fetch_page(cursor)
        yield from page.data
        next_cursor = page.next_cursor
        if not isinstance(next_cursor, str):
            return
        cursor = next_cursor
