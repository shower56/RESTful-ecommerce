from rest_framework.viewsets import GenericViewSet


class CustomViewSet(GenericViewSet):
    """
    Viewset에서 사전에 필요한 커스텀 기능을 작성할 수 있습니다.\
    예를 들어 `API 중복호출방지`, `log 수집` 등등의 작업을 할 수 있겠습니다.
    """

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
