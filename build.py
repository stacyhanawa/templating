import glob
all_html_files = glob.glob("content/*.html")
print(all_html_files)

import os

file_path = "content/blog.html"
file_name = os.path.basename(file_path)
print(file_name)
name_only, extension = os.path.splitext(file_name)
print(name_only)

pages = []
pages.append({
    "filename": "content/index.html",
    "title": "Index",
    "output": "doc/index.html",
})
print(pages)

def apply_template(template, page_title, file_name):
    index_content = open(file_name).read()
    finished_index_page = template.replace("{{content}}", index_content)
    finished_index_page = finished_index_page.replace("{{title}}", page_title)
    return finished_index_page
    
def print_page(template, page):
    file_name = page['filename']
    page_output = page['output']
    page_title = page['title']
    
    page_html = apply_template(template, page_title, file_name)
    open(page_output, "w+").write(page_html)
    
def main():
    template = open("templates/base.html").read()
    for page in pages:
        print_page(template, page)
    
if __name__ == "__main__":
    main()
