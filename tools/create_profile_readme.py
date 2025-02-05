import yaml
from typing import Dict


def read_yaml_file(file_path: str) -> Dict:
    """
    Reads a YAML file and returns its content as a dictionary.
    :param file_path: Path to the YAML file.
    :return: Parsed YAML content as a dictionary.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)


def write_markdown_file(file_path: str, content: str) -> None:
    """
    Writes the generated Markdown content to a file.
    :param file_path: Path to the Markdown file.
    :param content: Markdown content to write.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


def generate_logo(project_name: str) -> str:
    """
    Generates an HTML block for a project's logo using branding assets.
    :param project_name: Name of the project.
    :return: HTML picture element containing light and dark mode images.
    """
    project_slug = project_name.lower()
    logos_url = f"https://raw.githubusercontent.com/easyscience/assets-branding/refs/heads/master/{project_slug}/logos"
    return (f"<picture>"
            f"<source media='(prefers-color-scheme: light)' srcset='{logos_url}/light.svg'>"
            f"<source media='(prefers-color-scheme: dark)' srcset='{logos_url}/dark.svg'>"
            f"<img src='{logos_url}/light.svg' height='32px' alt='{project_name}'>"
            f"</picture>")


def generate_repository_links(data: Dict) -> str:
    """
    Generates a Markdown section with repository links for domain-specific projects and core modules.
    :param data: Dictionary containing project information from YAML.
    :return: Markdown-formatted repository links.
    """
    org_url = 'https://github.com/easyscience'
    links_md = "\n<!---Domain-Specific Projects--->\n"

    for project in data['domain-specific-projects']:
        for repo_type, repo_name in project['repos'].items():
            links_md += f"[{repo_name}]: {org_url}/{repo_name}\n"

    links_md += "\n<!---Core Framework Modules--->\n"
    for module in data['core-framework-modules']:
        links_md += f"[{module['repo']}]: {org_url}/{module['repo']}\n"

    return links_md


def generate_markdown(data: Dict) -> str:
    """
    Generates the full Markdown content for domain-specific projects and core framework modules.
    :param data: Dictionary containing project details from YAML.
    :return: Markdown-formatted string.
    """
    # Domain-Specific Projects Table
    markdown_output = "### Domain-Specific Projects"
    markdown_output += "\n\nThese projects focus on different scientific techniques for data analysis and reduction.\n\n"
    markdown_output += "| Project | 🏷 | 📖<br/>Description | 🏠<br/>Project<br/>Home | 📦<br/>Python<br/>Library | 🖥<br/>Desktop<br/>Application |\n"
    markdown_output += "|---------|----|--------------------|-------------------------|---------------------------|---------------------------------|\n"

    for project in data['domain-specific-projects']:
        logo = generate_logo(project['name'])
        shortcut = project['shortcut']
        desc = f"{project['description']['main']}<br/>`{project['description']['type']}`"

        project_home = f"[{project['repos'].get('project', '')}]" if 'project' in project['repos'] else ""
        python_lib = f"[{project['repos'].get('lib', '')}]" if 'lib' in project['repos'] else ""
        desktop_app = f"[{project['repos'].get('app', '')}]" if 'app' in project['repos'] else ""

        markdown_output += f"| {logo} | {shortcut} | {desc} | {project_home} | {python_lib} | {desktop_app} |\n"

    # Core Framework Modules Table
    markdown_output += "\n### Core Framework Modules"
    markdown_output += "\n\nThese are essential building blocks that support the domain-specific projects.\n\n"
    markdown_output += "| Project | 🏷 | 📖<br/>Description | 📦<br/>Library |\n"
    markdown_output += "|---------|----|---------------------|----------------|\n"

    for module in data['core-framework-modules']:
        logo = generate_logo(module['name'])
        shortcut = module['shortcut']
        desc = f"{module['description']['main']}<br/>`{module['description']['type']}`"
        repo = f"[{module['repo']}]"

        markdown_output += f"| {logo} | {shortcut} | {desc} | {repo} |\n"

    # Append Repository Links
    markdown_output += "\n" + generate_repository_links(data)

    return markdown_output


if __name__ == "__main__":
    yaml_file_path = "profile/README.yaml"  # Path to input YAML file
    markdown_file_path = "profile/README.md"  # Path to output Markdown file

    project_data = read_yaml_file(yaml_file_path)
    markdown_content = generate_markdown(project_data)
    write_markdown_file(markdown_file_path, markdown_content)

    print("Markdown file has been successfully generated.")
