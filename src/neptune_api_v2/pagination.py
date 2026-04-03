# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Any, List, Generic, TypeVar, Optional, cast
from typing_extensions import Protocol, override, runtime_checkable

from ._models import BaseModel, GenericModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = [
    "SyncTxHistoryPage",
    "AsyncTxHistoryPage",
    "IntervalMultiPageData",
    "IntervalMultiPagePagination",
    "SyncIntervalMultiPage",
    "AsyncIntervalMultiPage",
    "IntervalSinglePageData",
    "IntervalSinglePagePagination",
    "SyncIntervalSinglePage",
    "AsyncIntervalSinglePage",
]

_T = TypeVar("_T")


@runtime_checkable
class TxHistoryPageItem(Protocol):
    event_uuid: str


class SyncTxHistoryPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        data = self.data
        if not data:
            return None

        item = cast(Any, data[-1])
        if not isinstance(item, TxHistoryPageItem) or item.event_uuid is None:  # pyright: ignore[reportUnnecessaryComparison]
            # TODO emit warning log
            return None

        return PageInfo(params={"prev_event_uuid": item.event_uuid})


class AsyncTxHistoryPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        data = self.data
        if not data:
            return None

        item = cast(Any, data[-1])
        if not isinstance(item, TxHistoryPageItem) or item.event_uuid is None:  # pyright: ignore[reportUnnecessaryComparison]
            # TODO emit warning log
            return None

        return PageInfo(params={"prev_event_uuid": item.event_uuid})


class IntervalMultiPagePagination(BaseModel):
    interval_count: Optional[int] = None

    next_offset: Optional[int] = None


class IntervalMultiPageData(GenericModel, Generic[_T]):
    pagination: Optional[IntervalMultiPagePagination] = None

    series: Optional[List[_T]] = None


class SyncIntervalMultiPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    data: Optional[IntervalMultiPageData[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        series = None
        if self.data is not None:
            if self.data.series is not None:
                series = self.data.series
        if not series:
            return []
        return series

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_offset = None
        if self.data is not None:
            if self.data.pagination is not None:
                if self.data.pagination.next_offset is not None:
                    next_offset = self.data.pagination.next_offset
        if next_offset is None:
            return None  # type: ignore[unreachable]

        length = len(self._get_page_items())
        current_count = next_offset + length

        interval_count = None
        if self.data is not None:
            if self.data.pagination is not None:
                if self.data.pagination.interval_count is not None:
                    interval_count = self.data.pagination.interval_count
        if interval_count is None:
            return None

        if current_count < interval_count:
            return PageInfo(params={"offset": current_count})

        return None


class AsyncIntervalMultiPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    data: Optional[IntervalMultiPageData[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        series = None
        if self.data is not None:
            if self.data.series is not None:
                series = self.data.series
        if not series:
            return []
        return series

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_offset = None
        if self.data is not None:
            if self.data.pagination is not None:
                if self.data.pagination.next_offset is not None:
                    next_offset = self.data.pagination.next_offset
        if next_offset is None:
            return None  # type: ignore[unreachable]

        length = len(self._get_page_items())
        current_count = next_offset + length

        interval_count = None
        if self.data is not None:
            if self.data.pagination is not None:
                if self.data.pagination.interval_count is not None:
                    interval_count = self.data.pagination.interval_count
        if interval_count is None:
            return None

        if current_count < interval_count:
            return PageInfo(params={"offset": current_count})

        return None


class IntervalSinglePagePagination(BaseModel):
    interval_count: Optional[int] = None

    next_offset: Optional[int] = None


class IntervalSinglePageData(GenericModel, Generic[_T]):
    pagination: Optional[IntervalSinglePagePagination] = None

    points: Optional[List[_T]] = None


class SyncIntervalSinglePage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    data: Optional[IntervalSinglePageData[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        points = None
        if self.data is not None:
            if self.data.points is not None:
                points = self.data.points
        if not points:
            return []
        return points

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_offset = None
        if self.data is not None:
            if self.data.pagination is not None:
                if self.data.pagination.next_offset is not None:
                    next_offset = self.data.pagination.next_offset
        if next_offset is None:
            return None  # type: ignore[unreachable]

        length = len(self._get_page_items())
        current_count = next_offset + length

        interval_count = None
        if self.data is not None:
            if self.data.pagination is not None:
                if self.data.pagination.interval_count is not None:
                    interval_count = self.data.pagination.interval_count
        if interval_count is None:
            return None

        if current_count < interval_count:
            return PageInfo(params={"offset": current_count})

        return None


class AsyncIntervalSinglePage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    data: Optional[IntervalSinglePageData[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        points = None
        if self.data is not None:
            if self.data.points is not None:
                points = self.data.points
        if not points:
            return []
        return points

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_offset = None
        if self.data is not None:
            if self.data.pagination is not None:
                if self.data.pagination.next_offset is not None:
                    next_offset = self.data.pagination.next_offset
        if next_offset is None:
            return None  # type: ignore[unreachable]

        length = len(self._get_page_items())
        current_count = next_offset + length

        interval_count = None
        if self.data is not None:
            if self.data.pagination is not None:
                if self.data.pagination.interval_count is not None:
                    interval_count = self.data.pagination.interval_count
        if interval_count is None:
            return None

        if current_count < interval_count:
            return PageInfo(params={"offset": current_count})

        return None
