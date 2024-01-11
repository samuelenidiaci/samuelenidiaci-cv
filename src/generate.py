import json
import subprocess
from pathlib import Path
from shutil import rmtree, copytree, copy2

from jinja2 import Environment, FileSystemLoader


def load_resume_data(filename="resume.json"):
  with open(filename, 'r') as f:
    return json.load(f)
  

def load_template(template_name):
  output_folder = Path('temp')

  if output_folder.exists():
    rmtree(output_folder)
  
  template_folder = Path(f"templates/{template_name}")

  copytree(template_folder, output_folder)


def render_latex(data):
  environment = Environment(
    block_start_string='<block>',
    block_end_string='</block>',
    variable_start_string='<var>',
    variable_end_string='</var>',
    loader=FileSystemLoader("temp/")
  )
  template = environment.get_template("template.tex")

  content = template.render(
    **data
  )

  with open("temp/resume.tex", "w", encoding="utf-8") as f:
    f.write(content)
    

def render_pdf(filename="temp/resume.tex"):
  subprocess.run(["texliveonfly", '--arguments="-output-directory=temp"', filename]) #, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


if __name__ == '__main__':
  output_folder = Path('output')

  if output_folder.exists():
    for path in output_folder.glob("**/*"):
      if path.is_file():
          path.unlink()
      elif path.is_dir():
          rmtree(path)
  else:
    output_folder.mkdir()

  for path in Path('resumes').glob('*.json'):
    name = path.name.split(".")[0]

    print(f"creating {name}.pdf")
    data = load_resume_data(path)

    load_template(data["template"])

    render_latex(data)
    render_pdf()

    copy2("temp/resume.pdf", f"output/{name}.pdf")
