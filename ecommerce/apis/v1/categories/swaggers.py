from drf_spectacular.utils import extend_schema

CATEGORY_TAG = ["카테고리"]

CATEGORY_LIST = extend_schema(
    tags=CATEGORY_TAG,
    description="""
    카테고리 목록 조회 API입니다.
    - 익명 사용자도 호출 가능
    """,
    summary="카테고리 목록 조회",
    parameters=[],
)
