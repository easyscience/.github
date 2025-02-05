import yaml


def read_yaml_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)


def write_markdown_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


def generate_logo(name):
    name_lower = name.lower()
    logos_url = f"https://raw.githubusercontent.com/easyscience/assets-branding/refs/heads/master/{name_lower}/logos"
    light_logo_url = f"{logos_url}/light.svg"
    dark_logo_url = f"{logos_url}/dark.svg"
    return (f"<picture>"
            f"<source media='(prefers-color-scheme: light)' srcset='{light_logo_url}'>"
            f"<source media='(prefers-color-scheme: dark)' srcset='{dark_logo_url}'>"
            f"<img src='{light_logo_url}' height='32px' alt='{name}'>"
            f"</picture>")


def generate_links(data):
    org_url = 'https://github.com/easyscience'

    links_md = "\n<!---Domain-Specific Projects--->\n"
    for project in data['domain-specific-projects']:
        for key, repo in project['repos'].items():
            links_md += f"[{repo}]: {org_url}/{repo}\n"

    links_md += "\n<!---Core Framework Modules--->\n"
    for module in data['core-framework-modules']:
        links_md += f"[{module['repo']}]: {org_url}/{module['repo']}\n"

    return links_md


def generate_markdown(data):
    domain_projects_md = "### Domain-Specific Projects\n\nThese projects focus on different scientific techniques for data analysis and reduction.\n\n"
    domain_projects_md += "| Project | | Description | 🏠<br/>Project<br/>Home | 📦<br/>Python<br/>Library | 🖥<br/>Desktop<br/>Application |\n"
    domain_projects_md += "|---------|-|-------------|-------------------------|---------------------------|---------------------------------|\n"

    for project in data['domain-specific-projects']:
        logo = generate_logo(project['name'])
        shortcut = project['shortcut']
        desc = f"{project['description']['main']}<br/>`{project['description']['type']}`"

        project_home = f"[{project['repos'].get('project', '')}]" if 'project' in project['repos'] else ""
        python_lib = f"[{project['repos'].get('lib', '')}]" if 'lib' in project['repos'] else ""
        desktop_app = f"[{project['repos'].get('app', '')}]" if 'app' in project['repos'] else ""

        domain_projects_md += f"| {logo} | {shortcut} | {desc} | {project_home} | {python_lib} | {desktop_app} |\n"

    core_modules_md = "\n### Core Framework Modules\n\nThese are essential building blocks that support the domain-specific projects.\n\n"
    core_modules_md += "| Project | | Description | Repository |\n"
    core_modules_md += "|---------|-|-------------|------------|\n"

    for module in data['core-framework-modules']:
        logo = generate_logo(module['name'])
        shortcut = module['shortcut']
        desc = f"{module['description']['main']}<br/>`{module['description']['type']}`"
        repo = f"[{module['repo']}]"

        core_modules_md += f"| {logo} | {shortcut} | {desc} | {repo} |\n"

    links_md = generate_links(data)
    return domain_projects_md + "\n" + core_modules_md + "\n" + links_md


if __name__ == "__main__":
    yaml_file_path = "profile/README.yaml"  # Input YAML file
    markdown_file_path = "profile/README.md"  # Output markdown file

    data = read_yaml_file(yaml_file_path)
    markdown_content = generate_markdown(data)
    write_markdown_file(markdown_file_path, markdown_content)
