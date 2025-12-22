
import os

def replace_in_file(file_path, replacements):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = content
        for old, new in replacements.items():
            new_content = new_content.replace(old, new)
            
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {file_path}")
        else:
            print(f"No changes needed for {file_path}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")

def fix_paths():
    # Fix HTML files
    html_replacements = {
        'ContentNew/': 'contentnew/',
        'imagesNew/': 'imagesnew/',
        'ContentNew\\': 'contentnew/', # Handle Windows backslashes if any (though HTML usually /)
        'imagesNew\\': 'imagesnew/'
    }
    
    replace_in_file('index.html', html_replacements)
    replace_in_file('courses.html', html_replacements)
    
    # Fix CSS file
    # Path: contentnew/DalbirCSS.css
    # It references images.
    # We want to replace 'imagesNew/' and 'ContentNew/' if unrelated.
    # Note: CSS relative paths are key.
    css_replacements = {
        'imagesNew/': 'imagesnew/', 
        'ContentNew/': 'contentnew/', # Unlikely inside itself, but safe.
        '../imagesNew/': '../imagesnew/' 
    }
    
    replace_in_file('contentnew/DalbirCSS.css', css_replacements)

if __name__ == "__main__":
    fix_paths()
