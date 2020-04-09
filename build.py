

import glob
import os
from jinja2 import Template
pages = []
def main():
        #feedback
        print('hello website build')
main()
def make_pages():
    files_list = glob.glob('./content/*.html')
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
def startTemplating():
    single_template = open('./templates/base.html').read()
    template = Template(single_template)
    return template
template = startTemplating()

def makePage():
    for page in pages:
        page_content = open(page['filename']).read()
        page_html = template.render(
            title=page['title'],
            content=page_content,
            pages=pages,
            active_class='active'
        )
        open(page['output'], 'w+').write(page_html)
makePage()
