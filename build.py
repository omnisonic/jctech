# First, get the template files
top_template = open('./templates/top.html').read()
bottom_template = open('./templates/bottom.html').read()

# Read in index HTML code
content = open('./content/index.html').read()

# Combine template HTML code with content HTML code
index_html = top_template + content + bottom_template
open('./docs/index.html', 'w+').write(index_html)

# Rinse and repeat, but with blog HTML code
content = open('./content/blog.html').read()
blog_html = top_template + content + bottom_template
open('./docs/blog.html', 'w+').write(blog_html)

# And again, this time with project HTML code
content = open('./content/projects.html').read()
projects_html = top_template + content + bottom_template
open('./docs/projects.html', 'w+').write(projects_html)
# And again, this time with bio HTML code
content = open('./content/projects.html').read()
bio_html = top_template + content + bottom_template
open('./docs/bio.html', 'w+').write(bio_html)
# And again, this time with project HTML code
content = open('./content/contact.html').read()
contact_html = top_template + content + bottom_template
open('./docs/contact.html', 'w+').write(contact_html)
