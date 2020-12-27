import pdftotree
filename = "sample.pdf"
outputDir = "/home/moshe/workspace/projects/Automation/mail_server/"
a= pdftotree.parse(outputDir+filename, html_path=None, model_type=None, model_path=None, visualize=False)
print(a)