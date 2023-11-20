import os
import subprocess


def compress_file(input_path, output_path, file_type):
    if file_type == 'pdf':
        command = ['gs', '-sDEVICE=pdfwrite', '-dCompatibilityLevel=1.4', '-dPDFSETTINGS=/screen', '-dNOPAUSE',
                   '-dQUIET', '-dBATCH', '-sOutputFile=' + output_path, input_path]
    elif file_type == 'image':
        command = ['convert', input_path, '-quality', '50', output_path]
    elif file_type == 'video':
        command = ['ffmpeg', '-i', input_path, '-vcodec', 'libx264', '-crf', '23', '-preset', 'ultrafast', output_path]
    elif file_type == 'audio':
        command = ['ffmpeg', '-i', input_path, '-acodec', 'libmp3lame', '-ab', '128k', output_path]
    elif file_type == 'text':
        command = ['python', 'compress.py', input_path, output_path]
    else:
        raise ValueError('Invalid file type')
    subprocess.run(command)


if __name__ == '__main__':
    input_path = os.path.join(os.path.dirname(__file__), '../../algo.pdf')
    output_path = os.path.join(os.path.dirname(__file__), 'output.pdf')
    compress_file(input_path, output_path, 'text')
