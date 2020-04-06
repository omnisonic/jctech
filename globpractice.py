# trying out glob





# my loop to make a list of dictionary of my content pages
print('hello')
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
        myobj['output'] = '/.docs/' + os.path.basename(i) # add outpute destination to dict
        pages.append(myobj) # add each iteration to pages list
                
make_pages()

# import os
# def pagetitle():
#     for i in all_html_files:
#         mytitle = {}
#         file_path = i
#         file_name = os.path.basename(file_path)
#         name_only, extension = os.path.splitext(file_name)
#         mytitle['title'] = i
#         pages.append(mytitle)

#         # print(mytitle)
# pagetitle()
print(pages)




# def outputValues():
#     print()


# tying out os
# import os

# file_path = "content/blog.html"
# file_name = os.path.basename(file_path)
# name_only, extension = os.path.splitext(file_name)
# print(name_only)


# write 
# pages_globbed = []
# pages_globbed.append(all_html_files)
# open("globbed.html", "+w").wt(pages_globbed)
