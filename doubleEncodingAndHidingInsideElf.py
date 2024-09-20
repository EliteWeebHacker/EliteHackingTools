import base64
import os

global base64txt

def encode_file_with_hex_and_base64(input_path):
    # Read the original file
    with open(input_path, 'r') as file:
        content = file.read()
        
    # Convert the content to hexadecimal
    hex_encoded_content = ''.join([f'{ord(c):x}' for c in content])
    hex_encoded_content = hex_encoded_content[0:]

    # Encrypt the prefixed hexadecimal content in Base64
    base64txt = base64.b64encode(hex_encoded_content.encode('utf-8')).decode('utf-8')

def hide_inside_elf(input_path, output_path):
    # File names
    file_c = base64txt

    # Ensure the artifact directory exists
    artifact_dir = os.path.dirname(input_path)
    if not os.path.exists(artifact_dir):
        os.makedirs(artifact_dir)

    # Ensure the output directory exists
    output_dir = os.path.dirname(output_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Create file B if it doesn't exist
    if not os.path.exists(output_path):
        with open(output_path, 'wb') as fb:
            pass

    try:
        # Read the first 64 bytes from file A
        with open(input_path, 'rb') as fa:
            a_data = fa.read(64)
        
        # Write the first 64 bytes to file B
        with open(output_path, 'ab') as fb:
            fb.write(a_data)
        
        # Read the contents of file C
        with open(file_c, 'rb') as fc:
            c_data = fc.read()
        
        # Write the contents of file C to file B, starting from the position after the first 64 bytes
        with open(output_path, 'ab') as fb:
            fb.write(c_data)
        
        print("Operation completed successfully.")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except IOError as e:
        print(f"An error occurred while processing files: {e}")
    finally:
        print("File operations finished.")

def main():
    # read input path for the file to be encoded
    cover_file_path= './cover_files/nmap'
    input_path = 'randomerfile.txt'
    output_path = './nmap'

    input_path = input("Enter the path of the file to be encoded: ")
    encode_file_with_hex_and_base64(input_path)
    cover_file_path = input("Enter the path of the cover file: ")
    output_path = input("Enter the path of the output file: ")
    hide_inside_elf(cover_file_path, output_path)
    

