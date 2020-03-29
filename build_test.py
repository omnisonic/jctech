

# website pages List

pages = [
    {
        'filename': './content/index.html',
        'output': './docs/index.html',
        'title': 'Welcome!',
        'activeLink': 'index_class',
    },
    {
        'filename': './content/blog.html',
        'output': './docs/blog.html',
        'title': 'Blog',
        'activeLink': 'blog_class',
    },
    {
        'filename': './content/projects.html',
        'output': './docs/projects.html',
        'title': 'Projects',
        'activeLink': 'project_class'
    },
    {
        'filename': './content/bio.html',
        'output': './docs/bio.html',
        'title': 'Bio',
        'activeLink': 'bio_class',
    },
    {
        'filename': './content/contact.html',
        'output': './docs/contact.html',
        'title': 'Contact',
        'activeLink': 'contact_class',
    }
]

blog_posts = [
    {
        "filename": "blog/1.html",
        "date": "March 26th, 2018",
        "title": "My Experience so far at coding Bootcamp",
    },
    {
        "filename": "blog/2.html",
        "date": "March 27, 2018",
        "title": "My Experience so far at coding Bootcamp",
    },
    {
        "filename": "blog/3.html",
        "date": "March 28th, 2018",
        "title": "My Experience so far at coding Bootcamp",
    }
]

#refactored

def main():
    #feedback
    print('hello website build')

main()
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


# def baseReadin():
#     #import template libarary
#     from string import Template
#     single_template = open('./templates/base.html').read()
#     template = Template(single_template)
#     return template
    
# def templateReadin():
#     page_content = open(page['filename']).read()
#     page_html = template.safe_substitute(
#         title=page['title'],
#         content=page_content,
#         page['activeLink']='active'
#     )
#     return page_html

# #def addActiveLink():


# def writePage():
#     open(page['output'], 'w+').write(page_html)

# for page in pages:
#     baseReadin()
#     templateReadin()
#     writePage()


# def openContent():
#     page_content = open(page['filename']).read()
#     return 
# def appy_template()
#     page_html = template.safe_substitue(page_title)
#     )
#     return