import filetype
from django.core.exceptions import ValidationError

def is_valid_video(file):
    kind = filetype.guess(file.read(262))  # Read the first 262 bytes
    if not kind or not kind.mime.startswith('video/'):
        raise ValidationError("Upload a valid video. The file you uploaded was either not an video or a corrupted video")


def validate_video_size(value):
    limit_mb = 100  # Set your desired size limit in megabytes
    for image in value:
        if image.size > limit_mb * 1024 * 1024:
            raise ValidationError(f"Video size should be less than {limit_mb} MB.")
    

def validate_image_size(value):
    limit_mb = 2  # Set your desired size limit in megabytes

    if isinstance(value, bytes):
        # Handle the case where the value is a single image (bytes)
        if len(value) > limit_mb * 1024 * 1024:
            raise ValidationError(f"Image size should be less than {limit_mb} MB.")
    elif isinstance(value, list):
        # Handle the case where the value is a list of images
        for image in value:
            if len(image) > limit_mb * 1024 * 1024:
                raise ValidationError(f"Image size should be less than {limit_mb} MB.")
    else:
        raise ValidationError("Invalid image format.")
