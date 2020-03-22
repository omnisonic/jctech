#feedback
print('hello  combined website!')
#import templating
from string import Template
# get template files
single_template = open('./templates/base.html').read()
template = Template(single_template)

# Read in index HTML code
index_content = open('./content/index.html').read()
# Combine template HTML code with content HTML code
index_html = template.safe_substitute(
    title='Welcome!',
    index_class='active',
    content=index_content,
)
open('./docs/index.html', 'w+').write(index_html)

# Rinse and repeat, but with blog HTML code
blog_content = open('./content/blog.html').read()
blog_html = template.safe_substitute(
    title='Blog',
    blog_class='active',
    content=blog_content,
)
open('./docs/blog.html', 'w+').write(blog_html)

# And again, this time with project HTML code
projects_content = open('./content/projects.html').read()
projects_html = template.safe_substitute(
    title='Projects',
    projects_class='active',
    content=projects_content,
)
open('./docs/projects.html', 'w+').write(projects_html)

# And again, this time with bio HTML code
bio_content = open('./content/projects.html').read()
bio_html = template.safe_substitute(
    title='Bio',
    bio_class='active',
    content=bio_content,
)
open('./docs/bio.html', 'w+').write(bio_html)
# And again, this time with project HTML code
contact_content = open('./content/contact.html').read()
contact_html = template.safe_substitute(
    title='Contact',
    contact_class='active',
    content=contact_content,
)
open('./docs/contact.html', 'w+').write(contact_html)
