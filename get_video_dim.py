import struct

def get_mp4_dimensions(file_path):
    with open(file_path, 'rb') as f:
        data = f.read(100000)
        # Find 'tkhd' atom
        idx = data.find(b'tkhd')
        if idx != -1:
            # Check version
            version = data[idx+4]
            if version == 0:
                width_idx = idx + 80
                height_idx = idx + 84
            else:
                width_idx = idx + 92
                height_idx = idx + 96
            width = struct.unpack('>I', data[width_idx:width_idx+4])[0] >> 16
            height = struct.unpack('>I', data[height_idx:height_idx+4])[0] >> 16
            return width, height
    return 1920, 1080

w, h = get_mp4_dimensions('incognita_video.mp4')
print(f"Video Dimensions: {w}x{h} (Aspect Ratio: {w/h:.2f})")
