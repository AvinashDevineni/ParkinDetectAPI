from django.http import JsonResponse
from rest_framework.decorators import api_view

from skimage.feature import hog, canny
import cv2
import pickle

from .models import UploadFileForm
from .serializers import UploadFileFormSerializer

@api_view(['POST'])
def get_model_response(request):
    imgType: str = request.GET.get('type', '')

    if (imgType == ''):
        return JsonResponse({'error': 'no type provided'})
    
    imgType = imgType.lower()
    if (imgType != 'spiral' and imgType != 'wave'):
        return JsonResponse({'error': 'invalid type provided'})
    
    serializer = UploadFileFormSerializer(data=request.data)
    result: str = ''
    if (not serializer.is_valid()):
        return JsonResponse({'error': 'form not valid'})
    
    if ('image' not in request.data):
        return JsonResponse({'error': 'no image provided'})
    
    if (imgType == 'wave'):
        file = UploadFileForm.objects.create(title=request.data['image'].name, file=request.data['image'])

        image = cv2.imread(r'models\{}'.format(file.file.name))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = cv2.resize(image, (200, 200))
        image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

        image = canny(image)
        features = hog(
            image, orientations=9, pixels_per_cell=(10, 10),
            cells_per_block=(2, 2), transform_sqrt=True, block_norm="L1"
        )

        with open(r'models\waves_model.pkl', 'rb') as f:
            model = pickle.load(f)

        pred = model.predict(features.reshape(1, -1))
        if (pred == 1):
            result = "PARKINSON"

        else:
            result = "HEALTHY"

    else:
        file = UploadFileForm.objects.create(title=request.data['image'].name, file=request.data['image'])

        image = cv2.imread(r'models\{}'.format(file.file.name))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = cv2.resize(image, (200, 200))
        image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

        image = canny(image, sigma=1, low_threshold=5, high_threshold=50)
        features = hog(
            image, orientations=9, pixels_per_cell=(10, 10),
            cells_per_block=(2, 2), transform_sqrt=True, block_norm="L1"
        )

        with open(r'models\spirals_model.pkl', 'rb') as f:
            model = pickle.load(f)

        pred = model.predict(features.reshape(1, -1))
        if (pred == 1):
            result = "PARKINSON"

        else:
            result = "HEALTHY"

    return JsonResponse({'diagnosis': result})