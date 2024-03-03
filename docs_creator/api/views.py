import os

from django.conf import settings
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from .serializers import FileSerializer


@api_view(['POST'])
def upload_file(request):
    """Метод для загрузки файла в Google Drive"""

    serializer = FileSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    name = serializer.validated_data.get('name')
    data = serializer.validated_data.get('data')
    filename = f"{name}.txt"
    with open(filename, "w") as file:
        file.write(data)
        file.close()

    credentials = service_account.Credentials.from_service_account_file(
        settings.SERVICE_ACCOUNT_FILE, scopes=settings.SCOPES
    )
    try:
        service = build("drive", "v3", credentials=credentials)
        file_metadata = {
            "name": filename,
            "mimeType": "application/vnd.google-apps.document",
            "parents": [settings.FOLDER_ID]
        }
        media = MediaFileUpload(filename, mimetype="text/txt")
        service.files().create(
            body=file_metadata,
            media_body=media,
            fields="id"
        ).execute()

    except HttpError as error:
        print(f"An error occurred: {error}")

    os.remove(filename)
    return Response(serializer.validated_data, status=HTTP_200_OK)
