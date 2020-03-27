#feedback
print('hello website build')

#import templating
from string import Template

# webstite dictionary

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


def main():
    single_template = open('./templates/base.html').read()
    template = Template(single_template)


    for page in pages:
        page_content = open(page['filename']).read()
        page_html = template.safe_substitute(
            title=page['title'],
            page['active_link']='active',
            content=page_content,
        )
        open(page['output'], 'w+').write(page_html)
main()
