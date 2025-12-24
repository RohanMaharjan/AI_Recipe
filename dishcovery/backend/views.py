from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

from .serializers import FoodImageSerializer
from .yolo_service import detect_food
import os
from django.conf import settings


class DetectFoodAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = FoodImageSerializer
    def post(self, request):
        print("REQUEST DATA:", request.data)  # DEBUG

        serializer = FoodImageSerializer(data=request.data)

        if not serializer.is_valid():
            print("ERRORS:", serializer.errors)  # DEBUG
            return Response(serializer.errors, status=400)

        image = serializer.validated_data['image']

        os.makedirs(settings.MEDIA_ROOT, exist_ok=True)
        
        image_path = os.path.join(settings.MEDIA_ROOT, image.name)

        with open(image_path, "wb+") as f:
            for chunk in image.chunks():
                f.write(chunk)

        detected_items = detect_food(image_path)

        return Response({"detected_items": detected_items})
