

# website pages List

import glob
import os
all_html_files = glob.glob('./content/*.html')
# print(all_html_files)



# blog_posts = [
#     {
#         "filename": "blog/1.html",
#         "date": "March 26th, 2018",
#         "title": "My Experience so far at coding Bootcamp",
#     },
#     {
#         "filename": "blog/2.html",
#         "date": "March 27, 2018",
#         "title": "My Experience so far at coding Bootcamp",
#     },
#     {
#         "filename": "blog/3.html",
#         "date": "March 28th, 2018",
#         "title": "My Experience so far at coding Bootcamp",
#     }
# ]

#refactored

def main():
    #feedback
    print('hello website build')

main()
import glob
import os
files_list = glob.glob('./content/*.html')
# print(all_html_files)

pages = []
def make_pages():
    for i in files_list:
        myobj = {} # initialize page dict 
        myobj.update({'filename': i}) # add filename to dict
        file_name = os.path.basename(i) # get name of file
        name_only, extension = os.path.splitext(file_name) # remove file extension
        myobj['title'] = name_only # add title to dict
        myobj['output'] = './docs/' + os.path.basename(i) # add outpute destination to dict
        pages.append(myobj) # add each iteration to pages list
                
make_pages()
#import template libarary
from string import Template
single_template = open('./templates/base.html').read()
template = Template(single_template)
for page in pages:
    page_content = open(page['filename']).read()
    page_html = template.safe_substitute(
        title=page['title'],
        content=page_content,

    )
    
    # open(page['output'], 'w+').write(page_html)
    def writePage():
        open(page['output'], 'w+').write(page_html)
    writePage()
