from drf_spectacular.utils import extend_schema, OpenApiParameter

PRODUCT_TAG = ["상품"]

PATH_PARAMETER_PRODUCT_PK = OpenApiParameter(
    name="pk",
    type=int,
    location=OpenApiParameter.PATH,
    description="상품 id를 입력합니다.",
    required=True,
)

QUERY_PARAMETER_CATEGORY_PK = OpenApiParameter(
    name="pk",
    type=int,
    location=OpenApiParameter.QUERY,
    description="카테고리 id를 입력합니다.",
    required=False,
)

PRODUCT_LIST = extend_schema(
    tags=PRODUCT_TAG,
    description="""
    상품 목록 조회 API입니다.
    - 익명 사용자도 호출 가능
    """,
    summary="카테고리 목록 조회",
    parameters=[],
    
)

PRODUCT_RETRIEVE = extend_schema(
    tags=PRODUCT_TAG,
    description="""
    상품 상세 조회 API입니다.
    - 익명 사용자도 호출 가능
    """,
    summary="카테고리 목록 조회",
    parameters=[PATH_PARAMETER_PRODUCT_PK, QUERY_PARAMETER_CATEGORY_PK],
)
