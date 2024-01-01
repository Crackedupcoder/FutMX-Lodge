import filetype
from django.core.exceptions import ValidationError

def is_valid_video(file):
    kind = filetype.guess(file.read(262))  # Read the first 262 bytes
    if not kind or not kind.mime.startswith('video/'):
        raise ValidationError("Upload a valid video. The file you uploaded was either not an video or a corrupted video")


def validate_video_size(value):
    limit_mb = 100
    if value.size > limit_mb * 1024 * 1024:
        raise ValidationError(f"Maximum file size is {limit_mb} mb")
    

def validate_image_size(value):
    limit_mb = 10
    if value.size > limit_mb * 1024 * 1024:
        raise ValidationError(f"Maximum file size is {limit_mb} mb")